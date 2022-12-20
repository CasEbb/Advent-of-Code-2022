file = [int(x) * 811589153 for x in open("input")]
positions = list(range(len(file)))

for i in list(range(len(file))) * 10:
    j = positions.index(i)
    positions.pop(j)
    positions.insert((j + file[i]) % len(positions), i)

zero = positions.index(file.index(0))
print(sum(file[positions[(zero + x) % len(file)]] for x in [1000, 2000, 3000]))
