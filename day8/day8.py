import numpy as np

with open('input.txt') as input_data:
    input_data = [list(map(int, line.strip())) for line in input_data]
    trees =(np.array(input_data))
    visible_trees = []

    for x in range(len(trees)-2):
        for y in range(len(trees[x])-2):
            tree = trees[x+1][y+1]
            if all(tree > trees[x+1][y+2:]): # From the right
                visible_trees.append([tree, trees[x+1] , y])

            if all(tree > trees[x+2:,y+1]): # From the bottom
                visible_trees.append([tree, trees[x+1], y])

            if all(tree > trees[x+1][:y+1]): # From the left
                visible_trees.append([tree, trees[x+1], y])

            if all(tree > trees[:x+1:,y+1]): # From the top
                visible_trees.append([tree, trees[x+1], y])

    edge_count = (len(trees[x]) - 2) * 2 + (len(trees[x]) * 2)
    interior_count = len(set(str(tree) for tree in visible_trees))
    print(edge_count + interior_count)
