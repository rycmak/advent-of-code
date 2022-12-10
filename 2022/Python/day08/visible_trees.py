import numpy as np

tree_array = []

file = open("input.txt", 'r')
for line in file:
  tree_array.append([int(i) for i in list(line.strip())])

tree_array = np.array(tree_array)

num_rows = np.shape(tree_array)[0]
num_cols = np.shape(tree_array)[1]

# Trees on each of the 4 edges are all visible
num_visible_trees = 2 * num_rows + 2 * num_cols - 4

for row in range(1, num_rows-1):
  for col in range(1, num_cols-1):
    if all([tree_array[row, col] > tree for tree in tree_array[0:row, col]]):
      num_visible_trees += 1
    elif all([tree_array[row, col] > tree for tree in tree_array[row+1:, col]]):
      num_visible_trees += 1
    elif all([tree_array[row, col] > tree for tree in tree_array[row, 0:col]]):
      num_visible_trees += 1
    elif all([tree_array[row, col] > tree for tree in tree_array[row, col+1:]]):
      num_visible_trees += 1

print(f"Number of visible trees = {num_visible_trees}")