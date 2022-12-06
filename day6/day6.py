with open ('input.txt') as input_data:
    input_data = input_data.readline()
    # Part One
    print([set(input_data[i:i+4]) for i in range(0, len(input_data))].index([set(input_data[i:i+4]) for i in range(0, len(input_data)) if len(set(input_data[i:i+4])) == 4][0])+4)
    # Part Two
    print([set(input_data[i:i+14]) for i in range(0, len(input_data))].index([set(input_data[i:i+14]) for i in range(0, len(input_data)) if len(set(input_data[i:i+14])) == 14][0])+14)
