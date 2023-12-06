f = open('input.txt')
s = 0


def process_line(line):
    winning_part, have_part = line.split(":")[1].split("|")
    winning = {int(x) for x in winning_part.strip().split()}
    have = {int(x) for x in have_part.strip().split()}
    count = len(winning.intersection(have))
    if not count:
        return 0

    return 2**(count-1)


for line in f.readlines():
    points = process_line(line)
    print(line.strip(), "-->", points)
    s += points


print(s)