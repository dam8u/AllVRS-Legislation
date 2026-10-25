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
| [03-Annex-B-Fiscal-Assumptions-and-Sources.md](03-Annex-B-Fiscal-Assumptions-and-Sources.md) | VRS actuaries, House Appropriations, Senate Finance & Appropriations | **The package's evidence base — v2.0, reconciled.** Verified-fact register (the single pinpoint index for the whole package), assumption register with owner and sensitivity for every judgment in the model, the cost methodology, what a veteran pays today at published rates, open-claims index, consolidated primary sources, and a reconciliation log. **Carries no total-cost figure at all** — see the division-of-labour rule at its § 0. |
| [04-Annex-2-Closure-FM1-FM5.md](04-Annex-2-Closure-FM1-FM5.md) | VRS actuaries, House Appropriations, Senate Finance & Appropriations | **The package's cost figures — every derived and estimated number lives here.** Closes the five fiscal open items: official plan and employer-group denominators, the AEC/ANC multiple surface, every rate group including hazardous duty, the acceleration decomposition with take-up sensitivity, the exposure split, the guardrail dials, and the July 1, 2026 rate question. |
| [06-Annex-C-Stakeholder-Analysis.md](06-Annex-C-Stakeholder-Analysis.md) | **Policy Director, patron selection, anyone walking the halls** | **The political map — v1.0.** Concrete effects, stakeholder table with a reason and a confidence label on every row, the committee and subcommittee path with what each venue has done with similar bills, the real fight, the coalition ladder with the price of each ally, other-state precedent on purchase timing, patron recommendations, and the unknowns. Desk research on the public record only; no stakeholder was contacted. |
| [models/fm_model.py](models/fm_model.py) | Anyone checking the arithmetic | The reproducible model behind Annex 2 Closure. Every input tagged OFFICIAL / DERIVED / ESTIMATE. Run `python3 fm_model.py`. |

## Editable Word copies

Every Markdown file in this folder has a `.docx` twin alongside it, for anyone who
needs to edit, comment or track changes in Word — including
[00-ONE-PAGE-BRIEF.docx](00-ONE-PAGE-BRIEF.docx), the editable counterpart of the
printed leave-behind.

**The Markdown is the source of record.** The `.docx` files are generated, and a
hand-edit to one will be overwritten the next time they are rebuilt. Carry changes
back into the `.md` and regenerate, from the repository root:

```
python3 tools/md_to_docx.py      # rebuild every .docx in this folder
python3 tools/verify_docx.py     # word-by-word and figure-by-figure fidelity check
python3 tools/pagecheck.py       # confirm the one-pager still fits one letter page
```

`verify_docx.py` exists because a dropped digit in a Word copy is a worse failure
than a layout problem — the Word copy is the one that gets forwarded and edited. It
reconstructs the text of each `.docx` and diffs it against the Markdown, then
compares every money, percent and Code-section figure as a multiset, so a changed
count cannot hide inside an otherwise-matching diff. See
[tools/README.md](../../tools/README.md).

## Status

> **Read this before quoting any figure out of the table below. Lead attorney,
> October 25, 2026, 12:40.**
>
> The package is mid-reconciliation after the red team verdict, and the cost band has
> moved three times in one day. **The current authority is the banner at the top of
> [00-ONE-PAGE-BRIEF.md](00-ONE-PAGE-BRIEF.md), v1.3**, which states the corrected
> model run: **$28M–$166M** one-time present value, after the red team S-3 pool-pairing
> fix and with the floor taken from the current 10%–30% scenario set. That band
> **supersedes both `$13M–$182M` and the `$26M–$182M` interim figure**, and both of
> those appear in rows below that have not yet been rewritten.
>
> **Four retracted figures. Do not quote any of them:** "under $2 million one-time",
> "under $100,000 a year", **"$13M–$182M"**, **"$26M–$182M"**. Also retracted as a
> *claim*: **"General fund cost: $0"** — the defensible form is "this bill requests no
> appropriation" (red team F-2, now fixed in 00 v1.3).
>
> **Files 01, 03 and 04 are being reconciled to the $28M–$166M band separately** and
> still carry superseded figures until that lands. Of the fatal findings, **F-2 is
> fixed** in 00 v1.3; **F-1 is resolved in substance** — the guardrail is a mitigation
> worth roughly 59%–66% of the above-ANC excess, not a neutrality device — but the
> drafting choice it forces is open at Annex A Q3a and Q12.
>
> Everything in the table below pre-dates this banner where the two disagree.

| Component | Status |
|---|---|
| Title 51.1 legal analysis and draft language | **Complete, v1.1.** Counsel sign-off given; **cleared to go to the Division of Legislative Services** |
| Fiscal estimate | **Analyst estimate.** Requires VRS actuarial confirmation (Annex A, Q1–Q5) |
| Stakeholder analysis | **Complete, v1.0 — see [06-Annex-C-Stakeholder-Analysis.md](06-Annex-C-Stakeholder-Analysis.md).** The chokepoint is the **House Appropriations Subcommittee on Compensation and Retirement**, which tabled the closest analogue (HB 1867, 2023) **8-0** and killed **27 of the 28** VRS bills before it in 2026. The real fight is the price, not the deadline. Reconciled against the Red Team's F-1 and F-2 |
| Red team / adversarial counsel review | **Verdict recorded 10/25/2026 — see [05-Red-Team-Review.md](05-Red-Team-Review.md)** and the second, parallel review at [05-Red-Team-and-Counsel-Review.md](05-Red-Team-and-Counsel-Review.md). 18 findings: 2 fatal, 8 serious, 6 moderate, 2 minor. **Do not file until F-1 and F-2 are resolved.** **F-1 — resolved in the fiscal annexes 10/25/2026:** the 100%-recovery guardrail that drives the fiscal note to zero cannot be built from the authority Annex A § 2.2 grants. Verified over 60 priceable classes; a *lawful uniform* class rate recovers 0%–96% by classification, **59%–66% at the class mean**, and only ~23% in the long-service Plan 1 cohort the bill leads with. **The residual is $20M–$48M at 20% take-up, not $0.** The guardrail is a mitigation, not a neutrality device. See Annex 2 Closure § 4.8.1 and Annex B v2.1 A-28. **What stays open on F-1 is the drafting choice it forces** — Annex A Q3a and Q12 both need reframing. **F-2 — NOT yet resolved:** "General fund cost: $0" is contradicted by the package's own who-bears table ($20M–$40M on state agencies, GF + NGF; $13M–$33M on school divisions through the SOQ) and is still on the printed leave-behind. The one-pager is back on hold until it is fixed |
| JLCVSO policy decisions | **Scope and transition decided 10/24/2026: all VRS members, no local opt-in, immediate access. Draft already conforms.** Concession ladder (Annex A, Q12) still open. |
| Fiscal re-scope to full VRS membership (required by the scope decision) | **Complete — see [04-Annex-2-Closure-FM1-FM5.md](04-Annex-2-Closure-FM1-FM5.md)** |
| Fiscal open items FM-1 … FM-5 | **Closed 10/24/2026.** FM-3 and FM-5 fully official; FM-1 a sourced range plus a drafted VRS request; FM-2 and FM-4 modelled with the basis shown |
| Re-scoped figure applied to the full brief (01) | **Complete 10/24/2026 — v1.2.** All ten mechanical corrections from Annex 2 Closure applied, plus items 11–13 (the guardrail dial, three-way exposure split, DPB SOQ request) |
| Re-scoped figure applied to the one-page leave-behind (00) | **Applied 10/25/2026, then put back on HOLD the same day.** The board accepted Option C of the MOO-293 framing decision (lead with $0 general fund, state the range in our own words, name take-up as the swing factor, close with HB 1867) and the PDF was regenerated on it. **The hold was then re-imposed on the lead attorney's sign-off**, because Option C settled the framing but the board was not asked about the red team verdict, which had not yet been recorded. Two defects remain in the body copy: **F-2** (the "$0 general fund" overclaim, rated fatal) and the range itself — **"$13M–$182M" mixes the superseded 5% floor with the current 30% ceiling; the range to publish is $26M–$182M** (Annex B v2.1, A-22). `00-ONE-PAGE-BRIEF.md`, `.html`, `.pdf` and `.docx` all carry both and are all on hold. Fixing them is a drafting job against a fixed one-page budget |
| Annex A rate-schedule authority ("age" → "age and creditable service") | **Closed 10/25/2026 — Annex A v1.1, § 2.2.** Widened to age and creditable service, with the amount purchased added as a factor, publication and uniformity requirements, an actuarial-equivalent-cost ceiling, and an express no-spillover sentence confining the schedule to subdivision B 2. Counsel analysis at § 2.5. The package is now internally consistent |
| HB 1867 (2023) fiscal impact statement — pinpoint and re-read | **Closed 10/25/2026 — Annex B F-56, F-60…F-63, § 7.5.** Retrieved from LIS (HB1867F158, 1/16/2023). It carried more than the package was citing: VRS's own worked total of **$50M for teachers alone at 1% take-up on a $35,000 average**, which reframes the $13M–$182M range as the same order of magnitude as VRS's only published figure for a benefit of this shape and "under $2 million" as the outlier; our priced-to-free ratio of 0.704 lands inside the 0.638–0.718 band the AEC/ANC multiples predict; VRS's own statement that it **cannot identify** who holds the service; and a § 30-19.1:7 precedent that supports the *narrow* general-fund claim ("no appropriation requested") while refuting the broad one — VRS wrote "no **immediate** impact" and, beside it, that contribution rates may move over time, which makes F-61 evidence **for** Red Team F-2. Annex 2 Closure § 4.6 rewritten on it |
| Annex B reconciliation (the last file carrying pre-re-scope figures) | **Closed 10/25/2026 — Annex B v2.0.** Rewritten as the package's evidence base under a non-duplication rule: official facts here, derived and estimated figures in Annex 2 Closure only, so the two cannot diverge. Population and total-cost arithmetic removed; A-08…A-15 formally retired with a mapping to their replacements; four reconciliation checks logged at § 7, one of which corrects A-03 (Plan 1 COLA 3.0% → Board-adopted 2.50%) and one of which validates the live model's inherited salary basis to within 0.5%. New: member-price table for hazardous duty and judicial groups. **Annex B is cleared to circulate outside the working group** |
| Alternate hazardous duty option (10.01%, no plan column) | **Closed for the bill 10/25/2026 — Annex A v1.1, § 2.6.** Reached for subdivision B 2 purchases by factor (v) of the § 2.2 schedule authority, anchored to "the benefits permitted by § 51.1-138." The same pre-existing mismatch for other purchase categories is deliberately left alone. Two confirmations open at Annex A Q13–Q14 |

> **The superseded cost figure — retracted everywhere in the package as of 10/25/2026.**
> Brief v1.0/v1.1 and Annex B v1.1 carried "under $2 million one-time, under $100,000
> per year," built on state classified employees only and on the price-discount channel
> only. Re-scoped to all three plans and all employer groups, and with retirement-date
> acceleration priced, the modelled one-time present value of recommendation A-3 is
> **on the order of $26M–$182M** depending on pool and take-up, before the Board's
> graded rate schedule; **the residual after a lawful schedule is $20M–$48M at 20%
> take-up** (Annex 2 Closure § 4.8.1). See Annex 2 Closure, FM-4 § 4.4, and the
> HB 1867 cross-check at § 4.6.
>
> **Two figures are now retracted, not one. Do not quote the $2 million figure, and
> do not quote "$13M–$182M" either.** That range took its floor from the 5% take-up
> row, which belongs to the superseded v1.1 band, and its ceiling from the 30% row of
> the current scenario set — one range built from two assumption sets (Annex B v2.1,
> A-22, per red team S-5). On the current scenario set (Low 10% / Moderate 20% /
> High 30%) the range to publish is **$26M–$182M**.
>
> **The general fund ask remains, correctly, $0 — but say it the narrow way.** "This
> bill requests no appropriation" is true and defensible. **"General fund cost: $0" is
> not**, and is rated fatal at red team F-2: the state-agency and Standards-of-Quality
> shares of the employer contribution rates do reach the general fund in later
> biennia. See Annex B § 1 and F-61.
>
> **Annex B v2.1 states no total-cost figure by design** and records at its § 7.4 why
> the old one was wrong, so the retraction can be defended rather than merely
> asserted. **Not yet carrying the corrected figure: the one-pager (00), which is on
> hold for exactly this reason.** The full brief (01) states the range and needs the
> $13M–$182M → $26M–$182M correction applied with the F-1 residual.
>
> **How the two fiscal annexes divide, so that neither can be quoted against the other.**
> **OFFICIAL published values live in Annex B § 1**, cited once with a pinpoint.
> **Every DERIVED or ESTIMATED value lives in Annex 2 Closure only**, with Annex B
> carrying the pointer, owner and sensitivity but never the figure. The two documents
> compute nothing in common. Full rule and allocation table at Annex B § 0.

> **Board decision, now closed.** The present-value liability is in the tens of
> millions while the general fund ask remains, correctly, $0. Both are true — this is
> an employer-contribution-rate liability amortised under the VRS Funding Policy, not
> an appropriation — but which one leads on a one-page leave-behind was a political
> judgment, not a modelling one. Put to the board on **MOO-293** and **answered
> 10/25/2026: Option C.** The general fund ask leads as the headline claim; the range
> is stated in our own words with take-up named as the swing factor and the data
> request attached; the HB 1867 cross-check closes rather than opens.
>
> **Option C stands as a framing decision and is not reopened here.** But it was
> decided before the red team verdict was recorded, and two of the numbers it was
> expressed in have since changed: the headline must read "requests no appropriation"
> rather than "general fund cost: $0" (F-2), and the range is $26M–$182M rather than
> $13M–$182M (A-22). The one-pager has been put back on hold on the lead attorney's
> sign-off until the Option C framing is restated in those terms.

**Not final.** Do not present as final until VRS actuarial figures are in hand and
the red-team review records a verdict.
