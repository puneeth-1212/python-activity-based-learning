# Case Study 92: Multi-Event Sports Scheduling and Scoring
# Event tuple: (id, venue, start, end, team1, team2, score1, score2)

events = [
    ("E1", "Ground A", "09:00", "10:30", "Tigers", "Lions",   2, 1),
    ("E2", "Ground A", "10:00", "11:30", "Eagles", "Wolves",  0, 0),
    ("E3", "Ground B", "10:00", "11:00", "Tigers", "Wolves",  3, 3),
    ("E4", "Ground B", "11:30", "12:30", "Lions",  "Eagles",  1, 2),
    ("E5", "Ground A", "12:00", "13:00", "Wolves", "Lions",   0, 2),
]
WIN, DRAW = 3, 1

# ---- time conversion HH:MM -> minutes ----
mins = []
for ev in events:
    eid, venue, st, en, t1, t2, s1, s2 = ev
    start = int(st[0:2]) * 60 + int(st[3:5])
    end = int(en[0:2]) * 60 + int(en[3:5])
    mins.append((start, end))

# ---- conflict detection ----
print("=== Scheduling Conflicts ===")
conflicts = 0
for i in range(len(events)):
    for j in range(i + 1, len(events)):
        a = events[i]
        b = events[j]
        overlap = mins[i][0] < mins[j][1] and mins[j][0] < mins[i][1]
        if overlap:
            if a[1] == b[1]:
                print(f"{a[0]} & {b[0]}: venue clash at {a[1]}")
                conflicts = conflicts + 1
            shared = []
            for t in (a[4], a[5]):
                if t == b[4] or t == b[5]:
                    shared.append(t)
            for t in shared:
                print(f"{a[0]} & {b[0]}: team {t} scheduled in overlapping matches")
                conflicts = conflicts + 1
if conflicts == 0:
    print("No conflicts")

# ---- scoring ----
table = []     # [team, played, points, goals for, goals against]
for ev in events:
    for t in (ev[4], ev[5]):
        found = False
        for row in table:
            if row[0] == t:
                found = True
        if not found:
            table.append([t, 0, 0, 0, 0])

for ev in events:
    eid, venue, st, en, t1, t2, s1, s2 = ev
    for row in table:
        if row[0] == t1:
            row[1] += 1; row[3] += s1; row[4] += s2
            if s1 > s2:
                row[2] += WIN
            elif s1 == s2:
                row[2] += DRAW
        if row[0] == t2:
            row[1] += 1; row[3] += s2; row[4] += s1
            if s2 > s1:
                row[2] += WIN
            elif s1 == s2:
                row[2] += DRAW

# rank: points, goal difference, goals for, name
n = len(table)
for i in range(n - 1):
    for j in range(n - 1 - i):
        a = table[j]
        b = table[j + 1]
        ka = (-a[2], -(a[3] - a[4]), -a[3], a[0])
        kb = (-b[2], -(b[3] - b[4]), -b[3], b[0])
        if ka > kb:
            table[j] = b
            table[j + 1] = a

print("\n=== Final Rankings ===")
print(f"{'Pos':<4}{'Team':<8}{'P':>3}{'Pts':>5}{'GF':>4}{'GA':>4}{'GD':>4}")
pos = 1
for team, p, pts, gf, ga in table:
    print(f"{pos:<4}{team:<8}{p:>3}{pts:>5}{gf:>4}{ga:>4}{gf - ga:>4}")
    pos += 1
