# 12 red cubes, 13 green cubes, and 14 blue cubes
limits = {"red": 12, "green": 13, "blue": 14}

f = open('input.txt')
s=0
for line in f.readlines():
    line = line.strip()
    id_part, config_part = line.split(":", 1)
    game_id = int(id_part.split()[-1])

    configs = config_part.split(";")
    print()
    possible = True
    for config in configs:
        for c in config.split(","):
            count, color = c.strip().split(" ")
            count = int(count)
            print(game_id, color, count)
            if count > limits[color]:
                possible = False
                break
    if possible:
        s += game_id
        print("possible")
    else:
        print("IMPOSSIBLE")
    print()
print()
print(s)