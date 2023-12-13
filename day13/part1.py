f = open('input.txt')
# f = open('input_test.txt')


def same(line1, line2):
    return all(x == y for x, y in zip(line1, line2))


def horizontal(grid):
    n = len(grid)
    for i in range(1, n):
        all_same = True
        for j in range(min([n - i, i])):
            x = grid[i - 1 - j]
            y = grid[i + j]
            if not same(x, y):
                all_same = False
                break
        if all_same:
            print("MIRROR AT", i)
            return i
    return 0


def vertical(grid):
    n = len(grid)
    m = len(grid[0])
    for i in range(1, m):
        all_same = True
        for j in range(min([m - i, i])):
            x = [grid[x][i - 1 - j] for x in range(n)]
            y = [grid[x][i + j] for x in range(n)]
            if not same(x, y):
                all_same = False
                break
        if all_same:
            print("MIRROR AT", i)
            return i
    return 0


def process_grid(grid):
    return vertical(grid) + 100 * horizontal(grid)


s = 0
grid = []
for line in f.readlines():
    if not line.strip():
        if grid:
            s += process_grid(grid)
        grid = []
        continue
    grid.append(list(line.strip()))
if grid:
    s += process_grid(grid)

print(s)
