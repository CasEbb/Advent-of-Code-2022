import string

with open("input", "r") as file:
    sum = 0
    lines = file.readlines()
    for i in range(0, len(lines), 3):
        sum += (
            int(
                string.ascii_letters.index(
                    "".join(
                        set(lines[i].strip())
                        .intersection(lines[i + 1].strip())
                        .intersection(lines[i + 2].strip())
                    )
                )
            )
            + 1
        )
    print(sum)
