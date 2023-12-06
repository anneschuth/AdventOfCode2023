f = open('input.txt')


def overlap(y, start, stop):
    for yy in [y - 1, y, y + 1]:
        if start <= yy < stop:
            return True
    return False


def is_gear(grid, x, y):
    numbers = []
    for xx in [x - 1, x, x + 1]:
        if xx < 0:
            continue
        if xx >= len(grid):
            continue

        number = []
        start = None
        stop = None

        for yy in range(len(grid[xx])):
            v = grid[xx][yy]
            if v.isdigit():
                if len(number) == 0:
                    start = yy
                number.append(v)
            elif number:
                stop = yy
                if overlap(y, start, stop):
                    numbers.append(int("".join(number)))
                number = []
                start = None
                stop = None
    if len(numbers) == 2:
        return numbers[0] * numbers[1]
    return 0


s = 0
grid = []
for line in f.readlines():
    grid.append(list(line))

for x, line in enumerate(grid):
    for y, char in enumerate(line):
        if char == "*":
            gear = is_gear(grid, x, y)
            if gear:
                s += gear

print()
print(s)
