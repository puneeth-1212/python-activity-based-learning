# Case Study 100: Comprehensive Smart Campus Management Simulation (menu-driven)
subjects = ["Python", "Maths", "Physics"]
events = ["Hackathon", "Quiz", "Cultural Fest"]

# Student: [roll, name, classes attended, classes held, [marks]]
students = [
    ["101", "Anil",  36, 40, [80, 70, 90]],
    ["102", "Bhanu", 28, 40, [55, 38, 62]],
    ["103", "Chitra", 40, 40, [92, 88, 95]],
]
registrations = [("101", "Hackathon")]          # tuples (roll, event)
resources = [["Projector", 3, 0], ["Laptop", 10, 0], ["Seminar Hall", 1, 0]]   # name, total, allocated

while True:
    print("\n===== SMART CAMPUS MENU =====")
    print("1. Add student        2. View students     3. Update attendance")
    print("4. Enter marks        5. Register event    6. Allocate resource")
    print("7. Summary report     8. Exit")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        roll = input("Roll no: ").strip()
        name = input("Name: ").strip()
        dup = False
        for s in students:
            if s[0] == roll:
                dup = True
        if roll == "" or not roll.isdigit():
            print("Invalid roll number.")
        elif dup:
            print("Roll number already exists.")
        elif name == "" or not name.replace(" ", "").isalpha():
            print("Name must contain only letters.")
        else:
            students.append([roll, name.title(), 0, 0, [0, 0, 0]])
            print("Student added.")

    elif choice == "2":
        print(f"{'Roll':<6}{'Name':<10}{'Att%':>6}{'Avg':>7}")
        for roll, name, att, held, marks in students:
            pct = att * 100 / held if held > 0 else 0
            print(f"{roll:<6}{name:<10}{pct:>6.1f}{sum(marks) / len(marks):>7.1f}")

    elif choice == "3":
        roll = input("Roll no: ").strip()
        idx = -1
        for i in range(len(students)):
            if students[i][0] == roll:
                idx = i
        if idx == -1:
            print("Student not found.")
        else:
            held = input("Classes held: ").strip()
            att = input("Classes attended: ").strip()
            if held.isdigit() and att.isdigit() and int(att) <= int(held):
                students[idx][3] += int(held)
                students[idx][2] += int(att)
                print("Attendance updated.")
            else:
                print("Invalid numbers (attended cannot exceed held).")

    elif choice == "4":
        roll = input("Roll no: ").strip()
        idx = -1
        for i in range(len(students)):
            if students[i][0] == roll:
                idx = i
        if idx == -1:
            print("Student not found.")
        else:
            new_marks = []
            ok = True
            for sub in subjects:
                m = input(f"Marks in {sub} (0-100): ").strip()
                if m.isdigit() and 0 <= int(m) <= 100:
                    new_marks.append(int(m))
                else:
                    ok = False
            if ok:
                students[idx][4] = new_marks
                print("Marks saved.")
            else:
                print("Invalid marks; nothing saved.")

    elif choice == "5":
        roll = input("Roll no: ").strip()
        found = False
        for s in students:
            if s[0] == roll:
                found = True
        if not found:
            print("Student not found.")
        else:
            for i in range(len(events)):
                print(f"  {i + 1}. {events[i]}")
            e = input("Event number: ").strip()
            if e.isdigit() and 1 <= int(e) <= len(events):
                entry = (roll, events[int(e) - 1])
                if entry in registrations:
                    print("Already registered for this event.")
                else:
                    registrations.append(entry)
                    print("Registered for", entry[1])
            else:
                print("Invalid event number.")

    elif choice == "6":
        for i in range(len(resources)):
            name, total, used = resources[i]
            print(f"  {i + 1}. {name} (available {total - used})")
        r = input("Resource number: ").strip()
        q = input("Quantity: ").strip()
        if r.isdigit() and q.isdigit() and 1 <= int(r) <= len(resources) and int(q) > 0:
            res = resources[int(r) - 1]
            if int(q) <= res[1] - res[2]:
                res[2] += int(q)
                print(f"Allocated {q} x {res[0]}.")
            else:
                print("Request rejected: not enough available.")
        else:
            print("Invalid input.")

    elif choice == "7":
        print("\n--- STUDENT REPORT ---")
        print(f"{'Roll':<6}{'Name':<10}{'Att%':>6}{'Avg':>7}{'Events':>8}  Status")
        best = -1
        best_avg = -1
        for i in range(len(students)):
            roll, name, att, held, marks = students[i]
            pct = att * 100 / held if held > 0 else 0
            avg = sum(marks) / len(marks)
            count = 0
            for r, ev in registrations:
                if r == roll:
                    count += 1
            weak = False
            for m in marks:
                if m < 40:
                    weak = True
            if pct < 75 or weak:
                status = "AT RISK"
            else:
                status = "Good"
            if avg > best_avg:
                best_avg = avg
                best = i
            print(f"{roll:<6}{name:<10}{pct:>6.1f}{avg:>7.1f}{count:>8}  {status}")
        print(f"Top performer: {students[best][1]} ({best_avg:.1f})")
        print("\n--- EVENT REGISTRATIONS ---")
        for ev in events:
            c = 0
            for r, e in registrations:
                if e == ev:
                    c += 1
            print(f"  {ev:<14}{c}")
        print("\n--- RESOURCES ---")
        for name, total, used in resources:
            print(f"  {name:<14}allocated {used}/{total}")

    elif choice == "8":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Enter 1-8.")
