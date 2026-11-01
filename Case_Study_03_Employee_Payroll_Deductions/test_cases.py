"""
Test Suite for Case Study 03: Employee Payroll and Progressive Deductions
"""
from problem_04_employee_payroll import compute_employee_payroll, generate_batch_payroll

def run_tests():
    print("=" * 70)
    print("RUNNING TESTS FOR CASE STUDY 03")
    print("=" * 70)

    # Test Case 1: Low earner within 0% tax slab (Gross <= 30,000)
    # Basic = 15,000. DA = 2250, HRA = 3000, Special = 1500. OT = 0, Incentive = 0.
    # Gross = 15000 + 2250 + 3000 + 1500 = 21750.0.
    # Tax = 0. PF = 0.12 * 15000 = 1800. PT = 200. Health = 1000. Total Ded = 3000.
    # Net = 21750 - 3000 = 18750.0.
    emp1 = ("T1", "Low Earner", "Intern", 15000.0, 0, 1)
    earnings, deductions, net = compute_employee_payroll(emp1)
    b, da, hra, sp, ot, inc, gross = earnings
    tax, pf, pt, hi, tot_ded = deductions

    assert gross == 21750.0, f"Expected gross 21750.0, got {gross}"
    assert tax == 0.0, f"Expected 0 tax, got {tax}"
    assert pf == 1800.0, f"Expected 1800.0 PF, got {pf}"
    assert tot_ded == 3000.0, f"Expected 3000.0 total deductions, got {tot_ded}"
    assert net == 18750.0, f"Expected net 18750.0, got {net}"
    print("[PASS] Test Case 1: Nil tax slab and exact net pay verified.")

    # Test Case 2: Overtime calculation and Performance Incentive
    # Basic = 32,000. OT = 16 hours. Hourly rate = 32000 / 160 = 200.
    # OT Pay = 16 * 200 * 1.5 = 4800.0. Rating = 5 -> Incentive = 12,000.
    emp2 = ("T2", "High Achiever", "Lead", 32000.0, 16, 5)
    earnings, deductions, net = compute_employee_payroll(emp2)
    assert earnings[4] == 4800.0, f"Expected OT pay 4800.0, got {earnings[4]}"
    assert earnings[5] == 12000.0, f"Expected incentive 12000.0, got {earnings[5]}"
    print("[PASS] Test Case 2: Overtime rate multiplier and performance incentive verified.")

    # Test Case 3: Progressive Tax Crossing Multiple Slabs (> 100,000 gross)
    # Let Basic = 80,000. DA = 12000, HRA = 16000, Special = 8000.
    # Gross base = 80000 + 36000 = 116,000. Plus 12000 inc = 128,000.
    # Tax:
    # 0 - 30,000: 0
    # 30,000 - 60,000: 30000 * 0.05 = 1500
    # 60,000 - 100,000: 40000 * 0.10 = 4000
    # > 100,000: (128,000 - 100,000) * 0.20 = 28000 * 0.20 = 5600
    # Total Tax = 1500 + 4000 + 5600 = 11100.0.
    emp3 = ("T3", "Senior Exec", "Director", 80000.0, 0, 5)
    earnings, deductions, net = compute_employee_payroll(emp3)
    assert deductions[0] == 11100.0, f"Expected tax 11100.0, got {deductions[0]}"
    print("[PASS] Test Case 3: High-income progressive multi-slab taxation verified.")

    # Test Case 4: Batch aggregation consistency
    batch = [emp1, emp2, emp3]
    records, totals = generate_batch_payroll(batch)
    tot_g, tot_t, tot_p, tot_n = totals
    calc_gross = sum(r[1][6] for r in records)
    calc_net = sum(r[3] for r in records)
    assert tot_g == calc_gross and tot_n == calc_net
    print("[PASS] Test Case 4: Batch payroll register summation integrity verified.")

    print("=" * 70)
    print("ALL 4 UNIT TESTS PASSED FOR CASE STUDY 03!")
    print("=" * 70)

if __name__ == "__main__":
    run_tests()
