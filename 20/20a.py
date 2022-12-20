file = [int(x) for x in open("input")]
positions = list(range(len(file)))

for i in range(len(file)):
    j = positions.index(i)
    positions.pop(j)
    positions.insert((j + file[i]) % len(positions), i)

zero = positions.index(file.index(0))
print(sum(file[positions[(zero + p) % len(file)]] for p in [1000, 2000, 3000]))
