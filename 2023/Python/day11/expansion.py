import numpy as np

file = open("input.txt")

universe = []
empty_rows = []  # will contain indices of empty rows
num_rows = 0

for line in file:
  line = list(line.strip().split()[0])
  universe.append(line)
  if '#' not in line:
    empty_rows.append(num_rows)
  num_rows += 1

universe = np.array(universe)
num_rows, num_cols = universe.shape

empty_cols = []  # will contain indices of empty columns
for j in range(num_cols):
  if '#' not in universe[:, j]:
    empty_cols.append(j)

galaxies = []  # will contain coords of each galaxy
for i in range(num_rows):
  for j in range(num_cols):
    if universe[i, j] == '#':
      galaxies.append((i, j))

total_dist = 0
multiplier = 1000000
for i in range(len(galaxies) - 1):
  for j in range(i+1, len(galaxies)):
    num_empty_rows = len([row for row in empty_rows if row > galaxies[i][0] and row < galaxies[j][0]])
    num_empty_cols = len([col for col in empty_cols if 
                            col > min(galaxies[i][1], galaxies[j][1]) and
                            col < max(galaxies[i][1], galaxies[j][1])])
    num_extra_rows = (multiplier - 1) * num_empty_rows
    num_extra_cols = (multiplier - 1) * num_empty_cols
    dist = (abs(galaxies[i][0] - galaxies[j][0])
                    + abs(galaxies[i][1] - galaxies[j][1])
                    + num_extra_rows + num_extra_cols)
    total_dist += dist

print(f"Total distances between all galaxies = {total_dist}")