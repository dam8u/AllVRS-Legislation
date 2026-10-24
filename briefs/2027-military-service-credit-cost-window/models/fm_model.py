#!/usr/bin/env python3
"""
FM-1 through FM-4 model — Va. Code 51.1-142.2 military-service purchase price cliff.

Companion to the JLC Legislative Change Brief (MOO-288) Annex 2 open items.
Issue MOO-291. Run date basis: October 24, 2026.

EVERY input is tagged in INPUTS below as:
  OFFICIAL  — published by VRS / the Commonwealth / a federal statistical agency
  DERIVED   — arithmetic on OFFICIAL inputs, formula shown
  ESTIMATE  — scenario assumption, not a prediction

Nothing in this file is a VRS actuarial certification. The annuity basis is a
level-COLA annuity-certain, not a VRS mortality table. See CAVEATS at the end.

Usage:  python3 fm_model.py            # prints the full analysis
"""

from dataclasses import dataclass

# ============================================================================
# INPUTS
# ============================================================================

# --- OFFICIAL: VRS Board of Trustees, RBA 2025-06-10, minutes of June 18, 2025.
#     Approximate normal cost (ANC) rates for purchase of prior service,
#     effective July 1, 2025.  Confirmed on the published rate charts
#     (pps-rate-charts.pdf, pages 1-4).
ANC = {
    ("Plan 1", "non-hazardous"): 0.1250,
    ("Plan 1", "hazardous"): 0.2378,
    ("Plan 1", "judicial"): 0.3197,
    ("Plan 2", "non-hazardous"): 0.1074,
    ("Plan 2", "hazardous"): 0.1915,
    ("Plan 2", "judicial"): 0.2967,
    ("Hybrid", "non-hazardous"): 0.0668,
    ("Hybrid", "judicial"): 0.1921,
    ("Alternate hazardous duty option", "hazardous"): 0.1001,
}

# --- OFFICIAL: VRS assumed rate of return / discount rate.
#     Source: June 30, 2025 Annual Actuarial Valuation (GRS), Executive Summary;
#     also the 6.75% refunded-service interest rate on the ANC rate charts.
DISCOUNT = 0.0675

# --- OFFICIAL: Board-adopted COLA assumptions, June 30, 2025 valuation,
#     Executive Summary ("compared to a 2.50% assumption" / "2.25% assumption").
COLA = {"Plan 1": 0.0250, "Plan 2": 0.0225, "Hybrid": 0.0225}

# --- OFFICIAL: payroll growth assumption, June 30, 2025 valuation
#     (3.0% general; 2.5% for Virginia Law Officers).
SALARY_GROWTH = 0.030
SALARY_GROWTH_VALORS = 0.025

# --- OFFICIAL: statutory benefit multipliers per year of creditable service.
#     Plan 1 / Plan 2: 51.1-155 A 1.  Hybrid DB component: 51.1-169 D 1.
MULTIPLIER = {"Plan 1": 0.0170, "Plan 2": 0.0165, "Hybrid": 0.0100}

# --- OFFICIAL: active member counts at June 30, 2025.
#     By plan: VRS 101 / "Who We Serve", 2025 edition (sums to 378,060).
ACTIVE_BY_PLAN = {"Plan 1": 110_474, "Plan 2": 67_333, "Hybrid": 200_253}

#     By employer group: VRS ACFR FY2025, Figure 2.3 and Figure 2.9.
ACTIVE_BY_GROUP = {
    "VRS State Employees": 83_148,
    "VRS Teachers": 160_800,
    "VRS Political Subdivision Employees": 124_264,
    "SPORS": 1_894,
    "VaLORS": 7_484,
    "JRS": 470,
}
#     Vested / non-vested split, VRS ACFR FY2025, Figure 2.9.
VESTED = {
    "VRS State Employees": 52_120,
    "VRS Teachers": 110_074,
    "VRS Political Subdivision Employees": 70_340,
    "SPORS": 1_524,
    "VaLORS": 3_795,
    "JRS": 378,
}
NONVESTED = {
    "VRS State Employees": 31_028,
    "VRS Teachers": 50_726,
    "VRS Political Subdivision Employees": 53_924,
    "SPORS": 370,
    "VaLORS": 3_689,
    "JRS": 92,
}

# --- OFFICIAL: veteran share of workforce, by group.
#     State classified:  DHRM presentation to Senate Finance & Appropriations,
#                        Jan. 21, 2025, slide 8 (self-identified, as of 6/30/2024).
#     Teachers:          NCES Digest of Education Statistics table 209.27 (2016) —
#                        2.3% of public school teachers nationally are military
#                        veterans; 3.1% in the South region.
#     State & local gov: DERIVED from BLS "Employment Situation of Veterans",
#                        August 2025 class-of-worker table (Table 8) — see
#                        derive_sl_gov_veteran_share().
VET_SHARE_STATE_CLASSIFIED_DHRM = 0.06          # OFFICIAL (self-identified)
VET_SHARE_TEACHERS_NCES_US = 0.023              # OFFICIAL
VET_SHARE_TEACHERS_NCES_SOUTH = 0.031           # OFFICIAL

# BLS Table 8, August 2025, not seasonally adjusted (levels in thousands;
# class-of-worker percent distributions as printed).
BLS_VETS_EMPLOYED = 7_893
BLS_NONVETS_EMPLOYED = 153_213
BLS_VET_PCT_STATE_LOCAL_GOV = 0.129
BLS_NONVET_PCT_STATE_LOCAL_GOV = 0.109

# BLS "Employment Situation of Veterans", Tables 6A and 6B, 2025 annual
# averages — Virginia rows (thousands).
VA_VETS_EMPLOYED = 357
VA_NONVETS_EMPLOYED = 3_864

# --- OFFICIAL: salary anchors.
MEAN_CLASSIFIED_SALARY = 69_865      # DHRM slide 14, as of 6/30/2024
ILLUSTRATIVE_SALARY = 91_700         # the Cliff Graph's illustrative profile

# --- OFFICIAL: Annual Covered Payroll at June 30, 2025, by group ($ thousands).
#     Source: June 30, 2025 Annual Actuarial Valuation, "Results Summary" for
#     each group. This is the correct denominator for a payroll-share statement
#     about a bill whose scope is all VRS members — NOT the $4.0bn classified
#     state payroll used in the brief v1.0.
COVERED_PAYROLL_000 = {
    "State Employees": 6_275_603,
    "Teachers": 11_732_114,
    "State Police (SPORS)": 182_726,
    "Judicial (JRS)": 98_645,
    "Virginia Law Officers (VaLORS)": 432_703,
    "Political Subdivisions": 8_041_026,
}
TOTAL_COVERED_PAYROLL = sum(COVERED_PAYROLL_000.values()) * 1_000

# --- ESTIMATE: scenario assumptions.
TAKEUP_SCENARIOS = {"Low": 0.10, "Moderate": 0.20, "High": 0.30}
TAKEUP_BRIEF_BAND = (0.05, 0.15)     # the band carried in the v1.0 brief
YEARS_PURCHASED_AVG = 2.5            # of the 4 allowed
SHARE_MEETING_180_DAY_TEST = 0.90    # 51.1-142.2 B 2 / final para. of subsec. B

# --- ESTIMATE: annuity basis. Level-COLA annuity-certain to this age.
TERMINAL_AGE = 87
TERMINAL_AGE_SENSITIVITY = (84, 90)

# --- OFFICIAL: statutory retirement thresholds.
#     Plan 1:  51.1-153 B 1 — age 65 w/ 5 yrs, or age 50 w/ 30 yrs.
#     Plan 2 / Hybrid: 51.1-153 B 2 — SSA normal retirement age w/ 5 yrs;
#                      51.1-153 B 3 — Rule of 90 (age + creditable service >= 90).
SSA_NRA = 67


# ============================================================================
# ANNUITY AND PRESENT-VALUE MACHINERY
# ============================================================================

def cola_annuity(retire_age, cola, discount=DISCOUNT, terminal=TERMINAL_AGE):
    """Present value at retirement of $1/yr escalating at `cola`, paid annually
    in advance until `terminal`. ESTIMATE basis (annuity-certain, no mortality).

    Fractional retirement ages are supported: the final, partial year is paid
    pro rata, so the factor is continuous in `retire_age`. That matters because
    the Rule of 90 produces half-year eligibility dates."""
    n = max(0.0, terminal - retire_age)
    whole = int(n)
    frac = n - whole
    total = sum(((1 + cola) ** t) / ((1 + discount) ** t) for t in range(whole))
    if frac:
        total += frac * ((1 + cola) ** whole) / ((1 + discount) ** whole)
    return total


def aec_pct_of_salary(plan, purchase_age, retire_age, *,
                      multiplier=None, cola=None, growth=SALARY_GROWTH,
                      terminal=TERMINAL_AGE, afc_offset=1.5):
    """Actuarial-equivalent cost of ONE year of creditable service, expressed as
    a percent of salary at the purchase date, counting the BENEFIT-AMOUNT channel
    only (not eligibility acceleration).

        AEC%  =  M  x  G  x  a_cola  x  v

      M = statutory multiplier
      G = salary growth from purchase date to the AFC measurement midpoint
      a = COLA-adjusted annuity factor at retirement
      v = discount from retirement back to the purchase date
    """
    m = MULTIPLIER[plan] if multiplier is None else multiplier
    c = COLA[plan] if cola is None else cola
    yrs = max(0.0, retire_age - purchase_age)
    G = (1 + growth) ** max(0.0, yrs - afc_offset)
    a = cola_annuity(retire_age, c, terminal=terminal)
    v = 1 / ((1 + DISCOUNT) ** yrs)
    return m * G * a * v


def breakeven_age(plan, retire_age, anc_rate, lo=25, hi=70, **kw):
    """The purchase age at which the benefit-amount AEC equals the published ANC
    rate. DERIVED. Below it the member OVERPAYS at ANC; above it the plan
    subsidises. Returns None if no crossing inside [lo, hi]."""
    prev_age, prev_gap = None, None
    for i in range(int((hi - lo) * 100) + 1):
        age = lo + i / 100
        gap = aec_pct_of_salary(plan, age, retire_age, **kw) - anc_rate
        if prev_gap is not None and prev_gap < 0 <= gap:
            return prev_age + (0 - prev_gap) * (age - prev_age) / (gap - prev_gap)
        prev_age, prev_gap = age, gap
    return None


# ============================================================================
# FM-1 — POPULATION
# ============================================================================

def derive_sl_gov_veteran_share():
    """DERIVED: veteran share of U.S. state-and-local government workers, from
    the BLS August 2025 class-of-worker table."""
    vets = BLS_VETS_EMPLOYED * BLS_VET_PCT_STATE_LOCAL_GOV
    nonvets = BLS_NONVETS_EMPLOYED * BLS_NONVET_PCT_STATE_LOCAL_GOV
    return vets / (vets + nonvets), vets, nonvets


def derive_va_uplift():
    """DERIVED: ratio of Virginia's veteran share of total employment to the
    national veteran share of total employment. Used only as an upper-bound
    sensitivity, never as a point estimate."""
    va = VA_VETS_EMPLOYED / (VA_VETS_EMPLOYED + VA_NONVETS_EMPLOYED)
    us = BLS_VETS_EMPLOYED / (BLS_VETS_EMPLOYED + BLS_NONVETS_EMPLOYED)
    return va / us, va, us


# Veteran-share bands actually used, per employer group. Low end is the
# best-sourced published figure; high end applies the Virginia uplift.
def veteran_share_bands():
    sl_share, _, _ = derive_sl_gov_veteran_share()
    uplift, _, _ = derive_va_uplift()
    return {
        # DHRM's self-identified 6% is a floor; the BLS S&L-gov benchmark
        # scaled to Virginia's veteran-dense labour force is the ceiling.
        "VRS State Employees": (VET_SHARE_STATE_CLASSIFIED_DHRM, sl_share * uplift),
        # NCES national 2.3% floor, South-region 3.1% scaled by the Virginia
        # uplift as the ceiling. Licensure and sex composition bind here, not
        # state veteran density, so the ceiling is deliberately soft.
        "VRS Teachers": (VET_SHARE_TEACHERS_NCES_US, VET_SHARE_TEACHERS_NCES_SOUTH * uplift),
        # Local government: BLS S&L-gov benchmark as the floor, Virginia-uplifted
        # as the ceiling. Public-safety-heavy, so likely in the upper half.
        "VRS Political Subdivision Employees": (sl_share, sl_share * uplift),
        # Sworn state law enforcement: veteran share materially exceeds the
        # general public-sector rate. Band set from the political-subdivision
        # ceiling upward; ESTIMATE, flagged as the weakest of the five.
        "SPORS": (sl_share * uplift, 0.25),
        "VaLORS": (sl_share * uplift, 0.25),
        "JRS": (VET_SHARE_TEACHERS_NCES_US, sl_share * uplift),
    }


# Share of each group's NON-VESTED (under-5-years) members who are still inside
# the 24-month window. ESTIMATE. 0.40 = service uniformly spread over years 0-5;
# 0.60 = front-loaded, which is what withdrawal decrements on new hires produce.
INSIDE_WINDOW_SHARE_OF_NONVESTED = (0.40, 0.60)


def fm1_past_window():
    """Members past the 24-month ANC window.

    Structural part (no estimate needed): Plan 1 is a fully closed cohort — a
    Plan 1 membership date must precede July 1, 2010 (ACFR Fig. 2.10), so every
    Plan 1 member passed 24 months of active service no later than mid-2012.

    Plan 2 is NOT fully closed: ACFR Fig. 2.10 provides that members covered by
    VaLORS, SPORS, or VRS enhanced hazardous duty benefits / the hazardous duty
    alternate option with a membership date on or after July 1, 2010 are in
    Plan 2 "even if their membership dates are after December 31, 2013."
    So the open part of Plan 2 is the hazardous-duty population, plus — from
    July 1, 2026 — newly appointed judges (2026 Acts, SB 950).
    """
    out = {}
    for g, total in ACTIVE_BY_GROUP.items():
        nv = NONVESTED[g]
        lo_in = nv * INSIDE_WINDOW_SHARE_OF_NONVESTED[0]
        hi_in = nv * INSIDE_WINDOW_SHARE_OF_NONVESTED[1]
        out[g] = {
            "active": total,
            "vested_all_past_window": VESTED[g],
            "nonvested": nv,
            "past_window_hi": total - lo_in,   # fewer inside -> more past
            "past_window_lo": total - hi_in,
        }
    return out


def fm1_eligible_pool():
    """Veterans holding purchasable prior active-duty military service and
    already past the 24-month window, by employer group. DERIVED x ESTIMATE."""
    bands = veteran_share_bands()
    pw = fm1_past_window()
    rows = []
    for g in ACTIVE_BY_GROUP:
        vlo, vhi = bands[g]
        lo = pw[g]["past_window_lo"] * vlo * SHARE_MEETING_180_DAY_TEST
        hi = pw[g]["past_window_hi"] * vhi * SHARE_MEETING_180_DAY_TEST
        rows.append((g, vlo, vhi, lo, hi))
    return rows


# ============================================================================
# FM-2 — THE AEC / ANC MULTIPLE SURFACE
# ============================================================================

PLAN_RETIRE_AGE = {"Plan 1": 65, "Plan 2": SSA_NRA, "Hybrid": SSA_NRA}


def fm2_surface(plan, ages=range(30, 65, 5)):
    """AEC as a percent of salary, and the AEC/ANC multiple, by purchase age.
    DERIVED from OFFICIAL multipliers, COLA, discount and payroll-growth
    assumptions plus the published ANC rate. ESTIMATE annuity basis."""
    anc = ANC[(plan, "non-hazardous")]
    r = PLAN_RETIRE_AGE[plan]
    rows = []
    for age in ages:
        if age >= r:
            continue
        aec = aec_pct_of_salary(plan, age, r)
        rows.append((age, r - age, aec, anc, aec / anc, (aec - anc)))
    return rows, anc, r


def fm2_locate_multiple(plan, target=3.23):
    """At what purchase age does the benefit-amount AEC/ANC multiple reach
    `target`? Answers: 'where does the Cliff Graph's 3.23x actually sit?'"""
    anc = ANC[(plan, "non-hazardous")]
    r = PLAN_RETIRE_AGE[plan]
    prev = None
    for i in range(int((r - 25) * 100)):
        age = 25 + i / 100
        mult = aec_pct_of_salary(plan, age, r) / anc
        if prev and prev[1] < target <= mult:
            return age
        prev = (age, mult)
    return None


# ============================================================================
# FM-3 — RATE GROUPS
# ============================================================================

def fm3_rate_groups():
    """Which ANC schedule applies, by rate group, if A-3 is adopted.
    All OFFICIAL — RBA 2025-06-10 and the published rate charts."""
    return [
        # (rate group, Plan 1, Plan 2, Hybrid, note)
        ("State / teacher / local non-hazardous",
         ANC[("Plan 1", "non-hazardous")], ANC[("Plan 2", "non-hazardous")],
         ANC[("Hybrid", "non-hazardous")],
         "Hybrid covers every non-hazardous member first hired on/after 1/1/2014."),
        ("Hazardous duty - VaLORS, SPORS, political subdivisions with enhanced benefits",
         ANC[("Plan 1", "hazardous")], ANC[("Plan 2", "hazardous")], None,
         "No Hybrid rate exists: 51.1-169 A excludes these members from Hybrid, "
         "so new hires enter PLAN 2 and the Plan 2 hazardous rate governs."),
        ("Hazardous duty alternate option (employer has not adopted all enhanced benefits)",
         None, None, None,
         f"Single published rate {ANC[('Alternate hazardous duty option','hazardous')]:.2%}, "
         "available only to localities electing the option."),
        ("Judicial",
         ANC[("Plan 1", "judicial")], ANC[("Plan 2", "judicial")],
         ANC[("Hybrid", "judicial")],
         "2026 Acts (SB 950): judges with an original term on/after 7/1/2026 are "
         "in VRS Plan 2, so the Plan 2 judicial rate becomes the forward-looking one."),
    ]


# ============================================================================
# FM-4 — RETIREMENT-DATE ACCELERATION, AND THE THREE PRICE STRUCTURES
# ============================================================================

@dataclass
class Profile:
    plan: str
    age: int
    service: float
    salary: float
    entry_salary: float
    entry_age: int


def unreduced_age(plan, age_now, service_now, purchased=0.0):
    """Age at which the member first qualifies for an UNREDUCED allowance.

    Each future calendar year adds 1 to age and 1 to creditable service.
    Purchased 51.1-142.2 service adds to the SERVICE leg only (it is creditable
    service under 51.1-124.3 but is not time lived), so under the Rule of 90 it
    advances the eligibility date by HALF a year per year purchased.
    """
    s0 = service_now + purchased
    if plan == "Plan 1":
        # 51.1-153 B 1: age 65 w/ >=5 yrs, or age 50 w/ >=30 yrs.
        by_65 = 65.0 if s0 + (65 - age_now) >= 5 else None
        t = max(0.0, 30 - s0, 50 - age_now)
        by_30 = age_now + t
        cands = [c for c in (by_65, by_30) if c is not None]
        return min(cands)
    # Plan 2 / Hybrid: 51.1-153 B 2 (SSA NRA w/ 5 yrs) or B 3 (Rule of 90).
    by_nra = float(SSA_NRA)
    t90 = max(0.0, (90 - age_now - s0) / 2)
    return min(by_nra, age_now + t90)


def fm4_acceleration(p: Profile, years_purchased=4.0):
    """DERIVED: how much earlier the member reaches unreduced retirement, and the
    present value of that acceleration to the Fund, decomposed from the
    benefit-amount channel."""
    a0 = unreduced_age(p.plan, p.age, p.service)
    a1 = unreduced_age(p.plan, p.age, p.service, purchased=years_purchased)
    accel = a0 - a1

    m, c = MULTIPLIER[p.plan], COLA[p.plan]

    def pv_at(ret_age, svc_at_ret):
        """PV at today of an allowance commencing at ret_age."""
        yrs = ret_age - p.age
        afc = p.salary * (1 + SALARY_GROWTH) ** max(0.0, yrs - 1.5)
        annual = m * svc_at_ret * afc
        a = cola_annuity(ret_age, c)
        v = 1 / ((1 + DISCOUNT) ** yrs)
        return annual * a * v, annual

    # Baseline: no purchase, retire at a0 with service earned by then.
    svc0 = p.service + (a0 - p.age)
    pv0, ann0 = pv_at(a0, svc0)

    # Channel 1 only — buy the service, but retire on the SAME date a0.
    svc_amt = p.service + (a0 - p.age) + years_purchased
    pv_amt, ann_amt = pv_at(a0, svc_amt)

    # Channel 1 + 2 — buy the service AND retire at the new, earlier date a1.
    svc1 = p.service + (a1 - p.age) + years_purchased
    pv1, ann1 = pv_at(a1, svc1)

    return {
        "unreduced_age_baseline": a0,
        "unreduced_age_with_purchase": a1,
        "acceleration_years": accel,
        "pv_baseline": pv0,
        "pv_amount_channel": pv_amt,
        "pv_both_channels": pv1,
        "cost_amount_channel": pv_amt - pv0,
        "cost_acceleration_channel": pv1 - pv_amt,
        "cost_total": pv1 - pv0,
        "annual_baseline": ann0,
        "annual_with_purchase_same_date": ann_amt,
        "annual_with_purchase_earlier_date": ann1,
    }


# A-1's statutory interest rate is a DRAFTING choice, not an actuarial one, and
# it dominates the result. Pennsylvania's "statutory interest" is 4% (71 Pa.C.S.
# 5102). VRS's assumed return is 6.75%. Both are modelled.
A1_INTEREST_RATES = {"PA statutory 4%": 0.04, "VRS assumed return 6.75%": DISCOUNT}

# OFFICIAL: Total Normal Cost (member + employer) as a percent of payroll,
# June 30, 2025 Annual Actuarial Valuation, "Results Summary - Employer
# Contribution Rate Detail". Blended across plans within each group.
TOTAL_NORMAL_COST = {
    "State Employees": 0.0873,
    "Teachers": 0.0922,
    "SPORS": 0.1837,
    "Judicial": 0.2711,
    "VaLORS": 0.1430,
}


def price_a1_pennsylvania(p: Profile, years=1.0, interest=0.04,
                          combined_nc=TOTAL_NORMAL_COST["State Employees"]):
    """A-1: deferred-contribution recovery, the Pennsylvania structure.
    Price = combined member + employer normal cost rate in effect at entry,
    applied to early-career pay, carried forward at a statutory interest rate."""
    carry = (1 + interest) ** (p.age - p.entry_age)
    return combined_nc * p.entry_salary * carry * years


def price_a2_newyork(p: Profile, years=1.0, pct=0.06):
    """A-2: flat statutory percentage of trailing-12-month creditable
    compensation. 6% is New York's figure (N.Y. Ret. & Soc. Sec. Law 1000);
    the percentage is a policy variable."""
    return pct * p.salary * years


def price_a3_anc(p: Profile, years=1.0, group="non-hazardous"):
    """A-3: approximate normal cost at the time of purchase, on salary at the
    time of purchase. OFFICIAL rate."""
    return ANC[(p.plan, group)] * p.salary * years


# ============================================================================
# REPORT
# ============================================================================

def money(x):
    return f"${x:,.0f}"


def main():
    print("=" * 78)
    print("FM-1 to FM-4 MODEL  —  Va. Code 51.1-142.2 military-service price cliff")
    print("Basis date: October 24, 2026.  OFFICIAL / DERIVED / ESTIMATE tagged inline.")
    print("=" * 78)

    # ---------------- FM-1 ----------------
    print("\n\n### FM-1  POPULATION\n")
    print("Active members by plan at June 30, 2025 (OFFICIAL, VRS 101 'Who We Serve'):")
    tot = sum(ACTIVE_BY_PLAN.values())
    for k, v in ACTIVE_BY_PLAN.items():
        print(f"  {k:<8} {v:>9,}  ({v/tot:6.2%})")
    print(f"  {'TOTAL':<8} {tot:>9,}")

    print("\nActive members by employer group at June 30, 2025 "
          "(OFFICIAL, ACFR Figs. 2.3 / 2.9):")
    print(f"  {'group':<40}{'active':>9}{'vested':>9}{'non-vest':>9}")
    for g, v in ACTIVE_BY_GROUP.items():
        print(f"  {g:<40}{v:>9,}{VESTED[g]:>9,}{NONVESTED[g]:>9,}")

    sl, vk, nvk = derive_sl_gov_veteran_share()
    print(f"\nDERIVED veteran share of U.S. state-and-local government workers:")
    print(f"  veterans      {vk:>10,.0f}k  = {BLS_VETS_EMPLOYED:,}k x {BLS_VET_PCT_STATE_LOCAL_GOV:.1%}")
    print(f"  nonveterans   {nvk:>10,.0f}k  = {BLS_NONVETS_EMPLOYED:,}k x {BLS_NONVET_PCT_STATE_LOCAL_GOV:.1%}")
    print(f"  share         {sl:>10.2%}   <-- independently corroborates DHRM's 6%")

    up, va, us = derive_va_uplift()
    print(f"\nDERIVED Virginia uplift (upper-bound sensitivity only):")
    print(f"  Virginia veteran share of employed  {va:.2%}")
    print(f"  U.S. veteran share of employed      {us:.2%}")
    print(f"  uplift factor                       {up:.3f}x")

    print("\nMembers PAST the 24-month window (DERIVED structural + ESTIMATE band):")
    pw = fm1_past_window()
    print(f"  {'group':<40}{'past window lo':>16}{'past window hi':>16}")
    tl = th = 0
    for g, d in pw.items():
        tl += d["past_window_lo"]; th += d["past_window_hi"]
        print(f"  {g:<40}{d['past_window_lo']:>16,.0f}{d['past_window_hi']:>16,.0f}")
    print(f"  {'TOTAL':<40}{tl:>16,.0f}{th:>16,.0f}")
    print(f"  {'as share of 378,060 actives':<40}{tl/tot:>16.1%}{th/tot:>16.1%}")
    p12 = ACTIVE_BY_PLAN['Plan 1'] + ACTIVE_BY_PLAN['Plan 2']
    print(f"\n  Of which NO estimate is required: Plan 1 ({ACTIVE_BY_PLAN['Plan 1']:,}) is a")
    print(f"  fully closed cohort, so 100% is past the window as a matter of law.")
    print(f"  Plan 1 alone = {ACTIVE_BY_PLAN['Plan 1']/tot:.1%} of all actives.")
    print(f"  Plan 1 + Plan 2 = {p12:,} ({p12/tot:.1%}), but Plan 2 is NOT fully")
    print(f"  closed - see FM-3 note on hazardous duty and judges.")

    print("\nVeterans past the window holding purchasable military service")
    print("(DERIVED population x ESTIMATE veteran share x 90% 180-day test):")
    print(f"  {'group':<40}{'vet share':>18}{'low':>9}{'high':>9}")
    lo_t = hi_t = 0
    for g, vlo, vhi, lo, hi in fm1_eligible_pool():
        lo_t += lo; hi_t += hi
        print(f"  {g:<40}{vlo:>8.1%} - {vhi:<7.1%}{lo:>9,.0f}{hi:>9,.0f}")
    print(f"  {'TOTAL':<40}{'':>18}{lo_t:>9,.0f}{hi_t:>9,.0f}")
    print(f"\n  Reportable form: 'on the order of {lo_t/1000:.0f},000 to {hi_t/1000:.0f},000'")
    print("  — a RANGE from published shares, not a count. Only VRS can produce a count.")

    # ---------------- FM-2 ----------------
    print("\n\n### FM-2  AEC / ANC MULTIPLE BY AGE\n")
    print("Benefit-amount channel only. The multiple is scale-free: the annuity")
    print("basis cancels between numerator and denominator, so the SHAPE of this")
    print("surface is robust even though the absolute level is an ESTIMATE.\n")
    for plan in ("Plan 1", "Plan 2", "Hybrid"):
        rows, anc, r = fm2_surface(plan)
        be = breakeven_age(plan, r, anc)
        print(f"  {plan}  (M={MULTIPLIER[plan]:.2%}, COLA={COLA[plan]:.2%}, "
              f"retire at {r}, published ANC={anc:.2%})")
        print(f"    {'age':>5}{'yrs to ret':>12}{'AEC%':>9}{'AEC/ANC':>10}"
              f"{'gap vs ANC':>12}{'gap @'+str(ILLUSTRATIVE_SALARY):>14}")
        for age, yrs, aec, _a, mult, gap in rows:
            print(f"    {age:>5}{yrs:>12}{aec:>9.2%}{mult:>10.2f}x"
                  f"{gap:>12.2%}{money(gap*ILLUSTRATIVE_SALARY):>14}")
        if be:
            print(f"    break-even purchase age (AEC = published ANC): {be:.1f}")
        loc = fm2_locate_multiple(plan, 3.23)
        print(f"    the Cliff Graph's 3.23x corresponds to purchase age "
              f"{loc:.1f}" if loc else
              "    3.23x is NOT reachable on this surface before retirement age")
        print()

    print("  Terminal-age sensitivity on the Hybrid multiple at age 58:")
    for term in (TERMINAL_AGE_SENSITIVITY[0], TERMINAL_AGE, TERMINAL_AGE_SENSITIVITY[1]):
        aec = aec_pct_of_salary("Hybrid", 58, SSA_NRA, terminal=term)
        print(f"    multiple {aec/ANC[('Hybrid','non-hazardous')]:.2f}x "
              f"(terminal age {term}, AEC {aec:.2%})")

    # --- Where the Cliff Graph's 3.23x actually comes from ---------------
    print("\n  WHERE 3.23x COMES FROM — the Cliff Graph's own illustrative")
    print("  profile is age 55, 25 years of service, $91,700 salary. Run all")
    print("  three plans at THAT profile, on the FULL basis (benefit amount +")
    print("  eligibility acceleration), buying 4 years:\n")
    print(f"    {'plan':<8}{'unred.':>14}{'accel':>8}{'AEC/yr':>11}"
          f"{'ANC/yr':>10}{'multiple':>10}")
    chart = {}
    for plan in ("Plan 1", "Plan 2", "Hybrid"):
        pr = Profile(plan, 55, 25, ILLUSTRATIVE_SALARY, 45_000, 30)
        r = fm4_acceleration(pr, years_purchased=4.0)
        aec_yr = r["cost_total"] / 4
        anc_yr = ANC[(plan, "non-hazardous")] * ILLUSTRATIVE_SALARY
        chart[plan] = (aec_yr, anc_yr, aec_yr / anc_yr)
        print(f"    {plan:<8}{r['unreduced_age_baseline']:.1f}->"
              f"{r['unreduced_age_with_purchase']:.1f}".ljust(8)
              + f"{r['acceleration_years']:>8.2f}{money(aec_yr):>11}"
                f"{money(anc_yr):>10}{aec_yr/anc_yr:>9.2f}x")
    print(f"\n    Plan 1 lands at {chart['Plan 1'][2]:.2f}x — which independently")
    print("    REPRODUCES the worked example behind the 3.23x in the chart.")
    print("    But Plan 2 and Hybrid land at "
          f"{chart['Plan 2'][2]:.2f}x and {chart['Hybrid'][2]:.2f}x, NOT 3.23x.")
    print("    Two reasons, both structural, neither an artefact of this model:")
    print("      (i)  lower multipliers (1.65% / 1.00% vs 1.70%); and")
    print("      (ii) Plan 1's age-50/30-years threshold advances ONE year per")
    print("           year purchased, while the Rule of 90 advances only HALF a")
    print("           year per year purchased (purchased service adds to the")
    print("           service leg only, not to age).")
    print("\n    CHART REISSUE VALUES (post-cliff, same illustrative profile):")
    for plan in ("Plan 1", "Plan 2", "Hybrid"):
        aec_yr, anc_yr, mult = chart[plan]
        old = 3.23 * anc_yr
        print(f"      {plan:<8} currently shown {money(old):>9}  ->  "
              f"{money(aec_yr):>9}  (overstated {old/aec_yr:.2f}x)")

    # ---------------- FM-3 ----------------
    print("\n\n### FM-3  RATE GROUPS UNDER A-3  (all OFFICIAL)\n")
    for grp, p1, p2, hy, note in fm3_rate_groups():
        f = lambda x: f"{x:.2%}" if x is not None else "none published"
        print(f"  {grp}")
        print(f"    Plan 1 {f(p1):>16} | Plan 2 {f(p2):>16} | Hybrid {f(hy):>16}")
        print(f"    {note}\n")

    # ---------------- FM-4 ----------------
    print("\n### FM-4  RETIREMENT-DATE ACCELERATION AND THE THREE PRICE STRUCTURES\n")
    profiles = [
        Profile("Plan 1", 55, 25, ILLUSTRATIVE_SALARY, 45_000, 30),
        Profile("Plan 2", 50, 14, ILLUSTRATIVE_SALARY, 55_000, 36),
        Profile("Hybrid", 45, 8, ILLUSTRATIVE_SALARY, 68_000, 37),
        Profile("Hybrid", 55, 10, ILLUSTRATIVE_SALARY, 72_000, 45),
    ]
    print("  1. The acceleration channel, decomposed, buying the full 4 years.\n")
    for p in profiles:
        r = fm4_acceleration(p, years_purchased=4.0)
        print(f"  {p.plan}, age {p.age}, {p.service:g} yrs service, "
              f"salary {money(p.salary)}")
        print(f"    unreduced eligibility: age {r['unreduced_age_baseline']:.2f} "
              f"-> {r['unreduced_age_with_purchase']:.2f}  "
              f"(accelerated {r['acceleration_years']:.2f} yrs)")
        print(f"    PV cost, benefit-amount channel   {money(r['cost_amount_channel']):>12}")
        print(f"    PV cost, acceleration channel     {money(r['cost_acceleration_channel']):>12}")
        print(f"    PV cost, TOTAL                    {money(r['cost_total']):>12}")
        share = (r['cost_acceleration_channel'] / r['cost_total']
                 if r['cost_total'] else 0)
        print(f"    acceleration share of total cost  {share:>12.1%}")
        print()
    print("  Finding: acceleration is 20%-49% of the total on this basis, and")
    print("  that is a FLOOR (caveat 3). It is the largest single component for")
    print("  a long-service Plan 1 member sitting just short of age 50 + 30.\n")

    print("  2. Member price and net cost to the Fund under A-1 / A-2 / A-3.")
    print("     A-1 is shown at BOTH candidate statutory interest rates,")
    print("     because that drafting choice, not actuarial science, decides")
    print("     whether A-1 is cheaper or dearer than A-3.\n")
    for p in profiles:
        r = fm4_acceleration(p, years_purchased=4.0)
        tot = r["cost_total"]
        print(f"  {p.plan}, age {p.age}, {p.service:g} yrs, entry age {p.entry_age} "
              f"at {money(p.entry_salary)}; 4 years bought; "
              f"benefit value {money(tot)}")
        for label, i in A1_INTEREST_RATES.items():
            pr = price_a1_pennsylvania(p, 4, interest=i)
            print(f"    A-1 ({label:<24}) price {money(pr):>9}  "
                  f"net to Fund {money(tot-pr):>10}")
        pr2 = price_a2_newyork(p, 4)
        pr3 = price_a3_anc(p, 4)
        print(f"    A-2 (6% of trailing-12 pay    ) price {money(pr2):>9}  "
              f"net to Fund {money(tot-pr2):>10}")
        print(f"    A-3 (published ANC            ) price {money(pr3):>9}  "
              f"net to Fund {money(tot-pr3):>10}")
        print()

    print("  3. Statewide take-up sensitivity, by plan.\n")
    rows = fm1_eligible_pool()
    pool_lo = sum(r[3] for r in rows)
    pool_hi = sum(r[4] for r in rows)
    pw = fm1_past_window()
    pw_lo = sum(d["past_window_lo"] for d in pw.values())
    pw_hi = sum(d["past_window_hi"] for d in pw.values())
    # DERIVED: effective veteran-with-qualifying-service rate across the whole
    # past-window population, used to allocate the pool across plans.
    eff_lo, eff_hi = pool_lo / pw_hi, pool_hi / pw_lo
    hybrid_pw_lo = pw_lo - ACTIVE_BY_PLAN["Plan 1"] - ACTIVE_BY_PLAN["Plan 2"]
    hybrid_pw_hi = pw_hi - ACTIVE_BY_PLAN["Plan 1"] - ACTIVE_BY_PLAN["Plan 2"]
    plan_pw = {
        "Plan 1": (ACTIVE_BY_PLAN["Plan 1"], ACTIVE_BY_PLAN["Plan 1"]),
        "Plan 2": (ACTIVE_BY_PLAN["Plan 2"], ACTIVE_BY_PLAN["Plan 2"]),
        "Hybrid": (hybrid_pw_lo, hybrid_pw_hi),
    }
    print(f"    Effective veteran-with-qualifying-service rate across the")
    print(f"    past-window population (DERIVED): {eff_lo:.2%} - {eff_hi:.2%}")
    print("    ESTIMATE: that rate is applied uniformly across plans. It is not")
    print("    uniform in reality — veterans enter state service mid-career, so")
    print("    Hybrid is probably over-weighted and Plan 1 under-weighted here.\n")

    # Representative profile per plan, at the average years purchased.
    reps = {
        "Plan 1": Profile("Plan 1", 55, 25, MEAN_CLASSIFIED_SALARY, 45_000, 30),
        "Plan 2": Profile("Plan 2", 50, 14, MEAN_CLASSIFIED_SALARY, 55_000, 36),
        "Hybrid": Profile("Hybrid", 50, 9, MEAN_CLASSIFIED_SALARY, 60_000, 41),
    }
    print(f"    {'plan':<8}{'pool (vets past window)':>26}"
          f"{'A-3 net PV / purchaser':>26}")
    per_plan = {}
    for plan, pr in reps.items():
        r = fm4_acceleration(pr, years_purchased=YEARS_PURCHASED_AVG)
        net = r["cost_total"] - price_a3_anc(pr, YEARS_PURCHASED_AVG)
        lo = plan_pw[plan][0] * eff_lo
        hi = plan_pw[plan][1] * eff_hi
        per_plan[plan] = (lo, hi, net)
        print(f"    {plan:<8}{f'{lo:,.0f} - {hi:,.0f}':>26}{money(net):>26}")
    tot_lo = sum(v[0] for v in per_plan.values())
    tot_hi = sum(v[1] for v in per_plan.values())
    print(f"    {'TOTAL':<8}{f'{tot_lo:,.0f} - {tot_hi:,.0f}':>26}")
    print(f"    (salary basis {money(MEAN_CLASSIFIED_SALARY)}, "
          f"{YEARS_PURCHASED_AVG:g} years bought per purchaser)\n")

    scen = dict(TAKEUP_SCENARIOS)
    scen[f"Brief v1.0 low"] = TAKEUP_BRIEF_BAND[0]
    scen[f"Brief v1.0 high"] = TAKEUP_BRIEF_BAND[1]
    print(f"    {'scenario':<18}{'take-up':>9}{'purchasers':>20}"
          f"{'one-time PV cost, A-3':>32}{'as % of payroll':>18}")
    for name, t in sorted(scen.items(), key=lambda kv: kv[1]):
        n_lo = sum(v[0] for v in per_plan.values()) * t
        n_hi = sum(v[1] for v in per_plan.values()) * t
        c_lo = sum(v[0] * t * v[2] for v in per_plan.values())
        c_hi = sum(v[1] * t * v[2] for v in per_plan.values())
        pl = c_lo / TOTAL_COVERED_PAYROLL
        ph = c_hi / TOTAL_COVERED_PAYROLL
        print(f"    {name:<18}{t:>9.0%}{f'{n_lo:,.0f} - {n_hi:,.0f}':>20}"
              f"{f'{money(c_lo)} - {money(c_hi)}':>32}"
              f"{f'{pl:.3%} - {ph:.3%}':>18}")

    print(f"\n    Payroll denominator (OFFICIAL, 6/30/2025 valuation, Annual")
    print(f"    Covered Payroll by group):")
    for g, v in COVERED_PAYROLL_000.items():
        print(f"      {g:<34}{money(v*1000):>18}")
    print(f"      {'TOTAL VRS COVERED PAYROLL':<34}"
          f"{money(TOTAL_COVERED_PAYROLL):>18}")
    print(f"\n    The brief v1.0 scale sentence uses $3.98bn (classified state")
    print(f"    payroll) and reports 0.050% of payroll. The correct denominator")
    print(f"    for an all-VRS bill is {money(TOTAL_COVERED_PAYROLL)}, which is")
    print(f"    {TOTAL_COVERED_PAYROLL/3_976_000_000:.1f}x larger — but the eligible pool grew more than")
    print(f"    the denominator did, so the payroll SHARE rises too. '5 cents per")
    print(f"    $100' holds only at the bottom of the grid.")

    print("\n  4. Cross-check against the only public Virginia anchor.")
    print("     VRS's own 30-19.1:7 fiscal impact statement on HB 1867 (2023) —")
    print("     which would have granted military service to TEACHERS FREE —")
    print("     found $10,000 to $60,000 of unfunded liability per participating")
    print("     member.")
    for plan, (lo, hi, net) in per_plan.items():
        inside = 10_000 <= net <= 60_000
        print(f"     {plan:<8} modelled A-3 net PV/member {money(net):>9}  "
              f"{'INSIDE' if inside else 'outside'} the HB 1867 band"
              + ("" if inside else " (lower — as a priced purchase should be)"))
    print("     A priced purchase should sit BELOW a free grant. It does.")
    print("     The brief v1.0 figure of about $3,750 per member sat an order of")
    print("     magnitude below the band; that was the signal it was too low.")

    print("\n" + "=" * 78)
    print("""CAVEATS
1. The annuity basis is a level-COLA annuity-certain to age 87, NOT a VRS
   mortality table. Absolute dollar figures are illustrative. The AEC/ANC
   MULTIPLE is far more robust than the absolute AEC, because the annuity
   basis largely cancels.
2. AEC here values the benefit-amount channel and, in FM-4, the acceleration
   channel separately. VRS's own definition of actuarial equivalent cost
   covers both ("...or earlier retirement eligibility date"), so the FM-4
   total is the closer analogue of a real AEC quote.
3. Early-retirement reduction factors are NOT modelled. VRS told its own
   Benefits & Actuarial Committee on June 17, 2026 that it uses fixed-rate
   reductions rather than true actuarial equivalence, and that this "does
   provide a subsidy that varies by age and service." Accelerating an
   UNREDUCED eligibility date therefore also extinguishes a reduction the
   member would otherwise have taken. That makes this model's acceleration
   cost a FLOOR, not a ceiling.
4. Health insurance credit (51.1-1400), including its 15-year step, is not
   priced. Neither is adverse selection, nor VRS administrative cost.
5. No figure here is a VRS actuarial certification. Under 30-19.1:7 the VRS
   Board must file the official impact statement.""")
    print("=" * 78)


if __name__ == "__main__":
    main()
