f = open('input.txt')
s = 0


def process_line(line, i, lines):
    winning_part, have_part = line.split(":")[1].split("|")
    winning = {int(x) for x in winning_part.strip().split()}
    have = {int(x) for x in have_part.strip().split()}
    count = len(winning.intersection(have))
    s = 1
    for j, linej in enumerate(lines[i+1:i+count+1]):
        s += process_line(linej, i+1+j, lines)
    return s


lines = f.readlines()
for i, line in enumerate(lines):
    copies = process_line(line, i, lines)
    print(line.strip(), "-->", copies)
    s += copies

print(s)