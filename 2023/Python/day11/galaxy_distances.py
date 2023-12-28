import numpy as np

file = open("input.txt")

universe = []

for line in file:
  line = list(line.strip().split()[0])
  universe.append(line)
  if '#' not in line:
    universe.append(line)  # expand universe vertically

universe = np.array(universe)
num_rows, num_cols = universe.shape

empty_cols = []  # will contain indices of empty columns
for j in range(num_cols):
  if '#' not in universe[:, j]:
    empty_cols.append(j)

# Expand universe horizontally
for i, col_index in enumerate(empty_cols):
  universe = np.insert(universe, col_index+i, values=universe[:, empty_cols[0]], axis=1)

galaxies = []  # will contain coords of each galaxy
for i in range(universe.shape[0]):
  for j in range(universe.shape[1]):
    if universe[i, j] == '#':
      galaxies.append((i, j))

total_dist = 0
for i in range(len(galaxies) - 1):
  for j in range(i+1, len(galaxies)):
    total_dist += (abs(galaxies[i][0] - galaxies[j][0])
                    + abs(galaxies[i][1] - galaxies[j][1]))

print(f"Total distances between all galaxies = {total_dist}")