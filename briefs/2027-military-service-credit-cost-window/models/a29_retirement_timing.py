"""A-29 — retirement timing of purchasers, priced against the Board's own
retirement decrements instead of a deterministic earliest-unreduced-date rule.

WHY THIS FILE EXISTS
--------------------
`fm_model.fm4_acceleration` prices the acceleration channel deterministically:
the member retires exactly at `unreduced_age(...)`, both with and without the
purchase. Red team S-4 made that visible and Annex B registered it as A-29,
with its direction stated but not its magnitude: "pushes cost up; if real
behaviour is partial, the full-basis figures are conservative."

A-29's resolution was logged as needing "VRS retirement-pattern data for
purchasers (extension of data request item 5)." That turned out to be only
half true. VRS *publishes* its Board-adopted retirement decrements every year
in the Annual Comprehensive Financial Report — Figure 4.3, "Retirement Rates —
Pension Plans," FY2025, printed pp. 213-220 — as conditional annual
probabilities of retirement given eligibility, by plan, employer group, sex,
age and years of service. What is unavailable is the *purchaser-specific*
pattern. The general pattern is OFFICIAL and was never requested.

So A-29 moves from "unquantified estimate" to a quantified band with an
OFFICIAL lower leg:

    upper leg  (current model)  every purchaser retires at the earliest
                               unreduced date -> 100% of acceleration realised
    lower leg  (Board rates)    purchasers behave like the membership at large
                               -> this file computes what fraction survives

Neither leg is a prediction. A purchaser is a self-selected member who paid
cash to move an eligibility date, so the truth sits above the lower leg; and
nobody can retire *earlier* than eligibility, so it sits at or below the upper.
The point of the file is that the band is now bounded on both sides by
published numbers rather than open on one side.

THE SINGLE MOST IMPORTANT PUBLISHED NUMBER HERE
-----------------------------------------------
The footnote to Figure 4.3 for every Plan 2 / Hybrid table reads:

    "Rate is 11.50% when age plus service equals 90."   (State Employees, male)
    "Rate is 12.00% when age plus service equals 90."   (State Employees, female)
    "Rate is 22.50% when age plus service equals 90."   (Teachers, both sexes)

That is the Board's assumed probability that a member retires in the year they
attain the Rule of 90 — the exact event the bill accelerates. The live model
assumes 100%. The Board assumes 11.5%-22.5%. That gap is A-29, in VRS's own
published arithmetic.

BASIS AND LIMITS
----------------
- Figure 4.3 prints SAMPLE ages (50, 55, 59, 60, 61, 62, 64, 65, 67, 70, >=80).
  The full table is not published. Rates are linearly interpolated between
  printed sample ages. ESTIMATE, and the only interpolation in this file.
- Only the RETIREMENT decrement is applied after eligibility. Post-eligibility
  death and termination are not. That leaves more members alive and active to
  retire late, so it *understates* late retirement and therefore OVERSTATES the
  surviving acceleration share. The lower leg computed here is accordingly a
  conservative (high) estimate of acceleration cost under Board behaviour.
- Everything else - discount, COLA, multiplier, salary growth, annuity basis,
  eligibility rules - is imported from `fm_model` unchanged, so the comparison
  is apples-to-apples with FM-4 by construction and not by transcription.

Run:  python3 a29_retirement_timing.py
"""

from fm_model import (
    Profile, DISCOUNT, SALARY_GROWTH, MULTIPLIER, COLA, TERMINAL_AGE,
    MEAN_CLASSIFIED_SALARY, ILLUSTRATIVE_SALARY,
    cola_annuity, unreduced_age, fm4_acceleration, money,
)

# ============================================================================
# OFFICIAL: VRS ACFR FY2025, Figure 4.3 "Retirement Rates - Pension Plans",
# printed pp. 213-220. Board-adopted; demographic assumptions from the
# experience study covering July 1, 2020 - June 30, 2024, adopted by the
# Board of Trustees April 16, 2025.
#
# Each table maps (sample age) -> tuple of rates across the printed years-of-
# service bands. Transcribed verbatim; `verify()` re-checks the cells this
# analysis actually reads.
# ============================================================================

SAMPLE_AGES = (50, 55, 59, 60, 61, 62, 64, 65, 67, 70, 80)

# Service band lower bounds, as printed in the column headers.
BANDS_P1 = (5, 6, 10, 11, 30, 31)            # "5 | 6-9 | 10 | 11-29 | 30 | >=31"
BANDS_P2 = (30, 31, 33, 35, 37, 39, 40)      # "30 | 31 | 33 | 35 | 37 | 39 | >=40"

RATES = {
    # ---- State Employees, Plan 1 (p. 213)
    ("State Employees", "Plan 1", "M"): {
        50: (0.00, 0.00, 3.25, 3.25, 12.50, 12.50),
        55: (4.50, 4.50, 4.50, 3.50, 8.00, 9.00),
        59: (4.50, 4.00, 4.00, 4.00, 10.00, 9.00),
        60: (4.50, 5.00, 5.00, 5.00, 11.50, 9.00),
        61: (15.00, 7.50, 7.50, 7.50, 17.00, 15.00),
        62: (15.00, 10.00, 10.00, 10.00, 17.00, 20.00),
        64: (15.00, 13.50, 13.50, 13.50, 17.00, 17.50),
        65: (25.00, 25.00, 25.00, 25.00, 25.00, 25.00),
        67: (27.50, 22.00, 22.00, 22.00, 22.00, 22.00),
        70: (20.00, 22.00, 22.00, 22.00, 22.00, 22.00),
        80: (100.0,) * 6,
    },
    ("State Employees", "Plan 1", "F"): {
        50: (0.00, 0.00, 4.00, 4.00, 7.50, 7.50),
        55: (5.00, 5.00, 5.00, 4.00, 7.50, 8.00),
        59: (5.00, 5.00, 5.00, 5.00, 12.00, 9.00),
        60: (5.00, 5.50, 5.50, 5.50, 12.00, 12.50),
        61: (7.50, 8.00, 8.00, 8.00, 12.00, 16.00),
        62: (10.00, 12.00, 12.00, 12.00, 22.50, 20.00),
        64: (17.50, 15.00, 15.00, 15.00, 22.50, 17.50),
        65: (27.50, 27.50, 27.50, 27.50, 27.50, 30.00),
        67: (30.00, 25.00, 25.00, 25.00, 25.00, 25.00),
        70: (25.00, 27.00, 27.00, 27.00, 27.00, 27.00),
        80: (100.0,) * 6,
    },
    # ---- State Employees, Plan 2 and Hybrid (pp. 213-214). The printed male
    #      and female tables are identical cell for cell; only the Rule-of-90
    #      footnote differs (11.50% male, 12.00% female).
    ("State Employees", "Plan 2", "M"): {
        50: (0.00, 0.00, 0.00, 0.00, 0.00, 8.00, 8.00),
        55: (0.00, 0.00, 0.00, 8.00, 8.00, 8.00, 8.00),
        59: (8.00,) * 7,
        60: (8.00,) * 7,
        61: (8.00, 7.50, 7.50, 7.50, 7.50, 7.50, 7.50),
        62: (10.00,) * 7,
        64: (10.00,) * 7,
        65: (25.00,) * 7,
        67: (20.00,) * 7,
        70: (20.00,) * 7,
        80: (100.0,) * 7,
    },
    # ---- Teachers, Plan 1 (p. 214)
    ("Teachers", "Plan 1", "M"): {
        50: (0.00, 0.00, 2.50, 2.50, 15.00, 15.00),
        55: (7.00, 7.00, 7.00, 5.00, 22.50, 15.00),
        59: (10.00, 7.00, 7.00, 7.00, 22.50, 15.00),
        60: (10.00, 7.50, 7.50, 7.50, 22.50, 17.00),
        61: (11.00, 12.00, 12.00, 12.00, 35.00, 23.00),
        62: (17.00, 15.00, 15.00, 15.00, 35.00, 30.00),
        64: (18.00, 15.00, 15.00, 15.00, 35.00, 25.00),
        65: (30.00, 30.00, 30.00, 30.00, 30.00, 34.00),
        67: (30.00, 34.00, 34.00, 34.00, 34.00, 34.00),
        70: (30.00,) * 6,
        80: (100.0,) * 6,
    },
    ("Teachers", "Plan 1", "F"): {
        50: (0.00, 0.00, 3.00, 3.00, 15.00, 15.00),
        55: (4.50, 4.50, 4.50, 5.00, 22.50, 16.00),
        59: (8.00, 7.00, 7.00, 7.00, 22.50, 17.00),
        60: (9.00, 8.50, 8.50, 8.50, 30.00, 20.00),
        61: (25.00, 11.00, 11.00, 11.00, 30.00, 25.00),
        62: (25.00, 15.00, 15.00, 15.00, 35.00, 30.00),
        64: (25.00, 20.00, 20.00, 20.00, 35.00, 28.00),
        65: (35.00, 35.00, 35.00, 35.00, 35.00, 40.00),
        67: (30.00, 32.00, 32.00, 32.00, 32.00, 32.00),
        70: (30.00, 32.00, 32.00, 32.00, 32.00, 32.00),
        80: (100.0,) * 6,
    },
    # ---- Teachers, Plan 2 and Hybrid (p. 215). Male and female identical as
    #      printed; Rule-of-90 footnote 22.50% for both.
    ("Teachers", "Plan 2", "M"): {
        50: (0.00, 0.00, 0.00, 0.00, 0.00, 9.00, 9.00),
        55: (0.00, 0.00, 0.00, 9.00, 9.00, 9.00, 9.00),
        59: (9.00,) * 7,
        60: (9.00,) * 7,
        61: (14.00, 10.00, 10.00, 10.00, 10.00, 10.00, 10.00),
        62: (13.00,) * 7,
        64: (14.00,) * 7,
        65: (25.00,) * 7,
        67: (20.00,) * 7,
        70: (20.00,) * 7,
        80: (100.0,) * 7,
    },
}

# The female Plan 2 / Hybrid tables are printed identically to the male ones.
RATES[("State Employees", "Plan 2", "F")] = RATES[("State Employees", "Plan 2", "M")]
RATES[("Teachers", "Plan 2", "F")] = RATES[("Teachers", "Plan 2", "M")]
# Hybrid shares the Plan 2 table in Figure 4.3 ("Plan 2 and Hybrid").
for grp in ("State Employees", "Teachers"):
    for sex in ("M", "F"):
        RATES[(grp, "Hybrid", sex)] = RATES[(grp, "Plan 2", sex)]

# OFFICIAL: the Rule-of-90 footnote rate to Figure 4.3. This is the Board's
# assumed probability of retiring IN THE YEAR the Rule of 90 is attained --
# the precise event this bill accelerates.
RULE_OF_90_RATE = {
    ("State Employees", "M"): 0.1150,
    ("State Employees", "F"): 0.1200,
    ("Teachers", "M"): 0.2250,
    ("Teachers", "F"): 0.2250,
}

# OFFICIAL: Figure 4.3 forces retirement at >=80 for the non-hazardous tables
# used here (>=70 for hazardous duty / VaLORS / State Police, >=73 for judges).
FORCED_AGE = 80


def _band_index(bands, service):
    """Index of the printed years-of-service column covering `service`."""
    i = 0
    for k, lo in enumerate(bands):
        if service >= lo:
            i = k
    return i


def retirement_rate(group, plan, sex, age, service):
    """Conditional annual probability of retirement given eligible, from the
    Figure 4.3 sample rates, linearly interpolated between printed sample ages.

    OFFICIAL at the printed sample ages; ESTIMATE between them."""
    table = RATES[(group, plan, sex)]
    bands = BANDS_P1 if plan == "Plan 1" else BANDS_P2
    j = _band_index(bands, service)
    if age >= FORCED_AGE:
        return 1.0
    if age <= SAMPLE_AGES[0]:
        return table[SAMPLE_AGES[0]][j] / 100.0
    for lo, hi in zip(SAMPLE_AGES, SAMPLE_AGES[1:]):
        if lo <= age <= hi:
            r_lo = table[lo][j] / 100.0
            r_hi = table[hi][j] / 100.0
            if hi == lo:
                return r_lo
            w = (age - lo) / (hi - lo)
            return r_lo + w * (r_hi - r_lo)
    return 1.0


def _pv_at(p, ret_age, svc_at_ret):
    """PV today of an allowance commencing at ret_age. Identical basis to
    fm_model.fm4_acceleration.pv_at - deliberately duplicated rather than
    imported, because it is a closure there."""
    m, c = MULTIPLIER[p.plan], COLA[p.plan]
    yrs = ret_age - p.age
    afc = p.salary * (1 + SALARY_GROWTH) ** max(0.0, yrs - 1.5)
    annual = m * svc_at_ret * afc
    a = cola_annuity(ret_age, c)
    v = 1 / ((1 + DISCOUNT) ** yrs)
    return annual * a * v


def retirement_distribution(p, group, sex, elig_age, purchased, via_rule_of_90):
    """Probability distribution of retirement age, starting at first
    eligibility `elig_age` and running the Figure 4.3 decrements forward.

    Returns [(retire_age, probability, service_at_retirement), ...].

    `via_rule_of_90` selects the footnote rate for the FIRST year of
    eligibility when eligibility is attained by the Rule of 90 rather than by
    SSA normal retirement age or by the Plan 1 thresholds."""
    out = []
    alive = 1.0
    age = elig_age
    first = True
    while alive > 1e-12 and age < FORCED_AGE + 1:
        svc = p.service + (age - p.age) + purchased
        if first and via_rule_of_90 and p.plan in ("Plan 2", "Hybrid"):
            q = RULE_OF_90_RATE[(group, sex)]
        else:
            q = retirement_rate(group, p.plan, sex, age, svc)
        q = min(1.0, max(0.0, q))
        if age >= FORCED_AGE:
            q = 1.0
        out.append((age, alive * q, svc))
        alive -= alive * q
        age += 1.0
        first = False
    return out


def expected_pv(p, group, sex, elig_age, purchased, via_rule_of_90):
    """E[PV] of the allowance under the Board's retirement decrements."""
    dist = retirement_distribution(p, group, sex, elig_age, purchased,
                                   via_rule_of_90)
    return sum(prob * _pv_at(p, age, svc) for age, prob, svc in dist), dist


def _eligibility_is_rule_of_90(p, purchased):
    """True when the member's first unreduced date is set by the Rule of 90
    (51.1-153 B 3) rather than by SSA NRA (B 2) or the Plan 1 tests (B 1)."""
    if p.plan == "Plan 1":
        return False
    return unreduced_age(p.plan, p.age, p.service, purchased=purchased) < 67.0


def a29_profile(p, group, sex, years_purchased=4.0):
    """Decompose the two channels BOTH ways: deterministically (the live model's
    A-29 assumption) and under the Board's published retirement decrements."""
    a0 = unreduced_age(p.plan, p.age, p.service)
    a1 = unreduced_age(p.plan, p.age, p.service, purchased=years_purchased)

    # --- Deterministic, as in fm_model.fm4_acceleration.
    det = fm4_acceleration(p, years_purchased=years_purchased)

    # --- Behavioural. Three states, same three the deterministic model uses.
    r90_0 = _eligibility_is_rule_of_90(p, 0.0)
    r90_1 = _eligibility_is_rule_of_90(p, years_purchased)

    pv0, dist0 = expected_pv(p, group, sex, a0, 0.0, r90_0)
    pv_amt, _ = expected_pv(p, group, sex, a0, years_purchased, r90_0)
    pv_both, dist1 = expected_pv(p, group, sex, a1, years_purchased, r90_1)

    e_ret0 = sum(prob * age for age, prob, _ in dist0)
    e_ret1 = sum(prob * age for age, prob, _ in dist1)

    beh_amt = pv_amt - pv0
    beh_acc = pv_both - pv_amt
    beh_tot = pv_both - pv0

    return {
        "elig_baseline": a0,
        "elig_with_purchase": a1,
        "elig_acceleration_years": a0 - a1,
        "expected_retire_baseline": e_ret0,
        "expected_retire_with_purchase": e_ret1,
        "expected_acceleration_years": e_ret0 - e_ret1,
        "det_amount": det["cost_amount_channel"],
        "det_acceleration": det["cost_acceleration_channel"],
        "det_total": det["cost_total"],
        "beh_amount": beh_amt,
        "beh_acceleration": beh_acc,
        "beh_total": beh_tot,
        "acc_survival": (beh_acc / det["cost_acceleration_channel"]
                         if det["cost_acceleration_channel"] else float("nan")),
        "tot_survival": (beh_tot / det["cost_total"]
                         if det["cost_total"] else float("nan")),
        "first_year_rate": (RULE_OF_90_RATE[(group, sex)] if r90_1
                            and p.plan != "Plan 1"
                            else retirement_rate(group, p.plan, sex, a1,
                                                 p.service + (a1 - p.age)
                                                 + years_purchased)),
    }


# ============================================================================
# VERIFICATION
# ============================================================================

def verify():
    """Re-check the transcribed cells this analysis reads, and the internal
    consistency of the distribution machinery."""
    checks = []

    def ck(name, got, want, tol=1e-9):
        ok = abs(got - want) <= tol
        checks.append((ok, name, got, want))
        return ok

    # --- Transcription spot-checks against the printed tables.
    ck("ACFR p213 State P1 M age50 svc30 = 12.50%",
       retirement_rate("State Employees", "Plan 1", "M", 50, 30), 0.1250)
    ck("ACFR p213 State P1 M age55 svc25 = 3.50%",
       retirement_rate("State Employees", "Plan 1", "M", 55, 25), 0.0350)
    ck("ACFR p213 State P1 F age50 svc30 = 7.50%",
       retirement_rate("State Employees", "Plan 1", "F", 50, 30), 0.0750)
    ck("ACFR p213 State P1 M age65 svc25 = 25.00%",
       retirement_rate("State Employees", "Plan 1", "M", 65, 25), 0.2500)
    ck("ACFR p214 Teachers P1 M age55 svc30 = 22.50%",
       retirement_rate("Teachers", "Plan 1", "M", 55, 30), 0.2250)
    ck("ACFR p214 Teachers P1 F age61 svc5 = 25.00%",
       retirement_rate("Teachers", "Plan 1", "F", 61, 5), 0.2500)
    ck("ACFR p213 State P2 M age55 svc35 = 8.00%",
       retirement_rate("State Employees", "Plan 2", "M", 55, 35), 0.0800)
    ck("ACFR p213 State P2 M age55 svc33 = 0.00%",
       retirement_rate("State Employees", "Plan 2", "M", 55, 33), 0.0000)
    ck("ACFR p215 Teachers P2 M age61 svc30 = 14.00%",
       retirement_rate("Teachers", "Plan 2", "M", 61, 30), 0.1400)
    ck("ACFR p213 forced retirement at 80 = 100%",
       retirement_rate("State Employees", "Plan 1", "M", 80, 30), 1.0000)
    ck("Hybrid reads the Plan 2 table (age 60, svc 30) = 8.00%",
       retirement_rate("State Employees", "Hybrid", "M", 60, 30), 0.0800)

    # --- Interpolation: midpoint of 55 (3.50%) and 59 (4.00%) at svc 25.
    ck("interp age 57 State P1 M svc25 = 3.75%",
       retirement_rate("State Employees", "Plan 1", "M", 57, 25), 0.0375)

    # --- Band selection: service 29 sits in the "11-29" column, 30 in "30".
    ck("svc 29 uses the 11-29 column (age 50) = 3.25%",
       retirement_rate("State Employees", "Plan 1", "M", 50, 29), 0.0325)
    ck("svc 31 uses the >=31 column (age 62) = 20.00%",
       retirement_rate("State Employees", "Plan 1", "M", 62, 31), 0.2000)

    # --- Rule-of-90 footnote rates.
    ck("footnote State male Rule of 90 = 11.50%",
       RULE_OF_90_RATE[("State Employees", "M")], 0.1150)
    ck("footnote State female Rule of 90 = 12.00%",
       RULE_OF_90_RATE[("State Employees", "F")], 0.1200)
    ck("footnote Teachers Rule of 90 = 22.50%",
       RULE_OF_90_RATE[("Teachers", "M")], 0.2250)

    # --- Distribution machinery: probabilities must sum to 1.
    for plan, age, svc in (("Plan 1", 55, 25), ("Plan 2", 50, 14),
                           ("Hybrid", 45, 8), ("Hybrid", 55, 10)):
        p = Profile(plan, age, svc, MEAN_CLASSIFIED_SALARY, 45_000, 30)
        for sex in ("M", "F"):
            a = unreduced_age(plan, age, svc)
            dist = retirement_distribution(
                p, "State Employees", sex, a, 0.0,
                _eligibility_is_rule_of_90(p, 0.0))
            ck(f"dist sums to 1 ({plan} {age}/{svc} {sex})",
               sum(x[1] for x in dist), 1.0, 1e-9)

    # --- The behavioural total must be strictly below the deterministic total
    #     whenever eligibility actually moves (acceleration is discounted by
    #     the probability of not retiring at the first opportunity).
    for plan, age, svc in (("Plan 1", 55, 25), ("Plan 2", 50, 14),
                           ("Hybrid", 45, 8)):
        p = Profile(plan, age, svc, MEAN_CLASSIFIED_SALARY, 45_000, 30)
        r = a29_profile(p, "State Employees", "M")
        if r["elig_acceleration_years"] > 0:
            checks.append((r["beh_acceleration"] < r["det_acceleration"],
                           f"behavioural acceleration < deterministic ({plan})",
                           r["beh_acceleration"], r["det_acceleration"]))
            checks.append((r["beh_acceleration"] > 0,
                           f"behavioural acceleration still positive ({plan})",
                           r["beh_acceleration"], 0.0))

    # --- The amount channel must be almost unaffected by retirement timing in
    #     direction: it is a pure service-count effect at an unchanged date.
    p = Profile("Plan 1", 55, 25, MEAN_CLASSIFIED_SALARY, 45_000, 30)
    r = a29_profile(p, "State Employees", "M")
    checks.append((r["beh_amount"] > 0, "amount channel positive under Board rates",
                   r["beh_amount"], 0.0))

    npass = sum(1 for ok, *_ in checks if ok)
    print(f"  A-29 verification: {npass}/{len(checks)} checks pass")
    for ok, name, got, want in checks:
        if not ok:
            print(f"    FAIL  {name}: got {got!r}, want {want!r}")
    return npass == len(checks)


# ============================================================================
# REPORT
# ============================================================================

PROFILES = [
    ("Plan 1", 55, 25, "the cohort the one-pager leads with"),
    ("Plan 2", 50, 14, "FM-2 canonical Plan 2 profile"),
    ("Hybrid", 45, 8, "FM-2 canonical early-career Hybrid"),
    ("Hybrid", 55, 10, "FM-2 canonical late-entry Hybrid"),
]


def main():
    print("=" * 78)
    print("A-29 — RETIREMENT TIMING OF PURCHASERS")
    print("Board-adopted decrements (VRS ACFR FY2025, Fig. 4.3, pp. 213-220)")
    print("versus the live model's earliest-unreduced-date rule")
    print("=" * 78)

    print("\n1. THE ASSUMPTION, STATED AS TWO NUMBERS\n")
    print("   The live model assumes every purchaser retires at the earliest")
    print("   unreduced date. For a Plan 2 or Hybrid member reaching the Rule")
    print("   of 90, that is a 100% first-year retirement rate. The Board's")
    print("   own published footnote to Figure 4.3 assumes:\n")
    for (grp, sex), r in RULE_OF_90_RATE.items():
        print(f"     {grp:<18} {sex}   {r:>7.2%}  in the year age + service = 90")
    print("\n   A-29 is the distance between 100% and those rates.")

    print("\n2. PER-PROFILE DECOMPOSITION, buying 4 years, $69,865 salary basis\n")
    hdr = (f"   {'Profile':<20}{'elig':>12}{'E[retire]':>22}"
           f"{'accel yrs':>20}")
    print(hdr)
    print(f"   {'':<20}{'a0 -> a1':>12}{'base -> purchased':>22}"
          f"{'elig / expected':>20}")
    print("   " + "-" * 72)
    rows = []
    for plan, age, svc, _note in PROFILES:
        p = Profile(plan, age, svc, MEAN_CLASSIFIED_SALARY, 45_000, 30)
        r = a29_profile(p, "State Employees", "M")
        rows.append((plan, age, svc, r))
        print(f"   {plan + f' age {age}/{svc}yr':<20}"
              f"{r['elig_baseline']:>5.1f}->{r['elig_with_purchase']:<5.1f}"
              f"{r['expected_retire_baseline']:>13.1f}->"
              f"{r['expected_retire_with_purchase']:<7.1f}"
              f"{r['elig_acceleration_years']:>9.2f} /"
              f"{r['expected_acceleration_years']:>8.2f}")

    print("\n   Cost decomposition, per purchasing member, PV today:\n")
    print(f"   {'Profile':<20}{'channel':<16}{'deterministic':>16}"
          f"{'Board rates':>16}{'survives':>11}")
    print("   " + "-" * 79)
    for plan, age, svc, r in rows:
        label = f"{plan} age {age}/{svc}yr"
        print(f"   {label:<20}{'amount':<16}{money(r['det_amount']):>16}"
              f"{money(r['beh_amount']):>16}"
              f"{r['beh_amount'] / r['det_amount']:>10.0%}")
        print(f"   {'':<20}{'acceleration':<16}"
              f"{money(r['det_acceleration']):>16}"
              f"{money(r['beh_acceleration']):>16}"
              f"{r['acc_survival']:>10.0%}")
        print(f"   {'':<20}{'TOTAL':<16}{money(r['det_total']):>16}"
              f"{money(r['beh_total']):>16}"
              f"{r['tot_survival']:>10.0%}")
        print()

    accs = [r["acc_survival"] for *_x, r in rows]
    tots = [r["tot_survival"] for *_x, r in rows]
    print(f"   Acceleration channel surviving:  {min(accs):.0%} - {max(accs):.0%}")
    print(f"   Full per-purchaser cost surviving: {min(tots):.0%} - {max(tots):.0%}")

    print("\n3. SEX SENSITIVITY (the tables are printed by sex)\n")
    print(f"   {'Profile':<22}{'group':<18}{'M total':>12}{'F total':>12}"
          f"{'spread':>10}")
    print("   " + "-" * 74)
    for plan, age, svc, _n in PROFILES:
        p = Profile(plan, age, svc, MEAN_CLASSIFIED_SALARY, 45_000, 30)
        for grp in ("State Employees", "Teachers"):
            rm = a29_profile(p, grp, "M")
            rf = a29_profile(p, grp, "F")
            spread = (abs(rm["beh_total"] - rf["beh_total"])
                      / max(rm["beh_total"], rf["beh_total"]))
            print(f"   {plan + f' age {age}/{svc}yr':<22}{grp:<18}"
                  f"{money(rm['beh_total']):>12}{money(rf['beh_total']):>12}"
                  f"{spread:>10.1%}")

    print("\n4. TEACHERS VERSUS STATE EMPLOYEES — the 22.50% footnote matters\n")
    print("   The Teacher Rule-of-90 rate is 22.50% against 11.50%-12.00% for")
    print("   state employees: teachers are assumed roughly twice as likely to")
    print("   retire the moment they qualify. Since the eligible pool is")
    print("   teacher-heavy (A-19, A-25), the pool-weighted survival sits")
    print("   nearer the Teacher leg than the state leg.\n")
    for plan, age, svc, _n in PROFILES:
        p = Profile(plan, age, svc, MEAN_CLASSIFIED_SALARY, 45_000, 30)
        rs = a29_profile(p, "State Employees", "M")
        rt = a29_profile(p, "Teachers", "M")
        print(f"   {plan + f' age {age}/{svc}yr':<22}"
              f"state {rs['tot_survival']:>5.0%}   "
              f"teacher {rt['tot_survival']:>5.0%}")

    print("\n5. VERIFICATION\n")
    ok = verify()
    print(f"\n   {'ALL CHECKS PASS' if ok else 'CHECKS FAILED'}")

    print("\n6. WHAT THIS DOES AND DOES NOT LICENCE\n")
    print("   DOES:  A-29 now has a published lower leg. The honest statement is")
    print("          a band - the deterministic figures are an upper bound, the")
    print("          Board-rate figures a lower bound, and the band is bounded")
    print("          on both sides by VRS's own published arithmetic.")
    print("   DOES NOT: licence replacing the headline with the lower leg.")
    print("          A purchaser is self-selected - someone who paid cash to")
    print("          move an eligibility date is not a random member. The")
    print("          selection runs the other way, toward the upper leg, and")
    print("          its size is unmeasurable without purchaser-level data")
    print("          (data request item 5). Publishing the lower leg alone")
    print("          would repeat the v1.1 error in the opposite direction.")
    print("=" * 78)


if __name__ == "__main__":
    main()
