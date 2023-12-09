f = open('input.txt')
# f = open('input_test.txt')

def process(l):
    d = []
    done = True
    for i in range(len(l)-1):
        v = l[i+1] - l[i]
        if v != 0:
            done = False
        d.append(v)
    if not done:
        return l[-1] + process(d)
    return l[-1]

s = 0
for line in f.readlines():
    if not line.strip():
        continue
    output = process([int(x) for x in line.split()])
    print(line.strip(), "-->", output)
    s += output

print()
print(s)
