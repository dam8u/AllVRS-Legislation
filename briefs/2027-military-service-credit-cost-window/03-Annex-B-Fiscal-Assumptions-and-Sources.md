# Annex B — Fiscal Assumption Register, Claim/Evidence Table and Source Appendix

**Companion to:** JLC Legislative Change Brief — Virginia's 24-Month Military-Service Purchase Price Cliff (Va. Code § 51.1-142.2)
**Date:** October 25, 2026 | **Version:** **v2.0 — reconciled against Annex 2 Closure** | **Owner:** Fiscal & Impact Modeler
**Supersedes:** v1.1 in full. **Retrieval date for all sources:** October 24, 2026 | **Issue:** MOO-295

---

## 0. What this annex is, and the rule that keeps it from diverging from Annex 2 Closure

v1.1 of this annex carried its own population figures and its own total-cost arithmetic. Both were built on the state classified workforce alone and on the price-discount channel alone, and both were superseded by [Annex 2 Closure (04)](04-Annex-2-Closure-FM1-FM5.md). A package with two fiscal annexes disagreeing about the headline cost was an invitation to quote the wrong one.

**v2.0 removes that possibility rather than managing it.** This annex and Annex 2 Closure now divide the work by *kind of number*, under one rule:

> **OFFICIAL published values live here, in the fact register at § 1, cited once with a pinpoint.**
> **Every DERIVED or ESTIMATED value lives in Annex 2 Closure only.** This annex carries the pointer, the owner and the sensitivity for each — never the figure.

Two documents can only contradict each other about something they both compute. After this edit, they compute nothing in common. Annex A, § 9 already describes the package this way — "Assumptions in Annex B; re-scoped figures in Annex 2 Closure" — so this is the division of labour the rest of the package was already assuming.

| | This annex (03) | Annex 2 Closure (04) |
|---|---|---|
| Verified primary-source facts, with pinpoints | **Yes — § 1, the single index for the package** | Cites; does not re-index |
| Assumption register: owner, sensitivity, what would resolve it | **Yes — § 2** | States assumptions inline at point of use |
| Cost methodology — the governing identity and the AEC formula | **Yes — § 3** | Applies it |
| Population counts, eligible pool, veteran shares | Pointer only → FM-1 | **Yes** |
| Per-member and total cost, take-up grid, exposure split, guardrail dials | Pointer only → FM-2, FM-4 | **Yes** |
| What a veteran pays today at published rates (member price) | **Yes — § 4.** No counterpart in 04 | — |
| Unverified / open claims and the VRS data request | **Index — § 5** | Drafts the request at FM-1 § 1.7 |
| Primary source list for the whole package | **Yes — § 6** | Lists its own additions |
| Adversarial challenge to any of the above | — | — (see [Red Team Review (05)](05-Red-Team-Review.md), which tests both) |

**The one deliberate overlap, and why it is safe.** § 4 multiplies a published rate by a published salary. It is a *member price*, not a cost to the Fund, and Annex 2 Closure does not compute it. Everything else in § 4 is a pointer.

**No total-cost figure appears anywhere in this annex.** If you are looking for the cost of the bill it is [Annex 2 Closure, FM-4 § 4.4](04-Annex-2-Closure-FM1-FM5.md). The modelled one-time present value of recommendation A-3 is on the order of **$13M–$182M** depending on eligible pool and take-up.

**State the general-fund position narrowly.** **The bill requests no appropriation** — the cost is absorbed in future employer contribution rates under § 51.1-145 and amortised under the VRS Funding Policy. That is true and defensible. "General fund cost: $0" is **not**, because the state-agency and Standards-of-Quality shares of those rates do reach the general fund in later biennia; see FM-4 § 4.7 and **Red Team finding F-2**, which should be read before this claim is repeated anywhere.

**Do not quote "under $2 million one-time" or "under $100,000 per year."** Those figures originated in v1.1 § 3.4 of this annex. They are withdrawn by name in brief v1.2, in the one-page leave-behind, and here. § 7.4 records exactly what was wrong with them, so that the retraction can be defended rather than merely stated.

> **Status of every number in this package.** All *legal* claims are verified against primary sources. All *published rate* and *published workforce* claims are verified against primary sources. The actuarial-equivalent-cost estimates and all total-cost figures are **JLCVSO analyst estimates**, not VRS figures, and are shown with their formulas so VRS can replace them. Under § 30-19.1:7 the VRS Board files the official financial and policy impact statement; nothing in this package is an actuarial certification. See Annex A, § 7, Q1–Q5 and Q3a.

---

## 1. Source facts (verified)

Tier 1 = primary legal text. Tier 2 = VRS publication. Tier 3 = other Virginia or federal government publication.

### 1.1 Statutory and legal facts

| ID | Fact | Value | Source | Pinpoint | Tier | Confidence |
|---|---|---|---|---|---|---|
| F-01 | Members may purchase up to 4 years of prior active duty military service credit | 4 years | Code of Virginia § 51.1-142.2 | subdiv. B 2 | 1 | High |
| F-02 | Military purchase allowance is **in addition to** the separate 4-year cap for other service | 2 separate caps | § 51.1-142.2 | subdiv. B 1 (last sentence), B 2 (first words) | 1 | High |
| F-03 | Qualifying active duty requires at least 180 consecutive days; non-dishonorable discharge | 180 days | § 51.1-142.2 | subdiv. B 2; final para. of subsec. B | 1 | High |
| F-04 | Price is approximate normal cost if purchased or contracted within the first 24 months of active service following first date of hire; actuarial equivalent cost thereafter | 24 months | § 51.1-142.2 | subdiv. B 3, 2nd para. | 1 | High |
| F-05 | Purchased prior service under § 51.1-142.2 **is** "creditable service" | — | § 51.1-124.3 | definition of "Creditable service" | 1 | High |
| F-06 | Rule of 90: age + years of creditable service = 90 permits retirement with the allowance computed under § 51.1-155 A 1 (unreduced) | 90 | § 51.1-153 | subdiv. B 3 | 1 | High |
| F-07 | Normal retirement date is Social Security retirement age for post-7/1/2010 members and those lacking 60 months of creditable service as of 1/1/2013 | SSA NRA | § 51.1-124.3 | definition of "Normal retirement date" | 1 | High |
| F-08 | Hybrid plan DB multiplier | 1.0% of AFC per year | § 51.1-169 | subdiv. D 1 | 1 | High |
| F-09 | Everyone not already a VRS member who is first hired or rehired into a covered position on or after January 1, 2014 is in the Hybrid plan — **subject to the exclusions at F-41** | 1/1/2014 | § 51.1-169 | subsec. A, 3rd para. | 1 | High |
| F-10 | Hybrid members are deemed "a person who becomes a member on or after July 1, 2010" | — | § 51.1-169 | subdiv. D 3 | 1 | High |
| F-11 | Hybrid members may not retire for disability under the DB component | — | § 51.1-169 | subdiv. D 2 | 1 | High |
| F-12 | Plan 1 / Plan 2 benefit multipliers | 1.70% / 1.65%–1.70% | § 51.1-155 | subdiv. A 1 | 1 | High |
| F-13 | COLA: first 2% of CPI-U plus half the next 2%, max 3% (post-2010 members and Hybrid); 3% plus half of next 4%, max 5% for Plan 1 cohort | 3% / 5% caps | § 51.1-166 | subsec. B | 1 | High |
| F-14 | HIC: requires 15 years of total creditable service; $4.25/month per year of creditable service effective July 1, 2024 | 15 yrs; $4.25 | § 51.1-1400 | subsec. A | 1 | High |
| F-15 | VRS must actuarially determine HIC funding and reflect it in the employer contribution rate | — | § 51.1-1400 | subsec. D | 1 | High |
| F-16 | PLOP requires creditable service **performed** after first unreduced eligibility **and** being "in service" 1/2/3 full years after 1/1/2001 | — | § 51.1-165.01 | subsec. B | 1 | High |
| F-17 | VRS Board must file a financial and policy impact statement on VRS bills with both clerks, the Commission on Local Government, House Appropriations, and Senate Finance & Appropriations | — | § 30-19.1:7 | whole section | 1 | High |
| F-18 | Veterans receive a hiring preference for Commonwealth employment | — | § 2.2-2903 | subsecs. A, B | 1 | High |
| F-36 | 2026 Acts of Assembly c. 563 (HB 139) amended § 51.1-142.2 but concerned unpaid educational leave for employee association officers — **not** military service | — | Virginia LIS, 2026 Reg. Sess., HB 139 (CHAP0563) | chapter text | 1 | High |
| F-41 | Hybrid exclusions: anyone participating in or eligible for Chapter 2 (SPORS), Chapter 2.1 (VaLORS), the optional retirement plans, or eligible for § 51.1-138 benefits; and any EMS / firefighter / law-enforcement officer whose political subdivision adopted the irrevocable resolution under § 51.1-153 B 4 and § 51.1-155 A 3 | — | § 51.1-169 | subsec. A | 1 | High |
| F-42 | Judges appointed or elected to an original term on or after July 1, 2026 are in VRS **Plan 2** | 7/1/2026 | 2026 Acts of Assembly, SB 950 | as reported in VRS ACFR FY2025 legislative summary | 1 | Medium — *see § 5, U-07* |
| F-53 | Vesting is five years of service credit | 5 yrs | § 51.1-153; VRS ACFR FY2025 | Fig. 2.10 | 1 | High |

**Checked and found not to exist:** no Virginia Code section defines "earned service" or "benefit-calculation service"; no section of Title 51.1 other than § 51.1-142.2 B 3 and E contains the 24-month cost window; no conforming cross-reference to the window exists elsewhere in Title 51.1.

### 1.2 VRS published rates and administrative facts

| ID | Fact | Value | Source | Pinpoint | Tier | Confidence |
|---|---|---|---|---|---|---|
| F-19 | Approximate normal cost rate, **Hybrid**, state/teacher/local non-hazardous | **6.68% of salary** | VRS, *Purchase of Prior Service Cost Rates* | p. 1; rates eff. 7/1/2025 | 2 | High |
| F-20 | Approximate normal cost rate, **Plan 1**, state/teacher/local non-hazardous | **12.50% of salary** | same | p. 2 | 2 | High |
| F-21 | Approximate normal cost rate, **Plan 2**, state/teacher/local non-hazardous | **10.74% of salary** | same | p. 3 | 2 | High |
| F-22 | Hazardous duty normal cost rates, non-judicial | Plan 1 **23.78%**; Plan 2 **19.15%**; **no Hybrid rate exists** (see F-41) | same | pp. 2–3 | 2 | High |
| F-43 | **Hazardous duty alternate option** rate — published as a stand-alone rate with no plan column, available only to electing localities | **10.01%** | same | p. 4 | 2 | High |
| F-44 | **Judicial** ANC rates | Plan 1 31.97%; Plan 2 **29.67%**; Hybrid 19.21% | same; VRS Board, Request for Board Action **2025-06-10** | rate charts; minutes of 6/18/2025 | 2 | High |
| F-23 | Rate applies to creditable compensation or AFC at time of purchase, **whichever is higher** | — | *Purchase of Prior Service Cost Rates* | footnote * on each page | 2 | High |
| F-24 | VRS assumed rate of return used for refunded-service interest | 6.75% | same | refunded service rows, all pages | 2 | High |
| F-25 | "The approximate normal cost rate is the average cost of one year of VRS service credit." | verbatim | VRS Employer Manual, *Purchase of Prior Service Credit* (July 2026) | p. 11 | 2 | High |
| F-26 | "Actuarial equivalent represents the amount of money needed in today's dollars to pay for the total value of the increase in the employee's future retirement benefit **or earlier retirement eligibility date** resulting from purchasing prior service." | verbatim | same | p. 11 | 2 | High |
| F-27 | Purchase payment agreements run 6–12 months and "[t]he duration of an agreement may not extend beyond the two-year cost window." | verbatim | same | p. 12 | 2 | High |
| F-28 | Pre-tax purchase of prior service "has no effect on an employee's creditable compensation for retirement or group life insurance purposes." | verbatim | same | p. 12 | 2 | High |
| F-29 | Reserve/National Guard service may be purchased even if it qualifies the member for a military pension; DD-214 or orders required | — | same | pp. 5–6 | 2 | High |
| F-45 | "The approximate normal cost rates are **updated every four years** following the Board's acceptance of the new assumptions associated with the quadrennial experience study." | verbatim | VRS Board of Trustees minutes, June 18, 2025 | pp. 5–6 | 2 | High |
| F-46 | "**The actuarial equivalent cost rates are developed by the Plan Actuary** based on the assumptions and demographic data from the prior year valuations." | verbatim | same | pp. 5–6 | 2 | High |
| F-47 | The next quadrennial assumption review is **2029** | 2029 | VRS Board of Trustees minutes, June 17, 2026 (B&A Committee report) | Early Retirement Factors Study item | 2 | High |
| F-48 | VRS uses **fixed-rate** early-retirement reductions rather than true actuarial equivalence, which "does provide a subsidy that varies by age and service" | verbatim | same | same | 2 | High |
| F-49 | Rate-chart stamps: Hybrid page "Effective July 1, 2025 / **Updated: July 1, 2026**"; Plan 1, Plan 2 and alternate hazardous duty pages "Updated: **July 1, 2025**". PDF metadata creation/modification July 1, 2026. **No rate moved.** | — | *Purchase of Prior Service Cost Rates* | pp. 1–4 and file metadata | 2 | High |
| F-50 | **No 2026 Board or B&A action** approves, proposes or revises approximate normal cost rates. HB 139 "would not change VRS current procedures" | — | VRS Board minutes, Feb. 5, 2026 and Apr. 23, 2026 | HB 139 item | 2 | High |
| F-52 | VRS Plan Actuary is **Gabriel, Roeder, Smith & Company**; the quadrennial experience study for the period ending June 30, 2024 was accepted **April 16, 2025** | — | VRS Annual Actuarial Valuation, June 30, 2025 | Executive Summary | 2 | High |

### 1.3 VRS membership, payroll and Board-adopted assumptions

These are the official denominators. They replaced the DHRM classified-workforce population that v1.1 of this annex used.

| ID | Fact | Value | Source | Pinpoint | Tier | Confidence |
|---|---|---|---|---|---|---|
| F-37 | Active members by plan at 6/30/2025 | Plan 1 **110,474**; Plan 2 **67,333**; Hybrid **200,253**; total **378,060** | VRS, *VRS 101 / Who We Serve*, 2025 ed. | p. 4 | 2 | High |
| F-38 | Active members by employer group at 6/30/2025, with vested / non-vested split | State 83,148 (52,120 / 31,028); Teachers 160,800 (110,074 / 50,726); Political Subdivisions 124,264 (70,340 / 53,924); SPORS 1,894 (1,524 / 370); VaLORS 7,484 (3,795 / 3,689); JRS 470 (378 / 92). Total **378,060** (238,231 / 139,829) | VRS ACFR FY2025 | Figs. 2.3, 2.9 | 2 | High |
| F-39 | A **Plan 1** membership date must precede July 1, 2010 | 7/1/2010 | VRS ACFR FY2025 | Fig. 2.10 | 2 | High |
| F-40 | "Members covered under VaLORS, SPORS or VRS with enhanced hazardous duty benefits or the hazardous duty alternate option, and whose membership dates are on or after July 1, 2010, are in Plan 2 **even if their membership dates are after December 31, 2013**." | verbatim | same | Fig. 2.10 | 2 | High |
| F-51 | **Annual Covered Payroll** by group at 6/30/2025 | Teachers $11,732,114,000; Pol. Subdivisions $8,041,026,000; State $6,275,603,000; VaLORS $432,703,000; SPORS $182,726,000; JRS $98,645,000. **Total $26,762,817,000** | VRS Annual Actuarial Valuation, June 30, 2025 | Results Summary, each group | 2 | High |
| F-54 | **Total Normal Cost** by group | State 8.73%; Teachers 9.22%; SPORS 18.37%; VaLORS 14.30%; Judicial 27.11% | same | Results Summary — Employer Contribution Rate Detail | 2 | High |
| F-55 | **Board-adopted** long-term assumptions | Investment return **6.75%**; COLA **2.50% Plan 1**, **2.25% Plan 2 / Hybrid**; payroll growth **3.0%** (2.5% VaLORS) | same | Executive Summary | 2 | High |
| F-56 | **HB 1867 (2023)** — free grant of up to 4 years of prior active-duty military service to teachers. VRS: "each person who purchases up to 48 months of active military service would create an unfunded liability that **ranges from $10,000 - $60,000** depending on the age and service and compensation of the member" | verbatim | VRS, *2023 Fiscal Impact Statement*, HB 1867 | Item 6; dated 1/16/2023, doc. HB1867.DOC/VRS | 2 | High |
| F-60 | **VRS's own worked total for HB 1867**: "if 1,500 members (1% of the Teacher population) had this type of service, and the average cost was **$35,000**, the total cost to the fund could be **$50 million**." Current unfunded liability of the Teacher Plan: **$11.8 billion** | verbatim | same | Items 6 and 9 | 2 | High |
| F-61 | VRS cost to implement HB 1867: **approximately $78,000 for FY 2023** (NGF, Item 498 — handbooks, manuals, e-courses, web materials, employer and member communication). **Employer cost to implement: "None."** GF budget impact: **"No immediate impact."** | — | same | Items 6, 7, 8 | 2 | High |
| F-62 | **VRS cannot identify who holds unexercised military service.** "While VRS is not able to determine the number of current teachers or future teachers who would have prior active military service to purchase… it is unknown how many teachers have prior military service available to be granted." | verbatim | same | Item 6 | 2 | High |
| F-63 | VRS, on the value of the credit: "Prior service credit counts toward **vesting, eligibility for retirement and eligibility for the health insurance credit**, if offered by the employer." And: "Granting of service in a pooled plan will effectively **spread the cost of each period of granted service over all of the employers** in the Teacher plan." | verbatim | same | Items 12 and 6 | 2 | High |

### 1.4 Virginia and federal workforce facts

| ID | Fact | Value | Source | Pinpoint | Tier | Confidence |
|---|---|---|---|---|---|---|
| F-30 | Total classified state employees | **56,917** | DHRM presentation to Senate Finance & Appropriations Committee, 1/21/2025 | slide 6; data as of 6/30/2024 | 3 | High |
| F-31 | Share of classified state workforce **self-identifying** as veterans | **6%** | same | slide 8 | 3 | High |
| F-32 | Classified workforce average age / average years of service / average age of new hires | 46.7 / 10.3 / **37.7** | same | slide 8 | 3 | High |
| F-33 | FY24 recruitments; share that were new hires/rehires; turnover rate | 16,088; 64.0%; 14.4% | same | slide 10 | 3 | High |
| F-34 | **Mean** / median classified salary, all pay areas | **$69,865** / $61,305 | same | slide 14; as of 6/30/2024 | 3 | High |
| F-35 | Commonwealth statewide average salary increase, 2001–2023 | 2.9% | same | slide 16 | 3 | Medium |
| F-57 | Veterans and nonveterans employed in **state and local government**, U.S. | 7,893k employed veterans, 12.9% in S&L govt; 153,213k employed nonveterans, 10.9% in S&L govt | BLS, *Employment Situation of Veterans*, Table 8 | August 2025 | 3 | High |
| F-58 | Virginia veterans employed 357k; nonveterans employed 3,864k; Virginia **veteran civilian noninstitutional population 646,000** | 2025 annual averages | BLS, *Employment Situation of Veterans*, Tables 6A and 6B | 2025 annual averages | 3 | High |
| F-59 | **2.3%** of U.S. public school teachers are military veterans; **3.1%** in the South region | 2.3% / 3.1% | NCES, *Digest of Education Statistics*, table 209.27 | 2016 data | 3 | Medium — age of data |

> **The role of the DHRM block (F-30 → F-35) changed in v2.0 and must not be misread.**
> These remain verified Tier 3 facts, and two of them are still load-bearing. What changed is what they are *for*.
>
> - **F-30 and F-31 are no longer the population basis.** v1.1 built the eligible pool from 56,917 × 6%. The bill's scope is all 378,060 VRS active members (F-37, F-38), 6.6× larger. The official denominators are F-37 / F-38 and the sourced veteran-share bands are at FM-1 § 1.4. **F-31's 6% must not be extended to teachers** — the published teacher share is 2.3% (F-59).
> - **F-31 is a self-identification field and is therefore a floor, not a measurement.** It is also, usefully, independent corroboration: FM-1 § 1.4 derives 5.75% from F-57 by a wholly unrelated instrument and lands within a quarter of a percentage point. That agreement is cheap credibility and is worth stating to the money committees.
> - **F-34 is still the salary basis of the live cost model** (FM-4 § 4.4) and of § 4 below. § 7.1 of this annex now reconciles it against F-51 and finds it sound to within 0.5%.
> - **F-32, F-33 and F-35** remain the basis of A-04 and of the retired A-09 / A-14 (§ 2.3), and are state-classified context only.

---

## 2. Assumption register

Every entry: the value, its basis, who owns resolving it, and how much it moves the answer. Figures that this register *governs* but does not *state* carry a pointer to where they live.

### 2.1 Actuarial assumptions — reconciled against the June 30, 2025 valuation

| ID | Variable | Value used | Basis | Sensitivity | Owner |
|---|---|---|---|---|---|
| A-01 | Discount rate / assumed return | **6.75%** | **OFFICIAL — F-55**, F-24 | ±0.25% moves AEC roughly ∓4% at a 20-year horizon | VRS actuary |
| A-02 | Long-run COLA, Plan 2 and Hybrid | **2.25%** | **OFFICIAL — F-55.** Consistent with the F-13 cap structure at ~2.5% CPI-U | 1.5%–3.0% | VRS actuary |
| A-03 | Long-run COLA, Plan 1 cohort | **2.50%** | **OFFICIAL — F-55.** **Corrected in v2.0:** v1.1 used an analyst figure of 3.0% reasoned from the F-13 5% cap structure. The Board-adopted assumption is 2.50%. See § 7.2 | 2.0%–3.0% | VRS actuary |
| A-04 | Salary / payroll growth | **3.0%** | **OFFICIAL — F-55** (2.5% VaLORS). Corroborated by F-35 (2.9% historical) | 2.5%–4.0% | VRS actuary |
| A-05 | Retirement age, Plan 2 and Hybrid | Modelled from the member's own unreduced-eligibility date | F-07 (SSA NRA); § 51.1-153 B 3 | Earlier eligibility **raises** cost; this is the acceleration channel, priced at FM-4 § 4.2 | VRS actuary |
| A-06 | Retirement age, Plan 1 cohort | Modelled from the member's own unreduced-eligibility date | F-07; § 51.1-153 B 1 | as above | VRS actuary |
| A-07 | Annuity basis | Level-COLA **annuity-certain to age 87** | **ESTIMATE — not a VRS mortality table.** Reconciles to within ~3% of the v1.1 factors it replaces; see § 7.3 | Terminal age 84 / 87 / 90 moves the AEC/ANC **multiple** by roughly −10% / +9%; the multiple is far more stable than the dollar level (§ 3.4) | VRS actuary |
| A-16 | Combined member + employer normal cost, used to price recommendation A-1 | **OFFICIAL — F-54**, State Employees 8.73% | Applied to early-career pay and carried forward at a statutory interest rate, per A-1 as described in Annex A, § 6 | **A-1's whole character turns on that statutory interest rate, which is a drafting choice rather than an actuarial one.** At 4% A-1 is cheaper to the veteran than A-3; at 6.75% it is nearly double, and for both Hybrid profiles it over-recovers — the price exceeds the entire modelled value of the credit | Legislative Services; FM-4 § 4.3 |

> **A-05 and A-06 changed in substance, not merely in value.** v1.1 used flat retirement ages of 67 and 65. The live model derives each profile's unreduced-eligibility date and then moves it, because that movement *is* the dominant cost channel. A flat retirement age cannot price acceleration at all, which is the larger half of why v1.1's total was too low.

### 2.2 Population, take-up and allocation assumptions

These govern the cost figures. **The figures themselves are in Annex 2 Closure.** They are registered here so that every judgment in the model can be found in one place.

| ID | Variable | Value / band | Basis | Sensitivity | Owner | Figure lives at |
|---|---|---|---|---|---|---|
| A-17 | Members past the 24-month window, **Plan 1** | **All 110,474** | **Not an estimate.** F-39 + F-04: a Plan 1 membership date precedes 7/1/2010, so the window closed as a matter of law. A floor, not a point estimate, because the window runs on active service | None. This is the most defensible population statement in the package | — | FM-1 § 1.2 |
| A-18 | Share of **non-vested** members still inside the window | **40% – 60%** | ESTIMATE. Low = service spread uniformly over years 0–5; high = front-loaded, which is what withdrawal decrements actually produce | Moves the past-window total between 77.8% and 85.2% of actives | JLCVSO | FM-1 § 1.5 |
| A-19 | Veteran share, by employer group | State 6.0–9.9%; Teachers 2.3–5.4%; Pol. Subdivisions 5.7–9.9%; SPORS/VaLORS 9.9–25.0%; JRS 2.3–9.9% | Lows OFFICIAL (F-31, F-59) or derived from F-57; highs apply the Virginia uplift derived from F-58. **SPORS/VaLORS is the weakest band in the package** | Drives most of the ~2.5× width of the eligible pool | VRS / JLCVSO | FM-1 § 1.4 |
| A-20 | Share holding ≥1 year of qualifying active duty (the F-03 180-day test) | **90%** | ESTIMATE. Judgment; most veterans meet a 180-consecutive-day test | 80%–95%, roughly ±6% on the pool | JLCVSO | FM-1 § 1.6 |
| A-21 | Allocation of the eligible pool across plans | Effective rate applied **uniformly** across plans | ESTIMATE. Over-weights Hybrid and under-weights Plan 1, because veterans enter public service mid-career — so it is **conservative**, Plan 1 being the costliest plan per purchaser | Directional; correcting it raises the total | VRS (data request item 1) | FM-1 § 1.6 |
| A-22 | **Take-up over 5 years among eligible members** | **5% – 30%** | ESTIMATE. Prior-service purchase take-up is generally low because members fund it from pay. **The dominant uncertainty in the total** — roughly a factor of 6 of the grid's factor-of-14 span | Replace with VRS administrative data: **data request item 5**. If actual § 51.1-142.2 experience is in the low single digits, the honest headline is the bottom row of the grid | VRS / JLCVSO | FM-4 § 4.4, § 4.5 |
| A-23 | Average years purchased per purchasing member | **2.5 of 4** | ESTIMATE. Judgment | 1.5–4.0; roughly linear in the total | JLCVSO | FM-4 § 4.4 |
| A-24 | Salary basis for the statewide per-purchaser figure | **$69,865** (F-34) | Inherited from v1.1. **Validated in v2.0:** the pool-weighted average of official covered payroll per active member (F-51 ÷ F-38) is $70,120–$70,229, within **0.5%**. See § 7.1 | Immaterial statewide. Previously an unexamined proxy; now a checked one | — | FM-4 § 4.4 |
| A-25 | Blended per-purchaser PV applied **uniformly** across employer groups for the state / teacher / local split | Pool-weighted blend | ESTIMATE. Plan mix by employer group is not published. **Least reliable for SPORS and VaLORS**, where both benefit value and member price are materially higher and the net direction is genuinely unclear | Do not read the SPORS / VaLORS net off that table. § 7.1 states this in dollars | VRS (data request item 1) | FM-4 § 4.7 |
| A-26 | Standards of Quality composite share, to split the teacher line between the Commonwealth and localities | **Not assumed** | Deliberately unresolved. A budget input, not a VRS one | The teacher bucket is reported unsplit rather than guessed | **DPB** | FM-4 § 4.7 |
| A-27 | Amortisation of the one-time liability | **Not modelled as a schedule** | VRS applies its own amortisation layers under § 51.1-145 and the VRS Funding Policy. v1.1's 5-year catch-up was presentation convenience and is withdrawn | Presentational only; does not change the present value | VRS actuary | — |
| A-28 | **Guardrail dial setting** — share of the above-break-even excess recovered from the member under the Board's graded schedule | **Not assumed; reported as a dial from 0% to 100%** | Annex A, § 2.2 (v1.1) grants the authority graded on **age and creditable service**, equivalently distance from unreduced eligibility. At 100% recovery the bill is actuarially neutral by construction and the fiscal note is zero | **The most powerful cost control in the package.** Graded on age alone the dial removed only ~15% of the exposure; graded as now drafted it can remove all of it | JLCVSO policy choice (Annex A, Q12 — the dial, not the phrase) | FM-4 § 4.8 |

### 2.3 Retired assumptions — the v1.1 register, and what replaced each entry

Kept visible deliberately. These IDs appear in brief v1.0 / v1.1 and in correspondence, and a reader who meets one needs to be able to trace it.

| v1.1 ID | What it was | Status | Replaced by |
|---|---|---|---|
| A-08 | Veterans in classified workforce ≈ 3,400 (F-30 × F-31) | **Retired — wrong scope.** Covered state classified employees only | A-19 → FM-1 § 1.4, § 1.6 |
| A-09 | Share of veterans past the 24-month window = 85%, inferred from F-32 | **Retired — superseded by a better method.** The official vested / non-vested split does the same work with far less inference, and Plan 1 needs no inference at all | A-17, A-18 → FM-1 § 1.2, § 1.5 |
| A-10 | Share meeting the 180-day test = 90% | **Carried forward unchanged** | A-20 |
| A-11 | Take-up 5%–15% | **Widened to 5%–30%**, with v1.1's original band marked on the grid | A-22 |
| A-12 | Average years purchased = 2.5 of 4 | **Carried forward unchanged** | A-23 |
| A-13 | Average AEC-minus-ANC gap ≈ **$1,500 per year of credit** | **Retired — priced the wrong thing.** It valued the benefit-amount channel only and omitted retirement-date acceleration, which is 20%–49% of the cost and a floor at that | FM-4 § 4.2 (decomposition); § 4.4 (per-purchaser PV of $6,779–$47,967) |
| A-14 | Veteran new hires ≈ 600/yr, hence an "ongoing steady state" cost line | **Retired — scope and method.** State classified only; and DHRM publishes the veteran share of the standing workforce, not of new hires | No replacement. See § 7.4 — the live measure is a one-time present value, and a new-hire flow line also mis-frames the bill |
| A-15 | 5-year amortisation of the one-time liability | **Retired** | A-27 |

### 2.4 Excluded from the cost estimate — must be priced separately

All of these push the figure **upward**. None is netted against the pension cost.

- **Health insurance credit** (F-14, F-15), including the 15-year threshold step function. Material, not quantified.
- **Adverse selection** (Annex A, § 5.1). Immediate access on the effective date means the actuary prices an **unbounded cohort**, so the entire weight of control sits on the two Annex A guardrails — priced as dials at FM-4 § 4.8 and registered here as A-28.
- **The early-retirement reduction subsidy** (F-48). Reaching an *unreduced* date earlier also extinguishes a reduction the member would otherwise have borne. Runs in one direction only: upward. This is why the 20%–49% acceleration share is a **floor**.
- **Refund option value** (§ 51.1-128).
- **VRS administrative cost** of implementing a graded schedule and 60-month payment agreements. HB 1867's analogue was ~$78,000 of NGF implementation cost, with **employer cost to implement reported as "None"** (F-61).
- **Employer-side payroll and backfill consequences of earlier retirement.** A cost to agencies and school divisions, not to the Fund. **Must not be netted against the pension figures.**
- **Hazardous duty** is now *in* scope and priced at F-22 / F-43 rates — but see A-25: the net direction for SPORS and VaLORS is unresolved.

---

## 3. Cost methodology

The governing identity and the formula. **No figures.** The worked surface is at [FM-2 § 2.3](04-Annex-2-Closure-FM1-FM5.md); the totals are at FM-4 § 4.4.

### 3.1 Governing identity

From F-26, actuarial equivalent cost is the plan's break-even price. Therefore:

```
Cost to the Fund, per year of credit purchased
  = Actuarial Equivalent Cost  −  price actually paid by the member
```

If the gap is zero the bill is free. **If the gap is negative the member subsidises the Fund** — and below roughly age 47–48 it is negative in all three plans, which is the strongest fiscal argument the proposal has.

Because recommendations A-1, A-2 and A-3 differ **only in the member's price** and never in the value of the credit, the three structures can be compared directly against one benefit value. FM-4 § 4.3 does that.

### 3.2 The two channels — and why an annex-worth of arithmetic missed one of them

Purchased § 51.1-142.2 service **is** creditable service (F-05), and the unreduced-retirement thresholds of § 51.1-153 are written in terms of creditable service. So a purchase does two distinct things, and VRS's own definition of actuarial equivalent cost covers both (F-26):

1. **Benefit amount.** One more year of service in the allowance formula.
2. **Eligibility date.** The unreduced retirement date moves earlier.

v1.1 of this annex priced only (1).

**The mechanical asymmetry that drives channel (2)** — the most important mechanical fact in the package:

- **§ 51.1-153 B 1, age 50 with 30 years (Plan 1):** once the member is past 50 the service leg binds alone, so one purchased year advances eligibility by **one full year**.
- **§ 51.1-153 B 3, Rule of 90 (Plan 2 and Hybrid):** a year actually worked adds **two** points — one of age, one of service. A purchased year adds **one**. So one purchased year advances eligibility by **half a year**.

Purchased military service is creditable service, but it is not time lived.

This asymmetry is also why the guardrail had to be redrawn (A-28). Acceleration exposure is driven by proximity to an eligibility **threshold** — age *and* service together — so a schedule graded on age alone cannot reach it. Two 55-year-olds, one with 25 years of service and one with 8, would pay the same age-graded rate while costing the Fund very different amounts.

### 3.3 Estimating AEC as a percentage of salary — benefit-amount channel

```
AEC%  =  M × G × ä × v

  M  = plan multiplier per year of service            (F-08, F-12)
  G  = salary growth factor from purchase to AFC measurement
       = (1 + A-04) ^ (years to AFC midpoint)
  ä  = COLA-adjusted annuity factor at retirement     (A-02, A-03, A-07)
  v  = discount from retirement back to purchase date
       = 1 / (1 + A-01) ^ (years to retirement)
```

The acceleration channel is valued separately, as the present value of moving the whole benefit stream earlier net of the shorter accrual, at the member's own eligibility threshold. FM-4 § 4.1–§ 4.2.

### 3.4 Why the AEC/ANC *multiple* is more trustworthy than the dollar level

F-25 states that the approximate normal cost rate is "the average cost of one year of VRS service credit." So the ANC rate is, by construction, the correct actuarial price **at the plan's average member**. The AEC/ANC multiple at any other age is therefore a ratio of actuarial value at that age to value at the average age — a quantity in which the annuity basis **largely cancels**.

The shape of the surface is robust even where its absolute level is an estimate. That is why A-07's sensitivity is reported on the multiple (≈ ±10%) rather than on the dollar figure, and why the 47–48 break-even cluster survives assumption changes that move the dollars materially.

### 3.5 Reproducibility

The live model is [`models/fm_model.py`](models/fm_model.py) — `python3 fm_model.py`. Every input is tagged OFFICIAL / DERIVED / ESTIMATE. The assumption IDs in § 2 above are the register for that model's inputs.

---

## 4. What a veteran pays today (verified rates × published salary)

**Not modelled.** F-19 through F-22, F-43 and F-44 multiplied by published salary. This is the **member price**, not the cost to the Fund, and Annex 2 Closure does not compute it. It is the core affordability finding behind the brief's DISCUSSION section and the 60-month payment authority in Annex A, § 2.3.

Salary bases, both official: **$69,865** = mean classified salary (F-34). **$70,790** = VRS-wide covered payroll per active member (F-51 ÷ F-38), derived at § 7.1. Group-specific bases below are F-51 ÷ F-38 for that group.

**Non-hazardous, at the VRS-wide average of $70,790:**

| Plan | Rate | 1 year | **4 years** | 4 years at the $69,865 classified mean |
|---|---|---|---|---|
| Hybrid | 6.68% | $4,729 | **$18,915** | $18,668 |
| Plan 2 | 10.74% | $7,603 | **$30,411** | $30,014 |
| Plan 1 | 12.50% | $8,849 | **$35,395** | $34,932 |

**Hazardous duty and judicial — new in v2.0, and the sharper half of the affordability finding.** v1.1 omitted these groups entirely. Each is shown at its own group's average covered payroll, because applying a statewide mean to SPORS or JRS would be meaningless.

| Group and plan | Rate | Salary basis | 1 year | **4 years** |
|---|---|---|---|---|
| Hazardous duty **alternate option** (electing localities; F-43) | 10.01% | $70,790 | $7,086 | **$28,344** |
| **VaLORS**, Plan 2 hazardous duty | 19.15% | $57,817 | $11,072 | **$44,288** |
| **SPORS**, Plan 2 hazardous duty | 19.15% | $96,476 | $18,475 | **$73,901** |
| **SPORS**, Plan 1 hazardous duty | 23.78% | $96,476 | $22,942 | **$91,768** |
| **JRS**, Plan 2 judicial (F-42) | 29.67% | $209,883 | $62,272 | **$249,089** |

**Three things to take from this table.**

1. **These are floors.** F-23: the rate applies to creditable compensation **or AFC at the time of purchase, whichever is higher**. A mid- or late-career purchase is priced off a higher salary than these averages.
2. **Combined with F-27, current law is close to unusable for its intended beneficiaries.** Payment agreements run 6–12 months and may not extend beyond the two-year window. A Hybrid veteran must therefore find **$18,915** within two years of being hired — the point in a career at which someone transitioning out of the service has the least liquidity. A VaLORS officer must find **$44,288**. This is the affordability case for the 60-month payment authority, stated in published numbers rather than in modelled ones.
3. **Hazardous duty is where both the Fund's exposure and the member's price are largest** (FM-3). Those partly offset; the net is for the actuary — A-25.

---

## 5. Unverified, open and deliberately omitted claims

| ID | Claim | Status | What would resolve it |
|---|---|---|---|
| U-01 | **Historical take-up** for § 51.1-142.2 military purchases | **Not available publicly.** The single input that most changes the answer (A-22) | **VRS data request item 5** — purchases completed per year for ten years, split by ANC vs AEC pricing, with average years and average dollars. Annex A, Q5 |
| U-02 | Number of members holding **verified but unpurchased** military service | **Irreducibly unavailable — and now confirmed so by VRS itself.** F-62: VRS told the 2023 General Assembly it "is not able to determine the number of current teachers or future teachers who would have prior active military service to purchase." Verified military service exists in VRS records only for members who already applied (F-29); members who hold it and never applied are not identifiable from VRS data at all, only from an employer self-identification field — which is what F-31 is, and why it is a floor. **This is useful rather than merely limiting:** it means no one can produce a point estimate here, so the range in FM-1 § 1.6 is not a shortcoming of this analysis | Items 1–4 and 6–7 of the § 1.7 request still narrow it as far as it can be narrowed. **A point estimate should not be promised to anyone** |
| U-03 | Whether purchased military service counts toward **hazardous-duty service thresholds** | **Not determined.** More consequential than in v1.1, since hazardous duty is in scope and carries the largest per-member exposure | VRS counsel — Annex A, Q4 |
| U-04 | **Plan mix by employer group** | **Not published.** Governs A-25; the SPORS / VaLORS net is unresolvable without it | **VRS data request item 1** |
| U-05 | The **actuarial-equivalent-cost factor basis** | **Exists and is requestable — this changed between v1.1 and v2.0.** F-46: the Plan Actuary develops AEC rates annually from the prior-year valuation. It is a document, not a per-member computation that must be commissioned. Say "VRS does not publish it," not "VRS has none" | **VRS data request item 8**, naming Gabriel, Roeder, Smith & Company (F-52) |
| U-06 | **Pinpoint for the HB 1867 fiscal impact statement** (F-56) | **CLOSED October 25, 2026.** Retrieved from Virginia LIS (document HB1867F158, dated 1/16/2023). The band is verbatim and the statement contains **more** than was being cited: VRS's own worked total of **$50 million** at 1% teacher take-up on a **$35,000** average (F-60), the $78,000 administrative figure with "employer cost to implement: None" (F-61), VRS's own statement that it cannot identify who holds the service (F-62), and VRS confirming the credit reaches vesting, retirement eligibility and the HIC (F-63). Confidence raised Medium → High. See § 7.5 | — |
| U-07 | **SB 950 (2026)** putting new judges in Plan 2 (F-42) | **Verified only at one remove** — read from the VRS ACFR FY2025 legislative summary, not from the chapter text | Retrieve the 2026 Acts of Assembly chapter text for SB 950 |
| U-08 | **Standards of Quality composite share** | **Deliberately not assumed** (A-26) | DPB |
| U-09 | Veteran **new hires** per year into state service | **Estimate retired, not replaced** (A-14 → § 2.3). DHRM publishes the veteran share of the standing workforce, not of new hires. Likely above 6% given the § 2.2-2903 preference (F-18) | DHRM or Cardinal HCM new-hire data disaggregated by veteran status |
| U-10 | Prior General Assembly bills changing the **military** cost window | **Searched; none identified.** 2026 c. 563 amended § 51.1-142.2 for an unrelated purpose (F-36) | A full LIS bill-history search of § 51.1-142.2 amendments by Legislative Services |
| U-11 | Virginia's total veteran population | **Resolved in v2.0 — verified at 646,000** (F-58), inside the 630,000–665,000 band v1.1 flagged and omitted. Still not load-bearing, but citable if asked | — |
| U-12 | The DVS Commissioner's Annual Report FY2025 **does not state** a Virginia veteran population figure | **Verified absence.** Reports V3 program outputs only | — |
| U-13 | Age of the NCES teacher veteran share (F-59) | **2016 data, used as the teacher floor.** No more recent published figure located | A more recent NCES or BLS cut of teachers by veteran status |

---

## 6. Primary sources

All retrieved October 24, 2026. This is the consolidated list for the package; Annex 2 Closure's own table is this same set plus its derivations.

**Code of Virginia** (all retrieved and text-verified):

- [§ 51.1-142.2](https://law.lis.virginia.gov/vacode/title51.1/chapter1/section51.1-142.2/) · [§ 51.1-124.3](https://law.lis.virginia.gov/vacode/title51.1/chapter1/section51.1-124.3/) · [§ 51.1-128](https://law.lis.virginia.gov/vacode/title51.1/chapter1/section51.1-128/) · [§ 51.1-138](https://law.lis.virginia.gov/vacode/title51.1/chapter1/section51.1-138/) · [§ 51.1-145](https://law.lis.virginia.gov/vacode/title51.1/chapter1/section51.1-145/) · [§ 51.1-153](https://law.lis.virginia.gov/vacode/title51.1/chapter1/section51.1-153/) · [§ 51.1-155](https://law.lis.virginia.gov/vacode/title51.1/chapter1/section51.1-155/) · [§ 51.1-165.01](https://law.lis.virginia.gov/vacode/title51.1/chapter1/section51.1-165.01/) · [§ 51.1-166](https://law.lis.virginia.gov/vacode/title51.1/chapter1/section51.1-166/) · [§ 51.1-169](https://law.lis.virginia.gov/vacode/title51.1/chapter1/section51.1-169/) · [§ 51.1-1400](https://law.lis.virginia.gov/vacode/title51.1/chapter14/section51.1-1400/) · [§ 2.2-2903](https://law.lis.virginia.gov/vacode/title2.2/chapter29/section2.2-2903/) · [§ 30-19.1:7](https://law.lis.virginia.gov/vacode/title30/chapter1/section30-19.1:7/)

**Virginia Retirement System:**

- [*Purchase of Prior Service Cost Rates*](https://www.varetire.org/am/media/shared/pdf/publications/pps-rate-charts.pdf) — rates effective July 1, 2025, pp. 1–4
- [VRS Employer Manual, *Purchase of Prior Service Credit*](https://employers.varetire.org/media/shared/pdf/er-manual-purchase-of-prior-service-credit.pdf) — July 2026 edition
- [VRS Annual Comprehensive Financial Report FY2025](https://www.varetire.org/media/shared/pdf/publications/2025-annual-report.pdf) — Figures 2.3, 2.9, 2.10; legislative summary
- [VRS Annual Actuarial Valuation, June 30, 2025](https://employers.varetire.org/media/employers/pdf/financial-reporting/valuations/valuation-report-vrs.pdf) — Executive Summary; Results Summary by group
- [*VRS 101 / Who We Serve*](https://www.varetire.org/media/shared/pdf/publications/intro-to-vrs-brochure.pdf) — 2025 edition, p. 4
- VRS Board of Trustees minutes — [June 18, 2025](https://www.varetire.org/media/members/pdf/board/minutes/2025/board-of-trustees-minutes-06-18-25.pdf) (RBA 2025-06-10; the quadrennial-cycle and Plan-Actuary statements) · [February 5, 2026](https://www.varetire.org/media/members/pdf/board/minutes/2026/board-of-trustees-minutes-02-05-26.pdf) · [April 23, 2026](https://www.varetire.org/media/members/pdf/board/minutes/2026/board-of-trustees-minutes-04-23-26.pdf) · [June 17, 2026](https://www.varetire.org/media/members/pdf/board/minutes/2026/board-of-trustees-minutes-06-17-26.pdf) (B&A report; Early Retirement Factors Study)
- [VRS, *2023 Fiscal Impact Statement*, **HB 1867**](https://legacylis.virginia.gov/cgi-bin/legp604.exe?231+oth+HB1867F158+PDF) — the § 30-19.1:7 statement; dated January 16, 2023, document HB1867.DOC/VRS, 3 pp. Bill history: [LIS HB 1867, 2023 Reg. Sess.](https://legacylis.virginia.gov/cgi-bin/legp604.exe?231+sum+HB1867=) (patron P. Scott; left in Appropriations 2/7/2023)

**Virginia government:**

- [DHRM, *State Employee Workforce, Compensation, Health Benefits*](https://sfac.virginia.gov/pdf/General%20Gov/2025/01212025_No1_DHRM.pdf) — Senate Finance & Appropriations, January 21, 2025; data as of June 30, 2024
- [Virginia DVS, Commissioner's 2025 Annual Report](https://rga.lis.virginia.gov/Published/2025/RD986) (RD986) — reviewed; states no veteran population figure
- [Virginia LIS, 2026 Reg. Sess., HB 139 / Chapter 563](https://lis.virginia.gov/bill-details/20261/HB139/text/CHAP0563)
- 2026 Acts of Assembly, **SB 950** — **chapter text not yet retrieved, U-07**

**Federal:**

- BLS, *Employment Situation of Veterans* — [Table 8](https://www.bls.gov/news.release/vet.t08.htm) (August 2025) · [Table 6A](https://www.bls.gov/news.release/vet.t06a.htm) · [Table 6B](https://www.bls.gov/news.release/vet.t06b.htm) (2025 annual averages)
- [NCES, *Digest of Education Statistics*, table 209.27](https://nces.ed.gov/programs/digest/d17/tables/dt17_209.27.asp)
- 10 U.S.C. ch. 1223 (Reserve Component retirement), referenced in § 51.1-142.2 B 3; IRC § 415(n) (permissive service credit limits) — both flagged for counsel review, neither independently analysed

**Comparative:** N.Y. Ret. & Soc. Sec. Law § 1000 (6% of trailing-12-month compensation, remainder expressly on participating employers) — the model for recommendation A-2, FM-4 § 4.3.

---

## 7. Reconciliation log — what this pass changed, and the checks it produced

v2.0 is not a transcription of Annex 2 Closure. Reconciling the two documents required four arithmetic checks (§ 7.1–§ 7.3 and § 7.4), and all four produced findings. Closing the one citation gap the pass opened produced a fifth that was not sought (§ 7.5).

### 7.1 The salary basis of the live cost model was inherited unexamined — and it holds

FM-4 § 4.4 computes its statewide per-purchaser figure at **$69,865**, the DHRM mean *classified state* salary (F-34). But the pool it multiplies is roughly 72% teachers and political-subdivision employees. A state-classified salary applied to a statewide pool was an unflagged exposure in the live model.

It checks out. From official covered payroll (F-51) and official actives (F-38):

```
VRS-wide covered payroll per active member
  = $26,762,817,000 / 378,060  =  $70,790          (ratio to F-34: 1.013)

Weighted by the FM-1 § 1.6 eligible pool, low band  =  $70,120   (ratio 1.004)
Weighted by the FM-1 § 1.6 eligible pool, high band =  $70,229   (ratio 1.005)
```

**The inherited basis is within 0.4%–0.5% of the correctly pool-weighted official figure.** The two largest groups sit either side of it — teachers at $72,961, political subdivisions at $64,709 — and very nearly cancel. So no cost figure in FM-4 needs to move, and A-24 is now a checked assumption rather than a hidden one. Recorded because this is exactly the class of inherited input an assumption register exists to catch, and because a reviewer at Senate Finance is entitled to see that someone looked.

One consequence worth carrying: **group averages diverge far more than the mean does** — JRS $209,883, SPORS $96,476, VaLORS $57,817, against a statewide $70,790. The blended per-purchaser figure is therefore safe statewide and unsafe per group. That is A-25 stated in dollars, and it is the arithmetic reason FM-4 § 4.7's SPORS / VaLORS line must not be read as a net.

### 7.2 One assumption in v1.1's "still current" list was not current — A-03

v1.1's superseded-notice asserted that A-01 → A-07 were "additionally confirmed against the June 30, 2025 valuation." **That was true of six of the seven.** A-03 set the Plan 1 long-run COLA at **3.0%**, an analyst figure reasoned from the F-13 5% cap structure. The Board-adopted assumption in that same valuation is **2.50%** (F-55).

Corrected in § 2.1. Direction of the error: a lower COLA lowers the Plan 1 annuity factor and therefore lowers Plan 1 AEC, so v1.1's Plan 1 gap table was mildly *overstated* — the opposite direction from v1.1's main error, and small. Annex 2 Closure used the Board-adopted 2.50% throughout, so **no live figure is affected.** Logged because an annex that holds itself out as an assumption register has to be right about which of its own assumptions are official.

### 7.3 The retired annuity factors reconcile to the live basis, within A-07's own tolerance

v1.1's A-07 asserted factors of **13.3** (post-2010 / Hybrid) and **14.5** (Plan 1) from a "~20-year expectancy." Annex 2 Closure instead uses a level-COLA annuity-certain to age 87. On the live Board-adopted assumptions that gives:

```
Plan 2 / Hybrid, retire 67, net discount 1.0675/1.0225 − 1 = 4.401%, 20 yrs  →  13.70
Plan 1,          retire 65, net discount 1.0675/1.0250 − 1 = 4.146%, 22 yrs  →  14.84
```

**13.3 against 13.70 is 2.9% low; 14.5 against 14.84 is 2.3% low.** Both well inside A-07's stated ±10%. The two annexes were therefore using compatible annuity bases, which is why FM-2 § 2.3 independently reproduced v1.1's 47–48 break-even ages from a different construction. That reproduction is now explained rather than coincidental, and it is a genuine cross-validation of the one part of v1.1's model that survives.

### 7.4 What was actually wrong with "under $2 million one-time, under $100,000 per year"

So that the retraction can be defended rather than merely stated. Both figures came from v1.1 § 3.4 of this annex. The arithmetic was **internally consistent for what it covered**; it covered the wrong things.

| | v1.1 | Live basis | Effect |
|---|---|---|---|
| Population | 2,600 — state classified veterans past the window (A-08 × A-09 × A-10) | **10,561 – 26,321** across three plans and six employer groups (FM-1 § 1.6) | **4× – 10×** |
| Channels priced | Benefit amount only, at ~$1,500 per year of credit (A-13) | Benefit amount **and** retirement-date acceleration; $6,779 – $47,967 per purchaser (FM-4 § 4.2, § 4.4) | **~2× – 13×** per member |
| Payroll denominator | $3.98bn classified payroll (F-30 × F-34) | **$26.76bn** total covered payroll (F-51) | 6.7× — but the pool grew faster, so **the payroll share rises too** |
| Ongoing line | "Under $100,000/yr", from a flow of ~600 veteran new hires per year at a near-zero Hybrid gap (A-14) | **Withdrawn, not replaced.** The scope decision gives immediate access to a standing cohort, so the measure is a one-time present value, not a steady-state flow. A new-hire flow line also mis-frames the bill: the members it exists to help are precisely those already past the window | — |
| Rounding | $1.46M rounded up to "under $2 million" to absorb HIC and adverse selection | Those items remain **unpriced and excluded** (§ 2.4), and a 37% round-up cannot absorb them | The round-up was a judgment, not a calculation — and it was not conservative |

**The independent signal that it was too low was available at the time.** VRS's own fiscal impact statement on HB 1867 (2023) put a **free** grant of active-duty military service to teachers at $10,000–$60,000 of unfunded liability per participating member (F-56). v1.1 implied roughly **$3,750** per purchasing member — a factor of three below the *floor* of a band VRS produced for a benefit with no member price at all. A purchase at which the member still pays must cost the Fund less than a free grant; it cannot cost a third of the floor. FM-4 § 4.6.

**Also corrected:** the scale sentence. "About 5 cents out of every $100 of a single year's payroll" is right only at the very bottom of the live grid (0.049%) and understates the top by about fourteen times (0.681%). Brief v1.2 and the one-pager carry the corrected framing.

### 7.5 The HB 1867 statement, retrieved — and what it does and does not validate

U-06 was opened and closed in this pass. The statement (VRS, *2023 Fiscal Impact Statement*, HB 1867, dated 1/16/2023) turned out to carry three things the package was not using.

**1. VRS published its own total, and it is in our order of magnitude — for teachers alone, free, at 1% take-up.**

> "if 1,500 members (1% of the Teacher population) had this type of service, and the average cost was $35,000, the total cost to the fund could be **$50 million**." (F-60)

So the only total VRS has ever published for a benefit of this shape is **$50 million against the teacher population alone, at 1% participation, for a free grant.** Our $13M–$182M across six employer groups, three plans, 5%–30% take-up, for a benefit the member still pays for, is plainly the same order of magnitude. **It is the retracted "under $2 million" that is the outlier, not the new range** — and that can now be demonstrated from VRS's own arithmetic rather than argued.

**2. The per-member figures agree structurally, not just in magnitude.** A priced purchase must cost the Fund less than a free grant of identical service. By how much is predictable: the member pays the approximate normal cost, so the Fund bears `1 − 1/m` of the value, where `m` is the AEC/ANC multiple.

```
Our blended A-3 net PV per purchaser / VRS free-grant average
  = $24,627 / $35,000  =  0.704

Predicted band from the modelled multiples (FM-2 § 2.4, m = 2.76x - 3.54x):
  1 - 1/2.76 = 0.638   ...   1 - 1/3.54 = 0.718
```

**0.704 sits inside that band**, and nearest to the 3.23× profile (0.690). Two independently constructed quantities — our per-purchaser present value, and VRS's average cost for a free grant — stand in the ratio the pricing structure requires, and neither half was built to produce the other.

**The limit of this check, which must travel with it.** VRS's $35,000 is a **teacher-only** average for a **free** grant; our $24,627 is pool-weighted across all six employer groups and three plans. The plan mixes are not the same, and the teacher plan mix is unpublished (U-04). So this is a **magnitude-and-direction check, not a calibration** — it says the figures are the right size and in the right order, not that either is confirmed to three digits. Red Team finding S-8 makes the same point against a stronger version of this comparison on the one-pager, and it is right to. The direction of the residual uncertainty is knowable: teachers are a longer-tenure workforce, so if they skew more Plan 1 than our blend does, VRS's $35,000 reflects a costlier mix and the true comparable ratio is **higher** than 0.704, not lower.

**3. VRS's own words close two of our open items and support a third.**

- **F-62 confirms U-02 is irreducible.** VRS: it "is not able to determine the number of current teachers or future teachers who would have prior active military service to purchase." The population range in FM-1 § 1.6 is therefore not a weakness of this analysis — **nobody can do better, including VRS.** Say that plainly rather than apologising for the range.
- **F-63 confirms the eligibility channel from VRS's own mouth:** prior service credit "counts toward vesting, eligibility for retirement and eligibility for the health insurance credit." That is § 3.2's two channels and the § 2.4 HIC exclusion, stated by VRS in a filed impact statement.
- **F-61 gives a § 30-19.1:7 precedent for the *narrow* general-fund claim, and refutes the broad one.** For a *free* grant VRS put its own implementation cost at ~$78,000 NGF, employer cost to implement at **"None,"** and the general fund at **"no immediate impact."** Our A-3 requires no new rate-setting at all (FM-3, point 4), so its administrative footprint should be no larger — that part is good precedent.
  **But note the word "immediate," and the sentence VRS put beside it:** *"Depending on the number of teachers who take advantage of this provision over time, this may impact contribution rates."* VRS's own statement therefore supports "**this bill requests no appropriation**" and **does not** support an unqualified "general fund cost: $0." Read correctly, F-61 is **evidence for** Red Team finding F-2, not against it — the printed one-pager generalises a true narrow claim into a false broad one. I had this the wrong way round when I first logged it; corrected here. The defensible formulation is the one at Red Team F-2: no appropriation is requested, and the cost is absorbed in future employer rates under § 51.1-145, with the three exposure buckets named.

**One asymmetry to carry honestly.** F-63 also notes that granting service in a pooled plan "will effectively spread the cost of each period of granted service over all of the employers in the Teacher plan." That is the mechanism by which our political-subdivision and teacher exposure lines reach employers who have no veteran purchasing — and it is what the Commission on Local Government will focus on (FM-4 § 4.7). It cuts against us and should be in the brief before someone else puts it there.

**Scale comparator now available:** the Teacher Plan's unfunded liability is **$11.8 billion** (F-60). VRS's own $50M example is 0.42% of it.

### 7.6 Items this pass closed, and items it opened

**Closed by Annex A v1.1** (commit 3704a3e), both originating in FM-4 § 4.8 and FM-3:

| Item | Resolution |
|---|---|
| The Board's graded rate authority read **"attained age" alone**, which removes only ~15% of the modelled exposure | **Resolved.** Annex A § 2.2 now grades on **age and creditable service**, equivalently distance from unreduced eligibility, with the amount purchased as a third factor, plus publication, uniformity and actuarial-equivalent-cost-ceiling constraints and a no-spillover sentence confining the schedule to subdivision B 2. Registered here as A-28. **What remains open is the dial setting, not the phrase** (Annex A, Q12) |
| The **10.01% alternate hazardous duty option** is published as a stand-alone rate with no plan column, so drafting by reference to "the approximate normal cost of the retirement plan under which the member is covered" did not cleanly reach it | **Resolved** via Annex A § 2.2 factor (v), anchored to "the benefits permitted by § 51.1-138." Note that the same pre-existing mismatch for *other* purchase categories is deliberately left unamended |

**Opened or still open:**

| Item | Owner |
|---|---|
| **U-06 — pinpoint the HB 1867 fiscal impact statement** | **Closed in this pass.** Retrieved, verbatim, and it strengthened the package rather than merely citing it — § 7.5. F-56 confidence Medium → High; F-60 to F-63 added |
| **U-07 — retrieve the SB 950 (2026) chapter text** rather than relying on the ACFR legislative summary | Fiscal & Impact Modeler |
| Annex 2 Closure § 4.6 cited "the brief's own Annex 3 source list at S8." **There is no Annex 3 in this package** and no S-numbered source list | **Fixed in this pass** — 04 § 4.6 rewritten on the retrieved statement, citing F-56 and F-60 to F-63 |
| **A-26 / U-08 — the DPB Standards of Quality composite share**, to split the teacher exposure line | DPB request, via Fiscal & Impact Modeler |
| **A-28 — the guardrail dial setting.** Now a policy choice rather than a drafting defect: 0% is plain A-3, 100% drives the fiscal note to zero by removing the pricing subsidy from exactly the long-service Plan 1 veterans most eager for the bill | JLCVSO (Annex A, Q12) |
| **A-22 / U-01 — historical take-up.** Roughly a factor of 6 of the grid's factor-of-14 span | VRS data request item 5 |
