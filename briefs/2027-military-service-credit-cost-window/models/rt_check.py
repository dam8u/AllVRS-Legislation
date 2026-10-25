#!/usr/bin/env python3
"""Red-team re-runs of the team's model. Imports fm_model unchanged; adds nothing
to it. Four tests:
  T1  full-basis break-even age (benefit amount + acceleration), vs the 46.6/47.4/48.2
      figures the brief reports from the benefit-amount channel only
  T2  the early-purchase evasion of Guardrail A-prime
  T3  take-up: the published range floor vs the model's own current scenario set,
      and the cost at higher take-up
  T4  the uniformity + AEC-ceiling constraint in the draft: what a UNIFORM class
      rate can actually recover when the statute forbids charging any member more
      than that member's own actuarial equivalent cost

HISTORICAL FILE — DO NOT QUOTE ITS FIGURES AS CURRENT.  Note added October 25,
2026 in the MOO-301 reconciliation pass.  This is the red team's working file as
run on October 24, 2026, and it is deliberately left on the state of the model
it was reviewing: T3 hardcodes the by-plan pool at 10,561 - 26,321 and prints
"Published headline: $13M - $182M".  Both are RETRACTED.  They are kept here
because this file is the evidence for findings S-3 and S-5, and rewriting it
would destroy the record of what the reviewer actually ran.

The current figures, and where they come from:
  eligible pool      11,565 - 24,036, one pool on both derivations
                     (fm_model.fm1_pool_by_plan(), after the S-3 pairing fix)
  publishable band   $28M - $166M, the 10%-30% scenario set
                     (fm_model.py section 3; authority is 00-ONE-PAGE-BRIEF.md)
"""
import sys, statistics
sys.path.insert(0, __import__("os").path.dirname(__file__) or ".")
import fm_model as M

L = lambda s="": print(s)

L("=" * 78)
L("T1  FULL-BASIS BREAK-EVEN AGE  (acceleration included)")
L("=" * 78)
L("Brief 01 line 215/217 and model FM-2 report break-even 46.6 / 47.4 / 48.2 and")
L("say 'below that age the veteran subsidises the Fund'. That is the")
L("benefit-amount channel only. Re-run with FM-4's own full basis:")
L()
L(f"{'plan':8} {'age':>4} {'svc':>5} {'ANC price':>11} {'full value':>11} {'net to Fund':>12}")
for plan, svcs in (("Plan 1", (10, 20, 25)), ("Plan 2", (10, 14, 20)), ("Hybrid", (5, 8, 12))):
    for age in (35, 40, 42, 45, 48, 50):
        svc = svcs[1]
        p = M.Profile(plan, age, float(svc), 91_700.0, 45_000.0, age - svc)
        r = M.fm4_acceleration(p, years_purchased=4.0)
        price = M.price_a3_anc(p, years=4.0)
        L(f"{plan:8} {age:>4} {svc:>5} {M.money(price):>11} "
          f"{M.money(r['cost_total']):>11} {M.money(r['cost_total']-price):>12}")
    L()


def full_breakeven(plan, svc_at_age40, years=4.0, salary=91_700.0):
    """Purchase age at which full-basis value == ANC price. Service grows 1/yr."""
    prev = None
    for i in range(int((60 - 28) * 20) + 1):
        age = 28 + i / 20
        svc = max(0.0, svc_at_age40 - (40 - age))
        p = M.Profile(plan, age, svc, salary, 45_000.0, max(20, int(age - svc)))
        r = M.fm4_acceleration(p, years_purchased=years)
        gap = r["cost_total"] - M.price_a3_anc(p, years=years)
        if prev is not None and prev[1] < 0 <= gap:
            return prev[0] + (0 - prev[1]) * (age - prev[0]) / (gap - prev[1])
        prev = (age, gap)
    return None


L("Full-basis break-even purchase age, by plan and by service held at age 40:")
L(f"{'plan':8} {'svc@40':>7} {'benefit-amount-only':>21} {'FULL BASIS':>12}")
for plan, bo in (("Plan 1", 46.6), ("Plan 2", 47.4), ("Hybrid", 48.2)):
    for s40 in (5, 10, 15, 20):
        be = full_breakeven(plan, float(s40))
        L(f"{plan:8} {s40:>7} {bo:>21.1f} {('%.1f' % be) if be else 'none <60':>12}")
    L()

L("=" * 78)
L("T2  EARLY-PURCHASE EVASION OF GUARDRAIL A-PRIME")
L("=" * 78)
L("A-prime grades on distance from unreduced eligibility AT THE TIME OF PURCHASE")
L("(Annex A 2.2 factor (ii)). The acceleration exposure does not depend on when")
L("the member bought. Same member, same 4 years, bought early vs bought late:")
L()
for plan, age_late, svc_late in (("Plan 1", 52, 26), ("Hybrid", 55, 22)):
    late = M.Profile(plan, age_late, float(svc_late), 91_700.0, 45_000.0, age_late - svc_late)
    r_late = M.fm4_acceleration(late, 4.0)
    # same person, 10 years earlier: 10 fewer years of age and service, lower salary
    age_e = age_late - 10
    svc_e = svc_late - 10
    sal_e = 91_700.0 / (1 + M.SALARY_GROWTH) ** 10
    early = M.Profile(plan, age_e, float(svc_e), sal_e, 45_000.0, age_e - svc_e)
    r_early = M.fm4_acceleration(early, 4.0)
    L(f"  {plan}: buys at {age_late} with {svc_late} yrs  vs  buys at {age_e} with {svc_e} yrs")
    for lbl, p, r in (("late ", late, r_late), ("early", early, r_early)):
        for rec in (0.0, 1.0):
            price = M.price_threshold_graded(p, years=4.0, recovery=rec)
            L(f"    {lbl} recovery {rec:.0%}: price {M.money(price):>9}"
              f"  value-to-member {M.money(r['cost_total']):>9}"
              f"  net to Fund {M.money(r['cost_total']-price):>9}"
              f"  accel {r['acceleration_years']:.2f}yr")
    # what the Fund actually loses if the early buyer still retires on the
    # accelerated date his purchase bought him
    L(f"    -> early buyer pays {M.money(M.price_threshold_graded(early, 4.0, 1.0))} at the 100% dial,")
    L(f"       but the acceleration he collects is worth {M.money(r_early['cost_acceleration_channel'])}")
    L(f"       measured at age {age_e}; measured at age {age_late} the same acceleration is"
      f" {M.money(r_late['cost_acceleration_channel'])}.")
    L()

L("=" * 78)
L("T3  TAKE-UP  (assumption A-11)")
L("=" * 78)
pools = M.fm1_eligible_pool()
# reproduce the plan-split pool the headline grid uses
lo_hi = (10_561, 26_321)
per = {"Plan 1": 47_967, "Plan 2": 17_174, "Hybrid": 6_779}
blend = 24_627
L("Published headline: $13M - $182M.")
L("Floor cell = 5% take-up x low pool. 5% is the SUPERSEDED Annex B A-11 band,")
L("not a member of the model's current scenario set (Low 10 / Mod 20 / High 30).")
L()
L(f"{'take-up':>9} {'purchasers':>20} {'one-time PV (blended)':>30}")
for t in (0.05, 0.10, 0.15, 0.20, 0.30, 0.40, 0.50):
    p_lo, p_hi = lo_hi[0] * t, lo_hi[1] * t
    L(f"{t:>8.0%} {int(p_lo):>8,} - {int(p_hi):>8,}   "
      f"{M.money(p_lo*blend):>13} - {M.money(p_hi*blend):>13}")
L()
L("Range on the model's OWN current scenario set (10% low pool -> 30% high pool):")
L(f"  {M.money(lo_hi[0]*0.10*blend)} - {M.money(lo_hi[1]*0.30*blend)}")
L("Range if take-up reaches 50% (a publicised, subsidised, payroll-deductible")
L("benefit aimed at a self-identified population):")
L(f"  {M.money(lo_hi[0]*0.50*blend)} - {M.money(lo_hi[1]*0.50*blend)}")

L()
L("=" * 78)
L("T4  WHAT A UNIFORM CLASS RATE CAN RECOVER UNDER THE DRAFT'S OWN CEILING")
L("=" * 78)
L("Annex A 2.2 requires the schedule to 'apply uniformly to all members within")
L("the same classification' AND to 'not require payment of an amount exceeding")
L("the actuarial equivalent cost of the service credit purchased' - singular, the")
L("member's own. For a uniform rate to satisfy the ceiling for EVERY member in a")
L("class, it must be set at or below the MINIMUM actuarial value in that class,")
L("not the mean. Residual exposure = mean - min, and it is unrecoverable.")
L()
L("Classification as fine as the draft's five factors permit: plan x 5-yr age band")
L("x 10-yr service band x 4 years purchased. Salary held at $91,700 so the only")
L("variation is the risk the schedule is supposed to price.")
L()
for plan, ageband, svcband in (
        ("Plan 1", (50, 54), (20, 29)),
        ("Plan 1", (55, 59), (20, 29)),
        ("Plan 2", (50, 54), (10, 19)),
        ("Hybrid", (50, 54), (10, 19)),
        ("Hybrid", (55, 59), (10, 19))):
    vals = []
    for age in range(ageband[0], ageband[1] + 1):
        for svc in range(svcband[0], svcband[1] + 1):
            if svc > age - 18:
                continue
            p = M.Profile(plan, age, float(svc), 91_700.0, 45_000.0, age - svc)
            vals.append(M.fm4_acceleration(p, 4.0)["cost_total"])
    mn, mx, mean = min(vals), max(vals), statistics.mean(vals)
    anc = M.price_a3_anc(M.Profile(plan, ageband[0], float(svcband[0]), 91_700.0,
                                   45_000.0, 20), years=4.0)
    L(f"  {plan}, age {ageband[0]}-{ageband[1]}, service {svcband[0]}-{svcband[1]} "
      f"({len(vals)} member types)")
    L(f"    actuarial value of the 4 years:  min {M.money(mn)}   mean {M.money(mean)}"
      f"   max {M.money(mx)}")
    L(f"    ratio max/min {mx/mn:.2f}x")
    L(f"    highest lawful uniform class rate (= min)        {M.money(mn)}")
    L(f"    unrecoverable residual per purchaser (mean-min)  {M.money(mean-mn)}")
    L(f"    i.e. the 100% dial recovers {(mn-anc)/(mean-anc)*100 if mean>anc else float('nan'):.0f}% "
      f"of the above-ANC excess, not 100%")
    L()
