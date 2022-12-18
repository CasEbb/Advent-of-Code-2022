time = 0
cave = set()
abyss = 0

for line in open("input"):
    x = [list(map(int, p.split(","))) for p in line.strip().split(" -> ")]
    for (x1, y1), (x2, y2) in zip(x, x[1:]):
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                cave.add(x + y * 1j)
                abyss = max(abyss, y + 1)

while 500 not in cave:
    s = 500
    while True:
        if s.imag >= abyss:
            break
        if s + 1j not in cave:
            s += 1j
            continue
        if s + 1j - 1 not in cave:
            s += 1j - 1
            continue
        if s + 1j + 1 not in cave:
            s += 1j + 1
            continue
        break
    cave.add(s)
    time += 1

print(time)
