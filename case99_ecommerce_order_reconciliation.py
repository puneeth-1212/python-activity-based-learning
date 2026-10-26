# Case Study 99: Integrated E-Commerce Order Processing and Reconciliation
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
prices = [55000, 500, 1200, 9000]
stock = [10, 50, 30, 8]
opening = stock[:]

# Order tuple: (order id, product, quantity, discount %)
orders = [
    ("O1", "Laptop",   3, 5),
    ("O2", "Mouse",    20, 10),
    ("O3", "Monitor",  6, 0),
    ("O4", "Monitor",  4, 0),       # only 2 left -> backorder
    ("O5", "Keyboard", 10, 15),
    ("O6", "Tablet",   1, 0),       # unknown product
]
# Return tuple: (order id, quantity)
returns = [("O2", 5), ("O1", 1), ("O5", 12), ("O4", 1), ("O9", 1)]

dispatched = [0] * len(orders)
paid_per_unit = [0.0] * len(orders)
revenue = 0.0
log = []

print("=== Order Processing ===")
for i in range(len(orders)):
    oid, prod, qty, disc = orders[i]
    p = -1
    for k in range(len(products)):
        if products[k] == prod:
            p = k
    if p == -1:
        print(f"{oid}: unknown product '{prod}'")
        log.append(oid + " unknown product")
        continue
    if stock[p] >= qty:
        stock[p] -= qty
        dispatched[i] = qty
        unit = prices[p] * (100 - disc) / 100
        paid_per_unit[i] = unit
        revenue += unit * qty
        print(f"{oid}: {qty} x {prod} dispatched, billed Rs.{unit * qty:,.2f}")
    else:
        print(f"{oid}: {qty} x {prod} NOT dispatched (only {stock[p]} in stock) - backordered")
        log.append(oid + " backordered " + str(qty - stock[p]) + " short")

print("\n=== Returns ===")
refunds = 0.0
for oid, rq in returns:
    idx = -1
    for i in range(len(orders)):
        if orders[i][0] == oid:
            idx = i
    if idx == -1:
        print(f"{oid}: return for unknown order - DISCREPANCY")
        log.append(oid + " return without order")
    elif rq > dispatched[idx]:
        print(f"{oid}: return {rq} exceeds dispatched {dispatched[idx]} - DISCREPANCY")
        log.append(oid + " return exceeds dispatched")
    else:
        prod = orders[idx][1]
        for k in range(len(products)):
            if products[k] == prod:
                stock[k] += rq
        dispatched[idx] -= rq
        amt = rq * paid_per_unit[idx]
        refunds += amt
        print(f"{oid}: {rq} x {prod} returned, refund Rs.{amt:,.2f}")

print("\n=== Final Summary ===")
print(f"Gross revenue : Rs.{revenue:,.2f}")
print(f"Refunds       : Rs.{refunds:,.2f}")
print(f"Net revenue   : Rs.{revenue - refunds:,.2f}")
print(f"\n{'Product':<10}{'Opening':>8}{'Closing':>9}")
for k in range(len(products)):
    print(f"{products[k]:<10}{opening[k]:>8}{stock[k]:>9}")
print("\nDiscrepancies / exceptions:")
for l in log:
    print(" -", l)
