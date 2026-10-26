# Case Study 96: Multi-Criteria Library Resource Distribution
books = ["Python", "DSA", "DBMS", "Networks"]
copies = [30, 20, 10, 12]
total_copies = copies[:]

# Branch: [name, priority (1 = highest), [demand per book]]
branches = [
    ["CSE", 1, [25, 18, 8, 6]],
    ["ECE", 2, [15, 10, 6, 10]],
    ["EEE", 3, [12, 8, 5, 4]],
    ["MECH", 4, [8, 6, 4, 3]],
]

n = len(branches)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if branches[j][1] > branches[j + 1][1]:
            t = branches[j]
            branches[j] = branches[j + 1]
            branches[j + 1] = t

alloc = []
unmet_total = [0] * len(books)
print(f"{'Branch':<8}" + "".join([f"{b:>10}" for b in books]))
for br in branches:
    name, prio, demand = br
    row = []
    for k in range(len(books)):
        give = demand[k]
        if give > copies[k]:
            give = copies[k]
        copies[k] -= give
        unmet_total[k] += demand[k] - give
        row.append(give)
    alloc.append(row)
    print(f"{name:<8}" + "".join([f"{str(row[k]) + '/' + str(demand[k]):>10}" for k in range(len(books))]))
print("(allocated / demanded)\n")

print(f"{'Book':<10}{'Copies':>7}{'Left':>6}{'Unmet demand':>14}")
for k in range(len(books)):
    flag = "  <-- shortage" if unmet_total[k] > 0 else ""
    print(f"{books[k]:<10}{total_copies[k]:>7}{copies[k]:>6}{unmet_total[k]:>14}{flag}")
