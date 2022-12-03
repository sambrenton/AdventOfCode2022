with open('input.txt') as input_data:
    input_data = [line.strip() for line in input_data.readlines()]

priorities_sum = 0

for line in input_data:
    first_compartment, second_compartment = line[:int(len(line) / 2)], line[int(len(line) / 2):]
    in_both_compartments = (list(set(first_compartment).intersection(set(second_compartment)))[0])
    if in_both_compartments.isupper():
        priorities_sum += (ord(in_both_compartments) - 38)
    elif in_both_compartments.islower():
        priorities_sum += (ord(in_both_compartments) - 96)

print(priorities_sum)
