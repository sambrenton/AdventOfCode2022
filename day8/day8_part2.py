import numpy as np

with open('input.txt') as input_data:
    forest =(np.array([list(map(int, line.strip())) for line in input_data]))
    scenic_scores = []
    for x in range(len(forest)-2):
        for y in range(len(forest[x])-2):
            tree = forest[x+1][y+1]

            r_count = 0 # Count trees to the right
            for next_tree in forest[x+1][y+2:]:
                if tree > next_tree:
                    r_count += 1
                else:
                    r_count += 1
                    break

            l_count = 0 # Count trees to the left
            for next_tree in reversed(forest[x+1][:y+1]):
                if tree > next_tree:
                    l_count += 1
                else:
                    l_count += 1
                    break

            d_count = 0 # Count trees downwards
            for next_tree in forest[x+2:,y+1]:
                if tree > next_tree:
                    d_count += 1
                else:
                    d_count += 1
                    break
            
            u_count = 0 # Count tress upwards
            for next_tree in reversed(forest[:x+1:,y+1]):
                if tree > next_tree:
                    u_count += 1
                else:
                    u_count += 1     
                    break

            scenic_score = (u_count * d_count * l_count * r_count)
            scenic_scores.append(scenic_score)

print(max(scenic_scores))     
