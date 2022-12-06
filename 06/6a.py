stream = open("input").read()

for i in range(len(stream)):
    marker = stream[i : i + 4]
    if len(set(marker)) == 4:
        print(i + 4)
        break
