f = open('input.txt')
# f = open('input_test.txt')

directions = [
    ("Left", (0, -1), {"S", "-", "7", "J"}, {"-", "L", "F"}),
    ("Right", (0, 1), {"S", "-", "F", "L"}, {"-", "J", "7"}),
    ("Up", (-1, 0), {"S", "|", "J", "L"}, {"|", "7", "F"}),
    ("Down", (1, 0), {"S", "|", "F", "7"}, {"|", "L", "J"}),
]

STEPS = []
GRID = []


def print_grid():
    for l in STEPS:
        print("".join([str(x) for x in l]))
    print()


def search(x, y, step):
    STEPS[x][y] = step
    for d, (i, j), self_pipes, other_pipes in directions:
        if GRID[x][y] not in self_pipes:
            continue
        if 0 <= x + i < len(GRID) and 0 <= y + j < len(GRID[0]):
            g = GRID[x + i][y + j]
            if g in other_pipes:
                if STEPS[x + i][y + j] == ".":
                    yield x + i, y + j, step + 1


for i, line in enumerate(f.readlines()):
    if not line.strip():
        continue
    if "S" in line:
        y = line.index("S")
        x = i
    GRID.append(list(line.strip()))
    STEPS.append(["."] * len(line.strip()))

TODO = [(x, y, 0)]

while TODO:
    N = []
    for x, y, s in TODO:
        for n in search(x, y, s):
            N.append(n)
    TODO = N

# print_grid()


m = 0
for steps in STEPS:
    for s in steps:
        if s == ".":
            continue
        if s > m:
            m = s
print(m)
print(STEPS)