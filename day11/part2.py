def make_map(empty, n):
    m = {}
    shift = 0
    for x in range(n):
        if empty and x == empty[0]:
            shift += (1000000 - 1)
            empty.pop(0)
            continue
        m[x] = x + shift
    return m


def distance(g1, g2, galaxies, rowmap, colmap):
    r1 = rowmap[galaxies[g1][0]]
    r2 = rowmap[galaxies[g2][0]]
    c1 = colmap[galaxies[g1][1]]
    c2 = colmap[galaxies[g2][1]]
    return abs(r1 - r2) + abs(c1 - c2)


f = open('input.txt')

galaxies = {}
id = 1
nrows = 0
for x, line in enumerate(f.readlines()):
    if not line.strip():
        continue
    nrows += 1
    ncols = 0
    for y, v in enumerate(line.strip()):
        ncols += 1
        if v == "#":
            galaxies[id] = (x, y)
            id += 1

empty_rows = sorted(list(set(range(nrows)) - {g[0] for g in galaxies.values()}))
empty_cols = sorted(list(set(range(ncols)) - {g[1] for g in galaxies.values()}))
rowmap = make_map(empty_rows, nrows)
colmap = make_map(empty_cols, ncols)

galaxy_keys = list(galaxies.keys())
print("SUM", sum(distance(g1, g2, galaxies, rowmap, colmap)
                 for i, g1 in enumerate(galaxy_keys)
                 for g2 in galaxy_keys[i + 1:]))
