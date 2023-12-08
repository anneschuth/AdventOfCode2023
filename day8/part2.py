import math

# f = open('input_test.txt')
f = open('input.txt')

directions = f.readline().strip()

map = {}
starts = []
for line in f.readlines():
    if not line.strip():
        continue
    f, t = line.strip().split("=")
    f = f.strip()
    if f.endswith("A"):
        starts.append(f)
    map[f] = [x.strip() for x in t.strip()[1:-1].split(",")]

found = False
c = 0

locations = []
for n in starts:
    found = False
    c = 1
    while not found:
        for d in directions:
            if d == "L":
                n = map[n][0]
            elif d == "R":
                n = map[n][1]
            if n.endswith("Z"):
                locations.append(c)
                found = True
                break
            c += 1

print(locations)
print(math.lcm(*locations))
