# 12 red cubes, 13 green cubes, and 14 blue cubes

f = open('input.txt')
s=0
for line in f.readlines():
    line = line.strip()
    id_part, config_part = line.split(":", 1)
    game_id = int(id_part.split()[-1])

    configs = config_part.split(";")
    print()
    limits = {"red": 0, "green": 0, "blue": 0}
    for config in configs:
        for c in config.split(","):
            count, color = c.strip().split(" ")
            count = int(count)
            print(game_id, color, count)
            if count > limits[color]:
                limits[color] = count
    lv = list(limits.values())
    power = lv[0]
    for p in lv[1:]:
        power *= p
    s+=power
    print(power)
print()
print(s)