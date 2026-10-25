"""S-9 and F-1A — pricing the § 2.2 ceiling's DOWNWARD leg, and its ceiling on recovery.

Fiscal & Impact Modeler response to red team § 10 (MOO-298).  Imports
`fm_model` unmodified; writes nothing.  Companion to the red team's
`rt_check2.py` and to this desk's `f1_lawful_class_rate.py`.

WHAT IS BEING PRICED
--------------------
Red team S-9 holds that the drafted § 2.2 ceiling -- "shall not require payment
of an amount exceeding the actuarial equivalent cost of the service credit
purchased" -- is a cap with no floor, so below the break-even purchase age a
lawful schedule must charge LESS than § 51.1-142.2 B 3 charges today.  That is
correct as a matter of drafting and it is unpriced anywhere in `fm_model`:
every scenario floors at the published approximate normal cost.

Red team F-1A holds that the same ceiling, read as the statutory AEC (the
benefit-amount channel, `aec_pct_of_salary`) rather than as full cost to the
Fund (`fm4_acceleration(...)["cost_total"]`), caps recovery of the above-ANC
excess at 10%-16% rather than the 59%-66% class mean at Annex 2 Closure
§ 4.8.1.

Both are priced here.  BOTH TURN ON THE SAME UNSTATED INPUT, and that is the
principal finding of this pass:

    *** the retirement age at which the AEC is measured ***

`aec_pct_of_salary(plan, purchase_age, retire_age)` takes it as an argument.
`rt_check2.py` and `fm_model`'s own `multiple_at()` / `fm2_surface()` pass
`PLAN_RETIRE_AGE` -- 65 for Plan 1, SSA NRA 67 for Plan 2 and Hybrid.  But
`fm4_acceleration()`, which produces the full-basis cost the ceiling is being
compared against, values the allowance at the member's OWN unreduced
eligibility age, which for most members is 46-58, not 65-67.  So the red team's
comparison -- and the package's own break-even story -- values the member's
price at age 65 against the member's benefit at age 57.5.  That is not a
like-for-like comparison, and the direction of the error is large.

Every figure below is therefore reported on BOTH bases:

  basis NRA   AEC measured at PLAN_RETIRE_AGE (65 / 67 / 67).  The red team's
              basis, and the model's existing convention.
  basis OWN   AEC measured at the member's own unreduced age WITH the credit,
              `unreduced_age(..., purchased=years)`.  The basis on which
              `fm4_acceleration` values the benefit the credit buys.
  basis OWN0  the same, measured at the member's own unreduced age WITHOUT the
              credit, `unreduced_age(..., purchased=0)`.  Carried only as a
              sensitivity, for the reason in the next paragraph.

THE OBVIOUS OBJECTION TO BASIS OWN, AND THE ANSWER.  If the ceiling's AEC is
measured at the member's own POST-purchase retirement date, is that not
smuggling the retirement-date acceleration back inside the ceiling, which is
precisely what F-1A says the statutory reading excludes?  No, and basis OWN0
is carried to prove it.  The acceleration channel in `fm4_acceleration` is the
cost of commencing the member's WHOLE allowance -- all years of service -- 2.5
years early.  Valuing the 2.5 PURCHASED years at an earlier commencement date
is a far smaller quantity, and it is a property of the credit itself, not of
what the member subsequently does with it.  OWN0 excludes even that sliver.
Part 1c reports both and does not minimise the gap: OWN0 cuts recovery by
12-16 percentage points against OWN and roughly triples the (still small)
leak.  But it does not restore the NRA figures -- recovery on OWN0 is 31%-45%
against NRA's 10%-16%, and the leak tops out at $2.3M against $32.8M -- so no
sign or ranking below turns on OWN versus OWN0.  Everything turns on NRA
versus OWN.

VRS does not publish which basis its own AEC factors use (FM-2 § 2.1: the
actuary develops a factor table annually and it is not published).  So neither
basis can be asserted as correct here.  The honest output is a band whose ends
differ by an order of magnitude, plus a data request.

Run:  python3 s9_subanc_leak.py
"""

from fm_model import (
    ANC,
    INSIDE_WINDOW_SHARE_OF_NONVESTED,
    MEAN_CLASSIFIED_SALARY,
    PLAN_RETIRE_AGE,
    Profile,
    TERMINAL_AGE,
    YEARS_PURCHASED_AVG,
    aec_pct_of_salary,
    breakeven_age,
    fm1_past_window,
    fm4_acceleration,
    money,
    price_a3_anc,
    unreduced_age,
)

# The corrected by-plan pool lives in `fm_model.fm1_pool_by_plan()`, which is
# the single source of that derivation as of the red team S-3 fix and which
# forbids restating the numbers -- two files each keeping a private copy is how
# S-3 survived as long as it did.  That fix is owned separately (MOO-296) and
# may land after this file, so the import is guarded rather than duplicated: if
# the function is not there yet, the post-S-3 sensitivity is reported as
# unavailable and every pre-S-3 figure still prints.  It is never recomputed
# here.
try:
    from fm_model import fm1_pool_by_plan
except ImportError:                                 # pragma: no cover
    fm1_pool_by_plan = None

PLANS = ("Plan 1", "Plan 2", "Hybrid")
SAL = MEAN_CLASSIFIED_SALARY          # F-34, DHRM slide 14, as of 6/30/2024
YEARS = YEARS_PURCHASED_AVG           # 2.5 -- § 4.8's own basis
BASES = ("NRA", "OWN")

# § 4.8 / FM-1's representative profiles, unchanged, so every figure below is
# comparable to the published grid.
REPS = {
    "Plan 1": Profile("Plan 1", 55, 25, SAL, 45_000, 30),
    "Plan 2": Profile("Plan 2", 50, 14, SAL, 55_000, 36),
    "Hybrid": Profile("Hybrid", 50, 9, SAL, 60_000, 41),
}

# Plan-structural feasibility of (age, service) pairs, as of June 30, 2026.
# SOURCED, not assumed: ACFR Fig. 2.10 closes Plan 1 to membership dates before
# July 1, 2010 and Plan 2 (apart from the hazardous-duty and, from July 1, 2026,
# judicial openings) before January 1, 2014.  So a Plan 1 member necessarily has
# >= 16 years of membership and a Hybrid member necessarily has <= 12.5.  Lower
# bound 2.0 everywhere because the pool is defined as members PAST the 24-month
# window.  Upper bound age - 18 because service cannot precede employment.
SERVICE_FLOOR = {"Plan 1": 16.0, "Plan 2": 2.0, "Hybrid": 2.0}
SERVICE_CEIL = {"Plan 1": 99.0, "Plan 2": 16.0, "Hybrid": 12.5}

TAKEUP_BLEND = 0.20                   # A-22 Moderate, the § 4.8.1 basis


# ---------------------------------------------------------------------------
# pricing primitives
# ---------------------------------------------------------------------------

def anc_price(plan, years=YEARS, salary=SAL):
    """What § 51.1-142.2 B 3 charges TODAY inside the window, and what the
    draft's 0% dial setting charges.  OFFICIAL rate (F-25 / FM-5)."""
    return ANC[(plan, "non-hazardous")] * salary * years


def aec_retire_age(basis, plan, age, service, years=YEARS):
    """The retirement age at which the ceiling's AEC is measured."""
    if basis == "NRA":
        return float(PLAN_RETIRE_AGE[plan])
    purchased = years if basis == "OWN" else 0.0
    return unreduced_age(plan, age, float(service), purchased=purchased)


def ceiling_price(basis, plan, age, service, years=YEARS, salary=SAL):
    """The § 2.2 ceiling.

    On bases NRA / OWN / OWN0 this is the STATUTORY reading of "actuarial
    equivalent cost" -- the benefit-amount channel only, which is what
    `aec_pct_of_salary` models and what § 51.1-142.2 B 3 charges after 24
    months today.  Basis FULL is the FULL-COST reading, i.e. § 4.8.1's own, and
    it is carried through the same machinery so that § 4.8.1's published band
    reproduces here as a special case rather than being transcribed.
    """
    if basis == "FULL":
        return full_value(plan, age, service, years, salary)
    r = aec_retire_age(basis, plan, age, service, years)
    return aec_pct_of_salary(plan, age, r) * salary * years


def full_value(plan, age, service, years=YEARS, salary=SAL):
    """Full cost to the Fund: benefit-amount channel PLUS retirement-date
    acceleration.  What `price_threshold_graded` charges at the 100% dial, and
    the quantity § 4.8's 0% row nets the ANC price against."""
    p = Profile(plan, age, float(service), salary, salary, 30)
    return fm4_acceleration(p, years_purchased=years)["cost_total"]


def feasible(plan, age, service):
    """Is this (age, service) pair possible under the plan-date rules, and is
    the member priceable at all?

    Members who never reach unreduced eligibility inside the annuity-certain
    horizon are excluded: their modelled full value is 0 because the basis
    terminates at age 87.  That is a basis artefact, not a pricing fact, and
    `f1_lawful_class_rate.class_stats` excludes them for the same reason.
    """
    if not SERVICE_FLOOR[plan] <= service <= min(SERVICE_CEIL[plan], age - 18):
        return False
    return unreduced_age(plan, age, float(service), purchased=YEARS) < TERMINAL_AGE


def rule(title):
    print(f"\n{'=' * 78}\n  {title}\n{'=' * 78}")


# ---------------------------------------------------------------------------
# PART 1 — the downward leg, on both bases
# ---------------------------------------------------------------------------

def part1_breakevens():
    rule("PART 1  The ceiling's downward leg — where it bites, on both bases")
    print("  The ceiling bites DOWNWARD wherever the member's own AEC is below the")
    print("  published approximate normal cost, because the schedule may then not")
    print("  charge the published rate.  On the NRA basis that is a purchase-age")
    print("  test and service is irrelevant (aec_pct_of_salary does not see")
    print("  service).  On the OWN basis it is an age-AND-service test, because")
    print("  service is what sets the unreduced date.\n")

    be = {}
    print(f"  {'plan':<9}{'ANC rate':>10}{'ANC price':>12}"
          f"{'break-even age, NRA basis':>28}")
    for plan in PLANS:
        b = breakeven_age(plan, PLAN_RETIRE_AGE[plan],
                          ANC[(plan, "non-hazardous")])
        be[plan] = b
        print(f"  {plan:<9}{ANC[(plan, 'non-hazardous')]:>9.2%}"
              f"{money(anc_price(plan)):>12}{b:>28.2f}")

    print("\n  Same test on the OWN basis — the share of FEASIBLE (age, service)")
    print("  pairs at which the ceiling is below the published price:\n")
    print(f"  {'plan':<9}{'feasible pairs':>16}{'leaking, NRA':>15}"
          f"{'leaking, OWN':>15}")
    leaking = {}
    for plan in PLANS:
        pairs = [(a, s) for a in range(25, 65)
                 for s in range(0, 45) if feasible(plan, a, s)]
        nra = [1 for a, s in pairs if ceiling_price("NRA", plan, a, s)
               < anc_price(plan)]
        own = [1 for a, s in pairs if ceiling_price("OWN", plan, a, s)
               < anc_price(plan)]
        leaking[plan] = (len(pairs), len(nra), len(own))
        print(f"  {plan:<9}{len(pairs):>16,}"
              f"{f'{len(nra):,} ({len(nra) / len(pairs):.0%})':>15}"
              f"{f'{len(own):,} ({len(own) / len(pairs):.0%})':>15}")

    print("""
  READ THIS BEFORE THE DOLLARS.  The leak is real on the red team's NRA basis
  and it very nearly vanishes on the OWN basis.  The reason is structural: a
  member's own unreduced age is typically 46-58, not 65-67, so measuring the
  AEC at the plan's normal retirement age understates it by the whole
  difference in annuity-commencement timing.  Measured at the date the member
  will actually retire, the AEC of a year of credit EXCEEDS the published
  approximate normal cost for almost every member who has any service at all.
  The survivors are low-service members just past the 24-month window.""")
    return be, leaking


def part1_grid(be):
    print(f"\n  Per-member leak = ANC price − ceiling, {YEARS:g} years at "
          f"{money(SAL)}.  Zero means no leak.\n")
    for plan in PLANS:
        print(f"  {plan} — ANC price {money(anc_price(plan))}, "
              f"break-even (NRA) {be[plan]:.2f}, service feasible "
              f"{SERVICE_FLOOR[plan]:g}–"
              f"{SERVICE_CEIL[plan] if SERVICE_CEIL[plan] < 90 else '—'}")
        svcs = [s for s in (3, 10, 16, 20, 28)
                if SERVICE_FLOOR[plan] <= s <= SERVICE_CEIL[plan]]
        print(f"    {'age':>5}{'leak, NRA':>12}"
              + "".join(f"{f'OWN svc {s:g}':>13}" for s in svcs))
        for age in (30, 35, 40, 45, 50):
            cells = ""
            for s in svcs:
                if not feasible(plan, age, s):
                    cells += f"{'n/a':>13}"
                    continue
                lk = max(0.0, anc_price(plan) - ceiling_price("OWN", plan, age, s))
                cells += f"{money(lk):>13}"
            lk_nra = max(0.0, anc_price(plan) - ceiling_price("NRA", plan, age, 10))
            print(f"    {age:>5}{money(lk_nra):>12}{cells}")
        print()


def part1c_basis_sensitivity(be):
    """Does the OWN result depend on measuring the AEC at the member's
    post-purchase rather than pre-purchase unreduced age?  See the docstring:
    if it did, basis OWN would be smuggling the acceleration channel into the
    ceiling, which is the one thing F-1A says the statutory reading excludes."""
    print("  1c. OWN vs OWN0 — the objection that basis OWN smuggles")
    print("      acceleration into the ceiling.  OWN0 measures the AEC at the")
    print("      member's PRE-purchase unreduced age and so excludes it entirely.\n")
    print(f"  {'plan':<9}{'mean leak OWN':>15}{'mean leak OWN0':>16}"
          f"{'rec OWN':>10}{'rec OWN0':>10}")
    for plan in PLANS:
        p = REPS[plan]
        a = price_a3_anc(p, YEARS)
        full = fm4_acceleration(p, years_purchased=YEARS)["cost_total"]
        cells = ""
        for basis in ("OWN", "OWN0"):
            c = ceiling_price(basis, plan, p.age, p.service)
            cells += f"{(c - a) / (full - a):>10.0%}"
        m1, _ = cohort_mean(plan, "OWN", 25, int(be[plan]), leak_of)
        m0, _ = cohort_mean(plan, "OWN0", 25, int(be[plan]), leak_of)
        print(f"  {plan:<9}{money(m1):>15}{money(m0):>16}{cells}")
    print("""
      The objection has some force and it is reported, not waved away. OWN0
      cuts recovery by 12-16 percentage points against OWN, and it roughly
      triples the mean leak in Plan 2 and Hybrid. But it does not restore the
      NRA figures and it does not change a conclusion:

        * recovery on OWN0 is 31%-45%, still far above NRA's 10%-16%;
        * the mean leak on OWN0 is about $400 per member against NRA's
          $3,200-$5,400, so the aggregate leak tops out at $2.3M across
          every cell of Part 3, against $32.8M on the NRA basis.

      So the sensitivity that governs both findings is normal-retirement-age
      versus own-retirement-age. OWN is used below as the more coherent of
      the two own-date variants; substituting OWN0 moves the numbers and
      leaves every sign and ranking intact.
""")


# ---------------------------------------------------------------------------
# PART 2 — how big is the leaking cohort?
# ---------------------------------------------------------------------------

def nonvested_past_window_share():
    """DERIVED, from OFFICIAL inputs.  The share of the past-window population
    that is non-vested, i.e. has under five years of creditable service.

    This matters because on the OWN basis the leak survives only for low-service
    members, and this is the one handle on that cohort's size that does NOT
    require an age distribution: the vested / non-vested split is official (ACFR
    Fig. 2.9) and `fm1_past_window` already carries it.  The non-vested members
    who are PAST the 24-month window are nonvested x (1 - inside-window share).
    """
    pw = fm1_past_window()
    nv_lo = sum(d["nonvested"] * INSIDE_WINDOW_SHARE_OF_NONVESTED[0]
                for d in pw.values())
    nv_hi = sum(d["nonvested"] * INSIDE_WINDOW_SHARE_OF_NONVESTED[1]
                for d in pw.values())
    pw_lo = sum(d["past_window_lo"] for d in pw.values())
    pw_hi = sum(d["past_window_hi"] for d in pw.values())
    return nv_lo / pw_lo, nv_hi / pw_hi


# Share of the eligible pool below the break-even PURCHASE AGE.  This is a
# SCENARIO ASSUMPTION, not a derived estimate, and it cannot be made one: the
# age distribution of the veteran pool is not published (A-22 / U-01, and the
# § 4.8.1 note that no weighting inside a plan is defensible).  The anchors that
# bound it are:
#   * DHRM F-32 — classified workforce average age 46.7, which sits 0.1 years
#     BELOW the Plan 1 break-even of 46.60 and about a year below Plan 2's
#     47.43 and Hybrid's 48.16.  A symmetric distribution about that mean puts
#     roughly half the workforce under the break-even age.
#   * DHRM F-32 — average age of new hires 37.7, well under every break-even.
#   * Against that: Plan 1 is closed to membership dates before July 1, 2010,
#     so its members necessarily have >= 16 years of membership and skew old;
#     Hybrid opened January 1, 2014 and skews young.  The share should
#     therefore be LOW in Plan 1 and HIGH in Hybrid, which is the opposite of
#     where the per-member leak is largest.
UNDER_BE_SHARE = {"Low": 0.25, "Central": 0.50, "High": 0.65}

# Take-up among the under-break-even cohort.  SCENARIO ASSUMPTION.  Reported
# separately from the A-22 blend because the blend is the wrong rate for this
# cohort in a direction that is arguable BOTH ways, and the issue asks for it:
#   upward   — for these members the bill makes the price LOWER than today's
#              Code price, they have the longest runway over the 60-month
#              payroll-deduction term, and they are the cheapest purchase in
#              absolute dollars, so liquidity binds least;
#   downward — they are decades from any eligibility date, the purchase buys
#              them nothing they can feel, and § 51.1-142.2 purchases have
#              historically clustered near retirement (U-01, unpublished).
TAKEUP_UNDER = {"at the blend": 0.20, "elevated": 0.30, "stress": 0.50}


def cohort_mean(plan, basis, lo_age, hi_age, fn):
    """Equal-weighted mean of `fn` over feasible (age, service) pairs in an age
    window.  Equal weighting is the only defensible choice: see the note on
    UNDER_BE_SHARE, and § 4.8.1's identical reasoning about class weighting."""
    vals = [fn(plan, basis, a, s)
            for a in range(int(lo_age), int(hi_age) + 1)
            for s in range(0, 45) if feasible(plan, a, s)]
    return (sum(vals) / len(vals), len(vals)) if vals else (0.0, 0)


def leak_of(plan, basis, age, service):
    return max(0.0, anc_price(plan) - ceiling_price(basis, plan, age, service))


def net_of(plan, basis, age, service):
    """Residual net cost to the Fund per purchaser once the ceiling binds:
    full cost to the Fund minus the most the schedule may lawfully charge."""
    lawful = min(anc_price(plan), ceiling_price(basis, plan, age, service))
    return full_value(plan, age, service) - lawful


def part2(be):
    rule("PART 2  How many purchasers are in the leaking cohort?")
    nv_lo, nv_hi = nonvested_past_window_share()
    print(f"  DERIVED from official inputs — non-vested share of the past-window")
    print(f"  population, which is the cohort in which the leak survives on the")
    print(f"  OWN basis:  {nv_lo:.1%} – {nv_hi:.1%} of the pool.")
    print(f"  (nonvested x {INSIDE_WINDOW_SHARE_OF_NONVESTED[0]:.0%}–"
          f"{INSIDE_WINDOW_SHARE_OF_NONVESTED[1]:.0%} past-window share, over the")
    print(f"  past-window population.  Vested/non-vested split is OFFICIAL.)\n")
    print("  SCENARIO — share of the pool below the break-even PURCHASE AGE,")
    print("  which is the cohort on the NRA basis.  Not derivable; the age")
    print("  distribution of the pool is unpublished (A-22 / U-01):")
    for k, v in UNDER_BE_SHARE.items():
        print(f"    {k:<10}{v:>6.0%}")
    print(f"\n  Mean per-member leak inside the leaking cohort, {YEARS:g} years "
          f"at {money(SAL)}:\n")
    print(f"  {'plan':<9}{'age window':>14}{'pairs':>8}{'mean leak, NRA':>17}"
          f"{'mean leak, OWN':>17}")
    means = {}
    for plan in PLANS:
        hi = be[plan]
        m_nra, n = cohort_mean(plan, "NRA", 25, int(hi), leak_of)
        m_own, _ = cohort_mean(plan, "OWN", 25, int(hi), leak_of)
        means[plan] = {"NRA": m_nra, "OWN": m_own, "n": n}
        print(f"  {plan:<9}{f'25–{hi:.1f}':>14}{n:>8,}"
              f"{money(m_nra):>17}{money(m_own):>17}")
    print("""
  The OWN-basis column is near zero for Plan 1 because Plan 1's closure makes
  a young, low-service Plan 1 member nearly impossible: under 46.6 with at
  least 16 years of membership means hired before age 30.6.  Those members do
  exist, but they have the service that pushes their own unreduced date to
  age 50 and their AEC above the published price.""")
    return means


# ---------------------------------------------------------------------------
# PART 3 — the aggregate leak
# ---------------------------------------------------------------------------

# The by-plan eligible pool.  TWO BASES, deliberately, because the package is
# mid-correction and the two subsections must not be read against two pools.
#
# POOL_PREFIX is a FROZEN HISTORICAL CONSTANT, not a live derivation.  It is the
# by-plan pool as `fm_model` produced it BEFORE the red team S-3 pool-pairing
# fix, and it is the basis on which Annex 2 Closure § 4.8.1 and red team § 10.3
# publish $52.0M-$121.5M.  It is kept here only so that the figures in this file
# can be lined up against those published figures; it must not be used for
# anything else, and it should be deleted once § 4.8.1 is restated.
POOL_PREFIX = {"Plan 1": (3_966, 9_027), "Plan 2": (2_417, 5_502),
               "Hybrid": (4_177, 11_792)}


def pool_postfix():
    """The corrected by-plan pool, IMPORTED from `fm1_pool_by_plan()`.

    Post-fix it agrees with the by-employer-group derivation at both ends,
    which is what M-4 asked for.  Returns None if the S-3 fix has not landed
    yet; see the guarded import above.
    """
    if fm1_pool_by_plan is None:
        return None
    by_plan, _eff_lo, _eff_hi, _lo, _hi = fm1_pool_by_plan()
    return by_plan


def aggregate(pool, per_member, share, takeup, end):
    """sum over plans of pool x cohort share x take-up x per-member amount."""
    return sum(pool[p][end] * share * takeup * per_member[p] for p in PLANS)


def part3(means):
    rule("PART 3  Aggregate value of the leak — one-time PV, both pool ends")
    pools = {}
    post = pool_postfix()
    if post is None:
        print("\n  NOTE: fm_model.fm1_pool_by_plan() not present, so the red team")
        print("  S-3 pool correction has not landed yet. The corrected pool is")
        print("  omitted below rather than recomputed here.")
    else:
        pools["post-S-3, CORRECTED — the live basis"] = post
    pools["pre-S-3 — superseded, kept to tie to published figures"] = POOL_PREFIX
    out = {}
    for pool_label, pool in pools.items():
        tot = (sum(pool[p][0] for p in PLANS), sum(pool[p][1] for p in PLANS))
        print(f"\n  Pool basis: {pool_label}   {tot[0]:,.0f} – {tot[1]:,.0f}")
        for basis in BASES:
            pm = {p: means[p][basis] for p in PLANS}
            print(f"\n    AEC basis {basis} — mean leak "
                  + ", ".join(f"{p} {money(pm[p])}" for p in PLANS))
            print(f"      {'under-BE share':<18}"
                  + "".join(f"{f'take-up {t:.0%}':>25}" for t in
                            TAKEUP_UNDER.values()))
            for sk, sv in UNDER_BE_SHARE.items():
                cells = ""
                for tk, tv in TAKEUP_UNDER.items():
                    lo = aggregate(pool, pm, sv, tv, 0)
                    hi = aggregate(pool, pm, sv, tv, 1)
                    cells += f"{f'{lo / 1e6:.1f} – {hi / 1e6:.1f}':>25}"
                    out[(pool_label, basis, sk, tk)] = (lo, hi)
                print(f"      {f'{sk} ({sv:.0%})':<18}{cells}")
            print(f"      (figures are $M, one-time PV, low pool end – high "
                  f"pool end)")
    print("""
  The cell to quote is Central share x elevated take-up, because the issue's
  own reasoning is that this cohort buys above the blend.  On the NRA basis
  that is $6M-$15M; on the OWN basis it is under $0.4M and immaterial.  The
  leak is not a number -- it is a number TIMES an unstated basis choice.""")
    return pools, out


# ---------------------------------------------------------------------------
# PART 4 — the § 4.8.1 residual, with and without the leak
# ---------------------------------------------------------------------------

def rep_net():
    """§ 4.8's 0% row, from the representative profiles — the quantity § 4.8.1's
    residual table is built on."""
    out = {}
    for plan, p in REPS.items():
        out[plan] = (fm4_acceleration(p, years_purchased=YEARS)["cost_total"]
                     - price_a3_anc(p, YEARS))
    return out


def part4(pools, means, be):
    rule("PART 4  § 4.8.1's residual, WITH and WITHOUT the leak")
    net0 = rep_net()
    print("  § 4.8's 0% row reproduced: "
          + ", ".join(f"{p} {money(net0[p])}" for p in net0))
    print(f"\n  (A) AS ASKED — § 4.8.1's residual at the published recovery")
    print(f"      settings, plus the leak at Central share x elevated take-up.")
    print(f"      The two terms OVERLAP: § 4.8.1 prices the whole pool at the")
    print(f"      representative profile, which is above break-even in all three")
    print(f"      plans, so the under-break-even cohort is counted twice. This")
    print(f"      presentation is an UPPER bound on the leak's effect; (B) is")
    print(f"      the clean decomposition.\n")

    # § 4.8.1's full-cost-reading class means, recomputed through this file's
    # own class sweep rather than transcribed. Reproduces § 4.8.1 and
    # f1_lawful_class_rate.py exactly: 0%-96% / 0%-92% / 0%-92%, means
    # 59% / 66% / 65%, and 4 of 60 classes breached by the baseline price.
    full_sweep = class_sweep("FULL")
    plan_mean = {p: full_sweep[p]["mean"] for p in PLANS}
    settings = [("0% — plain published ANC", 0.0),
                ("59%–66% class mean (full-cost reading)", None),
                ("96% best class", 0.96)]

    for pool_label, pool in pools.items():
        print(f"  Pool basis: {pool_label}")
        for label, rec in settings:
            resid = {p: net0[p] * (1 - (plan_mean[p] if rec is None else rec))
                     for p in PLANS}
            base_lo = aggregate(pool, resid, 1.0, TAKEUP_BLEND, 0)
            base_hi = aggregate(pool, resid, 1.0, TAKEUP_BLEND, 1)
            print(f"    {label:<40}"
                  f"{f'{money(base_lo)} – {money(base_hi)}':>26}  no leak")
            for basis in BASES:
                pm = {p: means[p][basis] for p in PLANS}
                lk_lo = aggregate(pool, pm, UNDER_BE_SHARE["Central"],
                                  TAKEUP_UNDER["elevated"], 0)
                lk_hi = aggregate(pool, pm, UNDER_BE_SHARE["Central"],
                                  TAKEUP_UNDER["elevated"], 1)
                print(f"    {'':<40}"
                      f"{f'{money(base_lo + lk_lo)} – {money(base_hi + lk_hi)}':>26}"
                      f"  + leak, {basis}")
        print()

    print("  (B) CLEAN DECOMPOSITION — the pool split at the break-even age,")
    print("      each cohort priced on its own profiles and its own take-up,")
    print("      at the 59%–66% class-mean recovery for the above-break-even")
    print("      cohort and the lawful ceiling for the cohort below it.\n")
    # Reported on BOTH pools, as (A) and Part 3 already are. This loop was
    # pinned to the pre-S-3 pool until October 25, 2026; it was widened in the
    # MOO-301 reconciliation pass, because 04 section 4.8.3 (4) quotes these
    # cells and had no corrected-pool figure to quote.
    for pool_label, pool in pools.items():
        print(f"    Pool basis: {pool_label}")
        for basis in BASES:
            print(f"    AEC basis {basis}")
            print(f"      {'plan':<9}{'net/purchaser above BE':>24}"
                  f"{'net/purchaser below BE':>24}")
            net_above, net_below = {}, {}
            for plan in PLANS:
                na = net0[plan] * (1 - plan_mean[plan])
                nb, _ = cohort_mean(plan, basis, 25, int(be[plan]), net_of)
                net_above[plan], net_below[plan] = na, nb
                print(f"      {plan:<9}{money(na):>24}{money(nb):>24}")
            for sk, sv in UNDER_BE_SHARE.items():
                for tk, tv in TAKEUP_UNDER.items():
                    lo = (aggregate(pool, net_above, 1 - sv, TAKEUP_BLEND, 0)
                          + aggregate(pool, net_below, sv, tv, 0))
                    hi = (aggregate(pool, net_above, 1 - sv, TAKEUP_BLEND, 1)
                          + aggregate(pool, net_below, sv, tv, 1))
                    print(f"      share {sv:.0%}, below-BE take-up {tv:.0%}"
                          f"{f'{money(lo)} – {money(hi)}':>30}")
            print()
    print("""  Note which way (B) runs.  Below the break-even age the member's own
  full cost to the Fund is SMALL -- the allowance is decades away and heavily
  discounted -- so even after the ceiling cuts the price, the residual per
  purchaser below break-even is well under the representative profile's. A
  pool that is half young purchasers is CHEAPER in total than § 4.8.1's
  flat-profile arithmetic implies, leak included. The leak is a real receipts
  loss against current law; it is not a reason to raise the § 4.8.1 headline.""")
    return net0


# ---------------------------------------------------------------------------
# PART 5 — F-1A, and how it compounds with F-1
# ---------------------------------------------------------------------------

AGE_BANDS = [(40, 44), (45, 49), (50, 54), (55, 59), (60, 64)]
SVC_BANDS = [(0, 9), (10, 19), (20, 29), (30, 39)]


def class_sweep(basis):
    """F-1A compounded with F-1.  A lawful uniform class price is
    max(ANC price, min over the class of the CEILING); under the statutory
    reading the ceiling is the AEC rather than full cost, so the class minimum
    is lower and the uniform price is pinned lower.  Returns, per plan, the
    recovery band and mean across that plan's priceable classes, plus a count
    of classes in which the published ANC price itself exceeds the lowest
    member's ceiling (the § 4.8.1 four-class point, re-run on this basis).
    """
    per_plan = {}
    for plan in PLANS:
        recs, breached = [], 0
        for ab in AGE_BANDS:
            for sb in SVC_BANDS:
                vals = [(ceiling_price(basis, plan, a, s),
                         full_value(plan, a, s))
                        for a in range(ab[0], ab[1] + 1)
                        for s in range(sb[0], sb[1] + 1)
                        if unreduced_age(plan, a, float(s),
                                         purchased=YEARS) < TERMINAL_AGE]
                if not vals:
                    continue
                a_pr = anc_price(plan)
                lo_ceil = min(v[0] for v in vals)
                mean_full = sum(v[1] for v in vals) / len(vals)
                if mean_full <= a_pr:
                    continue
                if lo_ceil < a_pr:
                    breached += 1
                recs.append(max(0.0, (max(a_pr, lo_ceil) - a_pr)
                                / (mean_full - a_pr)))
        per_plan[plan] = {"lo": min(recs), "hi": max(recs),
                          "mean": sum(recs) / len(recs),
                          "n": len(recs), "breached": breached}
    return per_plan


def part5(pools, net0):
    rule("PART 5  F-1A — what the ceiling caps recovery at, on both bases")
    print(f"  5a. PER MEMBER, on § 4.8's representative profiles, {YEARS:g} "
          f"years, {money(SAL)}.")
    print("      max lawful recovery = (ceiling − ANC price) / (full cost − ANC price)")
    print("      This is the figure red team § 10.1 reports as 10%–16%; it")
    print("      reproduces exactly on the NRA basis.\n")
    print(f"  {'plan':<9}{'ANC price':>11}{'full cost':>11}{'net0':>11}"
          f"{'ceil NRA':>11}{'rec NRA':>9}{'ceil OWN':>11}{'rec OWN':>9}")
    rec = {b: {} for b in BASES}
    for plan, p in REPS.items():
        a = price_a3_anc(p, YEARS)
        full = fm4_acceleration(p, years_purchased=YEARS)["cost_total"]
        cells = ""
        for basis in BASES:
            c = ceiling_price(basis, plan, p.age, p.service)
            r = (c - a) / (full - a) if full > a else 0.0
            rec[basis][plan] = max(0.0, min(1.0, r))
            cells += f"{money(c):>11}{f'{r:.0%}':>9}"
        print(f"  {plan:<9}{money(a):>11}{money(full):>11}{money(full - a):>11}"
              f"{cells}")

    print("\n  5b. COMPOUNDED WITH F-1's uniformity constraint — the figure")
    print("      § 4.8.1 actually needs, because § 4.8.1's band is a CLASS band")
    print("      and § 10.1's 10%–16% is a three-profile per-member figure.")
    print("      Lawful uniform class price = max(ANC price, min of the class's")
    print("      ceilings); 60-class sweep, same classes as § 4.8.1.\n")
    sweeps = {}
    print(f"  {'basis':<7}{'plan':<9}{'classes':>9}{'recovery band':>18}"
          f"{'mean':>7}{'ANC > lowest ceiling':>23}")
    for basis in BASES + ("FULL",):
        sweeps[basis] = class_sweep(basis)
        for plan in PLANS:
            st = sweeps[basis][plan]
            band = "{:.0%} – {:.0%}".format(st["lo"], st["hi"])
            br = "{} of {}".format(st["breached"], st["n"])
            print(f"  {basis:<7}{plan:<9}{st['n']:>9}{band:>18}"
                  f"{st['mean']:>7.0%}{br:>23}")

    print(f"\n  5c. RESIDUAL PV at {TAKEUP_BLEND:.0%} take-up, the two readings "
          f"side by side.\n")
    for pool_label, pool in pools.items():
        print(f"    {pool_label}")
        for label, f in (
            ("0% — no schedule adopted", lambda p: 0.0),
            ("statutory reading, NRA, per member (§ 10.1)",
             lambda p: rec["NRA"][p]),
            ("statutory reading, NRA, class mean",
             lambda p: sweeps["NRA"][p]["mean"]),
            ("statutory reading, OWN, class mean",
             lambda p: sweeps["OWN"][p]["mean"]),
            ("full-cost reading, class mean (§ 4.8.1)",
             lambda p: sweeps["FULL"][p]["mean"]),
            ("100% individualised — NOT LAWFUL", lambda p: 1.0),
        ):
            resid = {p: net0[p] * (1 - f(p)) for p in PLANS}
            lo = aggregate(pool, resid, 1.0, TAKEUP_BLEND, 0)
            hi = aggregate(pool, resid, 1.0, TAKEUP_BLEND, 1)
            print(f"      {label:<44}"
                  f"{f'{money(lo)} – {money(hi)}':>26}")
        print()

    print("""  How to read 5b against 5a.  The red team's 10%–16% is a per-member
  figure on three profiles; it is right on the NRA basis and it is NOT the
  class band. Once uniformity compounds, the statutory reading gives a class
  mean of 22% on the NRA basis against § 4.8.1's 63% on the full-cost reading
  -- so the issue's expectation holds: the statutory reading pushes the
  residual most of the way back to the 0% row. On the OWN basis the two
  readings converge, because there the ceiling sits above the published price
  for most members and uniformity is the only constraint that bites -- which
  is F-1 exactly as § 4.8.1 already publishes it.""")
    return sweeps


# ---------------------------------------------------------------------------
# PART 6 — what only VRS can settle
# ---------------------------------------------------------------------------

def part6():
    rule("PART 6  The data request this pass generates")
    print("""  1. THE RETIREMENT-AGE BASIS OF THE AEC FACTORS.  New, and it now
     outranks most of the existing list. § 51.1-142.2 B 3 charges the
     "actuarial equivalent cost" today, so VRS's actuary already has a factor
     table (FM-2 § 2.1-2.2) and that table embeds a retirement-age assumption.
     Everything in Parts 1-5 swings by an order of magnitude on it. Ask: at
     what assumed retirement age, or on what retirement-decrement basis, are
     the post-24-month AEC factors developed, and are they a function of age
     at purchase alone or of age and service?

  2. Does any current VRS purchase price include a retirement-date
     acceleration component? (Red team F-1A asserts none ever has; routed to
     Statutory Researcher. If the answer is no, the full-cost reading of the
     drafted ceiling has no precedent in VRS practice and the 59%-66% band at
     § 4.8.1 rests on the weaker of the two readings.)

  3. Age-at-purchase distribution of completed § 51.1-142.2 purchases, ten
     years. This converts UNDER_BE_SHARE from a scenario into an estimate and
     is the single input that would most narrow Part 3.

  4. Service distribution of veterans past the 24-month window, by plan.
     Part 2's non-vested handle is a proxy for it.""")


if __name__ == "__main__":
    print(__doc__.split("Run:")[0].strip()[:0] or "", end="")
    be, _ = part1_breakevens()
    part1_grid(be)
    part1c_basis_sensitivity(be)
    means = part2(be)
    pools, _ = part3(means)
    net0 = part4(pools, means, be)
    part5(pools, net0)
    part6()
    print(f"\n{'-' * 78}")
    print("  Fiscal & Impact Modeler working file, MOO-298. fm_model.py imported")
    print("  unmodified; nothing written. Illustrative model, not a VRS")
    print("  actuarial certification.")
    print(f"{'-' * 78}")
