# Case Study 98: University Academic Progression Audit
subjects = ["Maths", "Physics", "Python", "English", "Chemistry"]
PASS_MARK = 40
MIN_ATTENDANCE = 75
MAX_BACKLOGS = 1                        # conditional promotion allowed up to this
REQUIRED = ["MAT101", "PHY101", "CSE101"]

# Student: (id, name, [marks], attendance %, [completed prerequisite codes])
students = [
    ("S01", "Arun",   [78, 65, 80, 70, 66], 88, ["MAT101", "PHY101", "CSE101"]),
    ("S02", "Bhanu",  [55, 38, 62, 70, 58], 80, ["MAT101", "PHY101", "CSE101"]),
    ("S03", "Chitra", [35, 30, 62, 70, 58], 90, ["MAT101", "PHY101", "CSE101"]),
    ("S04", "Dev",    [70, 72, 68, 60, 65], 70, ["MAT101", "PHY101", "CSE101"]),
    ("S05", "Esha",   [82, 75, 90, 88, 79], 95, ["MAT101", "CSE101"]),
]

promoted = conditional = detained = 0
for sid, name, marks, att, done in students:
    outstanding = []
    backlogs = []
    for i in range(len(subjects)):
        if marks[i] < PASS_MARK:
            backlogs.append(subjects[i] + "(" + str(marks[i]) + ")")
    if att < MIN_ATTENDANCE:
        outstanding.append("attendance " + str(att) + "% < " + str(MIN_ATTENDANCE) + "%")
    for code in REQUIRED:
        if code not in done:
            outstanding.append("prerequisite " + code + " pending")
    blocking = len(outstanding) > 0

    if len(backlogs) == 0 and not blocking:
        decision = "PROMOTED"
        promoted += 1
    elif len(backlogs) <= MAX_BACKLOGS and not blocking:
        decision = "CONDITIONALLY PROMOTED"
        conditional += 1
    else:
        decision = "DETAINED"
        detained += 1

    print(f"{sid} {name:<7} Total={sum(marks):<4} Att={att}%  -> {decision}")
    if len(backlogs) > 0:
        print("      Backlogs:", ", ".join(backlogs))
    for o in outstanding:
        print("      Outstanding:", o)

print(f"\nPromoted: {promoted}   Conditional: {conditional}   Detained: {detained}")
