f = open('input.txt')
# f = open('input_test.txt')

lines = f.readlines()

seeds = [int(x) for x in lines[0].strip().split(":")[1].strip().split()]

maps = {}
ranges = []
name = None


def make_map(ranges):
    map = {}
    for target, source, length in ranges:
        for x, y in zip(range(source, source+length), range(target, target+length)):
            map[x] = y
    return map


for line in lines[1:]:
    if line.strip().endswith(":"):
        name_parts = line.strip().split(" ")[0].split("-")
        name = (name_parts[0], name_parts[2])
    elif line.strip():
        ranges.append([int(x) for x in line.strip().split()])
    elif name:
        maps[name[0]] = (name[1], ranges)
        ranges = []
maps[name[0]] = (name[1], ranges)


def map_value(x, m):
    for r in m:
        target, source, length = r
        if source <= x < source+length:
            return target + (x - source)
    return x


def proces_seed(x, s, maps):
    if s not in maps:
        return x
    n, m = maps[s]
    y = map_value(x, m)
    return proces_seed(y, n, maps)


min_loc = None
for x in range(int(len(seeds)/2)):
    seed_start = seeds[x * 2]
    seed_length = seeds[x * 2 + 1]
    print(seed_start)
    print(seed_length)
    for seed in range(seed_start, seed_start+ seed_length):
        location = proces_seed(seed, "seed", maps)
        if not min_loc or location < min_loc:
            min_loc = location

print()
print(min_loc)