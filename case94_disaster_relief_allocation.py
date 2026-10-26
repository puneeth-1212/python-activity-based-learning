# Case Study 94: Disaster Relief Supply Allocation
# Policy: areas are served by urgency (3 = most urgent), then by name.
#         No single area may receive more than 50% of the initial stock of an item.

items = ["Food packs", "Water (L)", "Medical kits", "Blankets"]
stock = [500, 1000, 80, 200]
initial = stock[:]

# Area: [name, urgency, [need per item]]
areas = [
    ["Riverside", 3, [300, 600, 50, 100]],
    ["Hilltop",   2, [200, 400, 30, 80]],
    ["Old Town",  3, [250, 500, 40, 90]],
    ["Market",    1, [100, 300, 10, 50]],
]

n = len(areas)
for i in range(n - 1):
    for j in range(n - 1 - i):
        a = areas[j]
        b = areas[j + 1]
        if (-a[1], a[0]) > (-b[1], b[0]):
            areas[j] = b
            areas[j + 1] = a

total_unmet = [0] * len(items)
print("Service order:", ", ".join([a[0] + "(U" + str(a[1]) + ")" for a in areas]))
for area in areas:
    name, urgency, needs = area
    print(f"\n{name} (urgency {urgency})")
    print(f"  {'Item':<14}{'Need':>6}{'Given':>7}{'Unmet':>7}")
    for k in range(len(items)):
        cap = initial[k] // 2
        give = needs[k]
        if give > cap:
            give = cap
        if give > stock[k]:
            give = stock[k]
        stock[k] -= give
        unmet = needs[k] - give
        total_unmet[k] += unmet
        print(f"  {items[k]:<14}{needs[k]:>6}{give:>7}{unmet:>7}")

print("\n=== Summary ===")
print(f"{'Item':<14}{'Initial':>8}{'Remaining':>10}{'Total unmet':>13}")
for k in range(len(items)):
    print(f"{items[k]:<14}{initial[k]:>8}{stock[k]:>10}{total_unmet[k]:>13}")
