# Case Study 95: Integrated Manufacturing Production Planner
materials = ["Steel", "Plastic", "Rubber"]
stock = [900, 400, 300]

# Product: (name, [material per unit], order demand (good units), expected defect %,
#           last batch produced, last batch defective)
products = [
    ("Gear Box",  [4, 1, 0], 120, 5,  100, 3),
    ("Roller",    [2, 2, 1], 150, 10, 200, 30),
    ("Seal Kit",  [0, 1, 3], 80,  0,  50,  1),
]
QUALITY_LIMIT = 4    # % defects allowed in a batch

print(f"{'Product':<10}{'Demand':>7}{'Plan':>6}{'Feasible':>9}  Notes")
for p in products:
    name, req, demand, defect_pct, produced, defective = p

    # units to make so that after defects 'demand' good units remain (rounded up)
    plan = demand * 100 // (100 - defect_pct)
    if demand * 100 % (100 - defect_pct) != 0:
        plan = plan + 1

    # how many units the remaining stock can support
    feasible = plan
    short = []
    for k in range(len(materials)):
        if req[k] > 0:
            can = stock[k] // req[k]
            if can < feasible:
                feasible = can
    for k in range(len(materials)):
        need = req[k] * plan
        if need > stock[k]:
            short.append(f"{materials[k]} short by {need - stock[k]}")

    # consume material for what can actually be produced
    for k in range(len(materials)):
        stock[k] -= req[k] * feasible

    notes = []
    if feasible < plan:
        notes.append("CANNOT meet full order (" + ", ".join(short) + ")")
    else:
        notes.append("order feasible")
    rate = defective * 100 / produced
    if rate > QUALITY_LIMIT:
        notes.append(f"QUALITY VIOLATION: last batch defect {rate:.1f}% > {QUALITY_LIMIT}%")
    else:
        notes.append(f"quality ok ({rate:.1f}%)")
    good = feasible * (100 - defect_pct) // 100
    print(f"{name:<10}{demand:>7}{plan:>6}{feasible:>9}  " + "; ".join(notes))
    print(f"{'':<10}expected good units: {good}, unfulfilled demand: {demand - good if demand > good else 0}")

print("\nRemaining raw material:")
for k in range(len(materials)):
    print(f"  {materials[k]:<8}{stock[k]}")
