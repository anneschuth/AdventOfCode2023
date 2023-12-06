f = open('input.txt')
# f = open('input_test.txt')

times = [int(x) for x in f.readline().split(":")[1].strip().replace(" ", "").split()]
distances = [int(x) for x in f.readline().split(":")[1].strip().replace(" ", "").split()]



def game(race_time, record_distance):
    print()
    print(t, d)
    beats = 0
    for speed in range(race_time+1):
        distance = ((race_time-speed) * speed)
        # print("speed:", speed, "distance:", distance)
        if distance > record_distance:
            beats += 1

    return beats


s = 1

for t, d, in zip(times, distances):
    s *= game(t, d)

print()
print("result:", s)
