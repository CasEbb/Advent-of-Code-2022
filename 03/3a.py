import string

with open("input", "r") as file:
    sum = 0
    for line in file:
        midpoint = len(line) // 2
        first_half, second_half = line[:midpoint], line[midpoint:].strip()
        sum += (
            int(
                string.ascii_letters.index(
                    "".join(set(first_half).intersection(second_half))
                )
            )
            + 1
        )
    print(sum)
