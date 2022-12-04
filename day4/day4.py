# Fetch input data
with open('input.txt') as input_data:
    input_data = [line.strip() for line in input_data.readlines()]

    # Part One
    overlap_count = 0
    for line in input_data:
        pair_1, pair_2 = line.split(',')
        a, b = pair_1.split('-')
        x, y = pair_2.split('-')
        seta, setb = set(range(int(a), int(b)+1)), set(range(int(x), int(y)+1))
        combined = (seta | setb)
        if combined == seta:
            overlap_count += 1
        elif combined == setb:
            overlap_count += 1

    print(overlap_count)

    # Part Two
    overlap_count = 0
    for line in input_data:
        pair_1, pair_2 = line.split(',')
        a, b = pair_1.split('-')
        x, y = pair_2.split('-')
        if len(set(range(int(a), int(b)+1)) & set(range(int(x), int(y)+1))) != 0:
            overlap_count += 1

    print(overlap_count)
