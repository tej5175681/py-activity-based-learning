"""
Test Suite for Case Study 07: Multi-Warehouse Inventory Matrix Reconciliation
"""
from problem_46_inventory_reconciliation import reconcile_inventory

def run_tests():
    print("=" * 70)
    print("RUNNING TESTS FOR CASE STUDY 07")
    print("=" * 70)

    warehouses = ["WH-A", "WH-B"]
    products = ["Item1"]

    # Test Case 1: Simple 1-to-1 Transfer
    # WH-A has 50 (Target 30 -> +20 Surplus)
    # WH-B has 10 (Target 30 -> -20 Deficit)
    # Transfer 20 from WH-A to WH-B
    act1 = [[50], [10]]
    tgt1 = [[30], [30]]
    diff, xfers, unmet = reconcile_inventory(warehouses, products, act1, tgt1)

    assert diff[0][0] == 20 and diff[1][0] == -20
    assert len(xfers) == 1
    assert xfers[0] == ("WH-A", "WH-B", "Item1", 20)
    assert len(unmet) == 0
    print("[PASS] Test Case 1: Exact balanced surplus-deficit transfer verified.")

    # Test Case 2: Partial Internal Rebalancing with Unmet Deficit
    # WH-A has 35 (Target 30 -> +5 Surplus)
    # WH-B has 10 (Target 30 -> -20 Deficit)
    # Transfer 5 from WH-A to WH-B; WH-B still short by 15!
    act2 = [[35], [10]]
    tgt2 = [[30], [30]]
    diff, xfers, unmet = reconcile_inventory(warehouses, products, act2, tgt2)

    assert len(xfers) == 1 and xfers[0][3] == 5
    assert len(unmet) == 1 and unmet[0] == ("WH-B", "Item1", 15)
    print("[PASS] Test Case 2: Partial rebalancing and unmet deficit logging verified.")

    # Test Case 3: Already Balanced Inventory (Zero Transfers)
    act3 = [[30], [30]]
    tgt3 = [[30], [30]]
    diff, xfers, unmet = reconcile_inventory(warehouses, products, act3, tgt3)

    assert diff[0][0] == 0 and diff[1][0] == 0
    assert len(xfers) == 0 and len(unmet) == 0
    print("[PASS] Test Case 3: Zero-variance balanced state verified.")

    # Test Case 4: Multiple Sources to Single Destination
    wh3 = ["W1", "W2", "W3"]
    # W1 has +10, W2 has +15, W3 has -25
    act4 = [[40], [45], [5]]
    tgt4 = [[30], [30], [30]]
    diff, xfers, unmet = reconcile_inventory(wh3, products, act4, tgt4)

    assert len(xfers) == 2
    assert xfers[0] == ("W1", "W3", "Item1", 10)
    assert xfers[1] == ("W2", "W3", "Item1", 15)
    assert len(unmet) == 0
    print("[PASS] Test Case 4: Multi-source convergence transfer verified.")

    print("=" * 70)
    print("ALL 4 UNIT TESTS PASSED FOR CASE STUDY 07!")
    print("=" * 70)

if __name__ == "__main__":
    run_tests()
