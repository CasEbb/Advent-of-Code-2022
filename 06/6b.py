stream = open("input").read()

for i in range(len(stream)):
    marker = stream[i : i + 14]

    x = list(set(marker))
    y = list(marker)
    x.sort()
    y.sort()
    if x == y:
        print(i + 14)
        break
