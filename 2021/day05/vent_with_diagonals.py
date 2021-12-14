import re
import numpy as np

file = open("input.txt", 'r')

all_lines = []  # each line in all_lines will be a list [x1, y1, x2, y2]
max_point = 0

for line in file:
  line = re.split(',| -> ', line.replace('\n', ''))
  line = [int(x) for x in line]
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
  elif line[0] == line[2]:  # vertical lines
    y1 = min(line[1], line[3])
    y2 = max(line[1], line[3])
    x = line[0]
    grid[x, y1:y2+1] += 1
  else:  # diagonal lines
    x1, y1, x2, y2 = line[0], line[1], line[2], line[3]
    if x1 < x2:
      x_points = list(range(x1, x2+1))
    else:
      x_points = list(range(x1, x2-1, -1))
    if y1 < y2:
      y_points = list(range(y1, y2+1))
    else:
      y_points = list(range(y1, y2-1, -1))
    diagonal_points = list(zip(x_points, y_points))
    for point in diagonal_points:
      grid[point[0], point[1]] += 1

num_dangerous_points = len(np.where(grid > 1)[0])
print(f"Number of dangerous points = {num_dangerous_points}")
