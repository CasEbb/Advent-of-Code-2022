import re

lines = open("input").read().splitlines()
pattern = re.compile(
    r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs "
    r"(\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each "
    r"geode robot costs (\d+) ore and (\d+) obsidian."
)

blueprints = [list(map(int, pattern.match(line).groups())) for line in lines]


def heuristic(state):
    _, (_, _, mined) = state
    return 1000 * mined[3] + 100 * mined[2] + 10 * mined[1] + mined[0]


def search(costs, robots, t_max, top_queue=30000):
    queue = [(0, (robots, (0, 0, 0, 0), (0, 0, 0, 0)))]
    max_geodes_mined = 0
    depth = 0

    while queue:
        t, (robots, old_inventory, mined) = queue.pop(0)

        if t > depth:
            queue.sort(key=heuristic, reverse=True)
            queue = queue[:top_queue]
            depth = t

        if t == t_max:
            max_geodes_mined = max(max_geodes_mined, mined[3])
            continue

        new_inventory = tuple([old_inventory[i] + robots[i] for i in range(4)])
        new_mined = tuple([mined[i] + robots[i] for i in range(4)])

        queue.append((t + 1, (robots, new_inventory, new_mined)))

        for i in range(4):
            cost_robot = costs[i]

            if all([old_inventory[j] >= cost_robot[j] for j in range(4)]):
                new_robots = list(robots)
                new_robots[i] += 1
                new_robots = tuple(new_robots)

                new_inventory_state = tuple(
                    [new_inventory[j] - cost_robot[j] for j in range(4)]
                )
                queue.append((t + 1, (new_robots, new_inventory_state, new_mined)))

    return max_geodes_mined


# Part 1
total = 0
for (
    index,
    cost_ore_robot,
    cost_clay_robot,
    ob_ore,
    obs_clay,
    geode_ore,
    geode_ob,
) in blueprints:
    mined = search(
        [
            (cost_ore_robot, 0, 0, 0),
            (cost_clay_robot, 0, 0, 0),
            (ob_ore, obs_clay, 0, 0),
            (geode_ore, 0, geode_ob, 0),
        ],
        (1, 0, 0, 0),
        24,
        top_queue=1000,
    )
    total += index * mined
print(total)

# Part 2
total = 1
for (
    _,
    cost_ore_robot,
    cost_clay_robot,
    ob_ore,
    obs_clay,
    geode_ore,
    geode_ob,
) in blueprints[:3]:
    num_mined = search(
        [
            (cost_ore_robot, 0, 0, 0),
            (cost_clay_robot, 0, 0, 0),
            (ob_ore, obs_clay, 0, 0),
            (geode_ore, 0, geode_ob, 0),
        ],
        (1, 0, 0, 0),
        32,
        top_queue=10000,
    )
    total *= num_mined
print(total)
