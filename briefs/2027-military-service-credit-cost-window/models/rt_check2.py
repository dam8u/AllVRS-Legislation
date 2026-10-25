"""RT addendum — what does the section 2.2 ceiling actually cap?

Red team working file, second pass (MOO-289 continuation).  Imports
`fm_model` unmodified; writes nothing.  Companion to `rt_check.py`.

WHY THIS PASS EXISTS
--------------------
F-1 in `05-Red-Team-Review.md` tested the ceiling on ONE reading: that
"the actuarial equivalent cost of the service credit purchased" means the
member's own full-basis cost to the Fund, which is what
`price_threshold_graded` charges (`fm4_acceleration(...)["cost_total"]`,
benefit-amount channel PLUS retirement-date acceleration).

That reading is the FAVOURABLE one to the package, and it is probably the
wrong one.  "Actuarial equivalent cost" is a term already in use in the
immediately preceding sentence of the same paragraph of section 51.1-142.2
B 3 -- it is what a member pays today after the 24-month window closes.
Within one paragraph the same phrase carries one meaning, so the ceiling
is the STATUTORY AEC: the actuarial equivalent of the service credit
purchased, i.e. the benefit-amount channel, which is what the model models
at `aec_pct_of_salary`.  Retirement-date acceleration is a cost the Fund
bears because of what the member then DOES; it is not the actuarial
equivalent of the credit itself.

This pass asks three questions the first pass did not:

  Q1  On the statutory reading, how much of the above-ANC excess can the
      ceiling let the Board recover AT ALL -- before uniformity is even
      considered?
  Q2  The draft's ceiling binds only "any schedule of rates adopted
      pursuant to this paragraph."  For a member whose own statutory AEC
      is BELOW the published approximate normal cost, a schedule may not
      charge the published rate.  Who are those members and what is the
      mandatory discount worth per member?
  Q3  Does `price_age_graded`'s stated design assumption -- "the schedule
      never charges less than the published ANC, which is what makes it
      politically presentable as 'still a published rate'" -- survive the
      ceiling as drafted?

Run:  python3 rt_check2.py
"""

from fm_model import (
    ANC,
    MEAN_CLASSIFIED_SALARY,
    PLAN_RETIRE_AGE,
    Profile,
    YEARS_PURCHASED_AVG,
    aec_pct_of_salary,
    breakeven_age,
    fm4_acceleration,
    money,
    price_a3_anc,
    price_threshold_graded,
)

PLANS = ("Plan 1", "Plan 2", "Hybrid")
SAL = MEAN_CLASSIFIED_SALARY
YEARS = YEARS_PURCHASED_AVG     # 2.5, section 4.8's own basis

# Annex 2 Closure section 4.8's representative profiles, as reproduced in
# f1_lawful_class_rate.plan_nets().
REPS = {
    "Plan 1": Profile("Plan 1", 55, 25, SAL, 45_000, 30),
    "Plan 2": Profile("Plan 2", 50, 14, SAL, 55_000, 36),
    "Hybrid": Profile("Hybrid", 50, 9, SAL, 60_000, 41),
}


def statutory_aec_price(plan, purchase_age, years=YEARS, salary=SAL,
                        retire_age=None):
    """The ceiling, on the statutory reading: AEC of the credit purchased."""
    r = PLAN_RETIRE_AGE[plan] if retire_age is None else retire_age
    return aec_pct_of_salary(plan, purchase_age, r) * salary * years


def rule(title):
    print(f"\n{'=' * 78}\n  {title}\n{'=' * 78}")


# ---------------------------------------------------------------------------
# Q1 — the ceiling against what the 100% dial charges
# ---------------------------------------------------------------------------
rule("Q1  The 100% dial against the ceiling, on the STATUTORY reading")
print(f"  Annex 2 Closure section 4.8 representative profiles, {YEARS:g} years, "
      f"salary {money(SAL)}")
print(f"\n  {'plan':<9}{'ANC price':>12}{'AEC ceiling':>13}"
      f"{'100% dial charge':>18}{'over ceiling':>14}{'max lawful':>12}")
print(f"  {'':<9}{'(sentence 2)':>12}{'(sentence 4)':>13}"
      f"{'(price_threshold)':>18}{'by':>14}{'recovery':>12}")
for plan in PLANS:
    p = REPS[plan]
    anc = price_a3_anc(p, YEARS)
    ceil = statutory_aec_price(plan, p.age)
    dial100 = price_threshold_graded(p, YEARS, recovery=1.0)
    full = fm4_acceleration(p, years_purchased=YEARS)["cost_total"]
    excess = full - anc
    lawful = (ceil - anc) / excess if excess > 0 else None
    print(f"  {plan:<9}{money(anc):>12}{money(ceil):>13}{money(dial100):>18}"
          f"{money(dial100 - ceil):>14}"
          f"{(f'{lawful * 100:.0f}%' if lawful is not None else 'n/a'):>12}")
print("""
  Reading: the 100% dial charges the member the Fund's FULL cost, which
  exceeds the statutory AEC of the credit by the acceleration channel.  The
  ceiling therefore caps recovery well below 100% for every representative
  profile, BEFORE the uniformity constraint of F-1 is applied at all.  The
  two constraints compound; they are not alternatives.""")

# ---------------------------------------------------------------------------
# Q2 — the members a schedule may not charge the published rate
# ---------------------------------------------------------------------------
rule("Q2  Members whose own AEC is BELOW the published approximate normal cost")
print("  A schedule 'shall not require payment of an amount exceeding the")
print("  actuarial equivalent cost of the service credit purchased.'  Below the")
print("  break-even purchase age the AEC/ANC multiple is under 1.0, so the")
print("  published rate itself exceeds the ceiling and a SCHEDULE must charge")
print("  less than the published rate.  Break-even ages, recomputed:")
print()
for plan in PLANS:
    r = PLAN_RETIRE_AGE[plan]
    be = breakeven_age(plan, r, ANC[(plan, "non-hazardous")])
    print(f"    {plan:<9} retire at {r}   break-even purchase age "
          f"{be:.2f}" if be else f"    {plan:<9} no crossing")
print(f"\n  Mandatory discount per member, {YEARS:g} years at {money(SAL)}:")
print(f"\n  {'plan':<9}{'age':>5}{'ANC price':>12}{'AEC ceiling':>13}"
      f"{'schedule must':>16}{'vs. today':>12}")
print(f"  {'':<9}{'':>5}{'':>12}{'':>13}{'charge <=':>16}{'(B 3 ANC)':>12}")
total_rows = 0
for plan in PLANS:
    for age in (30, 35, 40, 45, 50, 55):
        anc = price_a3_anc(Profile(plan, age, 10.0, SAL, SAL, 30), YEARS)
        ceil = statutory_aec_price(plan, age)
        if ceil >= anc:
            continue
        total_rows += 1
        print(f"  {plan:<9}{age:>5}{money(anc):>12}{money(ceil):>13}"
              f"{money(ceil):>16}{money(ceil - anc):>12}")
print(f"\n  Rows where the ceiling bites below the published rate: {total_rows}")
print("""
  This is a LEAK, not a saving: for these members the bill as drafted makes
  the price lower than section 51.1-142.2 B 3 charges today, and nothing in
  the fiscal model prices a sub-ANC purchase.  Note the escape, and why it
  does not help: the ceiling binds only "any schedule of rates adopted
  pursuant to this paragraph", so the Board can avoid it by adopting NO
  schedule -- but the whole fiscal case depends on adopting one.""")

# ---------------------------------------------------------------------------
# Q3 — the model's own design assumption against the drafted ceiling
# ---------------------------------------------------------------------------
rule("Q3  price_age_graded's floor assumption against the drafted ceiling")
print("""  price_age_graded docstring: "the schedule never charges less than the
  published ANC -- which is what makes it politically presentable as 'still a
  published rate'."  The drafted ceiling contradicts that for every member
  below the break-even age: for them the ceiling is BINDING and below the
  floor the model assumes.  The model's floor is a modelling choice; the
  ceiling is statutory text.  Where they conflict the text wins, so the
  schedule is not a one-way upward grade -- it is graded in both directions,
  and the downward leg is unpriced.""")
print(f"\n  {'plan':<9}{'age':>5}{'AEC/ANC multiple':>20}{'model floor holds?':>22}")
for plan in PLANS:
    for age in (35, 45, 55):
        mult = (aec_pct_of_salary(plan, age, PLAN_RETIRE_AGE[plan])
                / ANC[(plan, "non-hazardous")])
        print(f"  {plan:<9}{age:>5}{mult:>19.2f}x"
              f"{('yes' if mult >= 1 else 'NO — ceiling binds'):>22}")

print(f"\n{'-' * 78}")
print("  Red team working file.  fm_model.py imported unmodified; nothing in")
print("  the package was altered by this pass.")
print(f"{'-' * 78}")
