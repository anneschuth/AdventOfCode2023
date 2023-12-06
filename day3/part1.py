f = open('input.txt')


def is_adjecent(number, grid, x, y):
    for xx in [x-1, x, x+1]:
        for yy in range(y-len(number)-1, y+1):
            if xx < 0 or yy < 0:
                continue
            if xx >= len(grid):
                continue
            if yy >= len(grid[xx]):
                continue
            v = grid[xx][yy]
            if v.isdigit() or v == "." or v == "\n":
                continue
            if int("".join(number)) == 388:
                    return True
            return True
    return False


s = 0
grid = []
for line in f.readlines():
    grid.append(list(line))


for x, line in enumerate(grid):
    number = []
    for y, char in enumerate(line):
        if char.isdigit():
            number.append(char)
        elif number and (y == len(line) or not char.isdigit()):

            if is_adjecent(number, grid, x, y):
                int_number = int("".join(number))
                s += int_number
                print(int_number)
                number = []
            else:
                print("SKIPPING", number)
                number = []

print()
print(s)
