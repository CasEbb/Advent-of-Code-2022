def adj_cubes(cube):
    a, b, c = cube
    yield a + 1, b, c
    yield a - 1, b, c
    yield a, b + 1, c
    yield a, b - 1, c
    yield a, b, c + 1
    yield a, b, c - 1


lines = open("input").read().splitlines()
cubes = [tuple(map(int, line.split(","))) for line in lines]
scanned_cubes = set()
part1 = 0

for cube in cubes:
    part1 += 6
    for adj in adj_cubes(cube):
        if adj in scanned_cubes:
            part1 -= 2
    scanned_cubes.add(cube)

print(part1)

part2 = part1
xs, ys, zs = zip(*cubes)
all_cubes = {
    (x, y, z)
    for x in range(min(xs) - 1, max(xs) + 2)
    for y in range(min(ys) - 1, max(ys) + 2)
    for z in range(min(zs) - 1, max(zs) + 2)
}
empty_cubes = all_cubes - scanned_cubes
q = [(min(xs) - 1, min(ys) - 1, min(zs) - 1)]

while q:
    c = q.pop()
    if c in empty_cubes:
        empty_cubes.remove(c)
        q.extend(adj_cubes(c))

for cube in empty_cubes:
    part2 += 6
    for adj in adj_cubes(cube):
        if adj in scanned_cubes:
            part2 -= 2
    scanned_cubes.add(cube)

print(part2)
