f = open('input.txt')
# f = open('input_test.txt')

ENERGY = []
GRID = []
TODO = [(0, -1, "r")]


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
        if nd not in ENERGY[nx][ny]:
            ENERGY[nx][ny].add(nd)
            TODO.append((nx, ny, nd))


def process_grid():
    for x, y, d in TODO:
        beam_pass(x, y, d)
    return sum(1 if r else 0 for row in ENERGY for r in row)


for line in f.readlines():
    if not line.strip():
        continue
    row = list(line.strip())
    ENERGY.append([])
    for r in row:
        ENERGY[-1].append(set())
    GRID.append(row)

print_grid(GRID)
s = process_grid()

print(s)
