OPERATIONS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}
data = [row.split(": ") for row in open("input").read().splitlines()]
known = {}

for var, op in data:
    if len(op.split(" ")) == 1:
        known[var] = int(op)

while "root" not in known:
    for var, op in data:
        if var in known:
            continue
        a, task, b = op.split(" ")
        if (a in known) and (b in known):
            v = OPERATIONS[task](known[a], known[b])
            known[var] = v

print(int(known["root"]))
