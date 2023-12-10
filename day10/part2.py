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


def print_grid(grid):
    for l in grid:
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

TODO = []
print_grid(GRID)
for x in range(len(STEPS)):
    for y in range(len(STEPS[x])):
        s = STEPS[x][y]
        if s != ".":
            continue
        if x == 0 or y == 0 or x == len(GRID) - 1 or y == len(GRID[0]) - 1:
            GRID[x][y] = "O"
        else:
            GRID[x][y] = "."

print_grid(GRID)



EXPANDED = []
for x in range(len(GRID)):
    row = []
    for y in range(len(GRID[x])):
        row.append(GRID[x][y])
        if y < len(GRID[x])-1:
            row.append(" ")
    EXPANDED.append(row)
    if x < len(GRID)-1:
        EXPANDED.append([" "] * len(row))
print_grid(EXPANDED)

for x in range(len(EXPANDED)):
    for y in range(len(EXPANDED[x])):
        if EXPANDED[x][y] == "O":
            TODO.append((x, y))
        if EXPANDED[x][y] != " ":
            continue
        try:
            left = EXPANDED[x][y - 1]
            right = EXPANDED[x][y + 1]
            if left in {"S", "-", "F", "L"} and right in {"S", "-", "J", "7"}:
                EXPANDED[x][y] = "-"
        except:
            continue
        try:
            up = EXPANDED[x - 1][y]
            down = EXPANDED[x + 1][y]
            if up in {"S", "|", "F", "7"} and down in {"S", "|", "J", "L"}:
                EXPANDED[x][y] = "|"
        except:
            continue

print_grid(EXPANDED)

print("TODO", TODO)
while TODO:
    N = []
    for x, y in TODO:
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                if 0 <= x + i < len(EXPANDED) and 0 <= y + j < len(EXPANDED[0]):
                    if EXPANDED[x + i][y + j] in {".", " "}:
                        N.append((x + i, y + j))
                        EXPANDED[x + i][y + j] = "O"
    TODO = N
print_grid(EXPANDED)

print("SUM:", sum([grid.count(".") for grid in EXPANDED]))