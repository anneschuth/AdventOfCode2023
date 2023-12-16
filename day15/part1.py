f = open('input.txt')
# f = open('input_test.txt')

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


for step in steps:
    s += ascii_hash(step)

print(s)
