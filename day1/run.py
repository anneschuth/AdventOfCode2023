f = open('input.txt')

digit_map = [("one", "1"),
             ("two", "2"),
             ("three", "3"),
             ("four", "4"),
             ("five", "5"),
             ("six", "6"),
             ("seven", "7"),
             ("eight", "8"),
             ("nine", "9")]

s = 0
for line in f.readlines():
    print()
    line=line.strip().lower()
    print(line)

    digits = []
    for i, x in enumerate(line):
        if x.isdigit():
            digits.append(int(x))
        else:
            for char_digit, y in digit_map:
                if line[i:].startswith(char_digit):
                    digits.append(int(y))
                    break

    print(digits)
    cal_val = int(digits[0]) * 10 + int(digits[-1])
    print(cal_val)
    s += cal_val




print()
print(s)
