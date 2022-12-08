# Read the map from the input
grid = [[int(cell) for cell in line] for line in open("input").read().splitlines()]


def score(base, trees):
    distance = 1
    for tree in trees:
        if tree >= base:
            break
        distance += 1
    return distance


# Calculate the viewing distance along each row and column
max_scenic_score = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        cell = grid[y][x]
        lines_of_sight = [
            grid[y][x + 1 :],
            grid[y][:x][::-1],
            [elem[x] for elem in grid[y + 1 :]],
            [elem[x] for elem in grid[:y]][::-1],
        ]
        visible = [
            [1 if tree >= cell else 0 for tree in direction]
            for direction in lines_of_sight
        ]
        scores = [(z.index(1) + 1) if 1 in z else len(z) for _, z in enumerate(visible)]

        score = 1
        for s in scores:
            score *= s

        max_scenic_score = max(score, max_scenic_score)

# Print the best scenic score
print(max_scenic_score)
