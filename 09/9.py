rope = [0] * 10
visited = [set([x]) for x in rope]
moves = {"L": +1, "R": -1, "D": 1j, "U": -1j}
move = lambda x: complex((x.real > 0) - (x.real < 0), (x.imag > 0) - (x.imag < 0))
lines = [line.split() for line in open("input").read().splitlines()]

for line in lines:
    d, n = line

    for _ in range(int(n)):
        rope[0] += moves[d]

        for i in range(1, 10):
            dist = rope[i - 1] - rope[i]
            if abs(dist) >= 2:
                rope[i] += move(dist)
                visited[i].add(rope[i])

print(len(visited[1]), len(visited[9]))
