input = open("input").read().splitlines()

# Setup
operations = [(input[x][23:]) for x in range(2, len(input), 7)]
tests = [int(input[x][21:]) for x in range(3, len(input), 7)]
conditions = [
    [int(input[x][29:]), int(input[x + 1][30:])] for x in range(4, len(input), 7)
]

modulo = 1
for i in tests:
    modulo *= i

# Loop
def loop(part1=True):
    inspections = [0 for _ in range(len(tests))]
    inventory = [
        [[int(x) for x in (input[y][18:]).split(", ")] for y in range(1, len(input), 7)]
    ][0]
    for _ in range(0, (20 if part1 else 10000)):
        for i in range(0, len(inspections)):
            for j in range(0, len(inventory[i])):
                current = inventory[i][j]
                if operations[i] == "* old":
                    current *= current
                elif operations[i][:2] == "* ":
                    current *= int(operations[i][2:])
                elif operations[i][:2] == "+ ":
                    current += int(operations[i][2:])
                current = current // 3 if part1 else current % modulo
                if current % tests[i] == 0:
                    inventory[conditions[i][0]].append(current)
                else:
                    inventory[conditions[i][1]].append(current)
                inspections[i] += 1
            inventory[i] = []
    return sorted(inspections)[-1] * sorted(inspections)[-2]


print(loop(True))
print(loop(False))
