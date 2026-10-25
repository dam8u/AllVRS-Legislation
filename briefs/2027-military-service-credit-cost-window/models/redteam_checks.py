#!/usr/bin/env python3
"""
Red-team verification harness for MOO-292.

This file does NOT modify fm_model.py. It imports it and re-runs four
challenges against it. Every number the brief relies on that is reproduced
here is reproduced from the team's own model and the team's own inputs.

Challenges:
  RT-1  pool pairing   — the low/high effective-rate pairing used to allocate
                         the pool across plans is cross-wired, so the cost grid
                         and the state/teacher/local table rest on two
                         different pools. Recompute both ways.
  RT-2  HB 1867        — restate the cross-check on a like-for-like basis
                         (free grant vs free grant, 4 years vs 4 years).
  RT-3  profile risk   — the per-member figures are single-profile point
                         estimates. Vary the representative profile.
  RT-4  rate impact    — convert the one-time present value into the number
                         that actually appears in a fiscal impact statement:
                         the employer contribution rate increase.

Run: python3 redteam_checks.py
"""

import fm_model as M

BAR = "=" * 74


def rt1_pool_pairing():
    print(BAR)
    print("RT-1  POOL PAIRING")
    print(BAR)
    rows = M.fm1_eligible_pool()
    pool_lo = sum(r[3] for r in rows)
    pool_hi = sum(r[4] for r in rows)
    pw = M.fm1_past_window()
    pw_lo = sum(d["past_window_lo"] for d in pw.values())
    pw_hi = sum(d["past_window_hi"] for d in pw.values())

    # As shipped (fm_model.py main(), "3. Statewide take-up sensitivity"):
    eff_lo_ship, eff_hi_ship = pool_lo / pw_hi, pool_hi / pw_lo
    # Like-for-like: the low pool was built on the low past-window population.
    eff_lo_fix, eff_hi_fix = pool_lo / pw_lo, pool_hi / pw_hi

    print(f"  FM-1 answer, veterans past window      : {pool_lo:,.0f} - {pool_hi:,.0f}")
    print(f"  past-window population                 : {pw_lo:,.0f} - {pw_hi:,.0f}")
    print(f"  effective rate AS SHIPPED (lo/hi cross): "
          f"{eff_lo_ship:.3%} - {eff_hi_ship:.3%}")
    print(f"  effective rate LIKE-FOR-LIKE           : "
          f"{eff_lo_fix:.3%} - {eff_hi_fix:.3%}")

    reps = {
        "Plan 1": M.Profile("Plan 1", 55, 25, M.MEAN_CLASSIFIED_SALARY, 45_000, 30),
        "Plan 2": M.Profile("Plan 2", 50, 14, M.MEAN_CLASSIFIED_SALARY, 55_000, 36),
        "Hybrid": M.Profile("Hybrid", 50, 9, M.MEAN_CLASSIFIED_SALARY, 60_000, 41),
    }
    nets = {}
    for plan, pr in reps.items():
        r = M.fm4_acceleration(pr, years_purchased=M.YEARS_PURCHASED_AVG)
        nets[plan] = r["cost_total"] - M.price_a3_anc(pr, M.YEARS_PURCHASED_AVG)

    hyb_lo = pw_lo - M.ACTIVE_BY_PLAN["Plan 1"] - M.ACTIVE_BY_PLAN["Plan 2"]
    hyb_hi = pw_hi - M.ACTIVE_BY_PLAN["Plan 1"] - M.ACTIVE_BY_PLAN["Plan 2"]
    plan_pw = {
        "Plan 1": (M.ACTIVE_BY_PLAN["Plan 1"], M.ACTIVE_BY_PLAN["Plan 1"]),
        "Plan 2": (M.ACTIVE_BY_PLAN["Plan 2"], M.ACTIVE_BY_PLAN["Plan 2"]),
        "Hybrid": (hyb_lo, hyb_hi),
    }

    def grid(eff_lo, eff_hi, label):
        pools = {p: (plan_pw[p][0] * eff_lo, plan_pw[p][1] * eff_hi)
                 for p in plan_pw}
        tlo = sum(v[0] for v in pools.values())
        thi = sum(v[1] for v in pools.values())
        print(f"\n  --- {label} ---")
        for p in pools:
            print(f"    {p:<8}{pools[p][0]:>9,.0f} - {pools[p][1]:>9,.0f}"
                  f"   net PV/purchaser {M.money(nets[p]):>10}")
        print(f"    {'TOTAL':<8}{tlo:>9,.0f} - {thi:>9,.0f}")
        out = {}
        for t in (0.05, 0.10, 0.15, 0.20, 0.30):
            lo = sum(pools[p][0] * t * nets[p] for p in pools)
            hi = sum(pools[p][1] * t * nets[p] for p in pools)
            out[t] = (lo, hi)
            print(f"    take-up {t:>4.0%}  {M.money(lo):>14} - {M.money(hi):>14}"
                  f"   {lo/M.TOTAL_COVERED_PAYROLL:>7.3%} - "
                  f"{hi/M.TOTAL_COVERED_PAYROLL:.3%} of payroll")
        return out, (tlo, thi)

    shipped, pool_ship = grid(eff_lo_ship, eff_hi_ship, "AS SHIPPED (brief v1.2 COST grid)")
    fixed, pool_fix = grid(eff_lo_fix, eff_hi_fix, "LIKE-FOR-LIKE")

    # The state/teacher/local table uses a pool-weighted blended per-purchaser
    # figure applied to the FM-1 pool, not the plan grid. Reproduce it.
    blended_num = sum(plan_pw[p][0] * eff_lo_ship * nets[p] for p in plan_pw) \
        + sum(plan_pw[p][1] * eff_hi_ship * nets[p] for p in plan_pw)
    blended_den = pool_ship[0] + pool_ship[1]
    blended = blended_num / blended_den
    bucket_lo = pool_lo * 0.20 * blended
    bucket_hi = pool_hi * 0.20 * blended
    print(f"\n  Reconciliation at 20% take-up:")
    print(f"    COST grid (brief line 157)              "
          f"{M.money(shipped[0.20][0])} - {M.money(shipped[0.20][1])}")
    print(f"    'Who bears it' table (brief line 173)   "
          f"{M.money(bucket_lo)} - {M.money(bucket_hi)}"
          f"   [blended {M.money(blended)} x FM-1 pool]")
    print(f"    LIKE-FOR-LIKE, single consistent pool   "
          f"{M.money(fixed[0.20][0])} - {M.money(fixed[0.20][1])}")
    print(f"\n  Headline band AS SHIPPED   : "
          f"{M.money(shipped[0.05][0])} - {M.money(shipped[0.30][1])}")
    print(f"  Headline band LIKE-FOR-LIKE: "
          f"{M.money(fixed[0.05][0])} - {M.money(fixed[0.30][1])}")
    return nets, fixed, pool_fix


def rt2_hb1867(nets):
    print("\n" + BAR)
    print("RT-2  THE HB 1867 CROSS-CHECK, RESTATED LIKE-FOR-LIKE")
    print(BAR)
    print("  VRS FIS on HB 1867 (1/16/2023), verbatim: 'each person who")
    print("  purchases up to 48 months of active military service would create")
    print("  an unfunded liability that ranges from $10,000 - $60,000'.")
    print("  VRS's own illustration uses an AVERAGE COST of $35,000.")
    print("  HB 1867 granted the service FREE and up to FOUR years.\n")
    print(f"  {'plan':<8}{'net PV @2.5y':>14}{'member price':>14}"
          f"{'free-grant 2.5y':>17}{'free-grant 4y':>15}")
    for plan in ("Plan 1", "Plan 2", "Hybrid"):
        rate = M.ANC[(plan, "non-hazardous")]
        price = rate * M.MEAN_CLASSIFIED_SALARY * M.YEARS_PURCHASED_AVG
        free25 = nets[plan] + price
        free4 = free25 * (4.0 / M.YEARS_PURCHASED_AVG)
        print(f"  {plan:<8}{M.money(nets[plan]):>14}{M.money(price):>14}"
              f"{M.money(free25):>17}{M.money(free4):>15}")
    print("\n  VRS band for exactly that (free, 4 years): $10,000 - $60,000,")
    print("  average $35,000.")
    print("  Implication: run like-for-like, the model is NOT conservative")
    print("  relative to VRS's own figure for Plan 1.\n")
    # And the reverse: what does VRS's own band imply for a PAID purchase?
    print("  Reverse test - take VRS's band as given and subtract the member")
    print("  price actually charged under A-3 for 4 years at $69,865:")
    for plan in ("Plan 1", "Plan 2", "Hybrid"):
        rate = M.ANC[(plan, "non-hazardous")]
        price4 = rate * M.MEAN_CLASSIFIED_SALARY * 4
        print(f"    {plan:<8} member pays {M.money(price4):>9}  ->  net to Fund"
              f" {M.money(10_000 - price4):>10} (VRS floor)"
              f" .. {M.money(60_000 - price4):>10} (VRS ceiling)"
              f" .. {M.money(35_000 - price4):>10} (VRS average)")


def rt3_profile_risk():
    print("\n" + BAR)
    print("RT-3  PROFILE RISK - the per-member figure is ONE profile")
    print(BAR)
    print("  The brief's Plan 1 representative purchaser is age 55 with 25")
    print("  years of service - i.e. sitting exactly 5 years short of age 50")
    print("  + 30 years. FM-2 calls that profile 'the worst case, not the")
    print("  typical one'. Vary it, holding everything else constant.\n")
    print(f"  {'plan':<8}{'age':>5}{'svc':>5}{'unreduced':>11}{'accel':>7}"
          f"{'total PV':>12}{'member price':>14}{'net to Fund':>13}")
    cases = [
        ("Plan 1", 55, 25), ("Plan 1", 52, 22), ("Plan 1", 50, 20),
        ("Plan 1", 48, 18), ("Plan 1", 45, 16), ("Plan 1", 60, 29),
        ("Plan 2", 50, 14), ("Plan 2", 45, 12), ("Plan 2", 58, 20),
        ("Hybrid", 50, 9), ("Hybrid", 42, 7), ("Hybrid", 38, 5),
        ("Hybrid", 58, 11),
    ]
    spread = {}
    for plan, age, svc in cases:
        p = M.Profile(plan, age, svc, M.MEAN_CLASSIFIED_SALARY, 50_000, 35)
        r = M.fm4_acceleration(p, years_purchased=M.YEARS_PURCHASED_AVG)
        price = M.price_a3_anc(p, M.YEARS_PURCHASED_AVG)
        net = r["cost_total"] - price
        spread.setdefault(plan, []).append(net)
        print(f"  {plan:<8}{age:>5}{svc:>5}"
              f"{r['unreduced_age_baseline']:>6.1f}->{r['unreduced_age_with_purchase']:<4.1f}"
              f"{r['acceleration_years']:>7.2f}{M.money(r['cost_total']):>12}"
              f"{M.money(price):>14}{M.money(net):>13}")
    print()
    for plan, vals in spread.items():
        print(f"  {plan:<8} net PV/purchaser ranges "
              f"{M.money(min(vals))} to {M.money(max(vals))}"
              f"  ({max(vals)/max(min(vals),1):.1f}x)")
    print("\n  The brief reports a point estimate per plan and attributes the")
    print("  whole cost range to pool size and take-up. Profile mix is a")
    print("  third source of variance of comparable size and is not banded.")


def rt4_rate_impact(fixed):
    print("\n" + BAR)
    print("RT-4  THE NUMBER THAT GOES IN A FISCAL IMPACT STATEMENT")
    print(BAR)
    print("  A present value is not what VRS files. Under Va. Code 51.1-145 I")
    print("  the Board certifies a CONTRIBUTION RATE, and under 51.1-145 K the")
    print("  appropriation bill carries the resulting employer contributions.")
    print("  Amortise the one-time PV as a level percent of payroll.\n")
    i, g = M.DISCOUNT, M.SALARY_GROWTH
    for n in (20, 25):
        # level-percent-of-payroll amortisation factor
        j = (1 + i) / (1 + g) - 1
        af = (1 - (1 + j) ** -n) / j
        print(f"  {n}-year level-percent-of-payroll amortisation "
              f"(i={i:.2%}, payroll growth={g:.1%}):")
        for t in (0.05, 0.20, 0.30):
            lo, hi = fixed[t]
            rlo = (lo / af) / M.TOTAL_COVERED_PAYROLL
            rhi = (hi / af) / M.TOTAL_COVERED_PAYROLL
            print(f"    take-up {t:>4.0%}  PV {M.money(lo):>13} - {M.money(hi):>13}"
                  f"   ->  rate impact {rlo*10000:>5.1f} - {rhi*10000:>5.1f} bp"
                  f"  ({rlo:.4%} - {rhi:.4%} of payroll)")
        print()
    print("  For scale: VRS statewide employer rates are in the 14%-20% range.")
    print("  A 1-7 basis point rate impact is the honest translation of the")
    print("  PV, and it is a far better number for the JLC than '$57 million'.")


if __name__ == "__main__":
    nets, fixed, _ = rt1_pool_pairing()
    rt2_hb1867(nets)
    rt3_profile_risk()
    rt4_rate_impact(fixed)
