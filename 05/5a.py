import re

INSTRUCTION_REGEX = re.compile(r"move (\d+) from (\d) to (\d)")

# Initial stacks from puzzle input
stacks = [
    list("RPCDBG"),
    list("HVG"),
    list("NSQDJPM"),
    list("PSLGDCNM"),
    list("JBNCPFLS"),
    list("QBDZVGTS"),
    list("BZMHFTQ"),
    list("CMDBF"),
    list("FCQG"),
]

# Read puzzle input
lines = open("input").read().splitlines()

# Skip first 10 lines
lines = lines[10:]

# Loop through instructions
for line in lines:
    num, src, dest = map(int, INSTRUCTION_REGEX.match(line).groups())
    for _ in range(num):
        stacks[dest - 1].append(stacks[src - 1].pop())

# Print top of each stack
for stack in stacks:
    print(stack[len(stack) - 1], end="")

# Print newline
print()
