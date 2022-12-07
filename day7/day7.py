# Fetch input data
with open('input.txt') as input_data:
    input_data = [line.strip('\n') for line in input_data.readlines()]
    current_dir = [r'/']
    dirs = {}
    for line in input_data[1:]:
        current_dir = current_dir

        # Create current directory path as a list
        if line.startswith('$ cd'):
            if not line.endswith('..'):
                current_dir.append(current_dir[-1]+line[5:])
            else:
                current_dir.pop()

        # Save directory names and contents to dictionary       
        if line[0].isdigit():
            for i in range(1, len(current_dir)+1):
                if current_dir[-i] in dirs:
                    dirs[current_dir[-i]].append(line)
                else:
                    dirs[current_dir[-i]]=[line]

# Calculate size of each directory
totals = []
for dir, files in dirs.items():
    sizes = [z.split(' ')[0] for z in files]
    total_size = sum(int(x) for x in sizes)
    dirs[dir] = total_size
    totals.append(total_size)

# Part One
totals = [a for a in totals if a <= 100000]
print(sum(totals))

# Part Two
unused_space = 70000000 - (dirs[r'/'])
required_space = 30000000 - unused_space
print(min([size for size in dirs.values() if size > required_space]))
