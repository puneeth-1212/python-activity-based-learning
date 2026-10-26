# Case Study 93: Smart Public Transport Fare Reconciliation
routes = ["R1", "R2", "R3"]
base_fare = [10, 15, 25]
categories = ["Adult", "Student", "Senior", "Child"]
factor = [1.0, 0.5, 0.5, 0.0]

# Trip record tuple: (route, category, passengers, amount collected)
trips = [
    ("R1", "Adult",   40, 400),
    ("R1", "Student", 30, 150),
    ("R1", "Senior",  10, 40),     # short by 10
    ("R2", "Adult",   25, 375),
    ("R2", "Child",   8,  0),
    ("R2", "Student", 20, 200),    # excess 50
    ("R3", "Adult",   15, 375),
    ("R3", "Senior",  6,  75),
    ("R3", "Pilot",   2,  0),      # invalid category
]

route_expected = [0.0] * len(routes)
route_collected = [0.0] * len(routes)
issues = 0

print(f"{'Route':<6}{'Category':<9}{'Pax':>4}{'Expected':>10}{'Collected':>11}  Status")
for trip in trips:
    route, cat, pax, collected = trip
    r = -1
    c = -1
    for i in range(len(routes)):
        if routes[i] == route:
            r = i
    for i in range(len(categories)):
        if categories[i] == cat:
            c = i
    if r == -1 or c == -1:
        print(f"{route:<6}{cat:<9}{pax:>4}{'-':>10}{collected:>11}  INVALID ROUTE/CATEGORY")
        issues = issues + 1
        continue
    expected = base_fare[r] * factor[c] * pax
    route_expected[r] += expected
    route_collected[r] += collected
    diff = collected - expected
    if diff == 0:
        status = "OK"
    elif diff < 0:
        status = "SHORT by " + str(-diff)
        issues = issues + 1
    else:
        status = "EXCESS by " + str(diff)
        issues = issues + 1
    print(f"{route:<6}{cat:<9}{pax:>4}{expected:>10.2f}{collected:>11.2f}  {status}")

print("\n=== Route-wise Reconciliation ===")
te = 0.0
tc = 0.0
for i in range(len(routes)):
    d = route_collected[i] - route_expected[i]
    print(f"{routes[i]}: expected {route_expected[i]:.2f}, collected {route_collected[i]:.2f}, difference {d:+.2f}")
    te += route_expected[i]
    tc += route_collected[i]
print(f"\nTOTAL expected {te:.2f}, collected {tc:.2f}, net difference {tc - te:+.2f}")
print(f"Records with discrepancies: {issues}")
