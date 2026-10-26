# Case Study 97: Smart Campus Incident and Maintenance Prioritization
# Report tuple: (id, description, location, severity 1-5, times reported)

loc_names = ["Hostel", "Lab", "Library", "Canteen", "Ground"]
loc_weight = [4, 4, 3, 3, 1]

reports = [
    ("M01", "Water pipe burst",      "Hostel",  5, 6),
    ("M02", "Projector not working", "Lab",     2, 3),
    ("M03", "Broken bench",          "Ground",  1, 1),
    ("M04", "Short circuit sparks",  "Lab",     5, 2),
    ("M05", "Fan noise",             "Library", 1, 8),
    ("M06", "Gas leak smell",        "Canteen", 5, 4),
    ("M07", "Lift stuck",            "Block Z", 4, 2),     # unknown location
]

scored = []      # [score, id, description, location, class]
for r in reports:
    rid, desc, loc, sev, freq = r
    w = -1
    for i in range(len(loc_names)):
        if loc_names[i] == loc:
            w = loc_weight[i]
    if w == -1:
        w = 2           # default weight for unknown location
    f = freq
    if f > 5:
        f = 5           # frequency contribution capped at 5
    score = sev * 10 + w * 5 + f * 2
    if score >= 70:
        cls = "CRITICAL"
    elif score >= 50:
        cls = "HIGH"
    elif score >= 30:
        cls = "MEDIUM"
    else:
        cls = "LOW"
    scored.append([score, rid, desc, loc, cls])

n = len(scored)
for i in range(n - 1):
    for j in range(n - 1 - i):
        a = scored[j]
        b = scored[j + 1]
        if (-a[0], a[1]) > (-b[0], b[1]):
            scored[j] = b
            scored[j + 1] = a

print(f"{'Rank':<5}{'ID':<5}{'Description':<24}{'Location':<9}{'Score':>6}  Class")
rank = 1
class_names = ["CRITICAL", "HIGH", "MEDIUM", "LOW"]
class_count = [0, 0, 0, 0]
for score, rid, desc, loc, cls in scored:
    print(f"{rank:<5}{rid:<5}{desc:<24}{loc:<9}{score:>6}  {cls}")
    class_count[class_names.index(cls)] += 1
    rank += 1

print("\n=== Priority Summary ===")
for i in range(4):
    print(f"{class_names[i]:<9}: {class_count[i]}")
print("Attend first:", scored[0][1], "-", scored[0][2], "at", scored[0][3])
