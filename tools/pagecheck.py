#!/usr/bin/env python3
"""
Estimate the rendered page length of a brief before it reaches Word.

Ported from the team's earlier VRSLite package
(legislation/military-service-retirement-bridge/source-markdown/pagecheck.py)
and re-pointed at tools/md_to_docx.py's layout profiles, so there is one set of
page-geometry numbers rather than two that can drift apart.

Why it exists: 00-ONE-PAGE-BRIEF is named for its length, so fitting on one
page is a correctness property, not a matter of taste. Neither LibreOffice nor
reliable Word automation is available here, so the length is computed from the
same geometry the .docx is written with, using real glyph widths from PIL.

Deliberately conservative, so a "FITS" verdict holds up in Word:
  * Arial metrics stand in for Calibri. Arial runs roughly 6-8% wider at the
    same point size, so every line is slightly over-measured.
  * Table rows carry full Word default cell margins plus padding.
  * The verdict requires the content to fit within FILL_LIMIT of the text
    block, leaving headroom for Word's own line-breaking differences.

Usage:
    python3 tools/pagecheck.py                      # the one-pager, vs 1 page
    python3 tools/pagecheck.py FILE.md [pages]      # any file, any budget
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

from PIL import ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import md_to_docx as conv

PAGE_W_IN, PAGE_H_IN = 8.5, 11.0
FILL_LIMIT = 0.95              # must fit within this fraction of the text block
TABLE_CELL_MARGIN_PT = 11.52   # Word default 0.08in left + right
TABLE_ROW_PAD_PT = 4.0         # space_before + space_after inside a cell
LIST_INDENT_PT = 18.0          # List Bullet / hanging-indent ordered item

FONT_DIR = "/System/Library/Fonts/Supplemental"
FONTS = {False: os.path.join(FONT_DIR, "Arial.ttf"),
         True: os.path.join(FONT_DIR, "Arial Bold.ttf")}
_font_cache: dict[tuple[float, bool], ImageFont.FreeTypeFont] = {}


def font(size_pt: float, bold: bool = False) -> ImageFont.FreeTypeFont:
    """Arial at a given point size, rasterised at 4x for sub-pixel accuracy."""
    key = (round(size_pt, 2), bold)
    if key not in _font_cache:
        _font_cache[key] = ImageFont.truetype(FONTS[bold], int(round(size_pt * 4)))
    return _font_cache[key]


def strip_markup(text: str) -> str:
    """Reduce inline Markdown to the characters that actually get rendered.

    Links are measured as their label only: md_to_docx.py writes real Word
    hyperlinks, so the URL takes no space on the page.
    """
    text = re.sub(r"\[([^\]]+)\]\([^)\s]+\)", r"\1", text)
    text = re.sub(r"\*\*\*|\*\*|~~|`|\*", "", text)
    return conv.ESCAPE.sub(r"\1", text)


def text_width(text: str, size_pt: float, bold: bool = False) -> float:
    return font(size_pt, bold).getlength(text) / 4.0


def wrapped_lines(text: str, width_pt: float, size_pt: float,
                  bold: bool = False) -> int:
    """Greedy word wrap, matching how Word breaks on spaces."""
    text = strip_markup(text).strip()
    if not text:
        return 1
    lines, current = 1, ""
    for word in text.split():
        trial = f"{current} {word}".strip()
        if current and text_width(trial, size_pt, bold) > width_pt:
            lines, current = lines + 1, word
        else:
            current = trial
    return lines


def column_widths(rows: list[list[str]], total_pt: float,
                  table_pt: float) -> list[float]:
    """Approximate Word's autofit: share width by longest cell per column."""
    columns = max(len(row) for row in rows)
    demand = []
    for index in range(columns):
        longest = max(
            (text_width(strip_markup(row[index]), table_pt, bold=True)
             for row in rows if index < len(row)),
            default=1.0,
        )
        demand.append(max(longest, 1.0))
    usable = total_pt - columns * TABLE_CELL_MARGIN_PT
    scale = usable / sum(demand)
    return [max(value * scale, 18.0) for value in demand]


def table_height(rows: list[list[str]], total_pt: float,
                 profile: conv.Profile) -> float:
    widths = column_widths(rows, total_pt, profile.table_pt)
    line_pt = profile.table_pt * 1.22
    height = 0.0
    for row_index, row in enumerate(rows):
        lines = 1
        for index, cell in enumerate(row):
            if index < len(widths):
                lines = max(lines, wrapped_lines(
                    cell, widths[index], profile.table_pt, bold=(row_index == 0)))
        height += lines * line_pt + TABLE_ROW_PAD_PT
    return height + 4.0  # the sized spacer md_to_docx adds after a table


def heading_metrics(profile: conv.Profile, level: int) -> tuple[float, float, float]:
    """(size, space before, space after) for a heading level.

    The brief profile restyles the heading styles, so its own numbers apply.
    The memo profile leaves Word's default template headings in place; these
    mirror what that template uses.
    """
    if profile.headings:
        return profile.headings[level]
    defaults = {1: (14.0, 24.0, 0.0), 2: (13.0, 10.0, 0.0),
                3: (11.0, 10.0, 0.0), 4: (10.5, 10.0, 0.0)}
    return defaults[level]


def measure(path: Path, profile: conv.Profile) -> tuple[float, list[tuple[float, str]]]:
    """Return (total content height in points, per-block breakdown)."""
    width = (PAGE_W_IN - 2 * profile.margin_lr) * 72
    body = profile.body_pt
    line = profile.line_pt if profile.line_pt is not None else body * 1.22
    after = profile.space_after_pt

    lines_in = path.read_text(encoding="utf-8").replace("\r\n", "\n").split("\n")
    index, provenance = conv.extract_provenance(lines_in)
    total, blocks = 0.0, []

    while index < len(lines_in):
        raw, current = lines_in[index], lines_in[index].strip()
        if not current:
            index += 1
            continue

        if current.startswith("<!--"):
            while index < len(lines_in) and "-->" not in lines_in[index]:
                index += 1
            index += 1
            continue

        if current.startswith("```"):
            index += 1
            count = 0
            while index < len(lines_in) and not lines_in[index].strip().startswith("```"):
                count += 1
                index += 1
            index += 1
            height = count * (profile.code_pt + 2) + 2 * after
            blocks.append((height, f"code block ({count} lines)"))
            total += height
            continue

        if current.startswith("|") and index + 1 < len(lines_in) \
                and conv.is_separator(lines_in[index + 1]):
            rows = [conv.split_row(current)]
            index += 2
            while index < len(lines_in) and lines_in[index].strip().startswith("|"):
                rows.append(conv.split_row(lines_in[index]))
                index += 1
            height = table_height(rows, width, profile)
            blocks.append((height, f"table ({len(rows)} rows)"))
            total += height
            continue

        if conv.RULE.match(raw):
            if not profile.render_rules:
                index += 1
                continue
            height = 9.0 + after
            blocks.append((height, "rule"))
            total += height
            index += 1
            continue

        heading = conv.HEADING.match(current)
        if heading:
            level = min(len(heading.group(1)), 4)
            size, before, after_h = heading_metrics(profile, level)
            count = wrapped_lines(heading.group(2), width, size, bold=True)
            height = count * (size + 2) + before + after_h
            blocks.append((height, f"h{level}: {strip_markup(heading.group(2))[:48]}"))
            total += height
            index += 1
            continue

        if current.startswith(">"):
            quote = []
            while index < len(lines_in) and lines_in[index].strip().startswith(">"):
                quote.append(re.sub(r"^\s*>\s?", "", lines_in[index]).strip())
                index += 1
            text = " ".join(part for part in quote if part)
            indent = 12.0 if profile is conv.BRIEF else 24.0
            count = wrapped_lines(text, width - indent, profile.quote_pt)
            height = count * line + 2 * after
            blocks.append((height, f"blockquote ({count}L)"))
            total += height
            continue

        item = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", raw)
        if item:
            text = item.group(3).strip()
            index += 1
            while index < len(lines_in):
                nxt, peek = lines_in[index], lines_in[index].strip()
                if not peek or not nxt.startswith(" ") \
                        or re.match(r"^([-*+]|\d+[.)])\s+", peek) \
                        or peek.startswith("#"):
                    break
                text += " " + peek
                index += 1
            count = wrapped_lines(text, width - LIST_INDENT_PT, body)
            height = count * line + profile.list_gap_pt
            blocks.append((height, f"list({count}L): {strip_markup(text)[:40]}"))
            total += height
            continue

        buffer = [current]
        index += 1
        while index < len(lines_in):
            nxt, peek = lines_in[index], lines_in[index].strip()
            if (not peek or peek.startswith(("#", ">", "|", "```", "<!--"))
                    or re.match(r"^\s*([-*+]\s+|\d+[.)]\s+)", nxt)
                    or conv.RULE.match(nxt)):
                break
            buffer.append(peek)
            index += 1
        text = " ".join(buffer)
        count = wrapped_lines(text, width, body)
        height = count * line + after
        blocks.append((height, f"p({count}L): {strip_markup(text)[:44]}"))
        total += height

    if provenance:
        blocks.append((0.0, "provenance comment (hidden text, 0 pt)"))
    return total, blocks


def main(argv: list[str]) -> int:
    if argv:
        path = Path(argv[0]).resolve()
        expected = int(argv[1]) if len(argv) > 1 else None
    else:
        path = conv.BRIEF_DIR / "00-ONE-PAGE-BRIEF.md"
        expected = 1

    profile = conv.profile_for(path)
    page_pt = (PAGE_H_IN - 2 * profile.margin_tb) * 72
    total, blocks = measure(path, profile)
    line = profile.line_pt if profile.line_pt is not None else profile.body_pt * 1.22

    print(f"{path.name}  [{profile.name} layout]")
    print(f"  text block per page : {page_pt:.0f} pt "
          f"({PAGE_H_IN - 2 * profile.margin_tb:.2f} in)")
    print(f"  content height      : {total:.0f} pt")
    print(f"  pages (conservative): {total / page_pt:.2f}")

    if expected is None:
        return 0

    budget = page_pt * expected
    fill = total / budget
    print(f"  budget for {expected} page(s): {budget:.0f} pt — fill {fill:.1%}")
    if fill <= FILL_LIMIT:
        slack = budget * FILL_LIMIT - total
        print(f"  VERDICT: FITS ({slack:.0f} pt of slack, ~{slack / line:.1f} body "
              f"lines, below the {FILL_LIMIT:.0%} limit)")
        status = 0
    else:
        over = total - budget * FILL_LIMIT
        print(f"  VERDICT: OVER by {over:.0f} pt "
              f"(~{over / line:.0f} body lines) — must cut")
        status = 1

    print("\n  largest blocks:")
    for height, label in sorted(blocks, reverse=True)[:10]:
        print(f"    {height:6.1f} pt  {label}")
    return status


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
