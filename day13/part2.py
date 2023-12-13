f = open('input.txt')


# f = open('input_test.txt')


def diff(line1, line2):
    return sum(0 if x == y else 1 for x, y in zip(line1, line2))


def horizontal(grid):
    n = len(grid)
    for i in range(1, n):
        diff_sum = 0
        for j in range(min([n - i, i])):
            x = grid[i - 1 - j]
            y = grid[i + j]
            diff_sum += diff(x, y)
            if diff_sum > 1:
                break
        if diff_sum == 1:
            return i
    return 0


def vertical(grid):
    n = len(grid)
    m = len(grid[0])
    for i in range(1, m):
        diff_sum = 0
        for j in range(min([m - i, i])):
            x = [grid[x][i - 1 - j] for x in range(n)]
            y = [grid[x][i + j] for x in range(n)]
            diff_sum += diff(x, y)
            if diff_sum > 1:
                break
        if diff_sum == 1:
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
