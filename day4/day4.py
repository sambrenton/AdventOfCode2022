import re
part_one_answer = 0
part_two_answer = 0
with open('input.txt') as input_data:
    for line in input_data.readlines():
        a, b, c, d = re.findall(r'[0-9][0-9]*', line)
        if set(range(int(a), int(b)+1)) | set(range(int(c), int(d)+1)) == set(range(int(a), int(b)+1)) or set(range(int(a), int(b)+1)) | set(range(int(c), int(d)+1)) == set(range(int(c), int(d)+1)):
            part_one_answer += 1
        if len(set(range(int(a), int(b)+1)) & set(range(int(c), int(d)+1))) != 0:
            part_two_answer += 1

print(part_one_answer)
print(part_two_answer)
