f = open('input.txt')
# f = open('input_test.txt')

GRID = []


def print_grid(grid):
    for l in grid:
        print("".join([str(x) for x in l]))
    print()


def beam_pass(x, y, d):
    i, j = {"r": (0, 1), "l": (0, -1), "d": (1, 0), "u": (-1, 0)}[d]
    nx = x + i
    ny = y + j
    if nx < 0 or nx >= len(GRID) or ny < 0 or ny >= len(GRID[0]):
        return

    v = GRID[nx][ny]

    nds = set()
    if v == ".":
        nds.add(d)
    if v == "|":
        if d in {"l", "r"}:
            nds.add("u")
            nds.add("d")
        else:
            nds.add(d)
    if v == "-":
        if d in {"u", "d"}:
            nds.add("l")
            nds.add("r")
        else:
            nds.add(d)
    if v == "/":
        if d == "d":
            nds.add("l")
        elif d == "u":
            nds.add("r")
        elif d == "r":
            nds.add("u")
        elif d == "l":
            nds.add("d")
    if v == "\\":
        if d == "d":
            nds.add("r")
        elif d == "u":
            nds.add("l")
        elif d == "r":
            nds.add("d")
        elif d == "l":
            nds.add("u")
    for nd in nds:
        yield nx, ny, nd


def process_start(m, n, start):
    print(start)
    todo = [start]
    energy = []
    for i in range(n):
        energy.append([])
        for r in range(m):
            energy[-1].append(set())

    for x, y, d in todo:
        for nx, ny, nd in beam_pass(x, y, d):
            if nd not in energy[nx][ny]:
                energy[nx][ny].add(nd)
                todo.append((nx, ny, nd))

    return sum(1 if r else 0 for row in energy for r in row)


def process():
    n = len(GRID)
    m = len(GRID[0])
    maxs = 0

    for i in range(n):
        start = (i, -1, "r")
        s = process_start(m, n, start)
        if s > maxs:
            maxs = s

    for i in range(n):
        start = (i, m, "l")
        s = process_start(m, n, start)
        if s > maxs:
            maxs = s

    for j in range(m):
        start = (-1, j, "d")
        s = process_start(m, n, start)
        if s > maxs:
            maxs = s

    for j in range(m):
        start = (n, j, "u")
        s = process_start(m, n, start)
        if s > maxs:
            maxs = s

    return maxs


for line in f.readlines():
    if not line.strip():
        continue
    row = list(line.strip())
    GRID.append(row)

s = process()

print(s)
