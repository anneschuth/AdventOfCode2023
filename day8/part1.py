f = open('input.txt')
# f = open('input_test.txt')


directions = f.readline().strip()

map = {}
for line in f.readlines():
    if not line.strip():
        continue
    f, t = line.strip().split("=")
    map[f.strip()] = [x.strip() for x in t.strip()[1:-1].split(",")]

n = "AAA"
found = False
c = 0
while not found:
    for d in directions:
        c += 1
        if d == "L":
            n = map[n][0]
        elif d == "R":
            n = map[n][1]
        if n == "ZZZ":
            found = True
            break

print(c)
