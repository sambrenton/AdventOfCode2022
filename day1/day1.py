# Fetch input data
with open('input.txt') as input_data:
    lines = [line.strip() for line in input_data.readlines()]

totals = []
count = 0
for line in lines:
    if not line == '':
        count += int(line)
    if line == '':
        totals.append(count)
        count = 0

totals.sort()

# Part 1
print(totals[-1])

# Part 2
print(totals[-1] + totals [-2] + totals[-3])