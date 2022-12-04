# Read input
with open("input", "r") as file:
    assignments = [line.strip() for line in file]

# Split the assignments into ranges
ranges = []
for assignment in assignments:
    ranges.append(
        list(list(map(int, range.split("-"))) for range in assignment.split(","))
    )

# Initialize a counter to keep track of the number of pairs where one range fully contains the other
num_contains = 0

# Iterate over the pairs of ranges
for range1, range2 in ranges:
    range1 = set(range(range1[0], range1[1] + 1))
    range2 = set(range(range2[0], range2[1] + 1))
    if len(range1.intersection(range2)):
        num_contains += 1

# Print the result
print(num_contains)
