# Case Study 91: Advanced String-Based Registration Record Analyzer
# Format: YY + BRANCH(3 capital letters) + 3 digits   ->  e.g. 23CSE045  (8 characters)

BRANCHES = ["CSE", "ECE", "EEE", "MEC", "CIV"]
MIN_YEAR = 20
MAX_YEAR = 26

records = ["23CSE001", "23CSE002", "23CSE001", "2ECE045", "24XYZ010",
           "24ece012", "25MEC12A", "23CIV0045", "", "24EEE099", "A4CSE010"]

error_names = ["Empty record", "Wrong length", "Invalid year", "Year out of range",
               "Invalid branch", "Branch not in capital letters", "Invalid serial number",
               "Duplicate record"]
error_counts = [0] * len(error_names)

seen = []
valid_count = 0
print(f"{'Record':<12}{'Status':<10}Details")
for rec in records:
    errors = []
    year = branch = serial = ""
    if len(rec) == 0:
        errors.append(0)
    elif len(rec) != 8:
        errors.append(1)
    else:
        year = rec[0:2]
        branch = rec[2:5]
        serial = rec[5:8]
        if not year.isdigit():
            errors.append(2)
        else:
            if int(year) < MIN_YEAR or int(year) > MAX_YEAR:
                errors.append(3)
        if not branch.isalpha():
            errors.append(4)
        elif branch != branch.upper():
            errors.append(5)
        else:
            if branch not in BRANCHES:
                errors.append(4)
        if not serial.isdigit():
            errors.append(6)

    if len(errors) == 0:
        if rec in seen:
            errors.append(7)
        else:
            seen.append(rec)

    if len(errors) == 0:
        valid_count = valid_count + 1
        print(f"{rec:<12}{'VALID':<10}year=20{year}, branch={branch}, serial={serial}")
    else:
        text = ""
        for e in errors:
            error_counts[e] = error_counts[e] + 1
            text = text + error_names[e] + "; "
        shown = rec if rec != "" else "(blank)"
        print(f"{shown:<12}{'INVALID':<10}{text}")

print("\n=== Error Classification Summary ===")
for i in range(len(error_names)):
    if error_counts[i] > 0:
        print(f"{error_names[i]:<32}: {error_counts[i]}")
print(f"\nTotal: {len(records)}   Valid: {valid_count}   Invalid: {len(records) - valid_count}")
