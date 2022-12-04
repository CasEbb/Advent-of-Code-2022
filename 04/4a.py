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
    # Check if range1 is fully contained within range2
    if range1[0] >= range2[0] and range1[1] <= range2[1]:
        num_contains += 1
    # Check if range2 is fully contained within range1
    elif range2[0] >= range1[0] and range2[1] <= range1[1]:
        num_contains += 1

# Print the result
print(num_contains)
