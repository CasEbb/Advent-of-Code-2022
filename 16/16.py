import collections
import functools
import itertools
import re

pattern = r"Valve (\w+) .*=(\d*); .* valves? (.*)"

valves, flow_rates, paths = set(), dict(), collections.defaultdict(lambda: 1000)

for v, f, us in re.findall(pattern, open("input").read()):
    valves.add(v)
    if f != "0":
        flow_rates[v] = int(f)
    for u in us.split(", "):
        paths[u, v] = 1

for k, i, j in itertools.product(valves, valves, valves):
    paths[i, j] = min(paths[i, j], paths[i, k] + paths[k, j])


@functools.cache
def search(time, u="AA", vs=frozenset(flow_rates), part2=False):
    return max(
        [
            flow_rates[v] * (time - paths[u, v] - 1)
            + search(time - paths[u, v] - 1, v, vs - {v}, part2)
            for v in vs
            if paths[u, v] < time
        ]
        + [search(26, vs=vs) if part2 else 0]
    )


print(search(30))
print(search(26, part2=True))
