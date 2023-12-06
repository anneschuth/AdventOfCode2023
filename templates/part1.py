# f = open('input.txt')
f = open('input_test.txt')


def process_line(line):
    pass


s = 0
for line in f.readlines():
    output = process_line(line)
    print(line.strip(), "-->", output)
    s += output

print(s)
