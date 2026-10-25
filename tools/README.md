# tools

Document tooling for the brief packages. Run from the repository root.

| Script | What it does |
|---|---|
| [md_to_docx.py](md_to_docx.py) | Converts every `.md` in a brief folder to an editable `.docx`. Two layouts: a *memo* layout for the full brief and annexes, and a compact *brief* layout for the fixed-length one-page leave-behind. |
| [verify_docx.py](verify_docx.py) | Checks each generated `.docx` against its Markdown source — word-by-word, and figure-by-figure as a multiset. Non-zero exit on any mismatch, so it can gate a commit. |
| [pagecheck.py](pagecheck.py) | Estimates rendered page length from the same page geometry the `.docx` is written with, using real glyph widths. Confirms a one-page brief is one page. |

```
python3 tools/md_to_docx.py      # rebuild every .docx in the 2027 brief folder
python3 tools/verify_docx.py     # fidelity check — must pass before committing
python3 tools/pagecheck.py       # one-pager vs a one-page budget
```

Each takes an optional file path to work on a single document.

## Why these exist rather than pandoc

Neither pandoc nor LibreOffice is installed in the working environment, and Word
automation on this machine proved unreliable. Converting directly with
`python-docx` also keeps the output deterministic and reviewable, and it is how
the team's earlier VRSLite package was produced — `md_to_docx.py` deliberately
follows that package's Calibri house style so the Word files look like the ones
the team already works in. Its module docstring lists the five places it departs
from the earlier tool and why.

## The rule that matters

**Markdown is the source of record; the `.docx` files are generated artifacts.**
A hand-edit to a `.docx` will be lost on the next rebuild. Carry changes back into
the `.md`, regenerate, and re-run `verify_docx.py`.

That verifier is not ceremony. This is a fiscal package whose headline figure has
already been corrected once in public, and the Word copies are what get forwarded
to legislative staff. A silently dropped digit there is a worse failure than any
layout problem, so the figures are checked rather than eyeballed.
