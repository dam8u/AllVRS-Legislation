# Red Team / Counsel Review — Military Service Credit Cost Window

**Issue:** MOO-289 (parent MOO-287) | **Date:** October 25, 2026 | **Reviewer:** Red Team / Counsel Reviewer
**Package reviewed:** `00-ONE-PAGE-BRIEF.md` / `.html` / `.pdf`; `01-JLC-Legislative-Change-Brief.md` (v1.2);
`02-Annex-A-Legal-Analysis-and-Draft-Bill.md` (v1.1); `03-Annex-B-Fiscal-Assumptions-and-Sources.md`;
`04-Annex-2-Closure-FM1-FM5.md`; `models/fm_model.py` (run, exit 0, reproduces every published figure).

> **Internal risk analysis. Not legal advice.** This review is not a legal opinion the organization
> may rely on, and nothing in it states or implies that counsel has cleared the proposal. I am not
> counsel of record. Every finding is about text, numbers, and evidence.

**Verdict in one line: do not file, and pull the one-pager back off print, until F-1 and F-2 are
resolved.** Everything else on this list is fixable inside the drafting cycle. F-1 and F-2 are not
drafting defects — they are two promises the package makes to two different audiences that cannot
both be kept.

**Count: 18 findings — 2 fatal, 8 serious, 6 moderate, 2 minor.** Most serious: **F-1**.

---

## 1. The strongest case against, in the opposition's voice

*(VRS Board staff / Department of Planning and Budget / House Appropriations / Commission on
Local Government, consolidated. This is the brief I would write if I were opposing.)*

> This bill asks the General Assembly to repeal a pricing rule without knowing what the repeal
> costs. The patron's own analysts moved their estimate from "under $2 million one-time" to
> "$13 million to $182 million" inside a single month — a factor of ninety — and the new number is
> still not VRS's. The honest reading of that history is not that the second number is right. It is
> that nobody outside VRS can produce a reliable number, and the bill asks the money committees to
> legislate first and price later.
>
> Second, the bill is advertised as costing the general fund nothing. That is true only in the
> narrow sense that it contains no appropriation. The patron's own annex puts $20 million to
> $40 million of present value on state agencies — general fund *and* nongeneral fund — another
> $13 million to $33 million on school divisions through the Standards of Quality, and $23 million
> to $45 million on localities through rates they never vote on. "General fund cost: $0" is a
> drafting convention, not a fiscal fact, and § 30-19.03 obliges the Commission on Local Government
> to say so in its own statement.
>
> Third, the cost control the patron offers is illusory, and the patron's own model says so. The
> money committees are told the VRS Board can dial the exposure to zero. Veterans are told the rate
> will be published, uniform, and predictable. Both cannot be true. A uniform published rate that
> may not exceed any individual member's actuarial equivalent cost must be set at the cheapest
> member in the class; on the patron's own arithmetic that recovers a quarter of the excess in the
> class that matters most. To recover all of it the Board must price member by member — which is
> the actuarial equivalent cost § 51.1-142.2 B 3 already charges today. So the choice on offer is
> between a bill that costs real money and a bill that changes nothing.
>
> Fourth, the 24-month window is not an accident and it is not about military service. It is the
> plan's standing answer to adverse selection in *every* purchase category. Carve out one category
> for one sympathetic population and the principle is conceded; the educational-leave, out-of-state
> service and part-time service purchasers will be back next session with the patron's own equity
> argument turned around. The patron's annex concedes the line was drawn where it was to "keep the
> bill narrow and the fiscal note small" — that is a budget rationale, not a principle, and it will
> not survive a hearing.
>
> Finally, the Commonwealth already honors this service. § 51.1-142.2 I grants it free to members
> who serve on leave and return. § 51.1-142.2 B 2 already lets every member buy four years. What
> this bill actually changes is the price paid by members who have had years — in the Plan 1 cohort,
> decades — to make the purchase and chose not to. The General Assembly is being asked to subsidize,
> retroactively, a decision not to buy, out of a trust fund the Constitution of Virginia requires
> be administered "solely in the interests of the members and beneficiaries thereof."

**Does the package answer this?** It answers the fourth paragraph well (§ 5 and § 8 of Annex A, the
narrow footprint, the targeted cross-reference). It answers the first paragraph honestly. It does
**not** answer paragraphs two, three, or five anywhere. See F-1, F-2, M-1, M-2.

---

## 2. Findings, ranked by severity

### FATAL

#### F-1 — The guardrail the fiscal case rests on cannot be built from the authority the bill grants
*Category: fiscal / drafting. Annex A § 2.2, § 2.5, § 5.1; Annex 2 Closure § 4.8; `fm_model.py:554`.*

Annex A § 5.1, Annex 2 Closure § 4.8 and brief 01 line 244 all tell the money committees that a
schedule graded on age **and** creditable service removes "all" of the exposure at the 100% recovery
setting, where "the bill is actuarially neutral by construction and the fiscal note is zero." That
claim is produced by `price_threshold_graded()`, which computes

```python
return anc_price + recovery * max(0.0, r["cost_total"] - anc_price)
```

where `r["cost_total"]` is **that one member's own** benefit-amount plus acceleration cost, from
`fm4_acceleration(p)`. At `recovery=1.0` the member pays exactly their own actuarial value and the
net is zero *by subtraction*. The function never computes a class rate. It is individualised
actuarial pricing, modelled.

The draft bill forbids that. § 2.2 requires any schedule to "apply uniformly to all members within
the same classification under the schedule" **and** to "not require payment of an amount exceeding
the actuarial equivalent cost of the service credit purchased." For a uniform rate to satisfy the
ceiling for *every* member in a class, it must be set at or below the **minimum** actuarial value in
that class — not the mean. I re-ran the team's own `fm4_acceleration` over classes as fine as the
draft's five factors permit (plan × 5-year age band × 10-year service band × 4 years purchased,
salary held constant so the only variation is the risk the schedule exists to price):

| Class | min value | mean | max | max/min | 100% dial actually recovers |
|---|---|---|---|---|---|
| Plan 1, age 50–54, svc 20–29 | $125,910 | $155,412 | $194,301 | 1.54× | **73%** |
| **Plan 1, age 55–59, svc 20–29** | **$71,438** | **$148,225** | **$192,855** | **2.70×** | **25%** |
| Plan 2, age 50–54, svc 10–19 | $67,841 | $79,395 | $92,219 | 1.36× | 71% |
| Hybrid, age 50–54, svc 10–19 | $41,116 | $48,118 | $55,890 | 1.36× | 70% |
| Hybrid, age 55–59, svc 10–19 | $34,837 | $47,411 | $56,726 | 1.63× | 45% |

The Plan 1, 55–59 class is the one that matters: it is the cohort the one-pager leads with and the
cohort § 2.5 names as "the cohort most eager for the bill." In that class the 100% dial recovers
**25%** of the above-ANC excess, not 100%. The fiscal note is not zero at any lawful setting.

The draft presents a dilemma, and both horns are already in the package:

- **Coarse classes** → a genuine published class rate, and the exposure is largely unrecoverable
  (table above). The $0 fiscal note is unreachable.
- **Fine classes** (factor (ii) permits exact distance-to-eligibility, so classes can be near
  singletons) → recovery approaches 100%, but the schedule is individualised pricing in substance.
  That is the thing Annex A § 2.2's own drafting note says was "considered and rejected" because it
  is "indistinguishable from individualised actuarial pricing, which is the thing veterans are being
  promised they will not face," and it is what § 8 point 4 was written to make unchallengeable.

And there is a third problem that survives both horns. At the 100% setting the member pays the
actuarial equivalent cost. **That is what § 51.1-142.2 B 3 already charges today after 24 months.**
So the setting that drives the fiscal note to zero is the setting at which the bill's price promise
is extinguished; what remains is a published rate and the 60-month term. § 2.5 concedes this in one
sentence for Plan 1 veterans. The one-pager does not concede it anywhere — it promises the "regular
price ... at any point in their career" on the same page.

**Concrete failure scenario.** The bill is heard in Senate Finance. The patron offers the 100% dial
to secure a neutral impact statement. VRS actuaries are asked what rate the Board would adopt; they
answer that a uniform class rate capped at each member's own AEC must be set at the class minimum,
and produce the Plan 1 55–59 number: 25% recovery, leaving roughly three-quarters of the exposure.
The patron must then either accept a materially adverse impact statement or accept member-by-member
pricing, at which point JLCVSO has delivered its veterans the statutory status quo plus a payment
plan. Either outcome was foreseeable from the package's own model and is not disclosed in it.

**Suggested direction.** Do not try to fix this in the rate-schedule sentence. Pick the dial you are
actually willing to deliver and draft to it: either (a) strike the individual-AEC ceiling and cap at
*the actuarial equivalent cost determined for the classification*, which makes a class rate lawful
and lets the dial bite — accepting that some members pay above their own AEC, which must be said out
loud; or (b) keep the individual ceiling, keep uniformity, and re-state the fiscal case on a
recovery band of roughly 25%–75%, which on the team's own § 4.8 grid is $14M–$43M of residual at 20%
take-up on the low pool. Q3a already asks half of this question; it needs to be reframed from "how
closely does a class rate track AEC" to "is a class rate that recovers the mean lawful under the
ceiling we drafted." Drafting Specialist owns the text; Fiscal & Impact Modeler owns the re-stated
band. **This finding must appear in the memo's risk section.**

---

#### F-2 — "General fund cost: $0" is contradicted by the package's own who-bears-the-cost table
*Category: evidence integrity. `00-ONE-PAGE-BRIEF.md:63`; Annex 2 Closure § 4.7; `fm_model.py:496`.*

The printed leave-behind — **cleared to print, HOLD lifted** — states: "**General fund cost: $0.**
That is structural, not a rounding." The package's own model says otherwise. `fm_model.py` comments
the bearer mapping as:

```
#   state       — state agency employer rates; general fund and nongeneral fund
```

and the § 4.7 table assigns **$20,258,560 – $39,890,588** of present value at 20% take-up to "State
agencies (GF + NGF)," plus $13.3M–$33.3M to school divisions through the Standards of Quality, which
is a shared state obligation. The $0 claim is accurate only about the *bill* (no appropriation
clause). It is not accurate about the *Commonwealth*. Brief 01 line 166 states the proposition
correctly and narrowly — "**local** exposure ... never touches the general fund." The one-pager
generalises that sentence to the whole bill and adds "That is structural, not a rounding," which
converts a true narrow claim into a false broad one.

**Concrete failure scenario.** DPB prepares the fiscal impact statement, assigns the state-agency
share of the employer rate increase to the general fund in the out-biennium, and the committee reads
the one-pager side by side with it. JLCVSO's single most repeated sentence is then publicly wrong on
its face, in the one document legislators keep. Every other number in the package loses the benefit
of the doubt — including the ones that are right.

**Suggested direction.** One sentence, and it costs nothing politically: "**This bill requests no
appropriation.** The cost is absorbed in future employer contribution rates under § 51.1-145 — on
our modelling, $20M–$40M of present value on state agencies, $13M–$33M on school divisions, and
$23M–$45M on localities." That is still a strong fiscal story and it is one DPB cannot contradict.
**Must appear in the memo's risk section.** Editor and Policy Director own the reprint decision; the
PDF should go back on hold until it is made.

---

### SERIOUS

#### S-1 — Enactment clause 2 (vi) restates the anti-duplication sentence incompletely, and the omitted limb may be the one that matters most
*Category: drafting / preemption. Annex A § 2.4 clause 2 (vi), § 4, § 8 point 7.*

The actual sentence in § 51.1-142.2 B 3 is:

> "Except as otherwise required by Chapter 1223 of Title 10 of the United States Code, as amended,
> no service credit may be purchased under this section if it is included in the calculation of any
> retirement allowance received or to be received by the member from this or another retirement
> system, **or if there is a balance in a defined contribution account that serves as a primary
> retirement account related to such service.**"

Annex A § 4 describes this sentence as barring "purchase of service already counted in another
retirement allowance" and never mentions the defined-contribution limb. Enactment clause 2 (vi)
reaffirms only the allowance limb. A no-spillover clause that enumerates what survives and omits one
limb of the provision it purports to preserve invites the *expressio unius* inference that the
omitted limb did not survive.

**And the omitted limb raises a question the package never asks.** Under the military Blended
Retirement System, in force for service entrants on and after January 1, 2018, Thrift Savings Plan
contributions are a component of the primary military retirement benefit rather than a supplement.
If VRS reads a BRS-era TSP balance as "a balance in a defined contribution account that serves as a
primary retirement account related to such service," then the bar in B 3 defeats a B 2 purchase
**regardless of price or deadline** — for exactly the forward-looking cohort the bill is meant to
serve. The package's population estimate is built from standing-workforce veteran shares, not from
service-entry dates, so it cannot detect this.

**Concrete failure scenario.** A veteran who enlisted in 2019, separated in 2025, and joined a
Virginia school division in 2026 applies in 2030 to buy four years under the new carve-out. VRS
denies the application on the DC-balance limb. She points to enactment clause 2 (vi), which does not
mention that limb, and appeals. Whichever way that is decided, JLCVSO has either lost the bill's
forward-looking population or won by accidentally repealing a federal-coordination provision it said
it was preserving verbatim.

**Suggested direction.** Either quote clause 2 (vi) verbatim from the statute or delete the clause
and rely on the fact that the sentence is not amended. Add to **Q7**: does a BRS-era TSP balance
trigger the defined-contribution bar in § 51.1-142.2 B 3, and if so for which service-entry cohorts?
Statutory Researcher and Drafting Specialist. **Must appear in the memo's risk section.**

#### S-2 — The 60-month payment term and the 12-month pre-retirement completion rule cancel each other, and neither has a remedy
*Category: drafting / enforcement reality. Annex A § 2.2 final new sentence, § 2.3.*

The draft grants both (i) payroll-deduction agreements of up to 60 months for B 2 purchases and
(ii) Board authority to require that a B 2 purchase "be completed not fewer than 12 months prior to
the member's effective date of retirement." Three defects compound:

1. **"Completed" is undefined.** § 51.1-142.2 F distinguishes entering a contract from completing
   payment, and provides that a member whose deduction terminates early "shall be credited with the
   number of full or partial months of service for which full payment has been made." If "completed"
   means fully paid, a 60-month agreement is unusable by anyone within six years of retirement.
2. **"Effective date of retirement" is not knowable when the purchase is made.** The member elects
   it later. The rule is therefore testable only retroactively.
3. **No remedy.** The draft states a requirement and provides no consequence for breach — no
   voiding, no repricing, no refund, no actor charged with enforcing it. A duty with no penalty and
   no enforcer is a press release.

**Concrete failure scenario.** A Plan 1 member, age 56 with 26 years, is 4 years from unreduced
eligibility (age 50 + 30, § 51.1-153 B 2). She buys 4 years, which makes her immediately eligible.
She elects a 60-month payroll deduction, running to age 61. If the Board imposes the 12-month rule
on completion-of-payment, she may not retire until 62 — six years *later* than the eligibility date
the purchase bought her. The two provisions handed to her in the same bill cancel out, and she
discovers it after signing.

**Suggested direction.** Tie the deadline to the date the purchase of service credit contract is
*entered into*, not completed; define the term; and say what happens on breach (the cleanest is that
credit vests only as paid under existing subsection F, so the rule needs no separate sanction — but
say so). Drafting Specialist.

#### S-3 — The PLOP analysis mis-describes § 51.1-165.01 B, and misses the channel through which the bill actually moves PLOP
*Category: citation integrity / unintended effect. Annex A § 5 PLOP row; clause 2 (v).*

Annex A § 5 states the PLOP test as "**Two independent gates**: creditable service *performed* after
the date first eligible for an unreduced allowance, **and** being 'in service' for 1, 2, or 3 full
years after January 1, 2001," and concludes that purchased service "cannot substitute for the
required actual service."

The statute's richest tier is **disjunctive** on the first prong:

> "Any retiring member who (i) has satisfied the requirements for normal retirement after January 1,
> 2004, **or** has been credited with at least three years of creditable service for service
> performed after the date he was first eligible for an unreduced service retirement allowance and
> (ii) was in service for at least three full years after January 1, 2001" — § 51.1-165.01 B.

Purchased military service **does** help a member "satisf[y] the requirements for normal retirement":
§ 51.1-153 A requires the normal retirement date plus five years of creditable service, and purchased
B 2 service is creditable service under § 51.1-124.3. So the first prong can be satisfied through the
disjunct without any post-eligibility *performed* service at all. Annex A's two-gate framing does not
describe the statute, and enactment clause 2 (v) does no work on this channel — the eligibility
*requirements* are indeed unaltered; what changes is the member's creditable service.

**Concrete failure scenario.** A veteran reaches Social Security retirement age with 3 years of
worked VRS service and buys 4 military years at approximate normal cost under the new carve-out. She
now holds 7 years of creditable service at her normal retirement date, satisfies § 51.1-153 A,
satisfies prong (i) by the disjunct and prong (ii) on her 3 worked years, and elects the maximum
three-year PLOP on a record in which more than half the service was purchased. Under current law
those 4 years would have been priced at actuarial equivalent cost. The package tells VRS counsel
that PLOP is reached only through acceleration of the clock; VRS counsel will find this route in an
afternoon, and will find it after the package asserted otherwise.

I did **not** verify whether the PLOP reduction to the ongoing allowance is actuarially equivalent,
so I am not asserting a fiscal consequence — only that the legal analysis is wrong and the fiscal
consequence is therefore unassessed. **Suggested direction:** rewrite the PLOP row to the statute's
actual structure, and add to Q6/Q7 whether the PLOP reduction factors are actuarially equivalent.
Statutory Researcher.

#### S-4 — "The strongest fiscal argument this proposal has" does not survive the package's own full basis
*Category: evidence integrity. Brief 01 lines 215, 217; one-pager lines 79–82; model FM-2.*

Brief 01: "The break-even clusters tightly at **age 47–48 in all three plans**. Below that age the
veteran subsidises the Fund. **That is the strongest fiscal argument this proposal has**, and it is
why the Hybrid per-member figure is only $6,779." The one-pager carries it as the explanation of why
per-member cost stays modest.

Those break-even figures (46.6 / 47.4 / 48.2) come from `breakeven_age()`, which calls
`aec_pct_of_salary()` — documented in the file as "counting the **BENEFIT-AMOUNT channel only** (not
eligibility acceleration)." The per-member figures they are offered to explain ($6,779 / $17,174 /
$47,967) come from `fm4_acceleration`, the **full** basis. The package's own correction notice says
acceleration is 20%–49% of the cost and that omitting it is what produced the discredited $2M
headline. The brief is using the superseded basis to explain the re-scoped number.

Re-run on the full basis, holding salary constant so the ratio is scale-free:

| plan | svc at 40 | break-even, benefit-amount only | break-even, FULL basis |
|---|---|---|---|
| Plan 1 | 5 / 10 / 15 / 20 | 46.6 | **none below age 60** |
| Plan 2 | 5 / 10 / 15 / 20 | 47.4 | **none below age 60** |
| Hybrid | 5 / 10 / 15 / 20 | 48.2 | **none below age 60** |

Spot check from the same run: a **Hybrid member at age 35** with 8 years pays $24,502 for 4 years and
receives $36,281 of value — the Fund is out **$11,779**, twelve years below the stated break-even.
The claim "below that age the veteran subsidises the Fund" is false on the package's own full basis
at every age I tested from 28 to 60.

**Concrete failure scenario.** A VRS actuary or a legislative fiscal analyst opens `fm_model.py`,
reads the `aec_pct_of_salary` docstring, and asks in open session why the brief's central fiscal
argument is computed on a channel the brief itself calls half the cost. There is no good answer.

**Counter-note, stated because honesty requires it.** The full basis assumes **every purchaser
retires at the earliest unreduced date**. That is an unstated load-bearing assumption and it pushes
cost *up*. A member who would have worked to 65 regardless collects no acceleration. If real
behaviour is partial, the full-basis figures are conservative and the true break-even sits between
the two columns above. The defect is that the package reports one basis for break-even and the other
for cost without reconciling them, and never names the behavioural assumption at all.

**Suggested direction.** Pick one basis and use it for both. If the full basis is kept, the brief's
"strongest fiscal argument" must be withdrawn and replaced with the argument that actually holds:
Hybrid per-member cost ($6,779) is an order of magnitude below Plan 1's, and Hybrid is 53% of actives
and 100% of future hires, so the bill's cost declines over time. That is defensible. Fiscal & Impact
Modeler and Editor. **Must appear in the memo's risk section.**

#### S-5 — Take-up (A-11): the published floor is drawn from the superseded band, and the assumption is biased in the one direction the bill is designed to cause
*Category: fiscal assumption. Annex B A-11; model FM-4 § 4.4; one-pager line 68.*

Two separate problems with the same assumption.

**(a) The floor is borrowed from a band the package retired.** The published headline is
"$13M–$182M." The $13.0M cell is **5% take-up on the low pool**, and the model labels that row
"Brief v1.0 low" — the Annex B A-11 band of 5%–15% that the re-scope superseded. The $182.2M ceiling
is from the model's *current* scenario set (High = 30%). The range therefore takes its floor from the
old assumption set and its ceiling from the new one. On the model's own current scenarios the range
is **$26.0M – $182.2M**: the floor doubles. Annex 2 Closure § 4.4 compounds it by calling the 5% row
"the honest headline."

**(b) Historical take-up is a downward-biased estimator of post-reform take-up.** The package's
justification for a low take-up assumption is that "prior-service purchase take-up is generally low
because members must fund it from pay." But the observed low take-up was produced under a regime
with (i) actuarial-equivalent pricing after 24 months, (ii) 6–12 month payment terms, and (iii) —
per the brief's own theory of the case — members who "never hear about it in time." **The bill
removes all three.** Using pre-reform behaviour to forecast post-reform behaviour, when the reform
targets precisely the frictions that suppressed the behaviour, is a selection error, and it is the
assumption most likely to be wrong in the direction that hurts. JLCVSO cannot simultaneously tell
legislators the bill will reach veterans who currently miss out and tell the money committees that
take-up will stay where it was.

**Alternate number, as required.** Scaling the team's own grid linearly in take-up:

| take-up | one-time PV (team's grid basis) |
|---|---|
| 5% (published floor, superseded band) | $13.0M – $30.4M |
| 10% (model's current "Low") | $26.0M – $60.7M |
| 20% ("Moderate") | $52.0M – $121.5M |
| 30% ("High", published ceiling) | $78.0M – $182.2M |
| **50%** (publicised, subsidised, payroll-deductible benefit, self-identified population) | **$130.0M – $303.7M** |

**Concrete failure scenario.** The bill passes with a fiscal note anchored on the 5% row. JLCVSO and
the VSOs run the outreach campaign the brief's own discussion section implies is needed. Take-up
lands at 35%. VRS books an unbudgeted employer-rate increase roughly eight times the noted figure,
and the 2031 General Assembly repeals or narrows the carve-out — with the veterans who bought in
year one keeping their credit and the rest losing the right. **Suggested direction:** restate the
published range as $26M–$182M on the current scenario set, state 50% as a stress case rather than
omitting it, and make item 5 of the § 1.7 data request a pre-filing blocker rather than a request.
Fiscal & Impact Modeler. **Must appear in the memo's risk section.**

#### S-6 — The new operative sentence reproduces the very pricing mismatch Annex A § 2.6 diagnoses
*Category: drafting. Annex A § 2.2, § 2.6, Q13.*

§ 2.6 establishes that the 10.01% alternate hazardous duty rate is "published as a stand-alone rate
**with no plan column at all**," so the statutory phrase "the approximate normal cost of **the
retirement plan** under which the member is covered" may not reach it. The draft's new operative
sentence then uses **that exact phrase**: "may purchase ... at the approximate normal cost of the
retirement plan under which the member is covered at the time of such purchase." The cure offered is
factor (v) of the schedule authority — but the schedule authority is **permissive** ("The Board
**may** ... determine"), while the pricing phrase is **mandatory**. A discretionary cure for a
mandatory defect is not a cure.

**Concrete failure scenario.** A deputy sheriff in a county that elected the alternate option, Plan 2,
past the window, applies on July 2, 2027 to buy three years. The Board has not yet adopted a
schedule. VRS must charge "the approximate normal cost of the retirement plan under which the member
is covered." There are three candidate rates — Plan 2 non-hazardous 10.74%, Plan 2 hazardous 19.15%,
and the plan-less alternate-option 10.01% — and the statute selects none of them. VRS either guesses,
holds the application, or denies it. The pre-existing ambiguity § 2.6 decided to leave alone for
subdivision B 1 has been imported into the one sentence that is supposed to be the operative grant
for B 2.

**Suggested direction.** In the new sentence, say "at the approximate normal cost applicable to the
member as determined by the Board" rather than re-using the plan-indexed phrase. That cures it for
B 2 without touching B 1 and without enlarging the bill — which is what § 2.6 says it wants. Fold
into Q13. Drafting Specialist.

#### S-7 — The health insurance credit exposure is analysed under the state-employee section only, for an all-members bill
*Category: citation integrity / scope. Annex A § 5 HIC row; brief 01 line 225; Annex 2 Closure § 4.9.*

Every HIC reference in the package cites **§ 51.1-1400** — "Health insurance credits for retired
**state employees**." The bill's scope, per the October 24 decision, is all VRS members. Chapter 14
places teachers under **§ 51.1-1401** and local government employees under **§ 51.1-1402**; neither
is cited anywhere in the package. Teachers are the largest employer group (160,800 actives, 42.5% of
all actives, $11.7bn of covered payroll) and the largest single bucket in the who-bears table.

I verified § 51.1-1400 A and D: the 15-year total-creditable-service threshold and the $4.25
per-year amount are correct as stated, and subsection D does require VRS to reflect HIC cost in the
§ 51.1-145 employer rate. So the row's *analysis* is right; its *scope* is wrong, and it is wrong in
exactly the way that produced the discredited "under $2 million" headline.

**Concrete failure scenario.** VRS prices the HIC step-function effect across all three chapter-14
regimes and reports a figure for teachers that JLCVSO has never seen, in the official § 30-19.1:7
statement, after telling the Commission on Local Government and the money committees that the HIC
impact was identified and flagged. **Suggested direction:** cite §§ 51.1-1400, 51.1-1401 and
51.1-1402; confirm whether the local credit under § 51.1-1402 is employer-elective (I did not
verify this) and what that does to the local bearer column; re-scope Q2 to all three. Statutory
Researcher and Fiscal & Impact Modeler.

#### S-8 — The HB 1867 cross-check does not say what the one-pager says it says
*Category: evidence integrity. One-pager lines 74–77; model FM-4 § 4.6.*

The one-pager closes with: "VRS's own impact statement found **$10,000 to $60,000** of unfunded
liability per participating member. Our veterans still pay — so this bill costs the Fund **less per
member** than the one VRS already scored: **$6,800 to $48,000**, depending on plan."

The model's own output is explicit that this is not what it found:

```
Plan 1   modelled A-3 net PV/member   $47,967  INSIDE the HB 1867 band
Plan 2   modelled A-3 net PV/member   $17,174  INSIDE the HB 1867 band
Hybrid   modelled A-3 net PV/member    $6,779  outside the HB 1867 band (lower ...)
```

Two of the three plans sit **inside** the band, not below it. $48,000 against a band of
$10,000–$60,000 does not support "less per member." And HB 1867 was a **free** grant to **teachers
only**, so the plan mix is not comparable in the first place. The comparison is being used as the
closer on the printed leave-behind, and it is the one claim on the page that an opponent can refute
using the patron's own model output.

**Concrete failure scenario.** A committee member asks: "Your own model says Plan 1 costs $47,967,
and you're comparing it to a band topping out at $60,000 for a bill that gave the service away
free — how is a priced purchase costing almost as much as a free grant?" There is a real answer
(plan mix, Plan 1 is closed), but it is not on the page, and the question lands as a caught error
rather than an explained nuance.

**Suggested direction.** State it the way the model states it: "A priced purchase should sit below a
free grant, and for Hybrid members — everyone hired since 2014 — it does, at $6,800 against VRS's
$10,000–$60,000. For the closed Plan 1 cohort it sits inside VRS's band." That is both true and
still favourable. Editor. **Must appear in the memo's risk section.**

---

### MODERATE

#### M-1 — § 30-19.03 is missing: the Commission on Local Government must prepare its own estimate
*Category: procedure. Annex A § 4, § 7 Q10; brief 01 line 297.*

The package treats the Commission on Local Government solely as a *recipient* of the VRS Board's
§ 30-19.1:7 statement. § 30-19.03 independently requires that whenever a bill requires "net
additional expenditure by any county, city, or town," "the Commission on Local Government shall
investigate and prepare an estimate" and forward it to the Clerk of the House for distribution to
patrons and committee chairs. On the package's own numbers the bill imposes $23.4M–$45.2M of present
value on political subdivisions at 20% take-up. So there will be **two** adverse local statements,
from two bodies, on two authorities — and only one is anticipated anywhere in the package.

**Failure scenario:** JLCVSO prepares a response to the § 30-19.1:7 statement and is surprised in
committee by a separate CLG local fiscal estimate it did not know was coming, on a bill whose
headline is "$0." **Fix:** add § 30-19.03 to Annex A § 4 and to the pre-filing checklist; pre-brief
CLG staff alongside VRS staff. Statutory Researcher and Stakeholder Analyst.

#### M-2 — Striking enactment clause 3, as the drafting note invites, removes the bill's only link to constitutionally adequate funding
*Category: constitutional. Annex A § 2.4 drafting note 2, Q8.*

Annex A's drafting note says clause 3 "may be redundant; if it is, strike it rather than risk
implying a new funding mechanism," and Q8 asks Legislative Services whether it is "necessary,
redundant, or affirmatively undesirable." That framing is backwards. **Va. Const. art. X, § 11**
requires that retirement benefits "be funded through methods which are consistent with generally
accepted actuarial principles." This bill *mandates* the sale of service credit below actuarial value.
Enactment clause 3 — directing VRS to reflect the cost in the § 51.1-145 employer rate — is the only
text in the bill tying the new below-cost pricing to an actuarially sound funding method. Striking it
does not make the bill cleaner; it removes the answer to the one constitutional question the bill
raises.

**Failure scenario:** Legislative Services takes the note's invitation and strikes clause 3 as
surplusage. The bill passes. A VRS retiree or non-veteran active member files in the Circuit Court of
the City of Richmond pleading art. X, § 11 — that the General Assembly mandated a below-cost benefit
with no funding method, and that the Board's adoption of a knowingly below-cost schedule is not
administration "solely in the interests of the members and beneficiaries thereof." The merits are
weak (veterans are members; the General Assembly may prescribe "restrictions, terms, and
conditions"), but the claim survives a demurrer and the bill spends two years under a cloud.

**Fix:** invert Q8 — ask Legislative Services to confirm clause 3 is *sufficient*, not whether it is
necessary. Add art. X, § 11 to Annex A's constitutional analysis, which currently addresses only age
discrimination. Drafting Specialist and Statutory Researcher.

#### M-3 — Factor (ii) grades on a proxy that is non-monotonic in the exposure it exists to price
*Category: fiscal / drafting. Annex A § 2.2 factor (ii); § 5.1.*

Factor (ii) permits grading on "the period remaining until the date on which the member would first
become eligible for an unreduced service retirement allowance." The exposure it is meant to recover
is retirement-date acceleration, and acceleration is not distance — it is
`min(distance, years purchased × advance rate)`. For Plan 1 the advance rate is 1.0, so **every**
member more than four years from eligibility who buys four years receives exactly 4.00 years of
acceleration.

Run on the team's own `unreduced_age()`: a Plan 1 member at **age 42 with 16 years** is 14 years from
eligibility; a Plan 1 member at **age 52 with 26 years** is 4 years from eligibility. Both accelerate
**exactly 4.00 years**. A schedule graded on distance puts them in different classes at different
rates for identical acceleration. (The discounted *value* of the younger member's acceleration is
lower — $32,315 against $100,753 — so a distance-graded rate is not simply wrong, but it is not
pricing acceleration either, and the package asserts that it is.)

The draft also does not say **when** distance is measured — before the purchase or after. For the
age-52 member the two readings are 4 years and 0 years, which could put him in the cheapest or the
dearest class in the schedule.

**Fix:** either specify "determined without regard to the service credit to be purchased," or drop
the distance formulation and rely on "age and creditable service," which is what the brief and the
one-pager already describe. Drafting Specialist; Fiscal & Impact Modeler to confirm which proxy the
§ 4.8 arithmetic actually supports.

#### M-4 — The eligible pool is derived two ways and the package quotes whichever is convenient
*Category: internal consistency. Model FM-1 vs FM-4 § 4.7; Annex A § 5.1.*

`fm_model.py` produces two pools for the same population: **10,561 – 26,321** by plan (used in the
headline take-up grid and quoted on the one-pager as "10,600 to 26,300") and **11,565 – 24,036** by
employer group (used in the who-bears table and in the guardrail dials). The high ends differ by
2,285 members, about 10%. Consequently Annex A § 5.1's guardrail arithmetic — "$57.0M → $48.6M,"
"$57.0M → $28.5M" — is the **low-pool end of the group derivation**, presented without qualification
as "the modelled exposure," against a published ceiling of $182M from the plan derivation. The
guardrails are being asked to carry a number about a third of the exposure the same package
advertises.

**Fix:** reconcile to one derivation, or state the guardrail dials at both pool ends ($57.0M–$118.4M
at 0% recovery). Fiscal & Impact Modeler.

#### M-5 — "Any member in service may purchase" is a new undefined phrase, in a sentence framed as a grant of eligibility rather than a pricing rule
*Category: drafting / term discipline. Annex A § 2.2; § 3 term table.*

Annex A § 3 is scrupulous about terms and states flatly: "**No new defined term is created.**" The
draft then introduces "**in service**," which appears nowhere else in § 51.1-142.2 — the paragraph
uses "**active service**" — and which Annex A § 5's own PLOP row treats as carrying independent
meaning under § 51.1-165.01 B. The term table lists "active service" and does not list "in service."

Worse, the sentence is structured as a **grant of authority to purchase** ("Any member in service
**may purchase** service credit for prior active duty military service pursuant to subdivision 2 at
the approximate normal cost ...") rather than as a pricing rule. All three "locks" Annex A § 2.5
relies on address whether the *schedule* spills into subdivision B 1; none addresses whether this
freestanding permission sentence alters *who* may purchase under B 2. The phrase "pursuant to
subdivision 2" is carrying the whole weight of importing B 2's conditions, including the
not-dishonourably-discharged condition, which Annex A never lists among the things to preserve.

The phrase also creates a gap at the boundary the draft was trying to close: a member on an approved
leave of absence is a member, but is she "in service"? The sentence disclaims the leave-of-absence
start point in the same breath.

**Fix:** reframe as pricing — "Service credit purchased pursuant to subdivision 2 shall be purchased
at the approximate normal cost ..., without regard to the time elapsed since ..." — which needs no
eligibility language at all. Drafting Specialist.

#### M-6 — Does subdivision B 2 even reach service performed while a member? The one-pager says "every veteran in VRS"
*Category: scope / messaging. § 51.1-124.3; Annex A § 5 subsection I row; one-pager line 54.*

§ 51.1-124.3 defines "prior service" as "service rendered **prior to becoming a member** of the
Retirement System," and Annex A § 3 itself places military service in that bucket. Subdivision B 2
is "**prior** active duty military service." On that reading, a member who took military leave from a
covered position and failed subsection I's one-year reentry condition cannot buy that service under
B 2 at all — at any price, under current law or under the bill. Annex A § 5 correctly says subsection
I serves "a different population" and leaves it alone, but never notices that the bill therefore does
nothing for that population. The one-pager's "**Who it helps:** every veteran in VRS" overclaims
against this gap.

**Fix:** add to Q7 — does VRS administer B 2 as reaching only pre-membership service? If so, say so
in the brief and stop saying "every veteran." Statutory Researcher; Editor.

---

### MINOR

#### Mi-1 — Enactment clause 4 is surplusage
**Va. Const. art. IV, § 13:** laws enacted at a regular session "shall take effect on the first day
of July following the adjournment," absent an earlier emergency date or a later date in the bill. For
a 2027 regular-session bill, July 1, 2027 **is** the default. Clause 4 states the default and thereby
invites the question of what else was intended. Strike it, or keep it and expect a drafting query.

#### Mi-2 — The title does not name the payment-agreement change
**Va. Const. art. IV, § 12:** "No law shall embrace more than one object, which shall be expressed in
its title." The title is "...; purchase of prior service credit; prior active duty military service;
cost." The bill also amends subsection F to authorise 60-month payment agreements and authorises a
pre-retirement completion deadline — timing and payment, not cost. Virginia courts construe the title
requirement liberally and I rate the risk low; I did not re-check case law for a minor point. The fix
is one word: add "payment" or "purchase of service credit contracts" to the title.

---

## 3. Citation verification

I re-opened the primary sources rather than the package's descriptions of them.

| Claim and where it appears | Source checked | Result |
|---|---|---|
| Purchased B 2 service is already "creditable service," so no benefit rule changes — Annex A § 3, § 5 (the hinge of the whole package) | § 51.1-124.3 | **HOLDS, verbatim.** "Creditable service" = "prior service as set forth in § 51.1-142.2 plus membership service for which credit is allowable." "Prior service" = "service rendered prior to becoming a member." The premise is correct and the term discipline in § 3 is sound. See M-6 for the one edge it does not cover. |
| The 24-month sentence reaches both subdivision B 1 and B 2 and must be carved out by express cross-reference — Annex A § 4, § 8 point 1 | § 51.1-142.2 B 3 | **HOLDS.** The sentence refers to "the service made available in this subsection." The draft's targeted carve-out is the right technique. |
| Both start points (first date of hire; final day of leave of absence) — Annex A § 8 point 2 | § 51.1-142.2 B 3 | **HOLDS, verbatim.** |
| The "inactive periods" sentence survives for B 1 — Annex A § 2.2 drafting note | § 51.1-142.2 B 3 | **HOLDS.** It sits immediately after the 24-month trigger in the statute, so "the preceding sentence" in the draft refers correctly to the trigger at the drafted insertion point. |
| The anti-duplication sentence and the 10 U.S.C. ch. 1223 exception — Annex A § 4, § 8 point 7, clause 2 (vi) | § 51.1-142.2 B 3 | **DOES NOT HOLD as described.** The statute has a second limb — "or if there is a balance in a defined contribution account that serves as a primary retirement account related to such service" — that Annex A never mentions and clause 2 (vi) omits. See **S-1**. |
| "active duty military service" = full-time service of at least 180 consecutive days — Annex A § 3, § 8 point 9 | § 51.1-142.2 B 3 final para. | **HOLDS.** |
| Subsection E carries identical 24-month language and is independent — Annex A § 4, § 8 point 8 | § 51.1-142.2 E | **HOLDS.** Workers' compensation, different population, untouched by the draft. |
| Subsection I serves a different population (leave from a covered position, reentry within one year) — Annex A § 5, § 8 point 10 | § 51.1-142.2 I | **HOLDS.** |
| Subsection F: current payment mechanics — Annex A § 2.3, § 4 | § 51.1-142.2 F | **HOLDS, and adds a problem.** F provides credit for "the number of full or partial months of service for which full payment has been made," which is what makes "completed" ambiguous in the new 12-month rule. See **S-2**. |
| PLOP: "two independent gates," purchased service cannot substitute — Annex A § 5 | § 51.1-165.01 B | **DOES NOT HOLD.** The first prong of the three-year tier is disjunctive: "has satisfied the requirements for normal retirement after January 1, 2004, **or** has been credited with at least three years ... for service performed after ..." See **S-3**. |
| HIC: 15-year total creditable service threshold; $4.25/month per year; § 51.1-145 funding — Annex A § 5, brief 01 | § 51.1-1400 A, D | **HOLDS on the merits, FAILS on scope.** § 51.1-1400 covers retired **state employees**. Teachers are § 51.1-1401 and local government employees § 51.1-1402; neither is cited. See **S-7**. |
| Unreduced-retirement pathways; Rule of 90 adds one service point per purchased year — Annex A § 3.1 | § 51.1-124.3 ("normal retirement date"), § 51.1-153 | **HOLDS.** Normal retirement date is the 65th birthday, or Social Security retirement age for post-July 1, 2010 members / those lacking 60 months at January 1, 2013. § 3.1's caution against collapsing this to "30 years" is correct and should be kept. |
| § 30-19.1:7 VRS Board impact statement — Annex A § 4 | § 30-19.1:7 | **HOLDS**, but incomplete as a procedural picture. **§ 30-19.03 is omitted entirely.** See **M-1**. |
| Constitutional analysis — Annex A § 2.5, Q14 (age discrimination only) | Va. Const. art. X, § 11; art. IV, §§ 12, 13 | **INCOMPLETE.** Art. X, § 11's actuarial-funding and sole-interest duties are unaddressed (**M-2**); art. IV, § 13 makes clause 4 surplusage (**Mi-1**); art. IV, § 12 title point (**Mi-2**). |
| DHRM's 6% veteran share corroborated at 5.75% from BLS Table 8 | `fm_model.py` `derive_sl_gov_veteran_share()` | **HOLDS.** 7,893 × 12.9% = 1,018k; 153,213 × 10.9% = 16,700k; 1,018 / 17,718 = 5.75%. Arithmetic reproduces. |
| "5 to 68 cents out of every $100 of VRS covered payroll ($26.8 billion)" | `fm_model.py` payroll table | **HOLDS.** $13.00M / $26.763bn = 0.049%; $182.22M / $26.763bn = 0.681%. |

---

## 4. Fiscal assumption challenge

**The load-bearing assumption is not A-11.** Take-up scales the answer; it does not decide whether
there is an answer. The assumption that decides the package's *conclusion* is the one in
`price_threshold_graded()`: that the Board can recover 100% of the above-ANC excess through the
authority the draft grants. Everything the package says to the money committees — "actuarially
neutral by construction," "the fiscal note is zero," "the single most powerful cost control
available," "offer it to the money committees first" — rests on that one function.

**Test.** Re-ran `fm4_acceleration` over classes as fine as the draft's own five factors permit, and
imposed the draft's own two constraints (uniformity within classification; payment not exceeding the
member's actuarial equivalent cost) on the resulting rate.

**Result.** The 100% dial recovers **25% to 73%** of the above-ANC excess, not 100%, and **25%** in
the Plan 1 age 55–59 / 20–29 years class that dominates the exposure. The $0 fiscal note is not
reachable at any lawful setting of a uniform published schedule. Full table at **F-1**.

**Secondary test — take-up (A-11), as the issue directs.** Two findings: the published $13M floor is
taken from the superseded 5%–15% band rather than the model's current scenario set (correct floor:
**$26.0M**), and pre-reform take-up is a downward-biased estimator of post-reform take-up because
the bill removes all three frictions that suppressed it. At 50% take-up the modelled range is
**$130.0M – $303.7M**. Full table at **S-5**.

**Tertiary test — break-even.** The full-basis break-even is below none of the ages tested (28–60),
against the published 46.6 / 47.4 / 48.2. Full table at **S-4**.

**Direction of the remaining errors.** Everything the package leaves unpriced pushes **up**: the
health insurance credit and its 15-year step across all three chapter-14 regimes; adverse selection;
the early-retirement reduction subsidy (which the model's caveat 3 correctly identifies as making
acceleration a floor, on VRS's own June 17, 2026 statement to its Benefits & Actuarial Committee);
VRS administrative cost; and the PLOP channel at **S-3**. The only assumption pushing **down** is the
unstated behavioural one at **S-4**: FM-4 assumes every purchaser retires at the earliest unreduced
date. That assumption should be named in Annex B's register — it is currently nowhere — because it is
the package's best honest answer to an actuary who says the numbers are too high.

---

## 5. Draft text defects, clause by clause

| Clause | Defect | Finding |
|---|---|---|
| § 2.2, sentence 1 ("The preceding sentence shall not apply...") | None. Correctly targeted; "the preceding sentence" resolves to the 24-month trigger at the drafted insertion point. | — sound |
| § 2.2, sentence 2 ("Any member in service may purchase...") | New undefined term "in service"; framed as a grant of eligibility, not a pricing rule; leaves a member on leave of absence in doubt | M-5 |
| § 2.2, sentence 2 ("...approximate normal cost of the retirement plan under which the member is covered") | Re-uses the plan-indexed phrase § 2.6 diagnoses as not reaching the 10.01% alternate option; cured only by a permissive factor | S-6 |
| § 2.2, sentence 3, factor (i) (attained age) | None | — sound |
| § 2.2, sentence 3, factor (ii) (creditable service / period remaining / or both) | Non-monotonic proxy for acceleration; measurement point (pre- or post-purchase) unspecified; two factors in one clause | M-3 |
| § 2.2, sentence 3, factors (iii), (iv) | None | — sound |
| § 2.2, sentence 3, factor (v) (position type, § 51.1-138 benefits) | Sound as drafted; the § 51.1-169 A borrowing is well chosen. But it is permissive and is being asked to cure a mandatory defect | S-6 |
| § 2.2, sentence 4 (publication; uniformity; AEC ceiling) | Uniformity and the individual-AEC ceiling are not simultaneously satisfiable in a non-trivial way. Either the ceiling forces the rate to the class minimum (uniformity survives, the dial dies) or "actuarial equivalent cost" means the Board's own class figure (the dial survives, the ceiling is self-referential and unenforceable) | **F-1** |
| § 2.2, sentence 5 (no spillover to other purchases) | None. This lock is real and does close the gap § 2.5 describes | — sound |
| § 2.2, sentence 6 (12-month pre-retirement completion) | "Completed" undefined; retirement date unknowable at purchase; no remedy for breach; collides with the 60-month term | S-2 |
| § 2.2, final sentence (inactive periods), retained | None. Correctly left to govern B 1 | — sound |
| § 2.3 (subsection F, 60-month agreements) | Sound in itself, including the "notwithstanding ... any policy of the Board" override, which § 8 point 3 correctly identifies as necessary. Collides with § 2.2 sentence 6 | S-2 |
| Clause 2 (i), (ii) (four-year caps) | None. Both caps preserved separately, as § 8 point 6 requires | — sound |
| Clause 2 (iii) (subsections C, D, E, H) | None | — sound |
| Clause 2 (iv) (subsection I) | None | — sound |
| Clause 2 (v) (PLOP) | Does no work on the channel that matters, and the negative inference cuts against veterans: a reader could conclude the General Assembly meant purchased service not to affect PLOP timing at all, reducing a right members hold today | S-3 |
| Clause 2 (vi) (anti-duplication) | Incomplete restatement; omits the defined-contribution-balance limb | S-1 |
| Clause 3 (§ 51.1-145 employer rates) | Sound and **necessary** — the drafting note's invitation to strike it is the defect | M-2 |
| Clause 4 (effective July 1, 2027) | Surplusage under art. IV, § 13 | Mi-1 |
| § 2.1 (title) | Does not name the payment-agreement change | Mi-2 |

---

## 6. Verdict by dimension, as the issue requires

| # | Dimension | Verdict |
|---|---|---|
| 1 | **Legal fit** — does § 2.2 confine the carve-out to B 2 without repricing B 1; are subsection E, subsection I, the anti-duplication sentence, the ch. 1223 exception, the 180-day definition and both four-year caps intact; every § 8 point | **PASS with two serious defects.** All ten § 8 drafting points are executed, and I verified each against the statute: the carve-out is keyed to subdivision 2 by express cross-reference; both start points are disclaimed; the 60-month authority is in statute; the schedule authority is express; the 12-month rule is permissive; both four-year caps, subsection E, subsection I and the 180-day definition are untouched; the no-spillover lock in § 2.2 sentence 5 is real. **But** the anti-duplication provision is incompletely restated in clause 2 (vi) (**S-1**) and the operative sentence reproduces the alternate-option pricing mismatch (**S-6**). |
| 2 | **Term discipline** — is purchased military service already "creditable service" under § 51.1-124.3, so that no benefit rule changes | **PASS. I attacked this hard and it holds.** § 51.1-124.3 verbatim: "prior service as set forth in § 51.1-142.2 plus membership service for which credit is allowable." B 2 service is granted under § 51.1-142.2, so it is already creditable service for every Title 51.1 purpose. § 3's refusal to use "earned service" and "benefit-calculation service," and § 3.1's refusal to collapse unreduced retirement to "30 years," are both correct and should be defended against any drafter who wants to tidy them. Two qualifications, neither fatal: the new sentence introduces "in service" and so does create a new undefined phrase, against § 3's claim that none is created (**M-5**); and the "prior" in "prior active duty military service" may exclude service performed while a member (**M-6**). |
| 3 | **Unintended effects** — re-run the § 5 matrix; stress-test PLOP and the HIC 15-year step | **FAIL on two rows of twenty.** Eighteen rows of the § 5 matrix are correct and I re-derived them: AFC genuinely is not affected (purchase payments are not creditable compensation); group life genuinely is not affected; the Hybrid disability row is right and is the dominant forward case; the Rule-of-90 "one service point and nothing more" caution is right; the § 51.1-166 D 4 twenty-year note is right; the refund option value is correctly identified as pre-existing and minor. **The PLOP row mis-states § 51.1-165.01 B (S-3)** and **the HIC row is scoped to state employees for an all-members bill (S-7)**. The hazardous-duty row correctly refuses to extrapolate, which is the right call. |
| 4 | **Fiscal uncertainty** — where is it most likely wrong, and in which direction; attack A-11 and the § 5.1 adverse-selection mitigation | **FAIL.** The mitigation does not work as drafted (**F-1**) — this is the most serious finding in the review. A-11's floor is borrowed from a superseded band and the assumption is biased downward by construction (**S-5**). The break-even argument is computed on the wrong channel (**S-4**). Every unpriced item pushes cost up; one unnamed behavioural assumption pushes it down and should be named. Model reproducibility itself is **excellent** — `fm_model.py` runs clean, tags every input, and reproduces every published figure. |
| 5 | **Administration** — can VRS implement an age-graded schedule and 60-month agreements without further legislation | **PASS on the 60-month term, QUALIFIED on the schedule.** § 2.3's "notwithstanding ... any policy of the Board limiting the duration" is the right technique and § 8 point 3 is correct that Board policy would otherwise survive. The schedule authority is express and sufficient to adopt *a* schedule without a second bill. But VRS cannot adopt a schedule that does what the fiscal case claims (**F-1**), and for an alternate-option member VRS may be unable to determine a price at all until the Board acts (**S-6**). |
| 6 | **Equity** — any new inequity between state and local, between plan cohorts, between hazardous and non-hazardous, between veterans and non-veterans | **QUALIFIED PASS — no new legal inequity, one serious political one.** State/local: the all-members scope avoids the inequity option (b) would have created; localities bear cost without a vote, which is an employer grievance, not an employee one, and § 30-19.03 is the channel for it (**M-1**). Hazardous/non-hazardous: a VaLORS Plan 2 veteran pays 19.15% — nearly double the one-pager's unlabelled $18,666 (**M-7**, below) — and the net direction for SPORS/VaLORS is genuinely unknown, which § 4.7 says honestly. Veterans/non-veterans: rational basis is easily met given Virginia's established veterans preference, and I record **no constitutional finding**; but Annex A § 5's own rationale for the line — "[k]eeps the bill narrow and the fiscal note small" — is a budget rationale, and it is the opposition's best line (see § 1, paragraph four). **Plan cohorts is the real inequity:** the same bill delivers $47,967 of value to a Plan 1 veteran and $6,779 to a Hybrid one, and Plan 1 is a closed cohort while Hybrid is every future hire. Under the 100% dial that the money committees are promised, the Plan 1 veterans the one-pager leads with pay the most and net the least. The bill sold to veterans and the bill sold to the money committees are different bills. |
| 7 | **Stakeholder opposition and messaging vulnerability** — strongest argument against, and does the package answer it | **FAIL.** The strongest argument is not fiscal and not legal; it is that the two cost-control promises are mutually exclusive (§ 1, paragraph three = **F-1**). The package does not answer it, does not acknowledge it, and hands over the material to prove it in `fm_model.py`. Three further messaging vulnerabilities are live on the **printed** leave-behind: the $0 general fund claim (**F-2**), the HB 1867 comparison (**S-8**), and the unlabelled $18,666 (**M-7**). |
| 8 | **Missing evidence** — what load-bearing claim lacks a primary source | **Four.** (a) No VRS actuarial figure for anything — correctly and repeatedly disclosed, and not a finding. (b) **A-11 take-up has no source at all**; it is labelled "Judgment" in Annex B and drives the headline (**S-5**). (c) **The recoverability of the above-ANC excess through a published class rate has no source and no model** — it is asserted, and the one model that addresses it prices individuals (**F-1**). (d) **The statutory authority for a political subdivision to elect the alternate hazardous duty option is still unidentified** — Annex A § 2.6 flags this honestly as "one citation gap to close before filing," and factor (v) should not be finalised until it is closed (Q13). |

#### M-7 — The one-pager's affordability figure is the cheapest plan's price, unlabelled, next to a population headline about the dearest plan
*Category: messaging. One-pager lines 40, 56; brief 01 line 59.*

Brief 01 labels it properly: "Hybrid Retirement Plan (most members hired since Jan. 1, 2014) | 6.68%
of salary | **$18,666**." The one-pager drops the label — "Four years of credit costs about
**$18,666**" — and six lines later leads the population claim with "**All 110,474 active Plan 1
members** are already past the deadline." A Plan 1 member pays 12.50%, so the same four years costs
**$34,933** at the same $69,865 salary — 87% more. A VaLORS Plan 1 hazardous-duty member pays
23.78%: **$66,453**. **Fix:** label it, or give the range. Editor.

---

## 7. What I checked and found sound — explicitly

These are not omissions. I looked for a problem in each and did not find one worth reporting.

- **The § 51.1-124.3 creditable-service premise.** Verified verbatim. The hinge of the package holds,
  and it is the single best thing about this proposal: it is why there are no benefit-rule changes to
  argue about. Eighteen of the twenty rows in the § 5 unintended-effects matrix follow correctly from
  it and I re-derived them.
- **The targeted-cross-reference technique.** Annex A § 4's identification of the shared 24-month
  sentence as "the single most important drafting point," and § 8 point 1's insistence on a
  cross-reference rather than deletion, are correct and well executed. A drafter who "simplified"
  this would silently reprice every category in subdivision B 1.
- **The no-spillover lock in § 2.2 sentence 5.** New in v1.1 and genuinely necessary. The gap § 2.5
  describes — that a graded schedule adopted as *the plan's* approximate normal cost could have been
  argued to reprice B 1 through the generic opening phrase — was real, and this sentence closes it.
- **Nondelegation.** No finding. § 51.1-142.2 B 3 **already** commits approximate normal cost to "the
  Board in its sole discretion" with no standards at all. The draft *adds* a closed list of five
  factors, a publication requirement, a uniformity requirement and a cost ceiling. Delegation risk
  goes **down**, not up. § 8 point 4's rationale is sound.
- **Dillon's Rule.** No finding. The bill grants no local power and imposes no local duty requiring a
  grant; local exposure arrives through § 51.1-145 employer rates, which are state-set. The local
  issue here is fiscal procedure (**M-1**), not local authority.
- **Special legislation, Va. Const. art. IV, § 14.** No finding. The classification is general across
  all VRS members who hold qualifying service, and Virginia's established veterans preference
  (§ 2.2-2903) supplies ample rational basis.
- **Federal preemption, both directions.** No finding. The existing 10 U.S.C. ch. 1223 exception is
  preserved and does the work; USERRA is not disturbed. Q7 is the right question to ask anyway.
- **Age discrimination (Q14).** I agree with counsel's expectation and record no finding. The
  statutory alternative the bill displaces — actuarial equivalent cost — is itself a function of age
  and service, and grading on service reduces reliance on age. § 2.5's reasoning on this is correct.
- **Model reproducibility.** `fm_model.py` runs clean (exit 0) from a cold checkout, tags every input
  OFFICIAL / DERIVED / ESTIMATE, and reproduces every figure in Annex 2 Closure § 4 and brief 01's
  grid. I spot-checked the BLS 5.75% derivation, the payroll-share arithmetic and the HB 1867
  comparison and all three tie out. The five caveats at the foot of the output are honest and, in the
  case of caveat 3, more candid than most official notes. **This is the best-documented artefact in
  the package and it is what made this review possible.** My findings at F-1, S-4 and S-8 are all
  drawn from it — the model does not hide any of them; the prose built on it does.
- **The $2M correction.** Disclosing the ninety-fold revision in the brief's own voice (line 137) was
  the right call and I would not reverse it, notwithstanding that the opposition will use it (§ 1,
  paragraph one). Burying it would have been worse.
- **§ 3.1's treatment of unreduced retirement.** The refusal to collapse three statutory pathways
  into "30 years," and the note that purchased service never makes a member chronologically older,
  are both right and both load-bearing. Keep them against editorial pressure to shorten.

---

## 8. Findings the memo's risk section must carry

Marked for Editor: **F-1, F-2, S-1, S-4, S-5, S-8.** F-1 and F-2 are not risk-section items only —
they are reasons not to file and not to print until resolved.

## 9. Routing

| Owner | Findings |
|---|---|
| **Policy Director** | F-1, F-2 — both require a decision, not a drafting fix. Whether to proceed despite any finding is yours. |
| **Drafting Specialist** | S-1, S-2, S-6, M-2, M-3, M-5, Mi-1, Mi-2 |
| **Fiscal & Impact Modeler** | F-1 (re-stated recovery band), S-4, S-5, M-4; name the retire-at-earliest-date assumption in Annex B's register |
| **Statutory Researcher** | S-1 (BRS/TSP question), S-3, S-7, M-1, M-6; add art. X § 11 to the constitutional analysis |
| **Stakeholder Analyst** | M-1 — the Commission on Local Government is a second adverse statement, not just a recipient. Also unmapped and bearing real cost: school divisions (SOQ-shared, $13M–$33M) and non-veteran VRS members/retirees, who are the only plausible plaintiffs on the art. X § 11 theory at M-2. |
| **Editor** | F-2, S-4, S-5, S-8, M-6, M-7; risk-section list at § 8 |

---

*Internal risk analysis for JLCVSO and the Virginia Policy Lab. Pre-decisional. Not legal advice and
not a clearance by counsel. Reviewer's working file: `rt_check.py`, run against an unmodified
`models/fm_model.py` — no file in the package was altered by this review.*
