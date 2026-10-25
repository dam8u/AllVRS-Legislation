# Annex 2 Closure — Fiscal Open Items FM-1 through FM-5

**Companion to:** JLC Legislative Change Brief — Virginia's 24-Month Military-Service Purchase Price Cliff (Va. Code § 51.1-142.2)
**Closes:** Annex 2 open items FM-1, FM-2, FM-3, FM-4, FM-5
**Date:** October 24, 2026 · **Revised October 25, 2026** (red team F-1, M-4, S-4, S-5 — see § 2.3, § 4.5, § 4.8.1, § 4.8.2) · **Owner:** Fiscal & Impact Modeler · **Issue:** MOO-291, MOO-295
**Reproducible models:** [`models/fm_model.py`](models/fm_model.py) — run `python3 fm_model.py`; [`models/f1_lawful_class_rate.py`](models/f1_lawful_class_rate.py) — the lawful-class-rate, full-basis break-even and restated-exposure checks behind the October 25 revisions

> **Labelling convention used throughout.** **OFFICIAL** = published by VRS, the Commonwealth, or a federal statistical agency. **DERIVED** = arithmetic on official inputs, formula shown. **ESTIMATE** = scenario assumption, not a prediction. No figure in this annex is a VRS actuarial certification; under § 30-19.1:7 the VRS Board files the official impact statement.

---

## Headline — read this before anything else

Three of the five items close with official sources. Two close as qualified negatives with the search recorded. But the work also produced **one finding that is material to the brief as currently drafted**:

> **The brief's cost headline — "under $2 million one-time" — is not sustainable and should not go to the JLC.** It was built on (i) state classified employees only and (ii) the price-discount channel only. Once the brief's own stated scope (all three plans, state + teacher + political-subdivision employers) and its own stated dominant cost driver (retirement-date acceleration) are both carried into the arithmetic, the modelled one-time present-value cost of recommendation A-3 is **on the order of $28 million to $166 million**, depending on the eligible-pool band and take-up. *(This passage read "$13 million to $182 million" when first written; that figure is retracted — see § 4.5.)*
>
> That is not a correction of a calculation error. The old arithmetic was internally consistent for what it covered. It covered roughly 2,600 people out of a pool this annex puts at 11,600–24,000, and it priced about 15%–30% of the cost per person. **See FM-4, § 4.4, and the independent cross-check against VRS's own HB 1867 fiscal impact statement at § 4.6, which supports the new magnitude and flags the old one as too low by roughly an order of magnitude.**

| Item | Status | One-line answer |
|---|---|---|
| **FM-1** | **Closed as a sourced range + a drafted VRS data request** | Official plan and employer-group denominators now in hand. The *veteran-held-purchasable-service* count does not exist publicly and only VRS can produce it. Reportable range: **11,600–24,000** past-window members. Plan 1 (110,474) requires **no estimate at all** — it is past the window as a matter of law. |
| **FM-2** | **Closed — no VRS factor table exists, but a better basis now does** | VRS publishes no actuarial-equivalent factor table. The 3.23× is **approximately right for the Cliff Graph's own illustrative profile** (modelled 2.8×–3.5× across the three plans) — but it sits near the **top** of a **0.5×–3.5×** range. Below about age 47 the member **overpays** at the ANC price. The graph should be reissued with an age dimension, not with different numbers at that one profile. |
| **FM-3** | **Closed — fully official** | Four rate groups, from the Board's own resolution. Includes a structural finding the brief does not yet carry: **there is no Hybrid hazardous-duty rate, because hazardous-duty members are statutorily excluded from Hybrid and enter Plan 2 instead — so Plan 2 is not a closed cohort.** |
| **FM-4** | **Closed as a modelled decomposition with take-up sensitivity** | Acceleration is **20%–49%** of the total cost on this basis, and that is a **floor**. A-1's cost turns almost entirely on the statutory interest rate — a drafting choice, not an actuarial one. |
| **FM-5** | **Closed — qualified negative, well sourced** | **No.** No new ANC rates took effect July 1, 2026. The rates are updated only on the quadrennial cycle, and VRS told its own committee on June 17, 2026 that the next assumption review is **2029**. The "Updated: July 1, 2026" stamp is a document refresh of one page. |

### And one finding that was not asked for but outranks most of what was

Pricing the Annex A guardrails as dials, as the scope decision requires, showed that **the age-graded rate schedule as originally described removes only about 15% of the exposure.** Grading on age recovers the benefit-amount excess but not the acceleration cost, which is driven by proximity to an eligibility threshold — age *and* service together. Graded instead on **distance from unreduced eligibility**, the same authority reaches the acceleration channel as well. That is a one-phrase drafting change and it remains the highest-leverage edit available anywhere in this package. **FM-4 § 4.8.** **Adopted October 25, 2026 in Annex A v1.1, § 2.2.**

> **Revised October 25, 2026 (red team F-1).** This passage previously said the redrawn authority "can remove anything up to 100%," and § 4.8 said the fiscal note goes to zero at the 100% setting. **Both are withdrawn.** That arithmetic prices each member individually, which Annex A § 2.2's uniformity-within-classification requirement and individual actuarial-equivalent-cost ceiling together forbid. A **lawful uniform class rate** recovers **0%–96% of the above-ANC excess depending on the class, with a 59%–66% class mean — and only about 23% in the Plan 1 long-service cohort the bill leads with.** The honest planning figure is a residual of **$22M–$44M** at 20% take-up, not $0 (restated onto the corrected pool — see § 4.8.1). **The guardrail is a mitigation, not a neutrality device.** Full analysis, the restated band and two drafting options at **§ 4.8.1**.

> **Qualified again, October 25, 2026 (red team F-1A and S-9), and this one is not a correction of the arithmetic — it is the discovery of an input the arithmetic was silently assuming.** The § 2.2 ceiling is priced against an actuarial-equivalent cost, and **nothing in this package states at what retirement age that cost is measured.** The package has been measuring the member's *price* at the plan's normal retirement age (65/67) and the member's *benefit* at the member's own unreduced age (typically 46–58). Resolving that one question either way moves both of the red team's new findings by **roughly an order of magnitude**: maximum lawful recovery is 10%–16% on the first basis and 47%–57% on the second, and the sub-ANC purchase leak S-9 identifies is worth $6M–$15M on the first and under $0.4M on the second. **So the $22M–$44M residual is one of two planning figures, and the other — $43M–$84M, on the statutory reading of the ceiling — is most of the way back to the $57M–$111M of doing nothing at all.** Neither can be chosen without (i) counsel settling which reading of "actuarial equivalent cost" governs and (ii) VRS stating the retirement-age basis of its existing factors (Annex B **U-16**, now second only to U-01). **§ 4.8.3.**

### Compliance with the October 24, 2026 scope decision

The JLCVSO decision (all VRS members, no local opt-in, immediate access on the effective date) set five requirements for this work. All five are met:

| Requirement | Where |
|---|---|
| Re-scope the estimate — Annex B is state classified only, bill is ~6× broader | FM-1 § 1.1 (6.6× by headcount), FM-4 § 4.4 |
| Verify active membership counts by employer class | FM-1 § 1.1 — OFFICIAL, ACFR FY2025 Figs. 2.3 / 2.9 |
| Source the veteran share for teachers and locals; do **not** extend DHRM's 6% | FM-1 § 1.4 — NCES 2.3% / 3.1% for teachers; BLS-derived 5.75% for state-and-local government. DHRM's 6% is used for state employees only. |
| Reuse the Annex B § 3 per-member gap methodology; only the population multiplier changes | FM-2 § 2.3 — the same M × G × ä × v identity, which independently reproduces Annex B's 47–48 break-even ages |
| Report state and local exposure separately (§ 51.1-145, Commission on Local Government) | FM-4 § 4.7 — three buckets; teacher line left unsplit pending the SOQ share from DPB |
| Price the two adverse-selection guardrails as dials (unbounded cohort) | FM-4 § 4.8 |

---

## FM-1 — How many members hold purchasable military service, and how many are past the window?

### 1.1 What is now official (new to this package)

**Active members by plan, at June 30, 2025** — OFFICIAL, VRS *VRS 101 / Who We Serve*, 2025 edition:

| Plan | Active members | Share |
|---|---:|---:|
| Plan 1 | **110,474** | 29.2% |
| Plan 2 | **67,333** | 17.8% |
| Hybrid | **200,253** | 53.0% |
| **Total** | **378,060** | 100.0% |

**Active members by employer group, at June 30, 2025** — OFFICIAL, VRS ACFR FY2025, Figures 2.3 and 2.9:

| Employer group | Active | Vested | Non-vested |
|---|---:|---:|---:|
| VRS State Employees | 83,148 | 52,120 | 31,028 |
| VRS Teachers | 160,800 | 110,074 | 50,726 |
| VRS Political Subdivision Employees | 124,264 | 70,340 | 53,924 |
| SPORS | 1,894 | 1,524 | 370 |
| VaLORS | 7,484 | 3,795 | 3,689 |
| JRS | 470 | 378 | 92 |
| **Total** | **378,060** | **238,231** | **139,829** |

The brief v1.0 used 56,917 classified state employees. The VRS member population in the brief's own stated scope is **378,060 — 6.6 times larger.**

### 1.2 The part of FM-1 that needs no estimate at all

A Plan 1 membership date must precede July 1, 2010 (VRS ACFR FY2025, Figure 2.10). The cost window closes 24 months after the first date of hire. Therefore:

> **All 110,474 active Plan 1 members — 29.2% of the entire VRS active population — are past the 24-month window as a matter of law.** This is not an estimate. It requires no VRS data run.

That single sentence is the most defensible population statement available to the JLC, and the brief should lead the population discussion with it.

Two qualifications, both small and both to be stated:

1. § 51.1-142.2 B 3 runs the window from first hire **or the final day of any applicable leave of absence**, and the VRS rate charts add "or the date you return to active employment after an eligible period of leave." A Plan 1 member returning from an eligible leave can therefore hold a fresh window. The number so situated is small and unpublished.
2. The window runs on **active service**, so inactive periods do not count. This can only push members *later* out of the window, never earlier, so it makes the 110,474 figure a floor on the count of members whose original window has closed.

### 1.3 Plan 2 is **not** a closed cohort — correction to the brief's premise

VRS ACFR FY2025, Figure 2.10, OFFICIAL, verbatim:

> "Members covered under VaLORS, SPORS or VRS with enhanced hazardous duty benefits or the hazardous duty alternate option, and whose membership dates are on or after July 1, 2010, are in Plan 2 **even if their membership dates are after December 31, 2013**."

So Plan 2 continues to admit new members today: SPORS officers, VaLORS officers, and political-subdivision hazardous-duty employees in localities that adopted the enhanced benefits or the alternate option. And from July 1, 2026, newly appointed judges — 2026 Acts of Assembly, SB 950, provides that judges appointed or elected to an original term on or after July 1, 2026 are in VRS Plan 2.

The brief v1.0 describes Plan 2 as a closed cohort ("hired July 2010 – Dec. 2013"). That is correct for non-hazardous members only. **The brief should not say Plan 2 is closed**, and the fiscal note must contemplate a continuing flow of new Plan 2 hazardous-duty members buying at the Plan 2 hazardous rate. See FM-3.

### 1.4 Veteran share — replacing one proxy with four sourced ones

The brief v1.0 applied DHRM's 6% self-identified classified-workforce veteran share to everything. That share is sound for state classified employees and wrong for teachers.

| Group | Share used | Basis |
|---|---|---|
| VRS State Employees | **6.0% – 9.9%** | Low: DHRM presentation to Senate Finance & Appropriations, Jan. 21, 2025, slide 8 (self-identified, 6/30/2024) — OFFICIAL. High: BLS benchmark × Virginia uplift — DERIVED. |
| VRS Teachers | **2.3% – 5.4%** | Low: NCES *Digest of Education Statistics* table 209.27 — **2.3% of U.S. public school teachers are military veterans** (3.1% in the South region) — OFFICIAL. High: South-region 3.1% × Virginia uplift — DERIVED. |
| VRS Political Subdivision Employees | **5.7% – 9.9%** | Low: BLS state-and-local-government benchmark — DERIVED. High: × Virginia uplift — DERIVED. Public-safety-heavy, so likely upper half. |
| SPORS / VaLORS | **9.9% – 25.0%** | ESTIMATE. The weakest band in this annex. Sworn law enforcement recruits heavily from the military; no published Virginia figure exists. |
| JRS | **2.3% – 9.9%** | ESTIMATE, bracketed by the teacher floor and the public-sector ceiling. |

**The BLS benchmark, derived in full** — U.S. Bureau of Labor Statistics, *Employment Situation of Veterans*, Table 8, August 2025:

```
veterans in state & local government     =  7,893k × 12.9%  =  1,018k
nonveterans in state & local government  = 153,213k × 10.9%  = 16,700k
veteran share of S&L government workers  =  1,018 / 17,718   =   5.75%
```

**5.75% independently corroborates DHRM's 6%.** Two unrelated instruments — a Virginia self-identification field and a national household survey's class-of-worker table — land within a quarter of a percentage point of each other. That materially strengthens the brief's population footing, and it is worth saying so explicitly to the money committees.

**The Virginia uplift** (used only as an upper bound, never as a point estimate) — BLS *Employment Situation of Veterans*, Tables 6A and 6B, 2025 annual averages:

```
Virginia veteran share of employed  =   357 / (357 + 3,864)      =  8.46%
U.S. veteran share of employed      = 7,893 / (7,893 + 153,213)  =  4.90%
uplift factor                       =  8.46 / 4.90               =  1.726×
```

Note DHRM's 6% is **self-identified** and therefore a floor, not a measurement. The gap between 6% and the Virginia-uplifted 9.9% is the honest width of this input.

### 1.5 Members past the 24-month window

For Plan 1 the answer is structural (§ 1.2). For the rest, the derivation uses the official vested / non-vested split. Vesting is five years of service credit (§ 51.1-153; ACFR Figure 2.10), so every **vested** member has more than five years and is necessarily past a 24-month window. The only uncertainty is how the **non-vested** 139,829 distribute across years 0–5.

- **ESTIMATE, low end:** 40% of non-vested are inside the window (service spread uniformly over years 0–5 → the 0–2 band is 2/5 of the band).
- **ESTIMATE, high end:** 60% (front-loaded, which is what withdrawal decrements on new hires actually produce — VaLORS is the visible case: 3,689 non-vested against 3,795 vested).

| Employer group | Past window, low | Past window, high |
|---|---:|---:|
| VRS State Employees | 64,531 | 70,737 |
| VRS Teachers | 130,364 | 140,510 |
| VRS Political Subdivision Employees | 91,910 | 102,694 |
| SPORS | 1,672 | 1,746 |
| VaLORS | 5,271 | 6,008 |
| JRS | 415 | 433 |
| **Total** | **294,163** | **322,128** |
| **as share of 378,060 actives** | **77.8%** | **85.2%** |

### 1.6 The answer to FM-1, in reportable form

| Employer group | Veteran share | Low | High |
|---|---|---:|---:|
| VRS State Employees | 6.0% – 9.9% | 3,485 | 6,316 |
| VRS Teachers | 2.3% – 5.4% | 2,699 | 6,768 |
| VRS Political Subdivision Employees | 5.7% – 9.9% | 4,753 | 9,169 |
| SPORS | 9.9% – 25.0% | 149 | 393 |
| VaLORS | 9.9% – 25.0% | 471 | 1,352 |
| JRS | 2.3% – 9.9% | 9 | 39 |
| **Total** | | **11,565** | **24,036** |

(Each row is past-window population × veteran share × 90% meeting the 180-consecutive-day test of § 51.1-142.2 B 2. The 90% factor is an ESTIMATE.)

Allocated across plans for the FM-4 cost model — ESTIMATE, applying the effective rate uniformly across plans, which over-weights Hybrid and under-weights Plan 1 because veterans enter public service mid-career:

| Plan | Eligible pool, low | Eligible pool, high |
|---|---:|---:|
| Plan 1 | 4,343 | 8,243 |
| Plan 2 | 2,647 | 5,024 |
| Hybrid | 4,575 | 10,769 |
| **Total** | **11,565** | **24,036** |

**This is a reallocation of the table above, not a second estimate, and the totals are therefore obliged to match it at both ends.** The effective veteran-with-qualifying-service rate is **3.93% – 7.46%** — the pool divided by the past-window population it was built from — and the three plan legs sum back to that same population, so the by-plan and by-employer-group derivations give one pool. **Corrected October 25, 2026 (red team S-3):** this table previously read 3,966 / 2,417 / 4,177 and 9,027 / 5,502 / 11,792 for a total of 10,561 – 26,321, which did not match. The effective rate had been computed by pairing each end of the pool with the opposite end of the past-window population, widening the band to 3.59%–8.17%. Account at § 4.8.2.

> **What to say to a legislator:** "Roughly twelve to twenty-four thousand members across the three plans, of whom over a hundred and ten thousand Plan 1 members are past the deadline as a matter of law. VRS can give you the exact count of those holding verified military service; nobody else can."
>
> **What not to say:** any single number. The brief's existing instruction on this point was right and should be kept.

### 1.7 FM-1 is partly an irreducible negative — here is the VRS data request

No published source reports VRS members by military-service status. VRS holds it: § 51.1-142.2 purchases require a DD-214 or service orders (VRS Employer Manual, *Purchase of Prior Service Credit*, July 2026, pp. 5–6), so **verified military service exists in VRS records only for members who have already applied.** Members who hold the service but never applied are not identifiable from VRS data at all — only from an employer self-identification field, which is where DHRM's 6% comes from and why it is a floor.

**Draft request to VRS (ready to send):**

1. Active members as of the most recent valuation date, cross-tabulated by **plan** (Plan 1 / Plan 2 / Hybrid) × **employer group** (state / teacher / political subdivision / SPORS / VaLORS / JRS) × **rate group** (non-hazardous / hazardous / alternate hazardous / judicial).
2. Of those, the number with **verified prior active-duty military service on file** under § 51.1-142.2 B 2, and the number with an **unexercised** purchase right.
3. The number whose 24-month approximate-normal-cost window **has closed**, and the number for whom it is **still open**, measured on active service as the statute requires.
4. Distribution of **unpurchased qualifying military service** in months, capped at the statutory four years.
5. **Historical take-up:** § 51.1-142.2 B 2 purchases completed per year for the last ten years, split by whether priced at approximate normal cost or at actuarial equivalent cost, with average years purchased and average dollar amount. *This is the single input that most changes the answer — see FM-4, § 4.5.*
6. Members **1, 2, 3 and 4 years of creditable service short** of the age-50/30-years threshold (§ 51.1-153 B 1) and of the Rule of 90 (§ 51.1-153 B 3), by plan. *This is the acceleration exposure.*
7. Age, service, and AFC distributions for the members identified in (2).
8. The **actuarial-equivalent-cost factor basis** developed by the Plan Actuary — see FM-2, § 2.2.

---

## FM-2 — The actual AEC-to-ANC multiple, by age and service

### 2.1 Does VRS publish a factor table? No. But it has one.

The published rate charts (*Purchase of Prior Service Cost Rates*, pages 1–4) say only "Actuarial Cost" in every post-window cell. There is no factor table, no age grading, and no worked example. That part of FM-2 closes as a negative.

### 2.2 But the actuary develops it annually — this is new and it changes the data request

VRS Board of Trustees minutes, June 18, 2025, reporting the Benefits and Actuarial Committee meeting of June 9, 2025 — OFFICIAL, verbatim:

> "The approximate normal cost rates are updated every four years following the Board's acceptance of the new assumptions associated with the quadrennial experience study. **The actuarial equivalent cost rates are developed by the Plan Actuary based on the assumptions and demographic data from the prior year valuations.**"

Two things follow, and both matter:

1. **"Rates," plural, "developed by the Plan Actuary," annually.** The brief v1.0 describes the actuarial-equivalent price as "an individualized present-value calculation." On the Board's own account it is administered from an actuary-developed rate basis refreshed each year against the prior-year valuation. That is a **document that exists and can be requested**, not a per-member computation that has to be commissioned. The brief's characterisation should be softened, and item 8 of the § 1.7 data request should ask for it by that description.
2. It is produced by **Gabriel, Roeder, Smith & Company**, VRS's Plan Actuary, named as such in the June 30, 2025 valuation. The request should name GRS.

### 2.3 A better basis than one worked example

Because VRS's own definition of the approximate normal cost rate is "**the average cost of one year of VRS service credit**" (Employer Manual, July 2026, p. 11), the ANC rate is by construction the correct actuarial price at the plan's *average* member. The AEC/ANC multiple at any other age is therefore the ratio of actuarial value at that age to value at the average age — a quantity in which the annuity basis **largely cancels**. The shape of the surface is robust even where the absolute level is an estimate. That is a materially better basis than a single data point.

Inputs, all OFFICIAL: multipliers 1.70% / 1.65% / 1.00% (§ 51.1-155 A 1; § 51.1-169 D 1); discount 6.75%; Board-adopted COLA assumptions **2.50% Plan 1 and 2.25% Plan 2 / Hybrid** (June 30, 2025 valuation, Executive Summary); payroll growth 3.0%. Annuity basis is a level-COLA annuity-certain to age 87 — ESTIMATE, not a VRS mortality table.

**Benefit-amount channel only** (DERIVED):

| Purchase age | Plan 1 (ANC 12.50%) | Plan 2 (ANC 10.74%) | Hybrid (ANC 6.68%) |
|---|---|---|---|
| 30 | 0.55× | 0.54× | 0.52× |
| 35 | 0.66× | 0.64× | 0.62× |
| 40 | 0.79× | 0.77× | 0.75× |
| 45 | 0.94× | 0.92× | 0.89× |
| 50 | 1.13× | 1.10× | 1.07× |
| 55 | 1.35× | 1.31× | 1.28× |
| 60 | 1.61× | 1.57× | 1.53× |
| **Break-even age** | **46.6** | **47.4** | **48.2** |

The break-even ages cluster tightly at **47–48 in all three plans** — **on the benefit-amount channel alone.** That restriction is load-bearing and was not previously stated here.

> **Correction, October 25, 2026 (red team S-4).** Brief v1.0 and v1.2 carried this as "below that age the veteran **overpays** — the member subsidises the Fund … **the strongest fiscal argument this proposal has**." **That claim is withdrawn.** It is computed on the benefit-amount channel only, which is the basis this package elsewhere calls roughly half the cost (§ 4.3: acceleration is 20%–49%, and that is a floor). It is therefore the superseded basis being used to explain a re-scoped number.
>
> Re-run on the **full basis** (benefit amount *plus* retirement-date acceleration), salary held constant at $69,865 and 2.5 years purchased, there is **no age at which the member overpays** — in any plan, at any age tested from 30 to 50:
>
> | Plan | ANC price | Full-basis value at age 35 | at 40 | at 45 | at 50 |
> |---|---:|---:|---:|---:|---:|
> | Plan 1 | $21,833 | $34,138 | $40,822 | $48,815 | $58,372 |
> | Plan 2 | $18,759 | $25,412 | $30,388 | $36,337 | $43,451 |
> | Hybrid | $11,667 | $15,401 | $18,417 | $22,022 | $26,334 |
>
> The Fund is out money at every cell. `models/f1_lawful_class_rate.py`, `breakeven_full_basis()`.
>
> **What replaces it.** The argument that actually holds on the full basis is the **plan-mix argument**: Hybrid per-member net cost is **$6,779**, roughly **one seventh** of Plan 1's $47,967, and Hybrid is **53% of actives today and 100% of future hires**. The bill's per-member cost therefore *declines* as the membership turns over, without any further legislation. That is defensible on the same basis the cost figures are computed on, and it is the sentence the brief and the one-pager should carry instead.
>
> **Counter-note, stated because the direction matters.** The full basis assumes **every purchaser retires at the earliest unreduced date** — now registered as **Annex B A-29**, previously unstated. That assumption pushes cost *up*: a member who would have worked to 65 regardless generates no acceleration cost. If real behaviour is partial, the full-basis figures are conservative and the true break-even lies between the two bases. The defect corrected here is reporting **one basis for break-even and the other for cost** without reconciling them, and never naming the behavioural assumption at all.

The benefit-amount-channel break-even remains the right number for one narrow purpose: it is what makes the AEC/ANC **multiple** fall below 1.0× for younger members, which is the § 2.4 point about the Cliff Graph. It is not a statement about whether the Fund gains or loses.

### 2.4 Where the 3.23× actually comes from — and what to do about the graph

On the benefit-amount channel alone, 3.23× is **unreachable**: the surface tops out near 1.6×. Adding the eligibility-acceleration channel, at the Cliff Graph's **own** illustrative profile — age 55, 25 years of service, $91,700 — reproduces it:

| Plan | Unreduced eligibility | Acceleration | Modelled AEC/yr | ANC/yr | **Multiple** |
|---|---|---:|---:|---:|---:|
| Plan 1 | 60.0 → 56.0 | 4.00 yrs | $40,531 | $11,462 | **3.54×** |
| Plan 2 | 60.0 → 58.0 | 2.00 yrs | $27,943 | $9,849 | **2.84×** |
| Hybrid | 60.0 → 58.0 | 2.00 yrs | $16,935 | $6,126 | **2.76×** |

**So the honest answer to FM-2 is better news for the chart than expected, for a reason the chart does not currently give.**

- The 3.23× **is** defensible at that profile — and independently reproduced here at 3.54× for Plan 1 from published assumptions, without access to the original worked example.
- Applying it to Plan 2 and Hybrid at that same profile overstates them only modestly: **1.14× for Plan 2, 1.17× for Hybrid.** The footnote calling those lines "illustrative only" is honest and turns out to be nearly accurate.
- Plan 1's post-cliff line is, if anything, **understated** by about 9%.

**But the chart is still misleading, and in a way the current footnotes do not cure.** A single-profile chart invites the inference that *every* veteran faces a 3.23× jump. The multiple ranges from **0.5× to 3.5×**, and for the large majority of the Hybrid population — every non-hazardous member hired since January 1, 2014, mostly under 47 — the multiple is **below 1.0×**, meaning the ANC price is already above actuarial value.

**Recommended reissue (for MOO-288 to action):** keep the existing values at the illustrative profile; do **not** change them. Add a second panel plotting the AEC/ANC multiple against purchase age, with the 47–48 **benefit-amount-channel** break-even line marked — labelled as such, per § 2.3's correction, because it is a statement about the multiple and not about whether the Fund gains — and replace caution 1 with: *"the multiple is profile-specific and ranges from about 0.5× to about 3.5×; 3.23× describes a long-service member sitting just short of an eligibility threshold, which is the worst case, not the typical one."*

Two reasons the spread is structural, not a modelling artefact:

1. Lower multipliers in the later plans (1.65% and 1.00% against 1.70%).
2. **Plan 1's age-50/30-years threshold advances one year per year purchased, while the Rule of 90 advances only half a year per year purchased** — purchased § 51.1-142.2 service adds to the service leg only; it is creditable service, but it is not time lived. This is the single most important mechanical asymmetry in the whole package and it is not currently stated anywhere in the brief.

Terminal-age sensitivity, Hybrid at age 58: 1.28× (age 84) / 1.42× (87) / 1.55× (90). The multiple is far more stable than the absolute dollar figure, as predicted.

---

## FM-3 — Which ANC rate schedules apply across rate groups under A-3

Fully closed, fully official. Source: VRS Board of Trustees, **Request for Board Action 2025-06-10**, minutes of June 18, 2025, and the published *Purchase of Prior Service Cost Rates* charts, pages 1–4.

| Rate group | Plan 1 | Plan 2 | Hybrid |
|---|---:|---:|---:|
| State / teacher / local **non-hazardous** | 12.50% | 10.74% | **6.68%** |
| **Hazardous duty** — VaLORS, SPORS, political subdivisions with enhanced benefits | 23.78% | **19.15%** | **none exists** |
| **Hazardous duty alternate option** (employer has not adopted all enhanced benefits) | — | — | **10.01%** (single published rate, localities electing the option only) |
| **Judicial** | 31.97% | **29.67%** | 19.21% |

Rates in **bold** are the forward-looking ones for new entrants in that group.

**The finding that matters for drafting.** There is no Hybrid hazardous-duty rate because there are no Hybrid hazardous-duty members. § 51.1-169 A excludes from the Hybrid plan anyone participating in or eligible for Chapter 2 (SPORS), Chapter 2.1 (VaLORS), the optional retirement plans, or "a person eligible to earn the benefits permitted by § 51.1-138," and any EMS / firefighter / law-enforcement officer whose political subdivision has adopted the irrevocable resolution described in § 51.1-153 B 4 and § 51.1-155 A 3. Confirmed independently in VRS ACFR FY2025, Figure 2.10 ("Non-Eligible Members").

Consequences for A-3:

1. A hazardous-duty employee hired today is in **Plan 2** and would purchase at **19.15%** — nearly double the non-hazardous Plan 2 rate and well over double the Hybrid rate. **Hazardous duty is where A-3's per-member exposure is largest and where the member price is also largest.** Those two partly offset; the net is for the actuary.
2. The 10.01% alternate hazardous duty option is published as a **stand-alone rate with no plan column at all**, available only to electing localities. If A-3 is drafted by reference to "the approximate normal cost of the retirement plan under which the member is covered," that phrase does not cleanly reach the alternate option. **Flag to Legislative Services.**
3. **Judicial:** 2026 Acts of Assembly, SB 950, puts judges with an original term on or after July 1, 2026 into VRS Plan 2, so the forward-looking judicial rate is the Plan 2 judicial rate of 29.67%, not the Hybrid judicial rate of 19.21%. Any drafting that assumes new judges are Hybrid is already out of date.
4. A-3 requires **no new rate-setting**. Every rate group already has a Board-adopted ANC rate. Striking the cliff for § 51.1-142.2 B 2 service simply extends an existing published rate in time. That is a real and quotable administrative advantage of A-3 over A-1 and A-2, and the brief should say so.

---

## FM-4 — Retirement-date acceleration under A-1, A-2 and A-3

### 4.1 Why acceleration is a separate channel

Purchased § 51.1-142.2 service **is** creditable service (§ 51.1-124.3), and the unreduced-retirement thresholds of § 51.1-153 are written in terms of creditable service. So a purchase does two distinct things: it raises the benefit *amount*, and it moves the eligibility *date* earlier. VRS's own definition of actuarial equivalent cost covers both — "the total value of the increase in the employee's future retirement benefit **or earlier retirement eligibility date**" (Employer Manual, July 2026, p. 11).

The mechanics differ sharply by threshold, and this is the key asymmetry:

- **§ 51.1-153 B 1, age 50 with 30 years (Plan 1):** once the member is past 50, the service leg binds alone. One purchased year advances eligibility by **one full year**.
- **§ 51.1-153 B 3, Rule of 90 (Plan 2 and Hybrid):** each year actually worked adds two points — one of age and one of service. A purchased year adds **one** point. So one purchased year advances eligibility by **half a year**.

### 4.2 The decomposition (DERIVED), buying the full four years

| Profile | Unreduced | Accel. | Benefit-amount PV | **Acceleration PV** | Total PV | Accel. share |
|---|---|---:|---:|---:|---:|---:|
| Plan 1, age 55, 25 yrs | 60.0 → 56.0 | 4.00 | $83,462 | **$78,661** | $162,123 | **48.5%** |
| Plan 2, age 50, 14 yrs | 63.0 → 61.0 | 2.00 | $55,590 | **$21,811** | $77,402 | **28.2%** |
| Hybrid, age 45, 8 yrs | 63.5 → 61.5 | 2.00 | $27,339 | **$10,636** | $37,975 | **28.0%** |
| Hybrid, age 55, 10 yrs | 67.0 → 65.5 | 1.50 | $31,293 | **$8,054** | $39,348 | **20.5%** |

Salary basis $91,700.

**The brief's premise is confirmed but should be stated more precisely.** Acceleration is **20%–49%** of the cost on this basis — large, often the largest single component, but **not** larger than the benefit-amount channel in every case. It dominates specifically for a long-service Plan 1 member sitting just short of age 50 plus 30 years. Saying "acceleration, not the price discount, is the dominant driver" is right for the Plan 1 cohort and an overstatement for a 45-year-old Hybrid member.

**And 20%–49% is a floor, not a ceiling.** VRS's Senior Staff Actuary told the Benefits and Actuarial Committee on **June 17, 2026** that VRS uses fixed-rate early-retirement reductions rather than true actuarial equivalence, and that this "does provide a subsidy that varies by age and service." Reaching an **unreduced** date earlier therefore also extinguishes a reduction the member would otherwise have borne. That second-order effect is not modelled here and runs in one direction only — upward.

### 4.3 The three price structures (DERIVED prices against modelled benefit value)

A-1, A-2 and A-3 differ **only in the member's price**, never in the value of the credit. So net cost to the Fund = benefit value − member price, and the structures can be compared directly.

| Profile (4 years bought) | Benefit value | A-1 @ 4% | A-1 @ 6.75% | A-2 @ 6% | A-3 (ANC) |
|---|---:|---:|---:|---:|---:|
| **Plan 1**, age 55, 25 yrs, entered at 30 on $45,000 | $162,123 | $41,891 | $80,442 | $22,008 | $45,850 |
| → net cost to the Fund | | $120,232 | $81,681 | $140,115 | $116,273 |
| **Plan 2**, age 50, 14 yrs, entered at 36 on $55,000 | $77,402 | $33,259 | $47,928 | $22,008 | $39,394 |
| → net cost to the Fund | | $44,143 | $29,474 | $55,394 | $38,007 |
| **Hybrid**, age 45, 8 yrs, entered at 37 on $68,000 | $37,975 | $32,497 | $40,043 | $22,008 | $24,502 |
| → net cost to the Fund | | $5,478 | **−$2,068** | $15,967 | $13,473 |
| **Hybrid**, age 55, 10 yrs, entered at 45 on $72,000 | $39,348 | $37,217 | $48,315 | $22,008 | $24,502 |
| → net cost to the Fund | | $2,131 | **−$8,968** | $17,340 | $14,845 |

A-1 priced per the brief's description: combined member + employer normal cost rate at entry, applied to early-career pay, carried forward at a statutory interest rate. Combined normal cost anchored to the OFFICIAL Total Normal Cost for State Employees, 8.73% (June 30, 2025 valuation, Results Summary — Employer Contribution Rate Detail; Teachers 9.22%, SPORS 18.37%, VaLORS 14.30%, Judicial 27.11%). A-2 at New York's 6% of trailing-12-month compensation (N.Y. Ret. & Soc. Sec. Law § 1000); the percentage is a policy variable. A-3 at the published ANC rate.

**Three findings the JLC needs.**

1. **A-1's whole character depends on the statutory interest rate, which is a drafting choice.** At Pennsylvania's 4% statutory rate, A-1 is **cheaper to the veteran than A-3** for the Plan 1 profile ($41,891 against $45,850). At VRS's 6.75% assumed return, A-1 is nearly **double** A-3 ($80,442). Counsel ranked A-1 preferred on fiscal-note grounds; this analysis supports that ranking **only if a high interest rate is chosen**, and a high interest rate is exactly what makes A-1 unaffordable to the long-tenure veterans the bill exists to help. **This tension should be surfaced to the JLC before a structure is chosen, not after.** It is a genuine trade-off, not a defect in the recommendation.
2. **A-1 can over-recover.** For both Hybrid profiles at 6.75%, A-1's price exceeds the entire modelled value of the credit — net cost to the Fund is **negative**. A structure that charges a veteran more than the benefit is worth is very easy to defend to an actuary and very hard to defend to a veterans' organisation.
3. **A-2 is the cheapest for the member in every case and therefore the costliest to the Fund in every case**, and its price is flat in age — so it is the structure most exposed to adverse selection. New York's answer is to put the remainder expressly on participating employers (§ 1000(6)); any Virginia version of A-2 needs the same sentence, and for political subdivisions that sentence is what the Commission on Local Government will read first.

### 4.4 Statewide take-up sensitivity, A-3

Representative net present-value cost per purchasing member, at the mean classified salary of $69,865 and 2.5 of the 4 allowed years purchased (DERIVED):

| Plan | Eligible pool | A-3 net PV per purchaser |
|---|---|---:|
| Plan 1 | 4,343 – 8,243 | **$47,967** |
| Plan 2 | 2,647 – 5,024 | **$17,174** |
| Hybrid | 4,575 – 10,769 | **$6,779** |
| **Total** | **11,565 – 24,036** | |

The plan legs sum to the employer-group total at § 1.6 exactly, at both ends. That is an identity rather than a coincidence, and until October 25, 2026 it did not hold — see § 4.8.2.

| Scenario | Take-up | Purchasers | **One-time PV cost, A-3** | As % of covered payroll |
|---|---:|---|---|---|
| *Brief v1.0 low — retired band* | *5%* | *578 – 1,202* | *$14.2M – $27.7M* | *0.053% – 0.104%* |
| **Low** | **10%** | **1,157 – 2,404** | **$28.5M – $55.5M** | **0.106% – 0.207%** |
| *Brief v1.0 high — retired band* | *15%* | *1,735 – 3,605* | *$42.7M – $83.2M* | *0.160% – 0.311%* |
| **Moderate** | **20%** | **2,313 – 4,807** | **$57.0M – $110.9M** | **0.213% – 0.415%** |
| **High** | **30%** | **3,470 – 7,211** | **$85.4M – $166.4M** | **0.319% – 0.622%** |

**The publishable range is the bold rows: $28M – $166M.** The 5% and 15% rows are the brief v1.0 band of 5%–15% that the re-scope superseded; they are kept on the grid as markers of where the retired figures came from and are **not** part of the current scenario set. Taking a floor from one set and a ceiling from the other is what produced the retracted "$13M–$182M" — see § 4.5.

> **Restated October 25, 2026 (red team S-3).** Both tables above previously stood on a by-plan pool of 10,561 – 26,321, which disagreed with the § 4.7 who-bears table 100 lines below. The cause was a pairing error in `fm_model.py`, not a difference of method: the effective veteran-with-qualifying-service rate band was computed as `pool_lo / pw_hi` and `pool_hi / pw_lo`, pairing each end of the pool with the **opposite** end of the past-window population, which widened the derived rate band from 3.93%–7.46% to 3.59%–8.17%. Pairing like with like reconciles the two tables on one pool. Full account at § 4.8.2; reproduce with [`models/fm_model.py`](models/fm_model.py), section 3.

**The payroll denominator, and why the brief's scale sentence also needs fixing.** Brief v1.0 and the one-page leave-behind both say the cost is "about 5 cents out of every $100 of a single year's payroll," against a classified state payroll of roughly $3.98 billion. For a bill reaching all VRS members the correct denominator is Annual Covered Payroll across all six groups — OFFICIAL, June 30, 2025 valuation, Results Summary for each group:

| Group | Annual Covered Payroll |
|---|---:|
| Teachers | $11,732,114,000 |
| Political Subdivisions | $8,041,026,000 |
| State Employees | $6,275,603,000 |
| Virginia Law Officers (VaLORS) | $432,703,000 |
| State Police (SPORS) | $182,726,000 |
| Judicial (JRS) | $98,645,000 |
| **Total VRS covered payroll** | **$26,762,817,000** |

The denominator is 6.7× larger than the one brief v1.0 used — but **the eligible pool grew by more than the denominator did**, so the payroll share rises as well. **"Five cents per $100" now survives nowhere on the live grid.** The lowest cell of the current scenario set is **0.106%**, about **11 cents** per $100, and the highest is **0.622%**, about **62 cents** — so the retired phrase understates the publishable floor by roughly a factor of two and the ceiling by roughly twelve. The one-pager's old hedge — that the statewide figure is larger "but it stays the same tiny share of payroll" — is therefore **not correct**, and should be replaced with a figure from this column.

**Against the brief's "under $2 million one-time."** The floor of the publishable range — 10% take-up on the low pool — is **$28 million**, **fourteen times** the brief's ceiling. (Even the retired 5% marker row is $14.2 million, seven times it.) The difference is entirely accounted for by the two things the brief said it would do but did not carry into the arithmetic: extending to all plans and all three employer groups (pool 2,600 → 11,565–24,036) and pricing acceleration (about $3,750 per member → $6,779–$47,967).

This is a present-value liability, not a cash appropriation. It would be absorbed in the employer contribution rate and amortised under the VRS Funding Policy, as the brief correctly says. But the number the money committees will see is the present value, and **$2 million is not that number.**

### 4.5 The one input that would most change this

**Historical take-up.** On the current scenario set the grid spans a factor of **about 6** from its gentlest to its harshest cell, and **a factor of 3 of that 6 is take-up alone** — the eligible-pool band contributes the remaining factor of about 2. Item 5 of the § 1.7 data request would collapse the larger half of it.

> **Correction, October 25, 2026 (red team S-5 and S-3) — three defects, two in the same assumption and one in the arithmetic beneath it.**
>
> **(a) The published floor was taken from a band this package retired.** The headline "$13M–$182M" took its **floor** from the 5% row, which is the **brief v1.0 band of 5%–15% that the re-scope superseded**, and its **ceiling** from the 30% row of the *current* scenario set. That is one range built from two assumption sets.
>
> **(b) The pool the grid stood on was mis-paired (S-3).** Independently of the floor question, the by-plan pool was built by pairing each end of the eligible pool with the opposite end of the past-window population (§ 4.8.2). On the single reconciled pool of **11,565 – 24,036**, and on the current scenario set alone (Low 10% / Moderate 20% / High 30%), the range is:
>
> | Take-up | One-time present value |
> |---|---:|
> | 5% — *superseded band, retained only as a marker of where the retired floor came from* | *$14.2M – $27.7M* |
> | **10% — current Low** | **$28.5M – $55.5M** |
> | 20% — current Moderate | $57.0M – $110.9M |
> | **30% — current High** | **$85.4M – $166.4M** |
> | **50% — stress case** (publicised, payroll-deductible, self-identified population) | **$142.4M – $277.3M** |
>
> **The range to publish is $28M–$166M.** The floor doubles and the ceiling comes in by about 9%. It supersedes **both** the published "$13M–$182M" **and** the "$26M–$182M" interim figure this subsection carried between the two corrections — that interim figure fixed (a) but not (b), and is itself retracted. The authority for the current band is the banner at the top of [`00-ONE-PAGE-BRIEF.md`](00-ONE-PAGE-BRIEF.md) v1.3.
>
> The previous sentence here — that if experience is in the low single digits "the honest headline is the bottom row" — **is withdrawn**: the bottom row is not on the current assumption set, and calling it "the honest headline" imported the retired floor into the live document.
>
> **(b) Historical take-up is a downward-biased estimator of post-reform take-up, and the bias runs the wrong way for us.** The justification for a low assumption is that members must fund purchases from pay. But the observed low take-up was produced under a regime with (i) actuarial-equivalent pricing after 24 months, (ii) 6–12 month payment terms, and (iii) members who, on this package's own theory of the case, never hear about the option in time. **The bill removes all three.** Using pre-reform behaviour to forecast post-reform behaviour, when the reform targets precisely the frictions that suppressed the behaviour, is a selection error — and it is the one assumption most likely to be wrong in the direction that hurts. JLCVSO cannot simultaneously tell legislators the bill will reach veterans who currently miss out and tell the money committees that take-up will stay where it was.
>
> **Consequences adopted here:** the 50% row is carried as a stress case rather than omitted; **data request item 5 is reclassified from a request to a pre-filing blocker** (Annex B A-22 / U-01); and historical take-up, when obtained, must be adjusted upward for the removal of the three frictions rather than used raw.

### 4.6 Independent cross-check — what it validates, and the conservatism claim withdrawn

**Source now pinpointed** (Annex B F-56, F-60 to F-63): VRS, *2023 Fiscal Impact Statement*, **HB 1867**, dated January 16, 2023, document HB1867.DOC/VRS — the § 30-19.1:7 statement on a bill that would have granted up to four years of active-duty military service to teachers **free**. VRS, Item 6, verbatim:

> "each person who purchases up to 48 months of active military service would create an unfunded liability that **ranges from $10,000 - $60,000** depending on the age and service and compensation of the member."

**The comparison must be drawn on a matched years basis, and the whole section is restated on one here.** HB 1867 priced a **free** grant of **up to 48 months**. The brief's per-member figures are **net of the member's price** for **2.5** purchased years (A-18). Those are not the same quantity, and until October 25, 2026 this section set one against the other and drew a conservatism conclusion from it. **That conclusion is withdrawn (red team S-1).** Everything below is the same model re-run at **4 years**, salary $69,865, so that both sides describe the thing VRS actually priced. Reproduce with `models/redteam_checks.py`, RT-2.

| At a matched 4 years | Plan 1 | Plan 2 | Hybrid | Pool-weighted blend |
|---|---:|---:|---:|---:|
| **Free-grant equivalent** — total PV to the Fund, no member price | **$123,520** | $58,971 | $30,281 | $71,864 lo / $68,254 hi |
| Member price at the A-3 approximate normal cost | $34,932 | $30,014 | $18,668 | — |
| Net PV to the Fund after the member pays | $88,587 | $28,957 | $11,614 | $44,491 lo / $41,637 hi |
| Against VRS's $10,000 – $60,000 (average **$35,000**), free, 4 years | **2.06× the ceiling** | inside | inside | — |

> **The honest statement is a bracket, and it is also the better one to take to the money committees.** This model and VRS's own HB 1867 figures straddle the answer, and **this model is the higher of the two.** Run the comparison the other way — take VRS's $35,000 average as given and subtract the A-3 member price for four years — and the net to the Fund is **$68 (Plan 1), $4,986 (Plan 2), $16,332 (Hybrid)**, an order of magnitude below what this annex carries and ordering the plans oppositely, because VRS's band is flat across plans while the A-3 price rises steeply with the plan's normal-cost rate. So the defensible sentence is: *the two estimates bracket the answer, this model has carried the costlier side of the bracket, and the only figure that will count is the one VRS files under § 30-19.1:7.* **The word "conservative" should not appear in this comparison in either direction**, because the package has used it in both senses — once to mean "our cost figure is modest against VRS's band," which is now false, and once to mean "we have assumed the expensive outcome," which is true. Say *more expensive than VRS's* and *less expensive than VRS's* and leave the adjective out.

**The `1 − 1/m` structural claim is withdrawn, because it fails on its own identity once the years are matched.** Because the member pays the approximate normal cost, the Fund bears `1 − 1/m` of the value, where `m` is the AEC/ANC multiple — and `1 − 1/m < 1` for every `m > 1`. The ratio this annex published was computed across the mismatch:

```
WITHDRAWN - 2.5-year net against VRS's 4-year average:
  $24,627 / $35,000  =  0.704      apparently inside 1 - 1/m for m = 2.76x - 3.54x (0.638 .. 0.718)

MATCHED at 4 years, this model's own blend:
  $44,491 / $35,000  =  1.271      (low-end plan mix)
  $41,637 / $35,000  =  1.190      (high-end plan mix)
  -> above 1, so NO value of m can produce it; the identity is violated,
     not satisfied. For 0.704 to hold at 4 years VRS's average would have
     to be $63,198 - above the $60,000 ceiling of its own band.
```

The arithmetic above is red team **S-1**, reproduced. Two divergences from it, both recorded because the figures here are the ones to quote: S-1's per-plan 4-year figures reproduce exactly, but its **blend** column pairs a $55,573 free-grant equivalent with a $42,455 net, which implies a blended member price of $13,118 — below the cheapest plan's own 4-year price of $18,668, so no plan mix produces that pair. The pool-weighted blend from this model is $71,864 / $44,491 at the low-end mix, giving a matched ratio of **1.19 – 1.27** rather than S-1's 1.213. The conclusion is unchanged and the margin is wider.

**The plan-mix limit travels with every line above.** VRS's $35,000 is a **teacher-only** average for a **free** grant; the blend here is pool-weighted across six employer groups and three plans, and the teacher plan mix is unpublished (§ 1.7 request item 1). This remains a **magnitude-and-direction check, not a calibration.** Red Team **S-8** makes that point against a stronger version of this comparison on the one-pager and is right to. The residual uncertainty has a knowable direction, and after the restatement it runs *against* us rather than for us: teachers are a longer-tenure workforce, so if they skew more Plan 1 than this blend, VRS's $35,000 reflects a costlier mix than ours and the matched ratio is **higher** than 1.19 – 1.27, not lower.

**What the comparison does still establish, on any basis: the retracted figure was far too low.** A purchase at which the member still pays must cost the Fund less than a free grant of the same service, and brief v1.0's **~$3,750** per purchasing member sat roughly a factor of three below even the **floor** of a band VRS produced for a **free** benefit. That signal was available in the HB 1867 statement at the time. The live per-member figures, on the brief's own 2.5-year paid basis, are **$47,967 / $17,174 / $6,779** (§ 4.4) — and they are not to be compared cell-by-cell against VRS's band, for the reason stated at the top of this section.

**VRS also published a worked total**, Items 6 and 9, verbatim: *"if 1,500 members (1% of the Teacher population) had this type of service, and the average cost was **$35,000**, the total cost to the fund could be **$50 million**."* That total is the subject of the next paragraph, and the same basis warning applies to it: it is a free grant, four years, teachers only, at 1% participation.

**And it reframes which figure is the outlier.** The only total VRS has ever published for a benefit of this shape is **$50 million for the teacher population alone, at 1% participation, with no member price.** Against that, **$28M–$166M** across six employer groups, three plans and a 10%–30% take-up set, for a benefit the member pays for, is plainly the same order of magnitude — while "under $2 million" is not. That can now be shown from VRS's own arithmetic rather than argued. *(Range restated October 25, 2026 from "$13M–$182M, 5%–30% take-up," which predated the S-3 pool pairing correction and the S-5 single-assumption-set rebuild — § 4.4.)* **This is an order-of-magnitude statement and nothing more:** VRS's $50M is teachers only, free, four years, at an assumed 1%; ours is six groups, paid, 2.5 years, at 10%–30%. It establishes that the retracted figure was the outlier. It does not establish that either range is conservative against the other. (Teacher Plan unfunded liability, for scale: **$11.8 billion**; VRS's $50M example is 0.42% of it.)

**Three further findings from the same document**, carried in full at Annex B § 7.5:

1. **VRS cannot identify who holds the service** — it "is not able to determine the number of current teachers or future teachers who would have prior active military service to purchase" (F-62). The FM-1 § 1.6 range is therefore not a shortcoming of this analysis; no one can do better, including VRS. **Do not promise anyone a point estimate.**
2. **VRS confirms the eligibility channel**: prior service credit "counts toward vesting, eligibility for retirement and eligibility for the health insurance credit" (F-63) — § 4.1's two channels and the § 4.9 HIC exclusion, in VRS's own filed words.
3. **Precedent for the *narrow* general-fund claim — and refutation of the broad one** (F-61). For a *free* grant VRS put implementation at ~$78,000 NGF, employer cost to implement at **"None,"** and the general fund at **"no immediate impact."** A-3 requires no new rate-setting at all (FM-3, point 4), so its administrative footprint should be no larger — that part is sound precedent. **But VRS wrote "immediate," and put this beside it:** *"Depending on the number of teachers who take advantage of this provision over time, this may impact contribution rates."* So VRS's own statement supports "this bill requests no appropriation" and **does not** support an unqualified "general fund cost: $0." F-61 is therefore **evidence for** Red Team **F-2**, not against it. Use the F-2 formulation: no appropriation requested, cost absorbed in future employer rates under § 51.1-145, three exposure buckets named (§ 4.7).

**One line in it cuts against us, and should be in the brief before someone else finds it.** F-63: granting service in a pooled plan "will effectively spread the cost of each period of granted service over all of the employers in the Teacher plan." That is the mechanism by which the teacher and political-subdivision exposure lines at § 4.7 reach employers who have no veteran purchasing at all — and it is what the Commission on Local Government will read first.

### 4.7 Who bears it — state, teacher and local exposure reported separately

Required by the JLCVSO scope decision of October 24, 2026 (all VRS members, no local opt-in). Local exposure flows through political-subdivision employer rates under § 51.1-145 and **never touches the general fund**, and the Commission on Local Government receives the § 30-19.1:7 statement — so the figures must not be presented as one number.

Pool-weighted blended A-3 net present value per purchaser: **$24,627** at the low end of the pool and **$23,077** at the high end (DERIVED). The two differ because the plan mix is not constant across the pool ends — Hybrid, by far the cheapest plan per purchaser, grows 2.35× between them against Plan 1's 1.90× — so a single blend cannot serve both.

| Who bears the employer-rate consequence | Eligible pool | PV cost at 20% take-up |
|---|---|---|
| **State agencies** (general fund + nongeneral fund) — VRS State Employees, SPORS, VaLORS, JRS | 4,113 – 8,099 | **$20.3M – $37.4M** |
| **Teachers** — school divisions, shared with the Commonwealth through the Standards of Quality | 2,699 – 6,768 | **$13.3M – $31.2M** |
| **Political subdivisions** — § 51.1-145 employer rates, no general fund | 4,753 – 9,169 | **$23.4M – $42.3M** |
| **Total** | 11,565 – 24,036 | **$57.0M – $110.9M** |

**The total reconciles to the § 4.4 grid's 20% row to the dollar, at both ends.** That is worth stating because it is the first arithmetic a money committee will do — add the three buckets, compare to the headline — and until October 25, 2026 it did not hold.

> **Corrected October 25, 2026.** The high ends above read $39.9M / $33.3M / $45.2M for a total of **$118.4M**, against a § 4.4 grid that gave **$110.9M** for the same 20% take-up on the same pool — a $7.5M gap. The cause was *not* the eligible pool, which red team S-3 had already reconciled. It was that this table struck the blended per-purchaser figure once, at the **low**-end plan weights, and then applied it to **both** ends of the employer-group headcount. The low-end blend overstates the high end by 6.3%, because Hybrid — the cheapest plan per purchaser — is a larger share of the high end. Striking the blend at each end closes the gap exactly. Left unfixed, this table would have reproduced the symptom S-3 was raised about, from a different cause, in the one place a reviewer is most likely to look.

Two things to be explicit about.

**Teachers are reported as their own bucket rather than split between the Commonwealth and localities.** Allocating the teacher line requires the Standards of Quality composite share, which is a budget input rather than a VRS one. **Flagged for DPB; not assumed here.**

**The blended per-purchaser figure is applied uniformly across employer groups, and that is an ESTIMATE.** Plan mix by employer group is not published. It is least reliable for SPORS and VaLORS, which are Plan 1 / Plan 2 hazardous duty, where *both* the benefit value (richer multipliers, earlier thresholds) and the member price (19.15% against 10.74%) are materially higher. The net direction for those two groups is genuinely unclear and should not be read off this table — it is item 1 of the § 1.7 data request.

**The political-subdivision line is the largest of the three.** That is the number the Commission on Local Government will see, and it arrives without a local opt-in. It is the most likely source of organised opposition to the bill and should be briefed before filing, not after.

### 4.8 The two guardrails, priced as dials

Immediate access on the effective date means the actuary prices an **unbounded cohort**, which puts the entire weight of adverse-selection control on the two guardrails in Annex A. Pricing them as dials produced the most consequential drafting finding in this package.

**Guardrail A — Board authority to set an age-graded approximate-normal-cost schedule.** Dial = the share of the above-break-even excess recovered from the member; 0% is plain A-3, 100% is full actuarial value.

| Recovery | Plan 1 | Plan 2 | Hybrid | Blended | PV at 20% take-up |
|---|---:|---:|---:|---:|---:|
| 0% | $47,967 | $17,174 | $6,779 | $24,627 | $57.0M |
| 50% | $44,142 | $16,273 | $6,382 | $22,827 | $52.8M |
| 100% | $40,317 | $15,371 | $5,985 | $21,027 | $48.6M |

> **Finding: the age-graded schedule as currently described is a weak dial.** Turning it all the way from 0% to 100% removes only about **15%** of the exposure.
>
> The reason is structural, not a modelling artefact. Grading on **age** recovers only the benefit-amount excess. The dominant cost driver is retirement-date acceleration, and acceleration is driven by proximity to an eligibility **threshold** — age *and* service together. A 55-year-old with 25 years of service and a 55-year-old with 8 years would pay the identical age-graded rate while costing the Fund very different amounts. Annex A asks this guardrail to carry the adverse-selection argument; as described, it cannot.

**Guardrail A′ — the same authority, graded on distance from unreduced eligibility rather than on age alone.** This is a *drafting* change, not a policy change: still a published schedule, still predictable, still no individualised actuarial bill handed to a veteran.

| Recovery | Plan 1 | Plan 2 | Hybrid | Blended | PV at 20% take-up |
|---|---:|---:|---:|---:|---:|
| 0% | $47,967 | $17,174 | $6,779 | $24,627 | $57.0M |
| 25% | $35,975 | $12,880 | $5,084 | $18,470 | $42.7M |
| **50%** | **$23,984** | **$8,587** | **$3,389** | **$12,313** | **$28.5M** |
| 75% | $11,992 | $4,293 | $1,695 | $6,157 | $14.2M |
| 100% | $0 | $0 | $0 | $0 | **$0** |

**This is the dial that bites** — but **not all the way, and the 100% row above is not a lawful setting.** See § 4.8.1, which supersedes the reading previously given here. The sentence this table originally carried — "at 100% the bill is actuarially neutral by construction and the fiscal note is zero" — **is withdrawn.**

#### 4.8.1 What a *lawful* uniform class rate can actually recover — F-1

> **Correction, October 25, 2026 (red team F-1, the most serious finding in the review).** The table above is produced by `price_threshold_graded()`, which charges each member `ANC + recovery × (that member's own full-basis value − ANC)`. At `recovery = 1.0` the member pays exactly their own actuarial value and the net is zero **by subtraction**. The function never computes a class rate: **it is individualised actuarial pricing, modelled.**
>
> Annex A § 2.2 forbids that. A Board schedule must (a) "apply uniformly to all members within the same classification" **and** (b) "not require payment of an amount exceeding the actuarial equivalent cost of the service credit purchased." Limb (b) binds **member by member**. So a single lawful uniform price for a class must be set at or below the **minimum** actuarial value in that class, not the mean:
>
> ```
> P*(class) = max( published ANC price , min over members of AEC )
> recovery  = (P* − ANC) / (class mean AEC − ANC)
> ```
>
> which equals 1.0 only if actuarial value is **constant** inside the class — and it never is, because the class is exactly where the variation the schedule exists to price has been pooled away.

**Verified independently** (`models/f1_lawful_class_rate.py`, not a re-run of the red team's script). Classes drawn as finely as the § 2.2 factors permit while remaining genuine published classes — plan × 5-year age band × 10-year service band, 2.5 years purchased, salary held constant at $69,865 so the only variation inside a class is the risk being priced. 60 priceable classes:

| Class | min AEC | mean AEC | max/min | **100% dial actually recovers** |
|---|---:|---:|---:|---:|
| Plan 1, age 50–54, svc 30–39 | $55,066 | $56,559 | 1.05× | **96%** |
| Plan 1, age 45–49, svc 30–39 | $46,394 | $50,057 | 1.17× | 87% |
| Plan 1, age 50–54, svc 20–29 | $58,372 | $73,583 | 1.76× | 71% |
| Plan 1, age 60–64, svc 20–29 | $35,256 | $55,745 | 2.77× | 40% |
| **Plan 1, age 55–59, svc 20–29** | **$32,822** | **$69,446** | **3.06×** | **23%** |
| Plan 1, age 50–54, svc 10–19 | $24,656 | $37,006 | 2.31× | 19% |
| Plan 1, age 45–49, svc 10–19 | $22,954 | $45,716 | 2.45× | **5%** |
| Plan 2, age 55–59, svc 10–19 | $26,410 | $35,987 | 1.64× | 44% |
| Hybrid, age 50–54, svc 0–9 | $12,461 | $14,705 | 1.48× | 26% |
| Hybrid, age 60–64, svc 30–39 | $26,047 | $27,291 | 1.09× | 92% |

**Recovery band across all 60 classes: 0% – 96%. Unweighted mean: 63%.** Per plan: Plan 1 **mean 59%**, Plan 2 **66%**, Hybrid **65%**.

**The class that matters recovers 23%.** Plan 1, age 55–59, 20–29 years of service is the cohort the one-pager leads with and the cohort Annex A § 2.5 names as "most eager for the bill." Within it, actuarial value spans **3.06×** — from $32,822 to over $100,000 — because a 55-year-old with 29 years is one year from the age-50/30-year door while a 59-year-old with 20 years is not. A uniform rate lawful for the first member recovers almost nothing from the second. **The fiscal note is not zero at any lawful setting of the schedule as drafted.**

**Restated exposure.** Because the age-and-service distribution of the veteran pool is **not published** (A-22 / U-01), no weighting inside a plan is defensible; the equal-weighted class mean is the central estimate and the extremes are bounds on a *single* classification, not settings the Board could adopt system-wide.

| Setting | Residual PV at 20% take-up |
|---|---:|
| 0% — plain published ANC, no schedule | $57.0M – $110.9M |
| Lawful uniform rate, **best** class in each plan (92%–96%) | $3.0M – $5.9M |
| **Lawful uniform rate, class mean (59%–66%) — the planning figure** | **$22.4M – $43.5M** |
| Lawful uniform rate, **worst** class in each plan (0%) | $57.0M – $110.9M |
| 100% individualised | $0 — **not lawful under § 2.2 as drafted** |

**So the guardrail is worth roughly $22M–$44M of residual rather than $0.** That is still the most powerful cost control in the package — it removes about 60% of the above-ANC excess — but it is a *mitigation*, not a neutrality device, and it must be offered to the money committees as one.

> **Restated October 25, 2026 onto the corrected eligible pool (red team S-3).** This table previously read **$20.5M – $47.7M** at the class mean, against a 0% row of **$52.0M – $121.5M**, because it was built on the **pre-correction** by-plan pool of 10,561 – 26,321. The pairing fix collapses that onto the single reconciled pool of **11,565 – 24,036** (§ 4.8.2), which raises every low end and lowers every high end. **The planning figure is now $22M–$44M, and "$20M–$48M" should not be quoted.**
>
> Nothing else in this subsection moves, and the reason is worth stating: the recovery band (0%–96%), the unweighted mean (63%), the per-plan means (59% / 66% / 65%) and the four breached classes below are all properties of the **class structure**, not of the pool. The pool scales the dollars; it does not touch what a lawful class rate can recover. Reproduce with [`models/f1_lawful_class_rate.py`](models/f1_lawful_class_rate.py), which now **imports** the pool from `fm_model.fm1_pool_by_plan()` instead of restating it — the duplication being what allowed S-3 to survive in the first place.
>
> Two models in this package print this row and **they now agree to the dollar at $22,415,208 – $43,529,148.** [`models/s9_subanc_leak.py`](models/s9_subanc_leak.py) briefly differed by 0.3% because it applied the *rounded* 59 / 66 / 65 dial; it now runs the full-cost reading through its own 60-class sweep and reproduces this subsection's band — 0%–96%, per-plan means 59% / 66% / 65%, four breached classes — as a control on its own machinery. `f1_lawful_class_rate.py` remains the source for this subsection; the agreement is a check, not a second opinion.

> **⚠ The band above is one of two, and the other is worse. Do not quote it alone.** Everything in this subsection prices the § 2.2 ceiling as the member's **full cost to the Fund** — benefit-amount channel *plus* retirement-date acceleration. Red team **F-1A** holds that "the actuarial equivalent cost of the service credit purchased" means the **statutory AEC** — the benefit-amount channel alone, the phrase's meaning two sentences earlier in the same paragraph of § 51.1-142.2 B 3. On that reading the recovery band is materially lower and the residual is close to the 0% row:
>
> | Reading of "actuarial equivalent cost" | Class-mean recovery | Residual PV at 20% take-up |
> |---|---:|---:|
> | **Full cost to the Fund** (this subsection) | 59%–66% | **$22.4M – $43.5M** |
> | **Statutory AEC** (F-1A) — per member, § 4.8 profiles | 10%–16% | $48.6M – $94.8M |
> | **Statutory AEC** (F-1A) — class mean, uniformity compounded | 20%–26% | **$43.2M – $84.2M** |
>
> (All three restated October 25, 2026 onto the corrected pool; the pre-correction figures were $20.5M – $47.7M, $44.4M – $103.8M and $39.4M – $92.2M. The recovery columns are pool-independent and unchanged.)
>
> Which reading governs is a question of law, routed to counsel, and **not settled here**. Until it is settled the planning figure is a pair, not a number. **§ 4.8.3 carries the derivation, and a third finding that moves both readings by an order of magnitude.**

**A further defect, not in F-1, found on this pass.** In **4 of the 60 classes** the published ANC price **itself exceeds the lowest member's own actuarial value**:

| Class | min AEC | ANC price | Shortfall |
|---|---:|---:|---:|
| Plan 1, age 40–44, svc 0–9 | $17,243 | $21,833 | $4,590 |
| Plan 1, age 45–49, svc 0–9 | $20,619 | $21,833 | $1,214 |
| Plan 2, age 45–49, svc 0–9 | $18,470 | $18,759 | $289 |
| Hybrid, age 45–49, svc 0–9 | $11,194 | $11,667 | $474 |

In these classes the § 2.2 individual-AEC ceiling is breached **by the baseline price**, before any dial is turned. Read literally, the ceiling would require the Board to charge those members **less than the published approximate normal cost** — so the ceiling is not merely a weak constraint on the dial, it is **inconsistent with the published-rate floor the draft also relies on.** This is a drafting matter for Annex A, flagged to the Drafting Specialist, and it strengthens the case for F-1's option (a) below.

**The two ways out, both of which have a price.**

- **(a) Strike the individual-AEC ceiling; cap at the actuarial equivalent cost determined *for the classification*.** A class rate becomes lawful and the dial recovers the class **mean** — close to the full $0-residual arithmetic. The cost: **some members pay above their own actuarial value**, which must be said out loud rather than discovered by a member. This also cures the four-class inconsistency above.
- **(b) Keep the individual ceiling and uniformity, and re-state the fiscal case on the band above** — a central residual of **$22M–$44M at 20% take-up**, and effectively **no** recovery in the Plan 1 long-service cohort.

**And a third problem that survives both.** At the 100% setting the member pays the actuarial equivalent cost — **which is what § 51.1-142.2 B 3 already charges today after 24 months.** The setting that drives the fiscal note toward zero is the setting at which the bill's *price promise* is extinguished; what remains is a published rate and the 60-month term. Annex A § 2.5 concedes this for Plan 1 veterans in one sentence. **The one-pager does not concede it anywhere** — it promises the "regular price … at any point in their career" on the same page. Flagged to Editor and Policy Director; it is not a modelling fix.

**Annex A Q3a needs reframing**, from "how closely does a class rate track AEC" to **"is a class rate that recovers the class mean lawful under the ceiling we drafted."** On the analysis above the answer is no, and that is the question to put to VRS and to Legislative Services.

#### 4.8.2 M-4 — the two eligible pools were one pool, and S-3 is why they looked like two

> **Reported October 25, 2026 as red team M-4. CLOSED the same day as a symptom of red team S-3, not an independent finding.** M-4's observation was correct and worth making: `fm_model.py` was producing **two** pools for the same population, and the package was quoting whichever was to hand.

| Derivation | Pool, as it stood when M-4 was raised | One-time PV at 20% take-up, 0% recovery |
|---|---|---:|
| **By plan** (FM-1 § 1.6 — the basis of the retracted $13M–$182M grid) | 10,561 – 26,321 | $52.0M – $121.5M |
| **By employer group** (FM-4 § 4.7 — the basis of the who-bears table) | 11,565 – 24,036 | $57.0M – $118.4M |

The first reading of this was that the two derivations answer different questions — the by-plan one applying the veteran rate uniformly across plans, the by-group one applying group-specific rates — and that both were therefore legitimate. **That reading was wrong, and S-3 is the reason.**

The by-plan figure is not a second estimate. It is a *reallocation* of the by-group pool onto plans, and the reallocation is an identity: the effective veteran-with-qualifying-service rate is the pool divided by the past-window population the pool was built from, and the three plan legs sum back to that same population. So the two derivations are arithmetically obliged to agree at both ends. They did not agree only because the effective-rate band was cross-wired — `eff_lo = pool_lo / pw_hi` and `eff_hi = pool_hi / pw_lo` paired each end of the pool with the **opposite** end of the past-window population. Pairing like with like:

| Derivation | Pool, corrected | One-time PV at 20% take-up, 0% recovery |
|---|---|---:|
| **By plan** (FM-1 § 1.6) | **11,565 – 24,036** | **$57.0M – $110.9M** |
| **By employer group** (FM-4 § 4.7) | **11,565 – 24,036** | **$57.0M – $110.9M** |

**There is one pool, and no smaller one for the dials to be quoted on.** The prior resolution of M-4 — "state every guardrail figure at both pool ends, and label the dial column as the group-derivation low end" — is therefore **withdrawn as unnecessary**: there are no longer two pool bases to reconcile. What survives of M-4 is the narrower and still-valid point that a dial figure must be stated at both ends of the *one* pool rather than at its low end alone, which § 4.8.1 now does.

Annex A § 5.1's guardrail arithmetic — "$57.0M → $48.6M," "$57.0M → $28.5M" — was the low end of the group derivation presented without qualification as "the modelled exposure," against a published ceiling of $182M taken from the plan derivation. On the corrected pool the low end is unchanged at $57.0M, the high end is $110.9M, and the ceiling of the published band is $166M. **Annex A § 5.1 still needs the two-ended restatement**; flagged to the Drafting Specialist, because the arithmetic is mine but the sentence is theirs.

**Structural fix, so this class of defect cannot recur.** The by-plan pool was derived in `fm_model.py` and *hardcoded* in two other scripts, which is how a single pairing error produced what looked like a disagreement between two methods. `fm_model.fm1_pool_by_plan()` is now the single source and every consumer imports it; `models/f1_lawful_class_rate.py` and `models/s9_subanc_leak.py` no longer restate the figures.

> **Recommendation to Legislative Services.** Express the Board's rate-schedule authority as varying by the member's **age and creditable service**, or by the member's **distance from unreduced retirement eligibility** — *not* by age alone. One phrase, and it is the difference between a guardrail that removes about 15% of the exposure and one that removes roughly **60%**. *(Originally written "and one that can remove all of it"; corrected per F-1 — see § 4.8.1.)*

> **Status: adopted, October 25, 2026 — Annex A v1.1, § 2.2; materially qualified October 25, 2026 by F-1.** Counsel widened the authority to age **and** creditable service (with distance from unreduced eligibility named as the equivalent alternative), added the amount of service purchased as a third factor, and attached publication, uniformity-within-classification, and actuarial-equivalent-cost-ceiling constraints plus an express sentence confining the schedule to subdivision B 2. The counsel analysis is at Annex A § 2.5. **Guardrail A as modelled above is therefore superseded by Guardrail A′ as the description of what Annex A actually grants** — the 15% figure is retained here as the record of why the change was made, not as a current description of the draft.
>
> **But the two constraints counsel attached are the binding ones.** Uniformity-within-classification plus an **individual** actuarial-equivalent-cost ceiling mean Guardrail A′ as *drafted* cannot be set to the values modelled in the A′ table above; the achievable band is **0%–96% recovery, 59%–66% at the class mean, ~23% in the dominant Plan 1 cohort**, for a residual of **$22M–$44M** rather than $0 (**§ 4.8.1**). What was adopted is therefore better than Guardrail A and materially weaker than the A′ table reads. **Annex A Q3a must be reframed** (§ 4.8.1), and **Q12 — the dial setting — is now a choice between two drafting options rather than a choice of a number on a 0–100% scale.** Q14 (age/service as rate factors) is unaffected.

**Guardrail B — require completion at least N months before the effective date of retirement.** This does not change the price. It caps how close to the unreduced date a purchase may be made, and therefore caps the multiple the Fund can be exposed to. Ceiling on the AEC/ANC multiple:

| Plan | Age / service | Unreduced at | No rule | 12 mo | 24 mo | 36 mo |
|---|---|---:|---:|---:|---:|---:|
| Plan 1 | 50 / 25 | 55.0 | 1.35× | 1.30× | 1.26× | 1.21× |
| Plan 1 | 55 / 25 | 60.0 | 1.61× | 1.56× | 1.50× | 1.45× |
| Plan 1 | 60 / 29 | 61.0 | 1.67× | 1.61× | 1.56× | 1.50× |
| Hybrid | 50 / 25 | 57.5 | 1.40× | 1.35× | 1.30× | 1.25× |
| Hybrid | 55 / 25 | 60.0 | 1.53× | 1.47× | 1.42× | 1.37× |
| Hybrid | 60 / 29 | 60.5 | 1.55× | 1.50× | 1.45× | 1.40× |

A 12-month window shaves the ceiling by only about 3%–4%, because the multiple is a smooth function of age — there is no cliff in it to cut off. **Guardrail B is worth having**: it is a clean anti-gaming rule, it costs veterans almost nothing, and it is easy to defend. But it is **not a substitute for Guardrail A′, and it should not be traded for it** in negotiation. If only one guardrail survives, it must be A′.

#### 4.8.3 The ceiling's second reading, its downward leg, and the unstated input both turn on — F-1A and S-9

> **Added October 25, 2026** in response to red team § 10 (F-1A, fatal; S-9, serious). Working file `models/s9_subanc_leak.py`, which imports `fm_model.py` unmodified and writes nothing. **This subsection does not supersede § 4.8.1 — it brackets it.** § 4.8.1's arithmetic is correct on its stated basis; what § 4.8.1 does not say is that its basis is one of several, and the choice among them moves the answer by an order of magnitude.

**The headline of this pass is not either red team finding. It is the input both of them silently depend on.**

##### (1) The unstated input: at what retirement age is the AEC measured?

`aec_pct_of_salary(plan, purchase_age, retire_age)` takes the retirement age as an argument, and nothing in the package states which value the ceiling should use. Two families of choice are defensible and they are not close:

| Basis | Retirement age used | Where the package already uses it |
|---|---|---|
| **NRA** | Plan normal retirement age — **65 / 67 / 67** | `multiple_at()`, `fm2_surface()`, the break-even ages, red team `rt_check2.py`, and the "below age 47–48 the veteran subsidises the Fund" claim |
| **OWN** | The member's **own unreduced eligibility age** — typically **46–58** | `fm4_acceleration()`, which produces the full-basis cost every ceiling figure is compared *against* |

**The package is currently comparing a price measured at age 65 against a benefit measured at age 57.5.** That is not like-for-like, and it is the dominant sensitivity in both F-1A and S-9. **VRS does not publish the basis.** FM-2 § 2.1–2.2 establishes that the actuary develops an AEC factor table annually and that it is not published; that table necessarily embeds a retirement-age assumption, and no figure in this subsection can be settled without it. **Registered as Annex B A-30 and open item U-16, which now outranks every open item except U-01.**

A sub-objection, tested rather than waved away: if the AEC is measured at the member's own **post**-purchase unreduced age, does that smuggle the retirement-date acceleration back inside the ceiling — the one thing the statutory reading excludes? Partly, and the model carries a third basis (**OWN0**, the member's **pre**-purchase unreduced age) to bound it. OWN0 cuts recovery by 12–16 percentage points against OWN and roughly triples the (still small) leak, but it does not restore the NRA figures: recovery on OWN0 is 31%–45% against NRA's 10%–16%, and the aggregate leak tops out at **$2.3M** against **$32.8M** on NRA. **The sensitivity that governs is normal-retirement-age versus own-retirement-age.**

##### (2) F-1A — the statutory reading of the ceiling, and what it caps recovery at

F-1A is **correct and it reproduces exactly** on the NRA basis. Per member, on § 4.8's own representative profiles, 2.5 years, $69,865:

| Plan | ANC price | Full cost to Fund | Ceiling, NRA | Max recovery, NRA | Ceiling, OWN | Max recovery, OWN |
|---|---:|---:|---:|---:|---:|---:|
| Plan 1 | $21,833 | $69,800 | $29,483 | **16%** | $45,560 | 49% |
| Plan 2 | $18,759 | $35,933 | $20,561 | **10%** | $28,480 | 57% |
| Hybrid | $11,667 | $18,446 | $12,461 | **12%** | $14,872 | 47% |

**One correction to how F-1A's number must be used.** 10%–16% is a **per-member** figure on three profiles. § 4.8.1's band is a **class** band, so the two are not comparable and the 10%–16% must not be dropped into § 4.8.1's table as though it were. Re-running § 4.8.1's own 60-class sweep with the ceiling set to the statutory AEC gives the comparable figure:

| Basis | Classes | Recovery band | Class mean | Classes where the published ANC price exceeds the lowest member's ceiling |
|---|---:|---:|---:|---:|
| **NRA** | 60 | 0% – 83% | **22%** | **24 of 60** |
| **OWN** | 60 | 0% – 96% | **48%** | 6 of 60 |
| *FULL — the full-cost reading, § 4.8.1's own* | *60* | *0% – 96%* | *63%* | *4 of 60* |

The FULL row is a **control, not a result**: `s9_subanc_leak.py` runs the full-cost reading through the identical sweep, and it reproduces § 4.8.1's published band — 0%–96% by class, per-plan means 59% / 66% / 65%, four classes breached by the baseline price — and `f1_lawful_class_rate.py`'s residual to the dollar. So the NRA and OWN rows differ from § 4.8.1 because of the *reading*, not because of the machinery.

Residual PV at 20% take-up, all readings side by side, on the **S-3-corrected pool** (11,565 – 24,036):

| Setting | Residual PV, low pool – high pool |
|---|---:|
| 0% — no schedule adopted | $57.0M – $110.9M |
| Statutory reading, NRA, per member (red team § 10.1) | $48.6M – $94.8M |
| **Statutory reading, NRA, class mean — uniformity compounded** | **$43.2M – $84.2M** |
| Statutory reading, OWN, class mean | $28.1M – $55.0M |
| Full-cost reading, class mean (§ 4.8.1's figure, restated) | $22.4M – $43.5M |
| 100% individualised | $0 — **not lawful** |

**The red team's expectation holds on the NRA basis and dissolves on the OWN basis.** On NRA the statutory reading pushes the residual most of the way back to the 0% row — **$43M–$84M against $22M–$44M, where doing nothing at all costs $57M–$111M** — and the compounding the red team describes is visible in the "24 of 60" column: uniformity pins each class price at the class's lowest ceiling, that ceiling is below the published rate in 40% of classes, so in those classes recovery is 0% *and* the baseline is unlawful. On OWN the two readings converge, because the ceiling then sits above the published price for most members and uniformity is the only constraint that bites — which is F-1 exactly as § 4.8.1 already publishes it.

##### (3) S-9 — pricing the downward leg

S-9 is **right as a drafting defect**: the drafted ceiling is a cap with no floor, so wherever the member's own AEC is below the published approximate normal cost a lawful schedule must charge **less than § 51.1-142.2 B 3 charges today**, and nothing in `fm_model` prices a sub-ANC purchase. Break-even purchase ages reproduce at **Plan 1 46.60, Plan 2 47.43, Hybrid 48.16** on the NRA basis.

But the leak's size is almost entirely an artefact of the NRA basis. Share of structurally feasible (age, service) pairs at which the ceiling falls below the published price:

| Plan | Feasible pairs | Leaking, NRA | Leaking, OWN |
|---|---:|---:|---:|
| Plan 1 | 493 | 91 (18%) | **0 (0%)** |
| Plan 2 | 555 | 300 (54%) | 43 (8%) |
| Hybrid | 425 | 249 (59%) | 62 (15%) |

*Feasibility is sourced, not assumed: ACFR Fig. 2.10 closes Plan 1 to membership dates before July 1, 2010 and Plan 2 (apart from the hazardous-duty and, from July 1, 2026, judicial openings) before January 1, 2014, so a Plan 1 member necessarily holds ≥ 16 years of membership and a Hybrid member ≤ 12.5. The floor is 2.0 years everywhere because the pool is defined as members past the 24-month window.*

On the OWN basis the leak survives only for **low-service members just past the 24-month window** — and that cohort's size *is* derivable without an age distribution, because the vested / non-vested split is official: non-vested members past the window are **19.0% – 26.0%** of the past-window population.

**Aggregate value of the leak**, one-time PV on the S-3-corrected pool. The share of the pool below the break-even purchase age is a **scenario assumption and cannot be made an estimate** — the age distribution of the veteran pool is unpublished (A-22 / U-01, registered as **A-31**). Take-up among this cohort is reported separately from the A-22 blend (**A-32**) because the blend is the wrong rate here, though the direction is arguable both ways: *upward*, because the bill makes their price lower than today's Code price, they have the longest runway over the 60-month payroll-deduction term, and theirs is the cheapest purchase in absolute dollars; *downward*, because they are decades from any eligibility date and the purchase buys them nothing they can feel.

| Under-break-even share | Take-up 20% | Take-up 30% | Take-up 50% |
|---|---:|---:|---:|
| **NRA basis** — mean leak $3,195 / $5,412 / $3,585 per member | | | |
| Low (25%) | $2.2M – $4.6M | $3.3M – $6.9M | $5.6M – $11.5M |
| **Central (50%)** | $4.5M – $9.2M | **$6.7M – $13.8M** | $11.2M – $23.0M |
| High (65%) | $5.8M – $12.0M | $8.7M – $18.0M | $14.5M – $29.9M |
| **OWN basis** — mean leak $0 / $123 / $153 per member | | | |
| Central (50%) | $0.1M – $0.2M | $0.2M – $0.3M | $0.3M – $0.6M |

**So the leak is worth roughly $6M–$15M at the central cell on the red team's basis, and under $0.4M on the other basis** — bands that hold at both ends of both pool derivations, which is why they are quoted rounded. The 50% central share is anchored on DHRM F-32: classified-workforce average age **46.7**, which sits 0.1 years *below* the Plan 1 break-even and about a year below Plan 2's and Hybrid's, so a symmetric distribution about that mean puts roughly half the pool under the break-even age. Against that anchor: Plan 1's closure skews it old and Hybrid's 2014 opening skews it young, which runs opposite to where the per-member leak is largest.

##### (4) The residual with and without the leak — and a caution about adding them

Asked for directly, at § 4.8.1's published settings plus the leak at the central cell:

| Setting | No leak | + leak, NRA | + leak, OWN |
|---|---:|---:|---:|
| 0% — plain published ANC | $57.0M – $110.9M | $63.7M – $124.8M | $57.1M – $111.3M |
| **59%–66% class mean (§ 4.8.1's figure)** | **$22.4M – $43.5M** | **$29.1M – $57.3M** | $22.6M – $43.9M |
| 96% best class | $2.3M – $4.4M | $9.0M – $18.3M | $2.4M – $4.8M |

**Those "+ leak" columns are upper bounds, and the reason matters.** § 4.8.1 prices the *whole* pool at the representative profile, and all three representative profiles sit **above** the break-even age — so the under-break-even cohort is counted once in the base figure and again in the leak. Decomposing properly — splitting the pool at the break-even age and pricing each cohort on its own profiles and its own take-up — gives, at the 50% share and 30% below-break-even take-up: **$42.1M – $83.0M on NRA** and **$35.6M – $69.6M on OWN**, against § 4.8.1's $22.4M – $43.5M.

**But note which way the decomposition runs, because it is the opposite of what "a leak understates the residual" suggests.** Below the break-even age the member's own full cost to the Fund is *small* — the allowance is decades away and heavily discounted — so net cost per purchaser below break-even ($29,369 Plan 1 / $15,272 Plan 2 / $8,333 Hybrid on NRA) is set against a representative-profile net of $47,967 / $17,174 / $6,779 before recovery, and $19,765 / $5,816 / $2,369 after it. A pool that is half young purchasers is **cheaper in total** than § 4.8.1's flat-profile arithmetic implies. **The leak is a real loss of receipts measured against current law, and it is a real answer to the opposition's best line — the bill does not merely delay the cliff, it discounts young purchasers below today's price. It is not, by itself, a reason to raise the § 4.8.1 headline.** Both things are true and the memo must carry both.

##### (5) Pool basis — now the S-3-corrected pool

Every figure above is on the **S-3-corrected** pool, 11,565 – 24,036, at both ends. Red team **S-3**, owned separately, found the effective-veteran-rate band in `fm_model` cross-wired, pairing each end of the pool with the opposite end of the past-window population. Correcting it collapses the by-plan pool onto the by-employer-group pool — so **M-4 at § 4.8.2 was a symptom of S-3, not an independent finding**, and the two derivations now agree exactly at both ends. `models/s9_subanc_leak.py` takes that pool by importing `fm1_pool_by_plan()`, which is the single source of the derivation, rather than restating it; a private second copy of this derivation in two files is what allowed S-3 to survive.

For continuity with anything already circulated on the **pre-correction** pool (10,561 – 26,321), the script prints every table on both, and the ends move as follows:

| Setting | Pre-correction pool | **Corrected pool** |
|---|---:|---:|
| 0% — no schedule | $52.0M – $121.5M | **$57.0M – $110.9M** |
| Full-cost reading, class mean (§ 4.8.1) | $20.5M – $47.7M | **$22.4M – $43.5M** |
| Statutory reading, NRA, class mean | $39.4M – $92.2M | **$43.2M – $84.2M** |

**The low ends rise, the high ends fall, and no conclusion in this subsection or in § 4.8.1 changes.** The leak bands quoted above are rounded precisely because they hold at both ends of both derivations.

##### (6) Routing

| Owner | Item |
|---|---|
| **Counsel / Statutory Researcher** | Which reading of "actuarial equivalent cost" governs. Until this is settled the fiscal case has two planning figures, not one. |
| **Drafting Specialist** | S-9's express floor — "provided that no such schedule shall require payment of less than the approximate normal cost otherwise determined under this subdivision." On the NRA basis it is worth $6M–$15M; on either basis it costs nothing to add and it removes the opposition's discount-to-young-veterans line. |
| **VRS (data request)** | Annex B U-16 — the retirement-age basis of the existing post-24-month AEC factors, and whether they are a function of age at purchase alone or of age and service. Plus the age-at-purchase distribution of completed § 51.1-142.2 purchases, which would convert the under-break-even share from a scenario into an estimate. |
| **Editor** | § 4.8.1's band must never appear without the § 4.8.1 warning box. Strike "25%–73%" wherever carried forward, per red team § 10.3. |

### 4.9 Not priced here

Carried forward from the brief, still unpriced, all pushing upward: the health insurance credit including its 15-year step function (§ 51.1-1400); adverse selection; the early-retirement reduction subsidy (§ 4.2); VRS administrative cost, for which HB 1867's analogue was about $78,000 one-time; and the employer-side payroll and backfill consequences of earlier retirement, which are a cost to agencies and school divisions, not to the Fund, and which must not be netted against the pension figures.

---

## FM-5 — Did the Board set new ANC rates effective July 1, 2026?

**No.** Closed as a qualified negative, with the search recorded.

**What was searched.** VRS Board of Trustees minutes for **February 5, 2026**, **April 23, 2026** and **June 17, 2026** (each of which carries the Benefits and Actuarial Committee's report in full); the Benefits and Actuarial Committee materials for **June 17, 2026**; and the current published *Purchase of Prior Service Cost Rates* charts, all four pages.

**What was found.**

1. **No rate action in 2026.** No 2026 Board or B&A item approves, proposes, or revises approximate normal cost rates. The only 2026 purchase-of-prior-service item is legislative: HB 139, which VRS staff told the Board "addresses several changes for school boards and their employees, including a purchase of prior service provision that **would not change VRS current procedures**" (minutes, April 23, 2026). This is consistent with Annex B F-36 — 2026 Acts c. 563 amended § 51.1-142.2 for an unrelated purpose.
2. **The rates are not on an annual cycle.** VRS Board minutes of June 18, 2025 — OFFICIAL, verbatim: *"The approximate normal cost rates are updated every four years following the Board's acceptance of the new assumptions associated with the quadrennial experience study."*
3. **The current rates were set once, for July 1, 2025.** Request for Board Action **2025-06-10** adopted them following the Board's **April 16, 2025** acceptance of the four-year experience study for the period ending June 30, 2024 (June 30, 2025 valuation, Executive Summary).
4. **The next review is 2029 — on VRS's own record.** The Benefits and Actuarial Committee minutes of **June 17, 2026** record staff recommending that the committee "review the actual experience during the **next quadrennial assumption review in 2029**."
5. **The "Updated: July 1, 2026" stamp is a document refresh, exactly as suspected.** On the current chart set, page 1 (Hybrid) is headed "Effective July 1, 2025" and footed "Updated: July 1, 2026," with the rate unchanged at 6.68%. Pages 2, 3 and 4 (Plan 1, Plan 2, alternate hazardous duty) are headed "Effective July 1, 2025" and footed "**Updated: July 1, 2025**." The file's own PDF metadata gives a creation and modification date of **July 1, 2026**. So one page was re-stamped when the file was regenerated and three were not. No rate moved.

**Therefore:** the rates to use are those effective **July 1, 2025**, and they are **expected to remain in force through at least June 30, 2029**, absent an off-cycle Board action. That is better than the brief needed — it means the rates quoted to the JLC will not go stale during the 2027 session, and the brief can say so.

---

## What this changes in the brief

For MOO-288 to action. Listed most material first.

0. **HOLD the printed one-page leave-behind.** `00-ONE-PAGE-BRIEF.pdf` is the artifact meant to be handed to legislators, and it carries both superseded figures: "under $2 million one time and under $100,000 a year," and "about 5 cents out of every $100." Its markdown source carries a hold banner as of this annex; **the PDF has not been regenerated and should not be distributed until the cost block is revised.** How to present a tens-of-millions present-value liability to a legislator — against a $0 general fund ask that remains entirely correct — is a presentational judgment for counsel, not a modelling one, which is why this annex flags it rather than rewriting it.

1. **Replace the cost headline.** "Under $2 million one-time; under $100,000 per year ongoing" cannot survive contact with the money committees. Replace with the FM-4 § 4.4 grid, a plain statement that the present value is in the tens of millions on central assumptions, and the § 4.6 cross-check in the form § 4.6 now states it — *this model and VRS's own HB 1867 figures **bracket** the answer, and this model is the higher of the two.* **Do not offer the cross-check as evidence that this figure is conservative relative to HB 1867** (red team S-1, applied October 25, 2026): matched at four years the free-grant equivalent for a Plan 1 member is $123,520, or 2.06× the top of VRS's band. The $0 general fund ask is unaffected and remains correct — this is an employer-contribution-rate liability amortised under the VRS Funding Policy, not an appropriation.
2. **Correct "Plan 2 is a closed cohort."** It is open for SPORS, VaLORS, political-subdivision hazardous duty, and — from July 1, 2026 — newly appointed judges. (FM-1 § 1.3, FM-3.)
3. **Lead the population discussion with the one number that needs no estimate:** 110,474 active Plan 1 members, 29.2% of the entire VRS active population, are past the window as a matter of law. Then give the 11,600–24,000 range. (FM-1 § 1.2, § 1.6.)
4. **Replace the single 6% veteran share with the four sourced bands**, and add the BLS 5.75% corroboration — it is the cheapest credibility the package can buy. (FM-1 § 1.4.)
5. **Keep the Cliff Graph's values; add an age panel.** The 3.23× is defensible at its profile and is independently reproduced here; the problem is that one profile reads as universal when the real range is 0.5×–3.5×. (FM-2 § 2.4.)
6. **Add the half-year-per-purchased-year Rule of 90 asymmetry.** It is the most important mechanical fact in the package and appears nowhere in the brief. (FM-4 § 4.1.)
7. **Soften "VRS publishes no actuarial-equivalent rate" to "VRS does not publish it."** The Plan Actuary develops it annually from the prior-year valuation; it is a requestable document. (FM-2 § 2.2.)
8. **Surface the A-1 interest-rate trade-off before the JLC picks a structure.** (FM-4 § 4.3.)
9. **Add A-3's administrative advantage:** every rate group already has a Board-adopted rate, so A-3 needs no new rate-setting. (FM-3.)
10. **State that the July 1, 2025 rates are good through at least June 30, 2029.** (FM-5.)

11. **Change one phrase in the Annex A rate-schedule authority.** Grade by age **and creditable service**, or by distance from unreduced eligibility — not by age alone. As originally described the guardrail removes about 15% of the exposure; redrawn it removes roughly **60%** — the class mean of what a *lawful uniform* rate can recover, leaving a residual of **$22M–$44M at 20% take-up** rather than zero (§ 4.8.1, red team F-1). **It remains the highest-leverage single edit in the package, but it is a mitigation and not a neutrality device**, and the accompanying § 2.2 ceiling has to be reframed with it. **And the 60% is itself conditional**: it assumes the ceiling means full cost to the Fund. On the statutory reading of "actuarial equivalent cost" the same redrawn authority recovers only about 22% and the residual is **$43M–$84M** against $57M–$111M for doing nothing — so the phrase change must be made *together with* a ceiling that says which cost it means. (FM-4 § 4.8, § 4.8.1, **§ 4.8.3**.)

12. **Report state, teacher and local exposure as three figures, never one.** The political-subdivision line is the largest of the three and arrives without a local opt-in. Brief the Commission on Local Government before filing. (FM-4 § 4.7.)

13. **Ask DPB for the Standards of Quality composite share** so the teacher line can be split between the Commonwealth and localities. It is a budget input, not a VRS one, and this annex deliberately does not assume it. (FM-4 § 4.7.)

---

## Sources added by this annex

All retrieved October 24, 2026.

| # | Claim | Source |
|---|---|---|
| C1 | Active members by plan at 6/30/2025 — Plan 1 110,474; Plan 2 67,333; Hybrid 200,253; total 378,060 | [VRS, *VRS 101 / Who We Serve*](https://www.varetire.org/media/shared/pdf/publications/intro-to-vrs-brochure.pdf), 2025 ed., p. 4 |
| C2 | Active members by employer group; vested / non-vested split; 864 participating employers | [VRS Annual Comprehensive Financial Report FY2025](https://www.varetire.org/media/shared/pdf/publications/2025-annual-report.pdf), Figures 2.3 and 2.9 |
| C3 | Plan 1 membership date must precede 7/1/2010; **Plan 2 remains open to VaLORS, SPORS and enhanced / alternate hazardous duty members hired after 12/31/2013**; Hybrid non-eligible members | same, Figure 2.10 |
| C4 | ANC rates by rate group, effective 7/1/2025 — RBA 2025-06-10; **"updated every four years following the quadrennial experience study"**; **"actuarial equivalent cost rates are developed by the Plan Actuary based on the assumptions and demographic data from the prior year valuations"** | [VRS Board of Trustees minutes, June 18, 2025](https://www.varetire.org/media/members/pdf/board/minutes/2025/board-of-trustees-minutes-06-18-25.pdf), pp. 5–6 |
| C5 | Rate-chart headings and footers: Hybrid page "Effective July 1, 2025 / Updated: July 1, 2026"; other three pages "Updated: July 1, 2025"; alternate hazardous duty option 10.01% | [VRS, *Purchase of Prior Service Cost Rates*](https://www.varetire.org/media/shared/pdf/publications/pps-rate-charts.pdf), pp. 1–4 |
| C6 | **No 2026 ANC rate action**; HB 139 "would not change VRS current procedures" | [VRS Board of Trustees minutes, February 5, 2026](https://www.varetire.org/media/members/pdf/board/minutes/2026/board-of-trustees-minutes-02-05-26.pdf); [April 23, 2026](https://www.varetire.org/media/members/pdf/board/minutes/2026/board-of-trustees-minutes-04-23-26.pdf) |
| C7 | **Next quadrennial assumption review is 2029**; VRS uses fixed-rate early-retirement reductions rather than true actuarial equivalence, providing "a subsidy that varies by age and service" | [VRS Board of Trustees minutes, June 17, 2026](https://www.varetire.org/media/members/pdf/board/minutes/2026/board-of-trustees-minutes-06-17-26.pdf) (B&A Committee report, Early Retirement Factors Study) |
| C8 | Board-adopted COLA assumptions 2.50% (Plan 1) and 2.25% (Plan 2 / Hybrid); 6.75% assumed return; payroll growth 3.0% (2.5% VaLORS); Total Normal Cost by group; Plan Actuary is Gabriel, Roeder, Smith & Company; experience study accepted April 16, 2025 | [VRS Annual Actuarial Valuation, June 30, 2025](https://employers.varetire.org/media/employers/pdf/financial-reporting/valuations/valuation-report-vrs.pdf), Executive Summary and Results Summary |
| C9 | Veteran share of U.S. state-and-local government workers derived as 5.75% | [BLS, *Employment Situation of Veterans*, Table 8](https://www.bls.gov/news.release/vet.t08.htm), August 2025 |
| C10 | Virginia veterans employed 357k; nonveterans employed 3,864k, 2025 annual averages | [BLS Table 6A](https://www.bls.gov/news.release/vet.t06a.htm); [Table 6B](https://www.bls.gov/news.release/vet.t06b.htm) |
| C11 | **2.3% of U.S. public school teachers are military veterans; 3.1% in the South region** | [NCES, *Digest of Education Statistics*, table 209.27](https://nces.ed.gov/programs/digest/d17/tables/dt17_209.27.asp) (2016) |
| C12 | Hybrid exclusions — SPORS, VaLORS, ORP, § 51.1-138 eligibility, and EMS / firefighter / law-enforcement officers in localities adopting the irrevocable resolution | [Va. Code § 51.1-169](https://law.lis.virginia.gov/vacode/title51.1/chapter1/section51.1-169/), subsec. A |
| C13 | Judges with an original term on or after July 1, 2026 are in VRS Plan 2 | 2026 Acts of Assembly, SB 950, as reported in VRS ACFR FY2025, legislative summary |

**Previously unverified, now verified:** Virginia's veteran population. BLS Table 6A, 2025 annual averages, reports a Virginia veteran civilian noninstitutional population of **646,000**, inside the 630,000–665,000 band Annex B § 4 had flagged as unverified and omitted. It remains not load-bearing for this proposal, but it can now be cited if asked.
