from collections import defaultdict, deque

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

grid = [list(x) for x in open("input").read().splitlines()]
height = len(grid)
width = len(grid[0])

sx, sy = [(i, j) for i in range(height) for j in range(width) if grid[i][j] == "S"][0]
tx, ty = [(i, j) for i in range(height) for j in range(width) if grid[i][j] == "E"][0]

grid[sx][sy] = "a"
grid[tx][ty] = "z"

grid = [[ord(c) - ord("a") for c in r] for r in grid]

distances = defaultdict(lambda: 1000000)
queue = deque([(sx, sy)])

for x, y in queue:
    distances[x, y] = 0

answer = 100000
while len(queue) > 0:
    cx, cy = queue.popleft()
    if (cx, cy) == (tx, ty):
        answer = distances[tx, ty]
        print(answer)
        break
    for dx, dy in DIRECTIONS:
        nx, ny = cx + dx, cy + dy
        if nx in range(height) and ny in range(width):
            if grid[cx][cy] >= grid[nx][ny] - 1:
                ndst = distances[cx, cy] + 1
                if ndst < distances[nx, ny]:
                    queue.append((nx, ny))
                    distances[nx, ny] = ndst
