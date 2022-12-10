import numpy as np

tree_array = []

file = open("input.txt", 'r')
for line in file:
  tree_array.append([int(i) for i in list(line.strip())])

tree_array = np.array(tree_array)

num_rows = np.shape(tree_array)[0]
num_cols = np.shape(tree_array)[1]

scenic_scores = np.zeros((num_rows, num_cols))

for current_row in range(1, num_rows-1):
  for current_col in range(1, num_cols-1):
    current_tree = tree_array[current_row, current_col]
    view_distances = [0, 0, 0, 0]  # viewing distances for up, down, left, right
    # Calculate viewing distances looking up
    for row in range(current_row-1, -1, -1):
      view_distances[0] += 1
      if tree_array[row, current_col] >= current_tree:
        break
    # Calculate viewing distances looking down
    for row in range(current_row+1, num_rows):
      view_distances[1] += 1
      if tree_array[row, current_col] >= current_tree:
        break
    # Calculate viewing distances looking left
    for col in range(current_col-1, -1, -1):
      view_distances[2] += 1
      if tree_array[current_row, col] >= current_tree:
        break
    # Calculate viewing distances looking right
    for col in range(current_col+1, num_cols):
      view_distances[3] += 1
      if tree_array[current_row, col] >= current_tree:
        break
    
    scenic_scores[current_row, current_col] = np.prod(view_distances)

print(f"Highest scenic score = {int(np.max(scenic_scores))}")