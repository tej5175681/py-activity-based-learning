"""
Test Suite for Case Study 02: Progressive Electricity Billing
"""
from problem_02_electricity_billing import calculate_single_bill, analyze_multimonth_consumption

def run_tests():
    print("=" * 70)
    print("RUNNING TESTS FOR CASE STUDY 02")
    print("=" * 70)

    # Test Case 1: First slab only (50 units, prompt payment)
    # Energy: 50 * 1.5 = 75. Fixed: 100. Surcharge: 0. Subtotal: 175.
    # Rebate 5%: 8.75. Net: 166.25.
    u, echg, fchg, sur, reb, net = calculate_single_bill(50, True)
    assert echg == 75.0, f"Expected 75.0, got {echg}"
    assert fchg == 100.0, f"Expected 100.0, got {fchg}"
    assert sur == 0.0, f"Expected 0.0 surcharge, got {sur}"
    assert reb == 8.75, f"Expected 8.75 rebate, got {reb}"
    assert abs(net - 166.25) < 1e-4, f"Expected 166.25, got {net}"
    print("[PASS] Test Case 1: Slab 1 consumption & prompt rebate verified.")

    # Test Case 2: Multi-slab crossing into Surcharge territory (>1500 energy)
    # 500 units:
    # 100 * 1.50 = 150
    # 100 * 3.00 = 300
    # 200 * 4.50 = 900
    # 100 * 6.00 = 600
    # Energy sum = 1950.0 (> 1500 -> surcharge 10% = 195.0)
    # Fixed = 100.0
    # Subtotal = 1950 + 100 + 195 = 2245.0
    # Paid on time = False -> Rebate = 0.0
    # Net = 2245.0
    u, echg, fchg, sur, reb, net = calculate_single_bill(500, False)
    assert echg == 1950.0, f"Expected 1950.0 energy charge, got {echg}"
    assert sur == 195.0, f"Expected 195.0 surcharge, got {sur}"
    assert reb == 0.0, f"Expected 0.0 rebate, got {reb}"
    assert net == 2245.0, f"Expected 2245.0 net bill, got {net}"
    print("[PASS] Test Case 2: High consumption slab 4 with surcharge verified.")

    # Test Case 3: Zero units boundary
    u, echg, fchg, sur, reb, net = calculate_single_bill(0, True)
    # Energy: 0. Fixed: 100. Surcharge: 0. Subtotal: 100. Rebate: 5. Net: 95.
    assert echg == 0.0 and fchg == 100.0 and net == 95.0
    print("[PASS] Test Case 3: Zero units minimum fixed charge verified.")

    # Test Case 4: Spike detection logic
    consumer = ("C1", "Test Consumer", "M1")
    history_data = [
        ("Month1", 100, True),
        ("Month2", 130, True), # +30% -> Spike!
        ("Month3", 140, True), # +7.69% -> Normal
    ]
    _, analysis = analyze_multimonth_consumption(consumer, history_data, 25.0)
    assert analysis[0][5] is False, "Month 1 should not be a spike"
    assert analysis[1][5] is True, "Month 2 should be flagged as spike"
    assert analysis[2][5] is False, "Month 3 should not be flagged as spike"
    print("[PASS] Test Case 4: Consecutive month spike detection verified.")

    print("=" * 70)
    print("ALL 4 UNIT TESTS PASSED FOR CASE STUDY 02!")
    print("=" * 70)

if __name__ == "__main__":
    run_tests()
