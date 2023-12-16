from collections import defaultdict, OrderedDict

# f = open('input_test.txt')
f = open('input.txt')

steps = f.readline().strip().split(",")

s = 0


def ascii_hash(step):
    """
    Determine the ASCII code for the current character of the string.
    Increase the current value by the ASCII code you just determined.
    Set the current value to itself multiplied by 17.
    Set the current value to the remainder of dividing itself by 256.
    """

    s = 0
    for char in step:
        s += ord(char)
        s *= 17
        s = s % 256

    return s


boxes = defaultdict(OrderedDict)

for step in steps:
    if step.endswith("-"):
        operation = "remove"
        label = step[:-1]
        focal = None
        box = ascii_hash(label)
        if label in boxes[box]:
            boxes[box].pop(label)
    else:
        operation = "add"
        label, focal = step.split("=")
        focal = int(focal)
        box = ascii_hash(label)
        boxes[box].update({label: focal})

s = 0
for b, lenses in boxes.items():
    for i, (l, f) in enumerate(lenses.items()):
        s += (b + 1) * (i + 1) * f

print(s)
