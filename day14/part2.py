from collections import defaultdict

f = open('input.txt')
# f = open('input_test.txt')


def print_grid(grid):
    for l in grid:
        print("".join([str(x) for x in l]))
    print()


def move_n(grid):
    # print("MOVE N")
    n = len(grid)
    m = len(grid[0])
    for i in range(m):
        for j in range(1, n):
            if grid[j][i] == "O":
                for ja in range(j - 1, -1, -1):
                    if grid[ja][i] == ".":
                        grid[ja][i] = "O"
                        grid[ja + 1][i] = "."
                    else:
                        break
    return grid


def move_w(grid):
    # print("MOVE W")
    n = len(grid)
    m = len(grid[0])
    for j in range(n):
        for i in range(1, m):
            if grid[j][i] == "O":
                for ia in range(i - 1, -1, -1):
                    if grid[j][ia] == ".":
                        grid[j][ia] = "O"
                        grid[j][ia + 1] = "."
                    else:
                        break
    return grid


def move_s(grid):
    # print("MOVE S")
    n = len(grid)
    m = len(grid[0])
    for i in range(m):
        for j in range(n - 1, -1, -1):
            if grid[j][i] == "O":
                for ja in range(j + 1, n):
                    if grid[ja][i] == ".":
                        grid[ja][i] = "O"
                        grid[ja - 1][i] = "."
                    else:
                        break
    return grid


def move_e(grid):
    # print("MOVE E")
    n = len(grid)
    m = len(grid[0])
    for j in range(n):
        for i in range(m - 1, -1, -1):
            if grid[j][i] == "O":
                for ia in range(i + 1, m):
                    if grid[j][ia] == ".":
                        grid[j][ia] = "O"
                        grid[j][ia - 1] = "."
                    else:
                        break
    return grid


def score(grid):
    n = len(grid)
    s = 0
    for line in grid:
        c = sum(1 if x == "O" else 0 for x in line)
        s += n * c
        n -= 1
    return s


def cycle(grid):
    grid = move_n(grid)
    grid = move_w(grid)
    grid = move_s(grid)
    grid = move_e(grid)
    return grid


def equal_grid(g1, g2):
    for l1, l2 in zip(g1, g2):
        for x1, x2 in zip(l1, l2):
            if x1 != x2:
                return False
    return True


def process_grid(grid):
    scores = defaultdict(int)

    order = []
    for i in range(2000):
        grid = cycle(grid)
        if i > 1000:
            s = score(grid)
            scores[s] += 1
            order.append((i, s))

    nth = (1000000000 - order[0][0]) % len(scores)

    return order[nth][1]


grid = []
for line in f.readlines():
    if not line.strip():
        continue
    grid.append(list(line.strip()))

s = process_grid(grid)

print(s)
