import json

input = open("input").read().splitlines()
pairs = [
    (json.loads(input[i]), json.loads(input[i + 1])) for i in range(0, len(input), 3)
]


def compare(l1, l2):
    if isinstance(l1, int) and isinstance(l2, int):
        if l1 == l2:
            return None
        return l1 < l2

    if isinstance(l1, list) and isinstance(l2, list):
        for e1, e2 in zip(l1, l2):
            if (comparison := compare(e1, e2)) is not None:
                return comparison
        return compare(len(l1), len(l2))

    if isinstance(l1, int):
        return compare([l1], l2)
    return compare(l1, [l2])


print(sum(i for i, (left, right) in enumerate(pairs, 1) if compare(left, right)))

packets = [p for pair in pairs for p in pair]
position_1 = 1 + sum(1 for p in packets if compare(p, [[2]]))
position_2 = 2 + sum(1 for p in packets if compare(p, [[6]]))
print(position_1 * position_2)
