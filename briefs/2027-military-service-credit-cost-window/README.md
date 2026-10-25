# Military Service Credit Cost Window — 2027 Session Package

**Proposal:** Amend § 51.1-142.2 of the Code of Virginia so that a veteran employed
by the Commonwealth may purchase up to four years of prior active duty military
service credit at the approximate normal cost at any point in their career, rather
than only within the first 24 months after their first date of hire.

## Contents

Read in this order. Most legislators and staff should never need to go past file 00.

| File | Audience | Contents |
|---|---|---|
| [00-ONE-PAGE-BRIEF.pdf](00-ONE-PAGE-BRIEF.pdf) | **Senators, delegates, busy staff — the printed leave-behind** | **HOLD LIFTED 10/25/2026 — cleared to print.** Regenerated against brief v1.2: $0 general fund leads, the $13M–$182M present value is stated in our own words, take-up is named as the swing factor, and the HB 1867 comparison closes. One page, letter. |
| [00-ONE-PAGE-BRIEF.md](00-ONE-PAGE-BRIEF.md) | Same content, editable | Markdown source of the one-pager. **Cost block revised 10/25/2026** (Option C, board-accepted) along with the five mechanical fixes that rode the same reprint. |
| [00-ONE-PAGE-BRIEF.html](00-ONE-PAGE-BRIEF.html) | — | Print template for the PDF. Regenerate with:<br>`"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --no-pdf-header-footer --print-to-pdf=00-ONE-PAGE-BRIEF.pdf file://$PWD/00-ONE-PAGE-BRIEF.html` |
| [01-JLC-Legislative-Change-Brief.md](01-JLC-Legislative-Change-Brief.md) | Legislative staff who want the backup | Same four sections, with every figure, citation and the fallback positions. **v1.2 — carries the re-scoped cost figure.** |
| [02-Annex-A-Legal-Analysis-and-Draft-Bill.md](02-Annex-A-Legal-Analysis-and-Draft-Bill.md) | Division of Legislative Services, VRS counsel | Draft bill language, defined-term analysis, statutory conflicts, unintended-effects check, alternatives, open questions. **v1.1 — the rate-schedule authority is now graded on age *and* creditable service, and the alternate hazardous duty option is addressed. This is the version to transmit.** |
| [03-Annex-B-Fiscal-Assumptions-and-Sources.md](03-Annex-B-Fiscal-Assumptions-and-Sources.md) | VRS actuaries, House Appropriations, Senate Finance & Appropriations | Claim/evidence table, fiscal assumption register, full cost model, unverified claims, primary sources |
| [04-Annex-2-Closure-FM1-FM5.md](04-Annex-2-Closure-FM1-FM5.md) | VRS actuaries, House Appropriations, Senate Finance & Appropriations | **Closes the five fiscal open items.** Official plan and employer-group denominators, the AEC/ANC multiple surface, every rate group including hazardous duty, the acceleration decomposition with take-up sensitivity, and the July 1, 2026 rate question. Supersedes Annex B's population and total-cost figures. |
| [models/fm_model.py](models/fm_model.py) | Anyone checking the arithmetic | The reproducible model behind Annex 2 Closure. Every input tagged OFFICIAL / DERIVED / ESTIMATE. Run `python3 fm_model.py`. |

## Status

| Component | Status |
|---|---|
| Title 51.1 legal analysis and draft language | **Complete, v1.1.** Counsel sign-off given; **cleared to go to the Division of Legislative Services** |
| Fiscal estimate | **Analyst estimate.** Requires VRS actuarial confirmation (Annex A, Q1–Q5) |
| Stakeholder analysis | Not started |
| Red team / adversarial counsel review | Not started |
| JLCVSO policy decisions | **Scope and transition decided 10/24/2026: all VRS members, no local opt-in, immediate access. Draft already conforms.** Concession ladder (Annex A, Q12) still open. |
| Fiscal re-scope to full VRS membership (required by the scope decision) | **Complete — see [04-Annex-2-Closure-FM1-FM5.md](04-Annex-2-Closure-FM1-FM5.md)** |
| Fiscal open items FM-1 … FM-5 | **Closed 10/24/2026.** FM-3 and FM-5 fully official; FM-1 a sourced range plus a drafted VRS request; FM-2 and FM-4 modelled with the basis shown |
| Re-scoped figure applied to the full brief (01) | **Complete 10/24/2026 — v1.2.** All ten mechanical corrections from Annex 2 Closure applied, plus items 11–13 (the guardrail dial, three-way exposure split, DPB SOQ request) |
| Re-scoped figure applied to the one-page leave-behind (00) | **Complete 10/25/2026.** Board accepted Option C (lead with $0 general fund, state the range in our own words, name take-up as the swing factor, close with HB 1867). PDF regenerated; HOLD lifted |
| Annex A rate-schedule authority ("age" → "age and creditable service") | **Closed 10/25/2026 — Annex A v1.1, § 2.2.** Widened to age and creditable service, with the amount purchased added as a factor, publication and uniformity requirements, an actuarial-equivalent-cost ceiling, and an express no-spillover sentence confining the schedule to subdivision B 2. Counsel analysis at § 2.5. The package is now internally consistent |
| Alternate hazardous duty option (10.01%, no plan column) | **Closed for the bill 10/25/2026 — Annex A v1.1, § 2.6.** Reached for subdivision B 2 purchases by factor (v) of the § 2.2 schedule authority, anchored to "the benefits permitted by § 51.1-138." The same pre-existing mismatch for other purchase categories is deliberately left alone. Two confirmations open at Annex A Q13–Q14 |

> **Carried figures that are now superseded.** The re-scope changed the headline.
> Brief v1.0/v1.1 and Annex B carry "under $2 million one-time," built on state
> classified employees only and on the price-discount channel only. Re-scoped to
> all three plans and all employer groups, and with retirement-date acceleration
> priced, the modelled one-time present value of recommendation A-3 is **on the
> order of $13M–$182M** depending on pool and take-up. See Annex 2 Closure,
> FM-4 § 4.4, and the HB 1867 cross-check at § 4.6. **Do not quote the $2 million
> figure.** The full brief (01) and the one-pager (00) now carry the corrected
> figure; **Annex B does not.**

> **Board decision, now closed.** The present-value liability is in the tens of
> millions while the general fund ask remains, correctly, $0. Both are true — this is
> an employer-contribution-rate liability amortised under the VRS Funding Policy, not
> an appropriation — but which one leads on a one-page leave-behind was a political
> judgment, not a modelling one. Put to the board on **MOO-293** and **answered
> 10/25/2026: Option C.** $0 general fund leads as the headline claim; the
> $13M–$182M range is stated in our own words with take-up named as the swing factor
> and the data request attached; the HB 1867 cross-check closes rather than opens.
> The PDF has been regenerated on that basis and the hold is lifted.

**Not final.** Do not present as final until VRS actuarial figures are in hand and
the red-team review records a verdict.
