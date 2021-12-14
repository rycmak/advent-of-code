import re
import numpy as np

file = open("input.txt", 'r')

all_lines = []  # each line in all_lines will be a list [x1, y1, x2, y2]
max_point = 0

for line in file:
  line = re.split(',| -> ', line.replace('\n', ''))
  line = [int(x) for x in line]
  if line[0] == line[2] or line[1] == line[3]:  # only horizontal or vertical lines 
    all_lines.append(line)
    max_point = max(max_point, max(line))

grid = np.zeros((max_point + 1, max_point + 1))

for line in all_lines:
  # Cover points on horizontal lines
  if line[1] == line[3]:
    x1 = min(line[0], line[2])
    x2 = max(line[0], line[2])
    y = line[1]
    grid[x1:x2+1, y] += 1
  else:  # vertical lines
    y1 = min(line[1], line[3])
    y2 = max(line[1], line[3])
    x = line[0]
    grid[x, y1:y2+1] += 1

num_dangerous_points = len(np.where(grid > 1)[0])
print(f"Number of dangerous points = {num_dangerous_points}")
