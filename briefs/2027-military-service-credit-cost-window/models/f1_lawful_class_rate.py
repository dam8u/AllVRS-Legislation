"""F-1 — what a LAWFUL uniform class rate can actually recover.

Red team finding F-1 (05-Red-Team-Review.md) holds that Annex 2 Closure
section 4.8's Guardrail A-prime dial is individualised actuarial pricing in
substance, and that the 100% row -- "actuarially neutral by construction and
the fiscal note is zero" -- is unreachable at any lawful setting of the
schedule the draft bill authorises.

This script tests that independently rather than taking the red team's table
at face value.  It is deliberately NOT a copy of their rt_check.py.

THE CONSTRAINT BEING MODELLED
-----------------------------
Annex A section 2.2 requires any Board rate schedule to

  (a) "apply uniformly to all members within the same classification under
      the schedule"; and
  (b) "not require payment of an amount exceeding the actuarial equivalent
      cost of the service credit purchased."

(b) binds member by member.  So for a single uniform price P to be lawful for
every member of class c:

      P <= min_{i in c} AEC_i

and the schedule is never set below the published approximate normal cost
(that floor is what makes it presentable as "still a published rate", and it
is how price_age_graded already behaves).  Hence the most aggressive LAWFUL
uniform price is

      P*_c = max( ANC_price , min_{i in c} AEC_i )

whereas section 4.8's price_threshold_graded charges, at recovery = 1.0,

      P_i = AEC_i                       (member by member)

The share of the class's above-ANC excess that P*_c recovers is therefore

      recovery_c = (P*_c - ANC_price) / (mean_i AEC_i - ANC_price)

which is 1.0 only if AEC is constant inside the class.  Residual net cost to
the Fund per member of the class is mean_i(AEC_i) - P*_c.

DEFINITIONS, stated because the result depends on them
------------------------------------------------------
* AEC_i = fm4_acceleration(...)["cost_total"] -- the full-basis present value
  of the granted service, benefit-amount channel PLUS retirement-date
  acceleration.  This is the same quantity section 4.8's 0% row nets the ANC
  price against, so the figures here are directly comparable to that table.
* Salary is HELD CONSTANT at the model's own basis, so the only variation
  inside a class is the risk the schedule exists to price (age and service).
  Salary variation would widen every band below, never narrow it.
* Classes are drawn as finely as the Annex A section 2.2 factors permit while
  still being a genuine published CLASS rather than a near-singleton:
  plan x 5-year age band x 10-year service band, at a fixed amount purchased.

Run:  python3 f1_lawful_class_rate.py
"""

from fm_model import (
    ANC,
    MEAN_CLASSIFIED_SALARY,
    YEARS_PURCHASED_AVG,
    Profile,
    fm4_acceleration,
    money,
    price_a3_anc,
)

# Section 4.8's own basis: pool-low-end plan weights, group-low-end headcount.
PLAN_WEIGHTS_LOW = {"Plan 1": 3_966, "Plan 2": 2_417, "Hybrid": 4_177}
POOL_GROUP = (11_565, 24_036)   # M-4: the who-bears derivation, both ends
POOL_PLAN = (10_561, 26_321)    # M-4: the by-plan derivation, both ends
TAKEUP = 0.20

AGE_BANDS = [(40, 44), (45, 49), (50, 54), (55, 59), (60, 64)]
SVC_BANDS = [(0, 9), (10, 19), (20, 29), (30, 39)]


def aec(plan, age, service, years, salary=MEAN_CLASSIFIED_SALARY):
    p = Profile(plan, age, float(service), salary, salary, 30)
    return fm4_acceleration(p, years_purchased=years)["cost_total"]


def anc_price(plan, years, salary=MEAN_CLASSIFIED_SALARY):
    return ANC[(plan, "non-hazardous")] * salary * years


def class_stats(plan, age_band, svc_band, years):
    """min / mean / max AEC inside one published classification.

    Members who never reach unreduced eligibility inside the modelled annuity
    horizon are EXCLUDED: their modelled AEC is 0 because the annuity-certain
    basis terminates at age 87, which is a basis artefact rather than a
    pricing fact, and they would not be purchasers.  Excluding them is the
    conservative choice -- keeping them would pin the lawful uniform rate at
    zero and make the dial look even weaker than reported here.
    """
    from fm_model import TERMINAL_AGE, unreduced_age

    vals = [
        aec(plan, a, s, years)
        for a in range(age_band[0], age_band[1] + 1)
        for s in range(svc_band[0], svc_band[1] + 1)
        if unreduced_age(plan, a, float(s), purchased=years) < TERMINAL_AGE
    ]
    if not vals:
        return None
    anc = anc_price(plan, years)
    lo, hi = min(vals), max(vals)
    mean = sum(vals) / len(vals)
    lawful = max(anc, lo)
    excess = mean - anc
    recovery = (lawful - anc) / excess if excess > 0 else None
    return {
        "n": len(vals),
        "min": lo,
        "mean": mean,
        "max": hi,
        "anc": anc,
        "lawful_price": lawful,
        "excess_mean": excess,
        "recovery": recovery,
        "residual_per_member": mean - lawful,
    }


def table(years, label):
    print(f"\n{'=' * 78}")
    print(f"  LAWFUL UNIFORM CLASS RATE — {label}")
    print(f"  plan x 5-yr age band x 10-yr service band, salary held at "
          f"{money(MEAN_CLASSIFIED_SALARY)}, {years:g} years purchased")
    print(f"{'=' * 78}")
    print(f"  {'class':<34}{'min AEC':>11}{'mean AEC':>11}{'max/min':>9}"
          f"{'100% dial':>11}")
    print(f"  {'':<34}{'':>11}{'':>11}{'':>9}{'recovers':>11}")
    rows = []
    for plan in ("Plan 1", "Plan 2", "Hybrid"):
        for ab in AGE_BANDS:
            for sb in SVC_BANDS:
                st = class_stats(plan, ab, sb, years)
                if st is None or st["recovery"] is None:
                    continue        # no priceable members in the class
                name = f"{plan}, age {ab[0]}-{ab[1]}, svc {sb[0]}-{sb[1]}"
                rows.append((plan, name, st))
                spread = (f"{st['max'] / st['min']:.2f}x" if st["min"] > 0
                          else "inf")
                print(f"  {name:<34}{money(st['min']):>11}"
                      f"{money(st['mean']):>11}{spread:>9}"
                      f"{st['recovery'] * 100:>10.0f}%")
    recs = [st["recovery"] for _, _, st in rows]
    print(f"\n  Recovery band across {len(rows)} priceable classes: "
          f"{min(recs) * 100:.0f}% - {max(recs) * 100:.0f}%")
    print(f"  Unweighted mean recovery: {sum(recs) / len(recs) * 100:.0f}%")

    # NEW FINDING, not in F-1: classes in which the published ANC rate ITSELF
    # exceeds some member's own AEC.  There the individual ceiling does not
    # merely disable the dial -- it makes the BASELINE price unlawful, and the
    # Board would have to charge that member LESS than the published rate.
    dead = [(n, st) for _, n, st in rows if st["min"] < st["anc"]]
    print(f"\n  Classes where the published ANC price EXCEEDS the lowest "
          f"member's own AEC: {len(dead)} of {len(rows)}")
    for n, st in dead:
        print(f"    {n:<34} min AEC {money(st['min'])} < ANC price "
              f"{money(st['anc'])}  (shortfall {money(st['anc'] - st['min'])})")
    if dead:
        print("    In these classes the section 2.2 individual-AEC ceiling is")
        print("    breached by the published rate itself, so the dial cannot be")
        print("    set above 0% AND the baseline is unlawful for those members.")
    return rows


# Section 4.8 / FM-1 price the pool PER PLAN and sum, rather than applying a
# blended rate to a total headcount.  The two give different answers because
# the plan mix is not constant across the pool ends, so every PV below is
# built the same way the published grid is built:  sum_plan(pool x t x net).
PLAN_POOL = {"Plan 1": (3_966, 9_027),
             "Plan 2": (2_417, 5_502),
             "Hybrid": (4_177, 11_792)}


def plan_nets(years):
    """Section 4.8's 0% row, reproduced from the model's own representative
    profiles so the restatement is anchored to the published table."""
    reps = {
        "Plan 1": Profile("Plan 1", 55, 25, MEAN_CLASSIFIED_SALARY, 45_000, 30),
        "Plan 2": Profile("Plan 2", 50, 14, MEAN_CLASSIFIED_SALARY, 55_000, 36),
        "Hybrid": Profile("Hybrid", 50, 9, MEAN_CLASSIFIED_SALARY, 60_000, 41),
    }
    out = {}
    for plan, p in reps.items():
        r = fm4_acceleration(p, years_purchased=years)
        out[plan] = r["cost_total"] - price_a3_anc(p, years)
    return out


def pv(net_by_plan, takeup, end):
    """one-time PV = sum over plans of pool x take-up x net, as FM-1 does."""
    return sum(PLAN_POOL[p][end] * takeup * net_by_plan[p] for p in net_by_plan)


def restated_pv(rows, years):
    """Residual exposure once the dial is capped at what a LAWFUL uniform
    class rate can recover, by plan, at both pool ends (M-4)."""
    print(f"\n{'-' * 78}")
    print("  RESTATED EXPOSURE — residual after a lawful uniform class rate")
    print(f"{'-' * 78}")

    per_plan = {}
    for plan in ("Plan 1", "Plan 2", "Hybrid"):
        recs = [st["recovery"] for p, _, st in rows if p == plan]
        # Equal-weighted across that plan's classes: the age/service
        # distribution of the veteran pool is NOT published (A-22/U-01), so no
        # weighting inside a plan is defensible.  A band is what is honest.
        per_plan[plan] = {"lo": min(recs), "hi": max(recs),
                          "mid": sum(recs) / len(recs)}
        print(f"  {plan:<10} lawful recovery across its classes: "
              f"{min(recs) * 100:>3.0f}% - {max(recs) * 100:>3.0f}%  "
              f"(mean {sum(recs) / len(recs) * 100:.0f}%)")

    net0 = plan_nets(years)
    print(f"\n  Section 4.8 0% row reproduced: "
          + ", ".join(f"{p} {money(net0[p])}" for p in net0))
    tw = sum(PLAN_WEIGHTS_LOW.values())
    print(f"  Pool-weighted blend: "
          f"{money(sum(PLAN_WEIGHTS_LOW[p] * net0[p] for p in net0) / tw)}")

    print(f"\n  {'recovery setting':<34}{'PV @20% take-up, both pool ends':>34}")
    settings = [
        ("0% — plain published ANC", lambda p: 0.0),
        ("lawful uniform, best class in plan", lambda p: per_plan[p]["hi"]),
        ("lawful uniform, class mean", lambda p: per_plan[p]["mid"]),
        ("lawful uniform, worst class in plan", lambda p: per_plan[p]["lo"]),
        ("100% individualised — NOT LAWFUL", lambda p: 1.0),
    ]
    out = {}
    for label, f in settings:
        resid = {p: net0[p] * (1 - f(p)) for p in net0}
        lo, hi = pv(resid, TAKEUP, 0), pv(resid, TAKEUP, 1)
        out[label] = (lo, hi)
        print(f"  {label:<34}{f'{money(lo)} - {money(hi)}':>34}")

    print(f"\n  M-4 check — the published 0% guardrail figure, both derivations:")
    print(f"    by plan (FM-1 headline basis) {POOL_PLAN[0]:>7,} - "
          f"{POOL_PLAN[1]:>7,}   "
          f"{money(pv(net0, TAKEUP, 0))} - {money(pv(net0, TAKEUP, 1))}")
    bl = sum(PLAN_WEIGHTS_LOW[p] * net0[p] for p in net0) / tw
    print(f"    by employer group (who-bears) {POOL_GROUP[0]:>7,} - "
          f"{POOL_GROUP[1]:>7,}   "
          f"{money(POOL_GROUP[0] * TAKEUP * bl)} - "
          f"{money(POOL_GROUP[1] * TAKEUP * bl)}")
    print("    Annex A section 5.1 quotes $57.0M, which is the LOW end of the")
    print("    group derivation, against a published ceiling of $182M from the")
    print("    plan derivation. The two are not the same number at either end.")
    return net0


def takeup_grid(net0):
    """S-5 — the published range on the CURRENT scenario set, plus a 50%
    stress case, at the 0% recovery setting, on the FM-1 headline basis."""
    print(f"\n{'-' * 78}")
    print("  S-5 — take-up grid on the current scenario set, 0% recovery")
    print(f"{'-' * 78}")
    print(f"  {'take-up':<44}{'one-time PV':>34}")
    for label, t in (
        ("5%  (published floor — SUPERSEDED band)", 0.05),
        ("10% (current Low)", 0.10),
        ("20% (current Moderate)", 0.20),
        ("30% (current High)", 0.30),
        ("50% (stress: publicised, payroll-deductible)", 0.50),
    ):
        print(f"  {label:<44}"
              f"{f'{money(pv(net0, t, 0))} - {money(pv(net0, t, 1))}':>34}")
    print("\n  The published headline takes its FLOOR from the 5% row (the")
    print("  superseded 5%-15% band) and its CEILING from the 30% row (the")
    print("  current scenario set). On the current set alone the range is")
    print(f"  {money(pv(net0, 0.10, 0))} - {money(pv(net0, 0.30, 1))}.")


def breakeven_full_basis(years):
    """S-4 — is there any age below 60 at which the member overpays on the
    FULL basis (benefit-amount + acceleration), as the brief's 47-48
    break-even claim requires?"""
    print(f"\n{'-' * 78}")
    print("  S-4 — does the veteran ever subsidise the Fund on the full basis?")
    print(f"{'-' * 78}")
    print(f"  {'plan':<9}{'age':>5}{'svc':>5}{'ANC price':>12}"
          f"{'full-basis value':>18}{'member net':>13}")
    any_subsidy = False
    for plan in ("Plan 1", "Plan 2", "Hybrid"):
        for age in (30, 35, 40, 45, 50):
            svc = max(1.0, age - 30)
            v = aec(plan, age, svc, years)
            pa = anc_price(plan, years)
            if pa > v:
                any_subsidy = True
            print(f"  {plan:<9}{age:>5}{svc:>5.0f}{money(pa):>12}"
                  f"{money(v):>18}{money(pa - v):>13}")
    print(f"\n  Any age/plan tested at which the member overpays on the full "
          f"basis: {'YES' if any_subsidy else 'NO'}")
    print("  The brief's 'below age 47-48 the veteran subsidises the Fund' is")
    print("  computed on the benefit-amount channel ALONE. On the full basis")
    print("  it does not hold at any age tested.")


if __name__ == "__main__":
    rows = table(YEARS_PURCHASED_AVG, "section 4.8 basis (2.5 years)")
    net0 = restated_pv(rows, YEARS_PURCHASED_AVG)
    takeup_grid(net0)
    breakeven_full_basis(YEARS_PURCHASED_AVG)
    table(4.0, "statutory maximum (4 years) — F-1's own basis")
