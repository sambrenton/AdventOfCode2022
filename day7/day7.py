import re

with open('input.txt') as input_data:
    input_data = [line.strip('\n') for line in input_data.readlines()]
    current_dir = [r'/']
    dirs = {}
    for line in input_data[1:]:
        current_dir = current_dir

        if line.startswith('$ cd'):
            if not line.endswith('..'):
                current_dir.append(current_dir[-1]+line[5:])
            else:
                current_dir.pop()
                
        if line[0].isdigit():
            for i in range(1, len(current_dir)+1):
                try:
                    dirs[current_dir[-i]].append(line)
                except KeyError:
                    dirs[current_dir[-i]]=[]
                    dirs[current_dir[-i]].append(line)

totals = []
for dir, files in dirs.items():
    sizes = [z.split(' ')[0] for z in files]
    total_size = sum(int(x) for x in sizes)
    dirs[dir] = total_size
    totals.append(total_size)

totals = [a for a in totals if a <= 100000]
print(sum(totals))
