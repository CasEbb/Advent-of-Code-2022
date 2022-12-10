input = open("input").read().splitlines()

register = 1
cycle = 0
total = 0
sprite = "###....................................."

for instruction in input:
    op = instruction.split()

    if op[0] == "noop":
        cycles = 1
    elif op[0] == "addx":
        cycles = 2

    for i in range(cycles):
        cycle += 1
        if cycle == 20 or (cycle + 20) % 40 == 0:
            total += cycle * register
        print(sprite[(cycle - 1) % 40], end="")
        if cycle % 40 == 0:
            print()

    if op[0] == "addx":
        register += int(op[1])
        sprite = ["."] * 40
        try:
            sprite[register] = "#"
            sprite[register - 1] = "#"
            sprite[register + 1] = "#"
        except:
            pass
        sprite = "".join(sprite)

print(total)
