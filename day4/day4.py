import re

# Fetch input data
with open('input.txt') as input_data:
    input_data = [line.strip() for line in input_data.readlines()]

    # Part One
    overlap_count = 0
    for line in input_data:
        a, b, c, d = re.findall(r'[0-9][0-9]*', line)
        seta, setb = set(range(int(a), int(b)+1)), set(range(int(c), int(d)+1))
        if seta | setb == seta or seta | setb == setb:
            overlap_count += 1
    print(overlap_count)

    # Part Two
    overlap_count = 0
    for line in input_data:
        a, b, x, y = re.findall(r'[0-9][0-9]*', line)
        if len(set(range(int(a), int(b)+1)) & set(range(int(x), int(y)+1))) != 0:
            overlap_count += 1
    print(overlap_count)
