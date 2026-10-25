# Annex 2 Closure — Fiscal Open Items FM-1 through FM-5

**Companion to:** JLC Legislative Change Brief — Virginia's 24-Month Military-Service Purchase Price Cliff (Va. Code § 51.1-142.2)
**Closes:** Annex 2 open items FM-1, FM-2, FM-3, FM-4, FM-5
**Date:** October 24, 2026 · **Owner:** Fiscal & Impact Modeler · **Issue:** MOO-291
**Reproducible model:** [`models/fm_model.py`](models/fm_model.py) — run `python3 fm_model.py`

> **Labelling convention used throughout.** **OFFICIAL** = published by VRS, the Commonwealth, or a federal statistical agency. **DERIVED** = arithmetic on official inputs, formula shown. **ESTIMATE** = scenario assumption, not a prediction. No figure in this annex is a VRS actuarial certification; under § 30-19.1:7 the VRS Board files the official impact statement.

---

## Headline — read this before anything else

Three of the five items close with official sources. Two close as qualified negatives with the search recorded. But the work also produced **one finding that is material to the brief as currently drafted**:

> **The brief's cost headline — "under $2 million one-time" — is not sustainable and should not go to the JLC.** It was built on (i) state classified employees only and (ii) the price-discount channel only. Once the brief's own stated scope (all three plans, state + teacher + political-subdivision employers) and its own stated dominant cost driver (retirement-date acceleration) are both carried into the arithmetic, the modelled one-time present-value cost of recommendation A-3 is **on the order of $13 million to $182 million**, depending on the eligible-pool band and take-up.
>
> That is not a correction of a calculation error. The old arithmetic was internally consistent for what it covered. It covered roughly 2,600 people out of a pool this annex puts at 10,600–26,300, and it priced about 15%–30% of the cost per person. **See FM-4, § 4.4, and the independent cross-check against VRS's own HB 1867 fiscal impact statement at § 4.6, which supports the new magnitude and flags the old one as too low by roughly an order of magnitude.**

| Item | Status | One-line answer |
|---|---|---|
| **FM-1** | **Closed as a sourced range + a drafted VRS data request** | Official plan and employer-group denominators now in hand. The *veteran-held-purchasable-service* count does not exist publicly and only VRS can produce it. Reportable range: **10,600–26,300** past-window members. Plan 1 (110,474) requires **no estimate at all** — it is past the window as a matter of law. |
| **FM-2** | **Closed — no VRS factor table exists, but a better basis now does** | VRS publishes no actuarial-equivalent factor table. The 3.23× is **approximately right for the Cliff Graph's own illustrative profile** (modelled 2.8×–3.5× across the three plans) — but it sits near the **top** of a **0.5×–3.5×** range. Below about age 47 the member **overpays** at the ANC price. The graph should be reissued with an age dimension, not with different numbers at that one profile. |
| **FM-3** | **Closed — fully official** | Four rate groups, from the Board's own resolution. Includes a structural finding the brief does not yet carry: **there is no Hybrid hazardous-duty rate, because hazardous-duty members are statutorily excluded from Hybrid and enter Plan 2 instead — so Plan 2 is not a closed cohort.** |
| **FM-4** | **Closed as a modelled decomposition with take-up sensitivity** | Acceleration is **20%–49%** of the total cost on this basis, and that is a **floor**. A-1's cost turns almost entirely on the statutory interest rate — a drafting choice, not an actuarial one. |
| **FM-5** | **Closed — qualified negative, well sourced** | **No.** No new ANC rates took effect July 1, 2026. The rates are updated only on the quadrennial cycle, and VRS told its own committee on June 17, 2026 that the next assumption review is **2029**. The "Updated: July 1, 2026" stamp is a document refresh of one page. |

### And one finding that was not asked for but outranks most of what was

Pricing the Annex A guardrails as dials, as the scope decision requires, showed that **the age-graded rate schedule as currently described removes only about 15% of the exposure.** Grading on age recovers the benefit-amount excess but not the acceleration cost, which is driven by proximity to an eligibility threshold — age *and* service together. Graded instead on **distance from unreduced eligibility**, the same authority can remove anything up to 100%. That is a one-phrase drafting change and it is the highest-leverage edit available anywhere in this package. **FM-4 § 4.8.** **Adopted October 25, 2026 in Annex A v1.1, § 2.2** — see the status note at the end of § 4.8.

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
| Plan 1 | 3,966 | 9,027 |
| Plan 2 | 2,417 | 5,502 |
| Hybrid | 4,177 | 11,792 |
| **Total** | **10,561** | **26,321** |

> **What to say to a legislator:** "Roughly ten to twenty-six thousand members across the three plans, of whom over a hundred and ten thousand Plan 1 members are past the deadline as a matter of law. VRS can give you the exact count of those holding verified military service; nobody else can."
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

The break-even ages cluster tightly at **47–48 in all three plans**. Below that age the veteran **overpays** at the approximate-normal-cost price — the member subsidises the Fund. That finding survives in the brief v1.0 and should be kept; it is the strongest fiscal argument the proposal has.

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

**Recommended reissue (for MOO-288 to action):** keep the existing values at the illustrative profile; do **not** change them. Add a second panel plotting the AEC/ANC multiple against purchase age, with the 47–48 break-even line marked, and replace caution 1 with: *"the multiple is profile-specific and ranges from about 0.5× to about 3.5×; 3.23× describes a long-service member sitting just short of an eligibility threshold, which is the worst case, not the typical one."*

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
| Plan 1 | 3,966 – 9,027 | **$47,967** |
| Plan 2 | 2,417 – 5,502 | **$17,174** |
| Hybrid | 4,177 – 11,792 | **$6,779** |
| **Total** | **10,561 – 26,321** | |

| Scenario | Take-up | Purchasers | **One-time PV cost, A-3** | As % of covered payroll |
|---|---:|---|---|---|
| Brief v1.0 low | 5% | 528 – 1,316 | **$13.0M – $30.4M** | 0.049% – 0.113% |
| Low | 10% | 1,056 – 2,632 | **$26.0M – $60.7M** | 0.097% – 0.227% |
| Brief v1.0 high | 15% | 1,584 – 3,948 | **$39.0M – $91.1M** | 0.146% – 0.340% |
| Moderate | 20% | 2,112 – 5,264 | **$52.0M – $121.5M** | 0.194% – 0.454% |
| High | 30% | 3,168 – 7,896 | **$78.0M – $182.2M** | 0.292% – 0.681% |

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

The denominator is 6.7× larger than the one brief v1.0 used — but **the eligible pool grew by more than the denominator did**, so the payroll share rises as well. "Five cents per $100" is right at the very bottom of the grid (0.049%) and understates the top by about fourteen times (0.681%, or about 68 cents per $100). The one-pager's hedge — that the statewide figure is larger "but it stays the same tiny share of payroll" — is therefore **not correct**, and should be replaced with a figure from this column.

**Against the brief's "under $2 million one-time."** Even the gentlest cell in this grid — the brief's own 5% take-up, on the low pool — is **$13 million**, more than six times the brief's ceiling. The difference is entirely accounted for by the two things the brief said it would do but did not carry into the arithmetic: extending to all plans and all three employer groups (pool 2,600 → 10,561–26,321) and pricing acceleration (about $3,750 per member → $6,779–$47,967).

This is a present-value liability, not a cash appropriation. It would be absorbed in the employer contribution rate and amortised under the VRS Funding Policy, as the brief correctly says. But the number the money committees will see is the present value, and **$2 million is not that number.**

### 4.5 The one input that would most change this

**Historical take-up.** The grid spans a factor of 14 from the gentlest to the harshest cell, and roughly 6 of that 14 is take-up alone. Item 5 of the § 1.7 data request would collapse most of it. Prior-service purchase take-up is generally low because members must fund it from pay; if VRS's actual § 51.1-142.2 experience is in the low single digits, the honest headline is the bottom row and not the top.

### 4.6 Independent cross-check — and why it validates this and not the old figure

VRS's own § 30-19.1:7 fiscal impact statement on **HB 1867 (2023)** — which would have granted active-duty military service to teachers **free** — found **$10,000 to $60,000 of unfunded liability per participating member.**

| | Modelled A-3 net PV per member | Against the HB 1867 band |
|---|---:|---|
| Plan 1 | $47,967 | **inside** |
| Plan 2 | $17,174 | **inside** |
| Hybrid | $6,779 | below — as a *priced* purchase should be |
| **Brief v1.0** | **~$3,750** | **an order of magnitude below the floor** |

A purchase at which the member still pays must cost the Fund **less** than a free grant of the same service. These figures do; two of three sit inside VRS's own band and the third sits just below it, which is exactly the expected pattern. The brief v1.0 per-member figure sat roughly a factor of three below even the floor of a band VRS produced for a **free** benefit. That was the signal, available in the brief's own Annex 3 source list at S8, that the arithmetic was too low.

### 4.7 Who bears it — state, teacher and local exposure reported separately

Required by the JLCVSO scope decision of October 24, 2026 (all VRS members, no local opt-in). Local exposure flows through political-subdivision employer rates under § 51.1-145 and **never touches the general fund**, and the Commission on Local Government receives the § 30-19.1:7 statement — so the figures must not be presented as one number.

Pool-weighted blended A-3 net present value per purchaser: **$24,627** (DERIVED).

| Who bears the employer-rate consequence | Eligible pool | PV cost at 20% take-up |
|---|---|---|
| **State agencies** (general fund + nongeneral fund) — VRS State Employees, SPORS, VaLORS, JRS | 4,113 – 8,099 | **$20.3M – $39.9M** |
| **Teachers** — school divisions, shared with the Commonwealth through the Standards of Quality | 2,699 – 6,768 | **$13.3M – $33.3M** |
| **Political subdivisions** — § 51.1-145 employer rates, no general fund | 4,753 – 9,169 | **$23.4M – $45.2M** |
| **Total** | 11,565 – 24,036 | **$57.0M – $118.4M** |

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

**This is the dial that bites.** At 50% recovery it halves the exposure; at 100% the bill is actuarially neutral by construction and the fiscal note is zero. It is the single most powerful cost control available and the one to offer the money committees first.

> **Recommendation to Legislative Services.** Express the Board's rate-schedule authority as varying by the member's **age and creditable service**, or by the member's **distance from unreduced retirement eligibility** — *not* by age alone. One phrase, and it is the difference between a guardrail that removes 15% of the exposure and one that can remove all of it.

> **Status: adopted, October 25, 2026 — Annex A v1.1, § 2.2.** Counsel widened the authority to age **and** creditable service (with distance from unreduced eligibility named as the equivalent alternative), added the amount of service purchased as a third factor, and attached publication, uniformity-within-classification, and actuarial-equivalent-cost-ceiling constraints plus an express sentence confining the schedule to subdivision B 2. The counsel analysis is at Annex A § 2.5. **Guardrail A as modelled above is therefore superseded by Guardrail A′ as the description of what Annex A actually grants** — the 15% figure is retained here as the record of why the change was made, not as a current description of the draft. Two confirmations remain open at Annex A Q3a (how closely a published *class* rate tracks true AEC at the 100% setting) and Q14 (age/service as rate factors).

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

1. **Replace the cost headline.** "Under $2 million one-time; under $100,000 per year ongoing" cannot survive contact with the money committees. Replace with the FM-4 § 4.4 grid, a plain statement that the present value is in the tens of millions on central assumptions, and the § 4.6 cross-check showing the figure is *conservative relative to VRS's own HB 1867 band*. The $0 general fund ask is unaffected and remains correct — this is an employer-contribution-rate liability amortised under the VRS Funding Policy, not an appropriation.
2. **Correct "Plan 2 is a closed cohort."** It is open for SPORS, VaLORS, political-subdivision hazardous duty, and — from July 1, 2026 — newly appointed judges. (FM-1 § 1.3, FM-3.)
3. **Lead the population discussion with the one number that needs no estimate:** 110,474 active Plan 1 members, 29.2% of the entire VRS active population, are past the window as a matter of law. Then give the 10,600–26,300 range. (FM-1 § 1.2, § 1.6.)
4. **Replace the single 6% veteran share with the four sourced bands**, and add the BLS 5.75% corroboration — it is the cheapest credibility the package can buy. (FM-1 § 1.4.)
5. **Keep the Cliff Graph's values; add an age panel.** The 3.23× is defensible at its profile and is independently reproduced here; the problem is that one profile reads as universal when the real range is 0.5×–3.5×. (FM-2 § 2.4.)
6. **Add the half-year-per-purchased-year Rule of 90 asymmetry.** It is the most important mechanical fact in the package and appears nowhere in the brief. (FM-4 § 4.1.)
7. **Soften "VRS publishes no actuarial-equivalent rate" to "VRS does not publish it."** The Plan Actuary develops it annually from the prior-year valuation; it is a requestable document. (FM-2 § 2.2.)
8. **Surface the A-1 interest-rate trade-off before the JLC picks a structure.** (FM-4 § 4.3.)
9. **Add A-3's administrative advantage:** every rate group already has a Board-adopted rate, so A-3 needs no new rate-setting. (FM-3.)
10. **State that the July 1, 2025 rates are good through at least June 30, 2029.** (FM-5.)

11. **Change one phrase in the Annex A rate-schedule authority.** Grade by age **and creditable service**, or by distance from unreduced eligibility — not by age alone. As described the guardrail removes about 15% of the exposure; redrawn it can remove all of it. **This is the highest-leverage single edit in the package.** (FM-4 § 4.8.)

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
