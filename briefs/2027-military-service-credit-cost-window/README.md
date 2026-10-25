# Military Service Credit Cost Window — 2027 Session Package

**Proposal:** Amend § 51.1-142.2 of the Code of Virginia so that a veteran employed
by the Commonwealth may purchase up to four years of prior active duty military
service credit at the approximate normal cost at any point in their career, rather
than only within the first 24 months after their first date of hire.

## Contents

Read in this order. Most legislators and staff should never need to go past file 00.

| File | Audience | Contents |
|---|---|---|
| [00-ONE-PAGE-BRIEF.pdf](00-ONE-PAGE-BRIEF.pdf) | **Senators, delegates, busy staff — the printed leave-behind** | **ON HOLD for the Policy Director's clearance — not cleared to print.** Regenerated 10/25/2026 against **v1.3**: it requests no appropriation and names the cost-bearers, the **$28M–$166M** present value is stated in our own words, take-up is named as the swing factor, and the HB 1867 comparison closes. One page, letter. Both print-blocking copy defects are fixed; what is outstanding is the clearance decision. |
| [00-ONE-PAGE-BRIEF.md](00-ONE-PAGE-BRIEF.md) | Same content, editable | Markdown source of the one-pager, **v1.3**. Restructured to the JLC Initiative format, cost block rebuilt on the corrected model run, and the retracted figures listed by name in its own header banner — which is the package's authority for the current band. |
| [00-ONE-PAGE-BRIEF.html](00-ONE-PAGE-BRIEF.html) | — | Print template for the PDF. Regenerate with:<br>`"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --no-pdf-header-footer --print-to-pdf=00-ONE-PAGE-BRIEF.pdf file://$PWD/00-ONE-PAGE-BRIEF.html` |
| [01-JLC-Legislative-Change-Brief.md](01-JLC-Legislative-Change-Brief.md) | Legislative staff who want the backup | Same four sections, with every figure, citation and the fallback positions. **v1.2 — carries the re-scoped cost figure.** |
| [02-Annex-A-Legal-Analysis-and-Draft-Bill.md](02-Annex-A-Legal-Analysis-and-Draft-Bill.md) | Division of Legislative Services, VRS counsel | Draft bill language, defined-term analysis, statutory conflicts, unintended-effects check, alternatives, open questions. **v1.1 — the rate-schedule authority is now graded on age *and* creditable service, and the alternate hazardous duty option is addressed. This is the version to transmit.** |
| [03-Annex-B-Fiscal-Assumptions-and-Sources.md](03-Annex-B-Fiscal-Assumptions-and-Sources.md) | VRS actuaries, House Appropriations, Senate Finance & Appropriations | **The package's evidence base — v2.0, reconciled.** Verified-fact register (the single pinpoint index for the whole package), assumption register with owner and sensitivity for every judgment in the model, the cost methodology, what a veteran pays today at published rates, open-claims index, consolidated primary sources, and a reconciliation log. **Carries no total-cost figure at all** — see the division-of-labour rule at its § 0. |
| [04-Annex-2-Closure-FM1-FM5.md](04-Annex-2-Closure-FM1-FM5.md) | VRS actuaries, House Appropriations, Senate Finance & Appropriations | **The package's cost figures — every derived and estimated number lives here.** Closes the five fiscal open items: official plan and employer-group denominators, the AEC/ANC multiple surface, every rate group including hazardous duty, the acceleration decomposition with take-up sensitivity, the exposure split, the guardrail dials, and the July 1, 2026 rate question. |
| [06-Annex-C-Stakeholder-Analysis.md](06-Annex-C-Stakeholder-Analysis.md) | **Policy Director, patron selection, anyone walking the halls** | **The political map — v1.0.** Concrete effects, stakeholder table with a reason and a confidence label on every row, the committee and subcommittee path with what each venue has done with similar bills, the real fight, the coalition ladder with the price of each ally, other-state precedent on purchase timing, patron recommendations, and the unknowns. Desk research on the public record only; no stakeholder was contacted. |
| [07-Annex-D-JLC-Sponsor-and-December-Submission.md](07-Annex-D-JLC-Sponsor-and-December-Submission.md) | **Policy Director, the board, JLCVSO** | **The JLC submission path — v1.0.** The 2026-12-17 gate and the calendar to it, what that meeting requires and who owns each piece, a **ranked list of candidate sponsoring JLC member organisations** from the public record, the Council-submission position paper in JLC format, the patron-list interaction, and the December-versus-2028 comparison. **Its § 4 is the finding to read first:** § 51.1-142.2 B 3 bars the regular 20-year military retiree and the 10 U.S.C. ch. 1223 exception protects only the Reserve and Guard member — so the bill's best-served constituency is the Guard and Reserve, not the career-retiree organisations, which **reverses Annex C v1.1's witness and sponsor read**. Desk research on the public record only; no organisation was contacted. |
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

| Component | Status |
|---|---|
| Title 51.1 legal analysis and draft language | **Complete, v1.1.** Counsel sign-off given; **cleared to go to the Division of Legislative Services** |
| Fiscal estimate | **Analyst estimate.** Requires VRS actuarial confirmation (Annex A, Q1–Q5) |
| Stakeholder analysis | **Complete, v1.0 — see [06-Annex-C-Stakeholder-Analysis.md](06-Annex-C-Stakeholder-Analysis.md).** The chokepoint is the **House Appropriations Subcommittee on Compensation and Retirement**, which tabled the closest analogue (HB 1867, 2023) **8-0** and killed **27 of the 28** VRS bills before it in 2026. The real fight is the price, not the deadline. Reconciled against the Red Team's F-1 and F-2 |
| Red team / adversarial counsel review | **Verdict recorded 10/25/2026 — see [05-Red-Team-Review.md](05-Red-Team-Review.md)** and the second, parallel review at [05-Red-Team-and-Counsel-Review.md](05-Red-Team-and-Counsel-Review.md). 18 findings: 2 fatal, 8 serious, 6 moderate, 2 minor. **Do not file until F-1 and F-2 are resolved.** **F-1 — resolved in the fiscal annexes 10/25/2026:** the 100%-recovery guardrail that drives the fiscal note to zero cannot be built from the authority Annex A § 2.2 grants. Verified over 60 priceable classes; a *lawful uniform* class rate recovers 0%–96% by classification, **59%–66% at the class mean**, and only ~23% in the long-service Plan 1 cohort the bill leads with. **The residual is $22M–$44M at 20% take-up, not $0.** The guardrail is a mitigation, not a neutrality device. See Annex 2 Closure § 4.8.1 and Annex B A-28. **What stays open on F-1 is the drafting choice it forces** — Annex A Q3a and Q12 both need reframing. **F-2 — resolved in the copy 10/25/2026:** the broad "General fund cost: $0" claim, which the package's own who-bears table contradicts ($20M–$37M on state agencies, GF + NGF; $13M–$31M on school divisions through the SOQ), is replaced by "this bill requests no appropriation" in **00 v1.3** and in **01 v1.3**, and is conceded as indefensible in Annex B § 0 and Annex 2 Closure § 4.6. The one-pager's remaining hold is a clearance decision, not a copy defect — see the row below |
| JLCVSO policy decisions | **Scope and transition decided 10/24/2026: all VRS members, no local opt-in, immediate access. Draft already conforms.** Concession ladder (Annex A, Q12) still open. |
| Fiscal re-scope to full VRS membership (required by the scope decision) | **Complete — see [04-Annex-2-Closure-FM1-FM5.md](04-Annex-2-Closure-FM1-FM5.md)** |
| Fiscal open items FM-1 … FM-5 | **Closed 10/24/2026.** FM-3 and FM-5 fully official; FM-1 a sourced range plus a drafted VRS request; FM-2 and FM-4 modelled with the basis shown |
| Re-scoped figure applied to the full brief (01) | **Complete 10/25/2026 — v1.3.** v1.2 applied all ten mechanical corrections from Annex 2 Closure plus items 11–13 (the guardrail dial, three-way exposure split, DPB SOQ request). v1.3 reconciles the COST section to **$28M–$166M** on one assumption set, narrows the general-fund claim per F-2, adds the amortised rate impact per M-5, and withdraws the guardrail-neutrality sentence per F-1 |
| Re-scoped figure applied to the one-page leave-behind (00) | **Copy defects fixed 10/25/2026 — v1.3. Still on HOLD, but now only for clearance.** The board accepted Option C of the MOO-293 framing decision (lead the general-fund position, state the range in our own words, name take-up as the swing factor, close with HB 1867), and the hold was then re-imposed on the lead attorney's sign-off because Option C was settled before the red team verdict was recorded. **Both print-blocking defects are now repaired in v1.3:** the "$0 general fund" overclaim is replaced with "this bill requests no appropriation" and the cost-bearers are named (F-2), and the range is **$28M–$166M** on a single assumption set (S-3 and S-5). `.md`, `.html`, `.pdf` and `.docx` are all regenerated on v1.3 and are consistent. **What remains is not a modelling or copy item: clearance to print is the Policy Director's call and has not been given.** Do not distribute any earlier copy |
| Annex A rate-schedule authority ("age" → "age and creditable service") | **Closed 10/25/2026 — Annex A v1.1, § 2.2.** Widened to age and creditable service, with the amount purchased added as a factor, publication and uniformity requirements, an actuarial-equivalent-cost ceiling, and an express no-spillover sentence confining the schedule to subdivision B 2. Counsel analysis at § 2.5. The package is now internally consistent |
| HB 1867 (2023) fiscal impact statement — pinpoint and re-read | **Closed 10/25/2026 — Annex B F-56, F-60…F-63, § 7.5.** Retrieved from LIS (HB1867F158, 1/16/2023). It carried more than the package was citing: VRS's own worked total of **$50M for teachers alone at 1% take-up on a $35,000 average**, which reframes the $28M–$166M range as the same order of magnitude as VRS's only published figure for a benefit of this shape and "under $2 million" as the outlier; VRS's own statement that it **cannot identify** who holds the service; and a § 30-19.1:7 precedent that supports the *narrow* general-fund claim ("no appropriation requested") while refuting the broad one — VRS wrote "no **immediate** impact" and, beside it, that contribution rates may move over time, which makes F-61 evidence **for** Red Team F-2. Annex 2 Closure § 4.6 rewritten on it. **Restated again 10/25/2026 on a matched four-year basis (red team S-1):** the priced-to-free ratio of 0.704 was a 2.5-year net set against VRS's four-year average; matched at four years it is **1.19 – 1.27**, which no `1 − 1/m` can equal, and the Plan 1 free-grant equivalent is **$123,520**, or 2.06× the top of VRS's band. The package no longer claims the estimate is conservative relative to HB 1867 — it states a **bracket**, with ours the higher. `01` COST, `03` § 7.5 and `04` § 4.6 all now say that; reproduce with `models/redteam_checks.py` RT-2 |
| Annex B reconciliation (the last file carrying pre-re-scope figures) | **Closed 10/25/2026 — Annex B v2.0, extended at v2.1 and v2.2.** Rewritten as the package's evidence base under a non-duplication rule: official facts here, derived and estimated figures in Annex 2 Closure only, so the two cannot diverge. Population and total-cost arithmetic removed; A-08…A-15 formally retired with a mapping to their replacements; four reconciliation checks logged at § 7, one of which corrects A-03 (Plan 1 COLA 3.0% → Board-adopted 2.50%) and one of which validates the live model's inherited salary basis to within 0.5%. New: member-price table for hazardous duty and judicial groups. **Annex B is cleared to circulate outside the working group** |
| Alternate hazardous duty option (10.01%, no plan column) | **Closed for the bill 10/25/2026 — Annex A v1.1, § 2.6.** Reached for subdivision B 2 purchases by factor (v) of the § 2.2 schedule authority, anchored to "the benefits permitted by § 51.1-138." The same pre-existing mismatch for other purchase categories is deliberately left alone. Two confirmations open at Annex A Q13–Q14 |

> ## Retracted figures and claims — the permanent list
>
> Everything named here was published by this package at some point on or before
> October 25, 2026 and is now withdrawn. **Do not quote any of it**, from any copy of
> any file, except to say that it was retracted. Reconciliation of `01`, `03` and `04`
> onto the current band completed **October 25, 2026**, so there is no longer a file in
> the package that carries a superseded figure outside a note like this one.
>
> **Retracted cost ranges — three, in the order they were published.**
>
> | Range | Why it is wrong |
> |---|---|
> | "under $2 million one-time, under $100,000 per year" | Brief v1.0/v1.1 and Annex B v1.1. Built on state classified employees only (about 2,600 people) and on the price-discount channel only, leaving out retirement-date acceleration — which is 20%–49% of the cost. Annex B § 7.4 records exactly what was wrong with it, so the retraction can be defended rather than merely asserted |
> | `$13M–$182M` | Took its **floor** from the 5% take-up row, which belongs to the superseded v1.1 band of 5%–15%, and its **ceiling** from the 30% row of the current scenario set — one range built from two assumption sets (red team **S-5**) |
> | `$26M–$182M` | The interim figure carried in Annex B A-22 between the two corrections. It fixed the floor but still stood on an eligible pool whose two ends were paired with the opposite ends of the past-window population (red team **S-3**) |
>
> **The current band is `$28M–$166M`** — one-time present value of recommendation A-3,
> on the single reconciled eligible pool of **11,565–24,036** and the current 10%–30%
> take-up set. That is **0.11%–0.62% of VRS covered payroll**, or about **0.8 to 4.4
> basis points** on employer contribution rates amortised over 20 years. The authority
> is the banner at the top of [00-ONE-PAGE-BRIEF.md](00-ONE-PAGE-BRIEF.md) v1.3;
> reproduce it with `models/fm_model.py`, section 3.
>
> **Retracted derived figures.** The eligible pool **10,561–26,321** and its by-plan
> legs 3,966 / 2,417 / 4,177 and 9,027 / 5,502 / 11,792 (S-3 — superseded by one pool
> of 11,565–24,036, which the by-plan and by-employer-group derivations now both
> produce). The residual after a lawful graded schedule of **$20M–$48M** at 20% take-up
> (recomputed on the corrected pool as **$22M–$44M**; the recovery band of 0%–96%, and
> its 59%–66% class mean, are pool-independent and did not move). "About 5 cents out of
> every $100 of payroll", and "about 3,400 in the state classified workforce".
>
> **Retracted claims, which matter more than the figures because they do not look like
> errors.**
>
> - **"General fund cost: $0."** Rated **fatal** at red team F-2 and refuted by this
>   package's own who-bears table, which books the state share as general fund *and*
>   nongeneral fund. The defensible form is **"this bill requests no appropriation"** —
>   the cost is absorbed in the employer contribution rates the VRS Board certifies
>   under § 51.1-145, and those reach the general fund in a later biennium for state
>   agencies and for the Commonwealth's share of teacher rates. Fixed in 00 v1.3 and
>   01 v1.3. VRS's own HB 1867 statement is evidence *for* F-2, not against it: it says
>   "no **immediate** impact" and, beside that, that contribution rates may move over
>   time (Annex B F-61).
> - **"At 100% recovery the bill is actuarially neutral and the fiscal note is zero."**
>   Withdrawn at red team **F-1**. That arithmetic prices each member individually,
>   which the uniformity-within-classification requirement and the **individual**
>   actuarial-equivalent-cost ceiling in Annex A § 2.2 together forbid. The guardrail is
>   a **mitigation**, not a neutrality device (Annex 2 Closure § 4.8.1).
> - **"This bill costs the Fund less per member than the one VRS already scored."**
>   Withdrawn at red team **S-1**: it set a 2.5-year paid purchase against a 4-year free
>   grant. HB 1867 is now cited only for what it is — evidence that VRS will file a
>   number of its own.
> - **"Below about age 47–48 a veteran pays more than the credit is actuarially worth."**
>   Withdrawn at red team **S-2** wherever it appears **unqualified**. It is true of the
>   benefit-amount channel alone; on the full basis the bill is priced on, there is no
>   such age. It survives in `01` only with that qualifier attached.
> - **"Every veteran in VRS."** Withdrawn at red team **S-4**: § 51.1-142.2 B 3 bars a
>   veteran whose service already counts toward a military retirement they draw, which
>   is why the population estimate is labelled a ceiling.
> - **"It stays the same tiny share of payroll."** The payroll share rises with the
>   re-scope, because the eligible pool grew by more than the denominator did.
>
> **Annex B states no total-cost figure by design**, and records at its § 7.4 why the
> original one was wrong. Annex 2 Closure holds every derived and estimated figure.
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
> expressed in have since changed. **Both changes are now carried in v1.3:** the
> headline reads "this bill requests no appropriation" rather than "general fund cost:
> $0" (F-2), and the range is **$28M–$166M** rather than $13M–$182M (S-3 and S-5).
> Option C's framing is intact under the restated numbers — the general-fund position
> still leads, the range is still in our own words, take-up is still named as the swing
> factor, and HB 1867 still closes. The one-pager remains on hold for the Policy
> Director's clearance only.

**Not final.** Do not present as final until VRS actuarial figures are in hand and
the red-team review records a verdict.
