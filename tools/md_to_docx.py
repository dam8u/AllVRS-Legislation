#!/usr/bin/env python3
"""
Markdown -> DOCX converter for the JLCVSO 2027-session brief package.

Why this exists
---------------
The package is authored in Markdown, which is the source of record and what
the git history diffs. The board asked for editable Word copies of every
brief, including an editable counterpart to the printed one-page leave-behind
(00-ONE-PAGE-BRIEF.pdf). Neither pandoc nor LibreOffice is installed here, so
the conversion runs directly on python-docx -- which is also how the team's
earlier VRSLite package (legislation/military-service-retirement-bridge) was
produced.

House style
-----------
Typography deliberately matches that earlier package's md2docx.py -- Calibri
body, Consolas for code, near-black headings on the compact layout -- so these
documents look like the Word files the team already works in:

  * memo layout  -- Calibri 10.5pt body, Word's default 1.0in / 1.25in
                    margins, the default template's blue heading styles.
                    Used for the full brief, the annexes and the index.
  * brief layout -- Calibri 9.3pt body on an exact 11.6pt line, 0.42in /
                    0.55in margins, 13.5/8.4pt near-black headings, 8.2pt
                    tables. Used for the one-page leave-behind, whose length
                    is a correctness property rather than a matter of taste.
                    These numbers come from 00-ONE-PAGE-BRIEF.html's print
                    stylesheet rather than the earlier package's brief layout,
                    because this .docx is the editable twin of that document's
                    own one-page PDF and has to match its geometry. At the
                    earlier layout's 0.6in / 9.5pt the content measures 109%
                    of a letter page. tools/pagecheck.py verifies the fit.

Five deliberate departures from that earlier tool, each for a reason:

  1. Links become real Word hyperlinks rather than "label (https://...)" text.
     This package is citation-dense; inlining full Virginia Code and VRS URLs
     would add pages to the annexes and would not fit on the one-pager at all.
  2. Table header rows repeat across page breaks -- the annex tables are long.
  3. Ordered lists get literal numbers with a hanging indent instead of Word's
     "List Number" style. The brief and annexes cross-reference items by
     number ("recommendation item 3"), and Word's automatic numbering runs
     continuously across the separate lists in one document, which would
     silently renumber them.
  4. A leading HTML comment is not printed. It is re-emitted as Word hidden
     text, so the one-pager's HOLD / superseded-figures banner travels with
     the file without consuming a line of a document that must stay on one
     page.
  5. On the brief layout a Markdown "---" draws nothing. The print stylesheet
     does not render those separators either -- the section headings carry
     their own rules -- and the five in the one-pager cost about nine body
     lines, which is the difference between one page and two.

Content is never edited: a .docx produced here holds exactly the text of its
.md source, verified word-by-word and figure-by-figure by tools/verify_docx.py.
Regenerate rather than hand-editing the Word files if the Markdown changes:

    python3 tools/md_to_docx.py                  # whole package
    python3 tools/md_to_docx.py path/to/file.md  # one file, memo layout
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

REPO_ROOT = Path(__file__).resolve().parent.parent
BRIEF_DIR = REPO_ROOT / "briefs" / "2027-military-service-credit-cost-window"

BODY_FONT = "Calibri"
MONO_FONT = "Consolas"
HEADING_INK = RGBColor(0x1F, 0x1F, 0x1F)
QUOTE_GREY = RGBColor(0x44, 0x44, 0x44)
CODE_GREY = RGBColor(0x30, 0x30, 0x30)
RULE_GREY = RGBColor(0x90, 0x90, 0x90)
LINK_HEX = "1A4F8A"


# --------------------------------------------------------------------------
# Layout profiles. The BRIEF numbers are mirrored in tools/pagecheck.py.
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Profile:
    name: str
    margin_tb: float
    margin_lr: float
    body_pt: float
    line_pt: float | None          # exact line height; None = Word default
    space_after_pt: float
    table_pt: float
    code_pt: float
    quote_pt: float
    list_gap_pt: float
    # heading level -> (size pt, space before pt, space after pt)
    headings: dict[int, tuple[float, float, float]] = field(default_factory=dict)
    restyle_headings: bool = False
    footer: bool = False
    # Whether a Markdown "---" becomes a visible separator. The one-pager's
    # print stylesheet does not render them -- the section headings carry
    # their own rules -- and five of them cost roughly nine body lines.
    render_rules: bool = True


# Compact layout for the fixed-length leave-behind.
#
# These numbers are taken from 00-ONE-PAGE-BRIEF.html's print stylesheet, not
# from the earlier package's brief layout. The .docx is the editable twin of
# this document's own one-page PDF, so it has to match that page's geometry:
# at the earlier layout's 0.6in/9.5pt the content measures 109% of a letter
# page and spills to two, which breaks a document named for its length.
BRIEF = Profile(
    name="brief",
    margin_tb=0.42,
    margin_lr=0.55,
    body_pt=9.3,
    line_pt=11.6,
    space_after_pt=4.0,
    table_pt=8.2,
    code_pt=8.5,
    quote_pt=8.6,
    list_gap_pt=2.0,
    headings={1: (13.5, 0.0, 4.0), 2: (8.4, 7.5, 3.0),
              3: (9.3, 6.0, 2.0), 4: (9.3, 5.0, 2.0)},
    restyle_headings=True,
    footer=False,
    render_rules=False,
)

# Standard layout for the full brief, the annexes and the index. Heading styles
# are left at Word's defaults, as the earlier package's memos were.
MEMO = Profile(
    name="memo",
    margin_tb=1.0,
    margin_lr=1.25,
    body_pt=10.5,
    line_pt=None,
    space_after_pt=6.0,
    table_pt=8.5,
    code_pt=9.0,
    quote_pt=10.0,
    list_gap_pt=3.0,
    headings={},
    restyle_headings=False,
    footer=True,
)


# --------------------------------------------------------------------------
# Inline markup
# --------------------------------------------------------------------------


@dataclass
class Span:
    text: str
    bold: bool = False
    italic: bool = False
    code: bool = False
    strike: bool = False
    link: str | None = None


# Underscore emphasis is deliberately unsupported: the briefs cite identifiers
# such as fm_model.py, and treating _ as emphasis would mangle them.
INLINE_PATTERNS = (
    ("code", re.compile(r"`([^`]+)`")),
    ("link", re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")),
    ("bold", re.compile(r"\*\*(.+?)\*\*", re.S)),
    ("strike", re.compile(r"~~(.+?)~~", re.S)),
    ("italic", re.compile(r"\*([^*]+)\*")),
)

ESCAPE = re.compile(r"\\([\\`*_{}\[\]()#+\-.!=~|>])")


def parse_inline(text: str, **inherited) -> list[Span]:
    """Recursively split Markdown inline markup into styled spans."""
    best_kind = best_match = None
    for kind, pattern in INLINE_PATTERNS:
        match = pattern.search(text)
        if match and (best_match is None or match.start() < best_match.start()):
            best_kind, best_match = kind, match

    if best_match is None:
        text = ESCAPE.sub(r"\1", text)
        return [Span(text, **inherited)] if text else []

    spans: list[Span] = []
    if best_match.start():
        spans += parse_inline(text[: best_match.start()], **inherited)

    if best_kind == "code":
        # Code spans are literal; no further markup parsing inside them.
        spans.append(Span(best_match.group(1), code=True, **inherited))
    elif best_kind == "link":
        spans += parse_inline(
            best_match.group(1), **{**inherited, "link": best_match.group(2)}
        )
    else:
        spans += parse_inline(best_match.group(1), **{**inherited, best_kind: True})

    if best_match.end() < len(text):
        spans += parse_inline(text[best_match.end():], **inherited)
    return spans


def add_spans(paragraph, spans: list[Span], profile: Profile,
              size_pt: float | None = None, color: RGBColor | None = None,
              force_bold: bool = False, force_italic: bool = False) -> None:
    """Write spans into a paragraph.

    Run-level font overrides are kept to the minimum the markup actually
    requires. Everything else inherits from the paragraph style, so whoever
    edits the file in Word can restyle a whole document from the style pane
    instead of fighting hard-coded formatting on every run.
    """
    for span in spans:
        if span.link:
            add_hyperlink(paragraph, span, profile, size_pt)
            continue
        run = paragraph.add_run(span.text)
        if span.bold or force_bold:
            run.bold = True
        if span.italic or force_italic:
            run.italic = True
        if span.strike:
            run.font.strike = True
        if span.code:
            run.font.name = MONO_FONT
            run.font.size = Pt(profile.code_pt)
            run.font.color.rgb = CODE_GREY
        else:
            if size_pt is not None:
                run.font.size = Pt(size_pt)
            if color is not None:
                run.font.color.rgb = color


def add_hyperlink(paragraph, span: Span, profile: Profile,
                  size_pt: float | None) -> None:
    """python-docx has no hyperlink API; build the w:hyperlink element by hand."""
    rel_id = paragraph.part.relate_to(
        span.link,
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True,
    )
    link = OxmlElement("w:hyperlink")
    link.set(qn("r:id"), rel_id)

    run = OxmlElement("w:r")
    props = OxmlElement("w:rPr")
    font_name = MONO_FONT if span.code else BODY_FONT
    elements: list[tuple[str, dict[str, str]]] = [
        ("w:rFonts", {"w:ascii": font_name, "w:hAnsi": font_name}),
        ("w:color", {"w:val": LINK_HEX}),
        ("w:u", {"w:val": "single"}),
    ]
    effective_size = profile.code_pt if span.code else size_pt
    if effective_size is not None:
        elements.append(("w:sz", {"w:val": str(int(round(effective_size * 2)))}))
    for tag, attrs in elements:
        element = OxmlElement(tag)
        for key, value in attrs.items():
            element.set(qn(key), value)
        props.append(element)
    if span.bold:
        props.append(OxmlElement("w:b"))
    if span.italic:
        props.append(OxmlElement("w:i"))
    run.append(props)

    text = OxmlElement("w:t")
    text.set(qn("xml:space"), "preserve")
    text.text = span.text
    run.append(text)
    link.append(run)
    paragraph._p.append(link)


# --------------------------------------------------------------------------
# Low-level docx helpers
# --------------------------------------------------------------------------


def set_table_indent(table, indent_pt: float) -> None:
    """Indent a whole table. python-docx has no API for w:tblInd."""
    element = OxmlElement("w:tblInd")
    element.set(qn("w:w"), str(int(round(indent_pt * 20))))  # twentieths of a pt
    element.set(qn("w:type"), "dxa")
    table._tbl.tblPr.append(element)


def repeat_header_row(row) -> None:
    props = row._tr.get_or_add_trPr()
    element = OxmlElement("w:tblHeader")
    element.set(qn("w:val"), "true")
    props.append(element)


def page_number_field(paragraph, size_pt: float) -> None:
    """'Page N of M' as live Word fields."""
    for instruction in ("PAGE", None, "NUMPAGES"):
        if instruction is None:
            run = paragraph.add_run(" of ")
            run.font.name = BODY_FONT
            run.font.size = Pt(size_pt)
            continue
        run = paragraph.add_run()
        run.font.name = BODY_FONT
        run.font.size = Pt(size_pt)
        begin = OxmlElement("w:fldChar")
        begin.set(qn("w:fldCharType"), "begin")
        field_code = OxmlElement("w:instrText")
        field_code.set(qn("xml:space"), "preserve")
        field_code.text = f" {instruction} "
        end = OxmlElement("w:fldChar")
        end.set(qn("w:fldCharType"), "end")
        for node in (begin, field_code, end):
            run._r.append(node)


# --------------------------------------------------------------------------
# Document scaffolding
# --------------------------------------------------------------------------


def new_document(profile: Profile) -> Document:
    document = Document()
    section = document.sections[0]
    section.page_width = Inches(8.5)
    section.page_height = Inches(11)
    section.top_margin = Inches(profile.margin_tb)
    section.bottom_margin = Inches(profile.margin_tb)
    section.left_margin = Inches(profile.margin_lr)
    section.right_margin = Inches(profile.margin_lr)

    normal = document.styles["Normal"]
    normal.font.name = BODY_FONT
    normal.font.size = Pt(profile.body_pt)
    normal.paragraph_format.space_before = Pt(0)
    normal.paragraph_format.space_after = Pt(profile.space_after_pt)
    if profile.line_pt is not None:
        normal.paragraph_format.line_spacing = Pt(profile.line_pt)

    if profile.restyle_headings:
        for level, (size, before, after) in profile.headings.items():
            style = document.styles[f"Heading {level}"]
            style.font.name = BODY_FONT
            style.font.size = Pt(size)
            style.font.bold = True
            style.font.color.rgb = HEADING_INK
            style.paragraph_format.space_before = Pt(before)
            style.paragraph_format.space_after = Pt(after)
            style.paragraph_format.line_spacing = Pt(size + 2)
            style.paragraph_format.keep_with_next = True
    else:
        for level in (1, 2, 3, 4):
            document.styles[f"Heading {level}"].paragraph_format.keep_with_next = True

    for name in ("List Bullet", "List Bullet 2"):
        style = document.styles[name]
        style.font.size = Pt(profile.body_pt)
        style.paragraph_format.space_after = Pt(profile.list_gap_pt)
        if profile.line_pt is not None:
            style.paragraph_format.line_spacing = Pt(profile.line_pt)

    if profile.footer:
        add_footer(document, profile)
    return document


def add_footer(document: Document, profile: Profile) -> None:
    section = document.sections[0]
    paragraph = section.footer.paragraphs[0]
    paragraph.paragraph_format.tab_stops.add_tab_stop(
        Inches(8.5 - 2 * profile.margin_lr), WD_TAB_ALIGNMENT.RIGHT
    )
    run = paragraph.add_run(
        "JLCVSO 2027 session — military service credit purchase price deadline\t"
    )
    run.font.name = BODY_FONT
    run.font.size = Pt(8)
    page_number_field(paragraph, 8)


def set_properties(document: Document, title: str) -> None:
    props = document.core_properties
    props.title = title
    props.author = "Policy Development Team"
    props.last_modified_by = "Policy Development Team"
    props.category = "Legislative brief — 2027 Virginia General Assembly session"
    props.subject = (
        "Virginia Retirement System § 51.1-142.2 military service credit "
        "purchase price deadline"
    )
    # The OPC "description" property is capped at 255 characters, so a long
    # provenance banner goes into the body as hidden text instead.
    props.comments = (
        "Generated from the Markdown source of record by tools/md_to_docx.py. "
        "The .md file in the repository is authoritative; regenerate rather "
        "than hand-editing it."
    )


PROVENANCE_LABEL = (
    "[Source provenance, hidden text — not printed. Reveal with Word's "
    "Show/Hide formatting marks.]"
)


def add_hidden_provenance(document: Document, provenance: str) -> None:
    """Carry the source file's HTML provenance comment without printing it.

    The leave-behind's Markdown opens with a HOLD / superseded-figures banner
    that must not be lost in conversion but also must not eat a line of a
    document that has to stay on one letter page. Word hidden text (w:vanish)
    is excluded from layout unless the reader turns it on.
    """
    paragraph = document.add_paragraph()
    paragraph.paragraph_format.space_before = Pt(0)
    paragraph.paragraph_format.space_after = Pt(0)
    run = paragraph.add_run(f"{PROVENANCE_LABEL} {provenance}")
    run.font.size = Pt(7.5)
    run.font.hidden = True


# --------------------------------------------------------------------------
# Block-level rendering
# --------------------------------------------------------------------------

BULLET = re.compile(r"^([-*+])\s+(.*)$")
ORDERED = re.compile(r"^(\d+)[.)]\s+(.*)$")
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
RULE = re.compile(r"^\s*(-{3,}|\*{3,}|_{3,})\s*$")


def is_separator(line: str) -> bool:
    return bool(re.fullmatch(r"\s*\|?[\s:|-]+\|?\s*", line)) and "-" in line


def split_row(line: str) -> list[str]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    return [cell.strip() for cell in stripped.split("|")]


def column_alignments(divider: str) -> list[int]:
    alignments = []
    for cell in split_row(divider):
        if cell.startswith(":") and cell.endswith(":"):
            alignments.append(WD_ALIGN_PARAGRAPH.CENTER)
        elif cell.endswith(":"):
            alignments.append(WD_ALIGN_PARAGRAPH.RIGHT)
        else:
            alignments.append(WD_ALIGN_PARAGRAPH.LEFT)
    return alignments


def extract_provenance(lines: list[str]) -> tuple[int, str | None]:
    """Consume a leading HTML comment; return (next index, flattened text)."""
    index = 0
    while index < len(lines) and not lines[index].strip():
        index += 1
    if index >= len(lines) or not lines[index].lstrip().startswith("<!--"):
        return 0, None

    collected = []
    while index < len(lines):
        collected.append(lines[index])
        if "-->" in lines[index]:
            index += 1
            break
        index += 1
    text = "\n".join(collected).replace("<!--", "").replace("-->", "")
    text = re.sub(r"={4,}", " ", text)
    return index, re.sub(r"\s+", " ", text).strip()


def render(markdown: str, profile: Profile, title: str) -> Document:
    lines = markdown.replace("\r\n", "\n").split("\n")
    index, provenance = extract_provenance(lines)

    document = new_document(profile)
    set_properties(document, title)

    while index < len(lines):
        raw, stripped = lines[index], lines[index].strip()

        if not stripped:
            index += 1
            continue

        if stripped.startswith("<!--"):
            while index < len(lines) and "-->" not in lines[index]:
                index += 1
            index += 1
            continue

        if stripped.startswith("```"):
            index += 1
            body = []
            while index < len(lines) and not lines[index].strip().startswith("```"):
                body.append(lines[index])
                index += 1
            index += 1
            add_code_block(document, body, profile)
            continue

        if stripped.startswith("|") and index + 1 < len(lines) \
                and is_separator(lines[index + 1]):
            header = split_row(stripped)
            alignments = column_alignments(lines[index + 1])
            index += 2
            rows = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                rows.append(split_row(lines[index]))
                index += 1
            add_table(document, header, rows, alignments, profile)
            continue

        if RULE.match(raw):
            if profile.render_rules:
                add_rule(document)
            index += 1
            continue

        heading = HEADING.match(stripped)
        if heading:
            level = min(len(heading.group(1)), 4)
            paragraph = document.add_heading("", level=level)
            # No size/colour overrides: the heading style governs, so the
            # document stays restyleable in Word.
            add_spans(paragraph, parse_inline(heading.group(2).strip()), profile)
            index += 1
            continue

        if stripped.startswith(">"):
            block = []
            while index < len(lines) and lines[index].strip().startswith(">"):
                block.append(re.sub(r"^\s*>\s?", "", lines[index]))
                index += 1
            render_quote(document, block, profile)
            continue

        bullet = BULLET.match(stripped)
        ordered = ORDERED.match(stripped)
        if bullet or ordered:
            text = (bullet or ordered).group(2).strip()
            index += 1
            # Wrapped continuation lines belong to the item they follow.
            while index < len(lines):
                nxt = lines[index]
                peek = nxt.strip()
                if not peek or not nxt.startswith(" ") or BULLET.match(peek) \
                        or ORDERED.match(peek) or HEADING.match(peek):
                    break
                text += " " + peek
                index += 1
            if ordered:
                add_ordered_item(document, ordered.group(1), text, profile)
            else:
                add_bullet_item(document, text, profile)
            continue

        # Hard-wrapped paragraph: join until a blank line or a new block.
        block = [stripped]
        index += 1
        while index < len(lines):
            nxt, peek = lines[index], lines[index].strip()
            if not peek or HEADING.match(peek) or RULE.match(nxt) \
                    or peek.startswith(("|", ">", "```", "<!--")) \
                    or BULLET.match(peek) or ORDERED.match(peek):
                break
            block.append(peek)
            index += 1
        add_spans(document.add_paragraph(), parse_inline(" ".join(block)), profile)

    if provenance:
        add_hidden_provenance(document, provenance)
    return document


def quote_indent_pt(profile: Profile) -> float:
    return 12.0 if profile is BRIEF else 24.0


def render_quote(document: Document, lines: list[str], profile: Profile) -> None:
    """Render the inside of a blockquote, preserving its block structure.

    A quote in this package is not always one run of prose. The F-1 correction
    in Annex 2 carries a formula block and two priced tables inside a single
    quote, and flattening a quote to one joined line turns those into a wall of
    pipes and stray backticks -- which is exactly what verify_docx.py caught.
    So the quote body is re-dispatched through the same helpers the equivalent
    top-level block would use, indented to sit under the quote. Only the
    constructs the package actually puts inside a quote are handled; anything
    else falls through to quoted prose, as before.

    `lines` are the quote lines with their "> " markers already removed and
    their own indentation intact, because code inside a quote keeps it.
    """
    indent = quote_indent_pt(profile)
    index = 0
    while index < len(lines):
        stripped = lines[index].strip()

        if not stripped:
            index += 1
            continue

        if stripped.startswith("```"):
            index += 1
            body = []
            while index < len(lines) and not lines[index].strip().startswith("```"):
                body.append(lines[index])
                index += 1
            index += 1
            add_code_block(document, body, profile, indent_pt=indent + 12)
            continue

        if stripped.startswith("|") and index + 1 < len(lines) \
                and is_separator(lines[index + 1]):
            header = split_row(stripped)
            alignments = column_alignments(lines[index + 1])
            index += 2
            rows = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                rows.append(split_row(lines[index]))
                index += 1
            add_table(document, header, rows, alignments, profile,
                      indent_pt=indent)
            continue

        if RULE.match(stripped):
            index += 1
            continue

        heading = HEADING.match(stripped)
        if heading:
            paragraph = document.add_heading("", level=min(len(heading.group(1)), 4))
            paragraph.paragraph_format.left_indent = Pt(indent)
            add_spans(paragraph, parse_inline(heading.group(2).strip()), profile)
            index += 1
            continue

        bullet = BULLET.match(stripped)
        ordered = ORDERED.match(stripped)
        if bullet or ordered:
            text = (bullet or ordered).group(2).strip()
            index += 1
            if ordered:
                add_ordered_item(document, ordered.group(1), text, profile,
                                 indent_pt=indent)
            else:
                add_bullet_item(document, text, profile, indent_pt=indent)
            continue

        # Quoted prose: join hard-wrapped lines up to a blank line or a new
        # block, so a multi-paragraph quote stays multi-paragraph.
        block = [stripped]
        index += 1
        while index < len(lines):
            peek = lines[index].strip()
            if not peek or peek.startswith(("|", "```")) or HEADING.match(peek) \
                    or RULE.match(peek) or BULLET.match(peek) or ORDERED.match(peek):
                break
            block.append(peek)
            index += 1
        add_blockquote(document, " ".join(block), profile)


def add_rule(document: Document) -> None:
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = paragraph.add_run("* * *")
    run.font.size = Pt(9)
    run.font.color.rgb = RULE_GREY


def add_bullet_item(document: Document, text: str, profile: Profile,
                    indent_pt: float = 0.0) -> None:
    paragraph = document.add_paragraph(style="List Bullet")
    if indent_pt:
        # The style's own 0.25in hanging indent, shifted under the quote.
        paragraph.paragraph_format.left_indent = Inches(0.25) + Pt(indent_pt)
    add_spans(paragraph, parse_inline(text), profile)


def add_ordered_item(document: Document, number: str, text: str,
                     profile: Profile, indent_pt: float = 0.0) -> None:
    """Literal numbers with a hanging indent, not Word's automatic numbering.

    The brief and its annexes cross-reference items by number
    ("recommendation item 3"), so the numbers must match the Markdown exactly.
    Word's List Number style numbers continuously across the many separate
    ordered lists in these documents, which would silently renumber them.
    """
    paragraph = document.add_paragraph()
    fmt = paragraph.paragraph_format
    fmt.left_indent = Inches(0.3) + Pt(indent_pt)
    fmt.first_line_indent = Inches(-0.3)
    fmt.space_after = Pt(profile.list_gap_pt)
    paragraph.add_run(f"{number}.\t").bold = True
    add_spans(paragraph, parse_inline(text), profile)


def add_blockquote(document: Document, text: str, profile: Profile) -> None:
    paragraph = document.add_paragraph()
    fmt = paragraph.paragraph_format
    fmt.left_indent = Pt(12 if profile is BRIEF else 24)
    fmt.space_before = Pt(profile.space_after_pt)
    fmt.space_after = Pt(profile.space_after_pt)
    add_spans(paragraph, parse_inline(text), profile,
              size_pt=profile.quote_pt, color=QUOTE_GREY, force_italic=True)


def add_code_block(document: Document, body: list[str], profile: Profile,
                   indent_pt: float = 12.0) -> None:
    while body and not body[0].strip():
        body.pop(0)
    while body and not body[-1].strip():
        body.pop()
    if not body:
        return
    for position, text in enumerate(body):
        paragraph = document.add_paragraph()
        fmt = paragraph.paragraph_format
        fmt.left_indent = Pt(indent_pt)
        fmt.space_before = Pt(profile.space_after_pt if position == 0 else 0)
        fmt.space_after = Pt(
            profile.space_after_pt if position == len(body) - 1 else 0
        )
        fmt.line_spacing = Pt(profile.code_pt + 2)
        run = paragraph.add_run(text if text.strip() else " ")
        run.font.name = MONO_FONT
        run.font.size = Pt(profile.code_pt)
        run.font.color.rgb = CODE_GREY


def add_table(document: Document, header: list[str], rows: list[list[str]],
              alignments: list[int], profile: Profile,
              indent_pt: float = 0.0) -> None:
    columns = max([len(header)] + [len(row) for row in rows])
    table = document.add_table(rows=0, cols=columns)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    if indent_pt:
        set_table_indent(table, indent_pt)

    def fill(values: list[str], is_header: bool) -> None:
        cells = table.add_row().cells
        for position, cell in enumerate(cells):
            text = values[position] if position < len(values) else ""
            paragraph = cell.paragraphs[0]
            paragraph.paragraph_format.space_before = Pt(1)
            paragraph.paragraph_format.space_after = Pt(1)
            if profile.line_pt is not None:
                paragraph.paragraph_format.line_spacing = Pt(profile.table_pt + 2)
            if position < len(alignments):
                paragraph.alignment = alignments[position]
            add_spans(paragraph, parse_inline(text), profile,
                      size_pt=profile.table_pt, force_bold=is_header)

    fill(header, True)
    repeat_header_row(table.rows[0])
    for values in rows:
        fill(values, False)

    # A sized spacer rather than a full empty body paragraph.
    spacer = document.add_paragraph()
    spacer.paragraph_format.space_before = Pt(0)
    spacer.paragraph_format.space_after = Pt(0)
    spacer.paragraph_format.line_spacing = Pt(4)
    spacer.add_run("").font.size = Pt(4)


# --------------------------------------------------------------------------
# Package driver
# --------------------------------------------------------------------------

# Only the fixed-length leave-behind needs the compact layout; everything else
# in the package is a memo. Driven by a glob rather than a file list so that
# documents added to the package later are converted without editing this tool.
BRIEF_LAYOUT_FILES = {"00-ONE-PAGE-BRIEF.md"}

# Document titles for Word's File > Info pane. Anything not listed falls back
# to the file's own first H1.
TITLE_OVERRIDES = {
    "00-ONE-PAGE-BRIEF.md":
        "One-Page Brief — Military Service Credit Price Deadline "
        "(JLCVSO, 2027 Session)",
    "README.md":
        "Brief Package Index and Status — Military Service Credit Price Deadline",
}


def profile_for(path: Path) -> Profile:
    return BRIEF if path.name in BRIEF_LAYOUT_FILES else MEMO


def title_for(path: Path, markdown: str) -> str:
    if path.name in TITLE_OVERRIDES:
        return TITLE_OVERRIDES[path.name]
    heading = re.search(r"^#\s+(.*)$", markdown, flags=re.M)
    if heading:
        return re.sub(r"\*\*|`|\*", "", heading.group(1)).strip()
    return path.stem


def convert(source: Path) -> tuple[Path, Profile]:
    markdown = source.read_text(encoding="utf-8")
    profile = profile_for(source)
    destination = source.with_suffix(".docx")
    render(markdown, profile, title_for(source, markdown)).save(destination)
    return destination, profile


def main(argv: list[str]) -> int:
    targets = ([Path(argument).resolve() for argument in argv] if argv
               else sorted(BRIEF_DIR.glob("*.md")))
    for source in targets:
        out, profile = convert(source)
        label = (out.relative_to(REPO_ROOT) if out.is_relative_to(REPO_ROOT)
                 else out)
        print(f"{label}  [{profile.name}]  "
              f"{out.stat().st_size / 1024:.0f} KB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
