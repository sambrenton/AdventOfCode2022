total_score = 0    

def main(their_throw, your_response):
    round_points = 0
    if their_throw == 'A': # Rock
        if your_response == 'X': # Rock (+1)
            round_points += 4 # Draw (+3)
        if your_response == 'Y': # Paper (+2)
            round_points += 8 # Win (+6)
        if your_response == 'Z': # Scissors (+3)
            round_points += 3 # Loss (+0)

    elif their_throw == 'B': # Paper
        if your_response == 'X': # Rock (+1)
            round_points += 1 # Loss (+0)
        if your_response == 'Y': # Paper (+2)
            round_points += 5 # Draw (+3)
        if your_response == 'Z': # Scissors (+3)
            round_points += 9 # Win (+6)    
    
    elif their_throw == 'C': # Scissors
        if your_response == 'X': # Rock (+1)
            round_points += 7 # Win (+6)
        if your_response == 'Y': # Paper (+2)
            round_points += 2 # Loss (+0)
        if your_response == 'Z': # Scissors (+3)
            round_points += 6 # Draw (+3)
    return round_points 

with open('input.txt') as input_data:
    input_data = [line.strip() for line in input_data.readlines()]

    for round in input_data:
        total_score += main(round[0], round[2])

print(total_score)
