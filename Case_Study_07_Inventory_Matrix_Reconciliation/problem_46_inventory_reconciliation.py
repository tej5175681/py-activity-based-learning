"""
Case Study 07: Multi-Warehouse Inventory Matrix Reconciliation System
=====================================================================
Syllabus Concepts Used:
- Nested Lists (2D Warehouse x Product Matrix)
- Variables, Data Types (int, str, list, tuple)
- Relational and Logical Operators
- Conditional Statements (if, elif, else)
- Nested Loops (row-wise and column-wise traversals)
- Tuples and Tuple Unpacking
- Greedy Rebalancing Algorithm without External Libraries
- Formatted Tabular Statements

Description:
Reconciles product stock across multiple regional warehouses:
1. Computes the deviation matrix (Actual Stock - Target Stock).
2. Classifies warehouse-product pairs into Surpluses, Deficits, or Balanced.
3. Computes automated inter-warehouse stock transfer dispatches:
   (source_wh, dest_wh, product_name, transfer_qty)
4. Determines post-transfer network balance and unmet supply deficits.
"""

def reconcile_inventory(warehouses, products, actual_matrix, target_matrix):
    """
    warehouses: List of strings (warehouse names)
    products: List of strings (product names)
    actual_matrix: 2D nested list [num_wh x num_products]
    target_matrix: 2D nested list [num_wh x num_products]
    """
    num_wh = len(warehouses)
    num_prod = len(products)

    # 1. Compute difference matrix (Actual - Target)
    diff_matrix = []
    for i in range(num_wh):
        row_diff = []
        for j in range(num_prod):
            row_diff.append(actual_matrix[i][j] - target_matrix[i][j])
        diff_matrix.append(row_diff)

    # 2. Product-wise transfer planning
    transfer_schedule = []
    unmet_deficits = []

    for j in range(num_prod):
        prod_name = products[j]

        # Extract surpluses and deficits for this product
        surplus_list = []  # List of [wh_index, qty]
        deficit_list = []  # List of [wh_index, qty]

        for i in range(num_wh):
            diff = diff_matrix[i][j]
            if diff > 0:
                surplus_list.append([i, diff])
            elif diff < 0:
                deficit_list.append([i, abs(diff)])

        # Greedy transfer matching algorithm
        s_idx = 0
        d_idx = 0

        while s_idx < len(surplus_list) and d_idx < len(deficit_list):
            src_wh_idx, s_qty = surplus_list[s_idx]
            dst_wh_idx, d_qty = deficit_list[d_idx]

            transfer_qty = min(s_qty, d_qty)
            src_name = warehouses[src_wh_idx]
            dst_name = warehouses[dst_wh_idx]

            transfer_schedule.append((src_name, dst_name, prod_name, transfer_qty))

            surplus_list[s_idx][1] -= transfer_qty
            deficit_list[d_idx][1] -= transfer_qty

            if surplus_list[s_idx][1] == 0:
                s_idx += 1
            if deficit_list[d_idx][1] == 0:
                d_idx += 1

        # Check remaining deficits that could not be satisfied internally
        while d_idx < len(deficit_list):
            dst_wh_idx, remaining_d = deficit_list[d_idx]
            if remaining_d > 0:
                unmet_deficits.append((warehouses[dst_wh_idx], prod_name, remaining_d))
            d_idx += 1

    return diff_matrix, transfer_schedule, unmet_deficits


def print_reconciliation_report(warehouses, products, actual, target, diff, transfers, unmet):
    print("=" * 105)
    print("                      DR. RVR NRI INSTITUTE OF TECHNOLOGY")
    print("          MULTI-WAREHOUSE INVENTORY MATRIX AUDIT & RECONCILIATION REPORT")
    print("=" * 105)

    headers = "".join([f"{p[:12]:>14}" for p in products])
    print(f"{'Warehouse Location':<26}{headers}")
    print("-" * 105)

    print("[SECTION 1: ACTUAL STOCK INVENTORY MATRIX]")
    for i in range(len(warehouses)):
        vals = "".join([f"{actual[i][j]:>14}" for j in range(len(products))])
        print(f"{warehouses[i]:<26}{vals}")

    print("\n[SECTION 2: TARGET THRESHOLD MATRIX]")
    for i in range(len(warehouses)):
        vals = "".join([f"{target[i][j]:>14}" for j in range(len(products))])
        print(f"{warehouses[i]:<26}{vals}")

    print("\n[SECTION 3: VARIANCE MATRIX (+Surplus / -Shortage)]")
    for i in range(len(warehouses)):
        diff_str = ""
        for j in range(len(products)):
            d = diff[i][j]
            prefix = "+" if d > 0 else ""
            diff_str += f"{prefix + str(d):>14}"
        print(f"{warehouses[i]:<26}{diff_str}")

    print("-" * 105)
    print("\n[SECTION 4: RECOMMENDED INTER-WAREHOUSE STOCK TRANSFERS]")
    print(f"{'Source Warehouse':<26}{'Destination Warehouse':<26}{'Product Name':<18}{'Transfer Qty':<12}")
    print("-" * 105)
    if len(transfers) == 0:
        print("No transfers needed. Inventory is fully balanced across warehouses.")
    else:
        for t in transfers:
            src, dst, prod, qty = t
            print(f"{src:<26}{dst:<26}{prod:<18}{qty:<12}")

    print("-" * 105)
    print("\n[SECTION 5: UNMET NETWORK SHORTAGES (EXTERNAL PROCUREMENT NEEDED)]")
    if len(unmet) == 0:
        print("> All warehouse deficits successfully fulfilled via internal network rebalancing.")
    else:
        for u in unmet:
            wh, prod, qty = u
            print(f"> Shortage Alert: {wh} requires {qty} units of '{prod}' [External Purchase Required]")
    print("=" * 105)


if __name__ == "__main__":
    wh_list = [
        "WH-1 Central Eluru",
        "WH-2 North Vijayawada",
        "WH-3 East Guntur",
        "WH-4 South Mangalagiri"
    ]

    prod_list = ["Laptops", "Servers", "Routers", "Projectors", "Smartboards"]

    # 4 x 5 Actual stock nested list
    actual_stock = [
        [50, 12, 80, 25, 15],  # WH-1
        [15,  4, 20, 10,  5],  # WH-2
        [30, 15, 60, 18, 12],  # WH-3
        [10,  2, 15,  5,  3],  # WH-4
    ]

    # 4 x 5 Target stock nested list
    target_stock = [
        [30,  8, 40, 15, 10],  # WH-1 has surplus
        [25,  8, 40, 15, 10],  # WH-2 has deficit
        [25,  8, 40, 15, 10],  # WH-3 has surplus
        [25,  8, 40, 15, 10],  # WH-4 has deficit
    ]

    diff_mat, xfers, unfulfilled = reconcile_inventory(wh_list, prod_list, actual_stock, target_stock)
    print_reconciliation_report(wh_list, prod_list, actual_stock, target_stock, diff_mat, xfers, unfulfilled)
