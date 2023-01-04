with open('input.txt') as input_data:
    input_data = (line.strip() for line in input_data)
        
    head_pos = [0,0]
    tail_pos = [0,0]
    journey = []

    for line in input_data:
        direction, distance = line.split()
        distance = int(distance)
        for move in range(1,distance+1): # Split instructions into individual moves
            Hx, Hy = head_pos
            Tx, Ty = tail_pos

            # Move head postition
            if direction == 'R':
                Hx += 1
            elif direction == 'L':
                Hx -= 1
            elif direction == 'D':
                Hy -= 1
            elif direction == 'U':
                Hy += 1
                                   
            # Move tail position
            if direction == 'R' or direction == 'U':
                if Hx - Tx > 1 or Hy - Ty > 1:
                    Tx, Ty = head_pos

            if direction == 'L' or direction == 'D':
                if Tx - Hx > 1 or Ty - Hy > 1:
                    Tx, Ty = head_pos
            
            journey.append((Tx, Ty))
            head_pos = Hx, Hy
            tail_pos = Tx, Ty

    print(len(set(journey))) # Number of indivual locations visited 
