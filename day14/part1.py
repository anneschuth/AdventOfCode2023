f = open('input.txt')


# f = open('input_test.txt')


def print_grid(grid):
    for l in grid:
        print("".join([str(x) for x in l]))
    print()


def move(grid):
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


def score(grid):
    n = len(grid)
    s = 0
    for line in grid:
        c = sum(1 if x == "O" else 0 for x in line)
        s += n * c
        n -= 1
    return s


def process_grid(grid):
    grid = move(grid)
    return score(grid)


grid = []
for line in f.readlines():
    if not line.strip():
        continue
    grid.append(list(line.strip()))

print_grid(grid)
s = process_grid(grid)
print_grid(grid)

print(s)
