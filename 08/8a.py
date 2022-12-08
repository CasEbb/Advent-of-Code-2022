# Read the map from the input
grid = [[int(cell) for cell in line] for line in open("input").read().splitlines()]

# Count the number of visible trees along each row and column
count = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        cell = grid[y][x]
        row = grid[y]
        col = [grid[i][x] for i in range(len(grid))]

        # Check left of tree
        if cell > max(row[0:x], default=-1):
            count += 1
            continue
        # Check right of tree
        if cell > max(row[x + 1 :], default=-1):
            count += 1
            continue
        # Check up
        if cell > max(col[0:y], default=-1):
            count += 1
            continue
        # Check down
        if cell > max(col[y + 1 :], default=-1):
            count += 1
            continue

# Print the total number of visible trees
print(count)
