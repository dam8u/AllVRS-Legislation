#!/usr/bin/env python3
"""
Fidelity check for the generated .docx copies of the brief package.

Run after tools/md_to_docx.py:

    python3 tools/verify_docx.py

Why this is worth having. These documents are a fiscal package whose figures
have already been corrected once in public; a silently dropped digit in a Word
copy is a worse failure than a layout problem, because the Word copy is the one
that gets forwarded and edited. The check therefore does not eyeball the output
-- it reconstructs the plain text of each .docx (paragraphs, table cells and
hidden runs, in document order) and diffs it word-by-word against the plain
text of the Markdown source, then separately compares every money, percent and
Code-section token as a multiset so a changed count cannot hide inside an
otherwise-matching diff.

Exit status is non-zero if any file fails, so this can gate a commit.
"""

from __future__ import annotations

import difflib
import re
import sys
from pathlib import Path

from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph

REPO_ROOT = Path(__file__).resolve().parent.parent
BRIEF_DIR = REPO_ROOT / "briefs" / "2027-military-service-credit-cost-window"

# Markers the converter introduces or drops for layout reasons; they carry no
# content and are excluded from the word-sequence diff on both sides.
LAYOUT_NOISE = {"•", "|", "-", "--", "---", "*", "#", "##", "###", "####", ">"}

MATERIAL_TOKEN = re.compile(
    r"\$\s?[\d,]+(?:\.\d+)?"          # $26,762,817,000  $18,666  $1.2
    r"|\d[\d,]*(?:\.\d+)?\s?%"        # 0.68%  29.2%
    r"|§+\s?[\d][\d.\-:]*"            # § 51.1-142.2  § 30-19.1:7
    r"|\b\d[\d,]*(?:\.\d+)?\b"        # 110,474  37.7  1867
)

PROVENANCE_PREFIX = "[Source provenance, hidden text"
# Must stay in step with add_hidden_provenance() in tools/md_to_docx.py.
PROVENANCE_LABEL = (
    "[Source provenance, hidden text — not printed. Reveal with Word's "
    "Show/Hide formatting marks.]"
)


def docx_text(path: Path) -> tuple[str, list[str]]:
    """Return (full text including hidden runs, list of hidden run prefixes)."""
    document = Document(path)
    chunks: list[str] = []
    hidden: list[str] = []

    def walk_block_items(parent):
        body = parent.element.body if hasattr(parent, "element") else parent._tc
        for child in body.iterchildren():
            if child.tag.endswith("}p"):
                yield Paragraph(child, parent)
            elif child.tag.endswith("}tbl"):
                yield Table(child, parent)

    def emit_paragraph(paragraph: Paragraph) -> None:
        text = paragraph.text
        for run in paragraph.runs:
            if run.font.hidden and run.text.strip():
                hidden.append(run.text[:60])
        if text.strip():
            chunks.append(text)

    for item in walk_block_items(document):
        if isinstance(item, Paragraph):
            emit_paragraph(item)
        else:
            for row in item.rows:
                for cell in row.cells:
                    for paragraph in cell.paragraphs:
                        emit_paragraph(paragraph)

    # Hyperlinks are w:hyperlink children, which Paragraph.text skips in some
    # python-docx versions; pull their text straight from the XML as a backstop.
    from docx.oxml.ns import qn

    link_text = "".join(
        node.text or ""
        for node in document.element.body.iter(qn("w:t"))
    )
    if len(link_text) > len(" ".join(chunks)):
        chunks = [link_text]

    return "\n".join(chunks), hidden


def markdown_text(path: Path) -> str:
    source = path.read_text(encoding="utf-8")
    source = re.sub(r"<!--.*?-->", " ", source, flags=re.S)  # hidden in docx; see below

    # Code is literal on the .docx side -- the converter never parses markup
    # inside it -- so it must be shielded from the emphasis stripping below.
    # Without this, a formula such as "P*(class)" in a code block loses its
    # asterisk here but keeps it in the Word file and reads as a mismatch.
    literals: list[str] = []

    def shield(text: str) -> str:
        literals.append(text)
        return f"\x00{len(literals) - 1}\x00"

    lines = []
    in_fence = False
    for line in source.split("\n"):
        # The quote marker goes first so that a table, fence, heading or list
        # inside a blockquote is classified as that block rather than as prose.
        stripped = line.strip()
        while stripped.startswith(">"):
            stripped = re.sub(r"^>\s?", "", stripped)
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            lines.append(shield(stripped))
            continue
        if re.match(r"^\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?$", stripped):
            continue  # table alignment divider
        if re.match(r"^([-*_])(\s*\1){2,}$", stripped):
            continue  # horizontal rule
        stripped = re.sub(r"^#{1,6}\s+", "", stripped)
        stripped = re.sub(r"^([-*+])\s+", "", stripped)
        stripped = stripped.replace("|", " ")
        lines.append(stripped)
    text = "\n".join(lines)
    text = re.sub(r"`([^`]+)`", lambda m: shield(m.group(1)), text)
    text = re.sub(r"\[([^\]]+)\]\([^)\s]+\)", r"\1", text)  # link text only
    text = text.replace("**", "").replace("~~", "")
    text = re.sub(r"(?<!\*)\*(?!\*)", "", text)
    text = text.replace("`", "")
    return re.sub(r"\x00(\d+)\x00", lambda m: literals[int(m.group(1))], text)


def words(text: str) -> list[str]:
    return [
        token for token in text.split()
        if token not in LAYOUT_NOISE and token.strip()
    ]


def material_tokens(text: str) -> list[str]:
    return sorted(
        token.replace(" ", "") for token in MATERIAL_TOKEN.findall(text)
    )


def check(md_path: Path) -> bool:
    docx_path = md_path.with_suffix(".docx")
    if not docx_path.exists():
        print(f"FAIL {md_path.name}: no .docx generated")
        return False

    body, hidden = docx_text(docx_path)
    md_raw = md_path.read_text(encoding="utf-8")
    md_body = markdown_text(md_path)

    # The leading HTML comment is stripped from the body and re-emitted as a
    # hidden run, so compare against Markdown that includes it.
    comment = re.search(r"<!--(.*?)-->", md_raw, flags=re.S)
    if comment:
        md_body = md_body + "\n" + re.sub(r"={4,}", " ", comment.group(1))

    # The hidden run is prefixed with a label explaining what it is; that label
    # is the converter's own text, not content, so drop it before diffing.
    body_for_diff = body.replace(PROVENANCE_LABEL, " ")

    md_words, docx_words = words(md_body), words(body_for_diff)
    md_tokens, docx_tokens = material_tokens(md_body), material_tokens(body)

    problems: list[str] = []

    if md_tokens != docx_tokens:
        missing = [t for t in md_tokens if docx_tokens.count(t) < md_tokens.count(t)]
        extra = [t for t in docx_tokens if md_tokens.count(t) < docx_tokens.count(t)]
        if missing:
            problems.append(f"figures missing from .docx: {sorted(set(missing))[:12]}")
        if extra:
            problems.append(f"figures only in .docx: {sorted(set(extra))[:12]}")

    diff = [
        line for line in difflib.unified_diff(md_words, docx_words, n=0, lineterm="")
        if line.startswith(("+", "-")) and not line.startswith(("+++", "---"))
    ]
    if diff:
        problems.append(f"{len(diff)} word-level differences, e.g. {diff[:8]}")

    if comment and not hidden:
        problems.append("source provenance comment was dropped, not hidden")
    if hidden and not hidden[0].startswith(PROVENANCE_PREFIX):
        problems.append(f"unexpected hidden text: {hidden[0]!r}")

    label = f"{md_path.name} -> {docx_path.name}"
    if problems:
        print(f"FAIL {label}")
        for problem in problems:
            print(f"     {problem}")
        return False

    print(
        f"OK   {label}  {len(docx_words):>5} words, "
        f"{len(docx_tokens):>4} figures matched"
        + (", provenance hidden" if hidden else "")
    )
    return True


def main(argv: list[str]) -> int:
    targets = ([Path(argument).resolve() for argument in argv] if argv
               else sorted(BRIEF_DIR.glob("*.md")))
    failures = [path for path in targets if not check(path)]
    print()
    print(
        f"{len(targets) - len(failures)}/{len(targets)} files verified"
        + (f", {len(failures)} FAILED" if failures else "")
    )
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
