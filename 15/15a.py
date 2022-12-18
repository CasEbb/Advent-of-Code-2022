def possible(x, y):
    for sx, sy, d in sensors:
        if abs(x - sx) + abs(y - sy) <= d and (x, y) not in beacons:
            return False
    return True


data = open("input").read().strip()
sensors, beacons = set(), set()
for line in data.split("\n"):
    parts = line.split()
    sx, sy = int(parts[2][2:-1]), int(parts[3][2:-1])
    bx, by = int(parts[8][2:-1]), int(parts[9][2:])
    d = abs(sx - bx) + abs(sy - by)
    sensors.add((sx, sy, d))
    beacons.add((bx, by))

ct = 0
y = 2_000_000
for x in range(
    min(x - d for x, _, d in sensors), max(x + d for x, _, d in sensors)
):
    if not possible(x, y) and (x, y) not in beacons:
        ct += 1
print(ct)
