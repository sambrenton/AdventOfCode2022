with open ('input.txt') as input_data:
    input_data = input_data.readline()
    for i in range(0, len(input_data)):
        if  len(set((input_data[i:i+4]))) == 4:
            print(i+4) # <- Answer
            exit()
