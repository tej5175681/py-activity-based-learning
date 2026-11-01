"""
Test Suite for Case Study 09: Campus Festival Financial Audit
"""
from problem_74_festival_audit import audit_festival_finances

def run_tests():
    print("=" * 70)
    print("RUNNING TESTS FOR CASE STUDY 09")
    print("=" * 70)

    # Test Case 1: Duplicate Registration Detection
    regs1 = [
        ("R1", "S101", "Student A", "EVENT_X", 500.0, "PAID"),
        ("R2", "S101", "Student A", "EVENT_X", 500.0, "PAID"), # Exact duplicate
        ("R3", "S101", "Student A", "EVENT_Y", 300.0, "PAID"), # Different event -> valid
    ]
    spons1 = []
    exp1 = []
    val, dup, short, exps, summary = audit_festival_finances(regs1, spons1, exp1)

    assert len(val) == 2, f"Expected 2 valid registrations, got {len(val)}"
    assert len(dup) == 1 and dup[0][0] == "R2"
    assert summary[2] == 800.0, f"Expected 800 revenue, got {summary[2]}"
    print("[PASS] Test Case 1: Duplicate detection for same student & event verified.")

    # Test Case 2: Unpaid / Pending Fee Isolation
    regs2 = [
        ("R1", "S1", "Name", "E1", 400.0, "PAID"),
        ("R2", "S2", "Name", "E1", 400.0, "PENDING"),
    ]
    val, dup, short, exps, summary = audit_festival_finances(regs2, [], [])
    assert summary[2] == 400.0  # Paid
    assert summary[3] == 400.0  # Pending
    print("[PASS] Test Case 2: Separation of realized and pending registration fees verified.")

    # Test Case 3: Sponsorship Shortfall Calculation
    spons3 = [
        ("SP1", "Alpha", "Title", 100000.0, 75000.0), # 25k shortfall
        ("SP2", "Beta", "Gold", 50000.0, 50000.0),    # 0 shortfall
    ]
    val, dup, short, exps, summary = audit_festival_finances([], spons3, [])
    assert len(short) == 1
    assert short[0][5] == 25000.0
    print("[PASS] Test Case 3: Sponsorship collection shortfall detection verified.")

    # Test Case 4: Net Surplus / Deficit Balance Sheet
    # Income: 10,000. Expenses: 12,000 -> Deficit of 2,000.
    regs4 = [("R1", "S1", "N1", "E1", 10000.0, "PAID")]
    exp4 = [["General", "Hall", 10000.0, 12000.0]]
    val, dup, short, exps, summary = audit_festival_finances(regs4, [], exp4)
    tot_inc, net_bal, is_surp = summary[6], summary[7], summary[8]
    assert tot_inc == 10000.0
    assert net_bal == -2000.0
    assert is_surp is False
    print("[PASS] Test Case 4: Net deficit calculation and boolean flag verified.")

    print("=" * 70)
    print("ALL 4 UNIT TESTS PASSED FOR CASE STUDY 09!")
    print("=" * 70)

if __name__ == "__main__":
    run_tests()
