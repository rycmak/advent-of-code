import numpy as np

file = open("input.txt", 'r')

all_points = None

for line in file:
  points = [int(x) for x in list(line.replace('\n', '').strip())]
  if all_points is not None:
    all_points = np.r_[all_points, [points]]
  else:
    all_points = np.array([points])

width = all_points.shape[1]  # 10 for test input
height = all_points.shape[0]  # 5 for test input

# Pad edges with 9's
all_points = np.r_[np.full((1, width), 9), all_points]
all_points = np.r_[all_points, np.full((1, width), 9)]
all_points = np.c_[np.full((height + 2, 1), 9), all_points]
all_points = np.c_[all_points, np.full((height + 2, 1), 9)]

low_points = []

for i in range(1, height + 1):
  for j in range(1, width + 1):
      neighbours = [all_points[i, j-1], all_points[i, j+1], all_points[i-1, j], all_points[i+1, j]]
      if all([all_points[i, j] < x for x in neighbours]):
        low_points.append((i, j))

basin_size = 0
basin = []

def calc_num_higher_points(point):
  global basin_size
  global basin
  (i, j) = point
  neighbours = [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]
  for neighbour in neighbours:
    if neighbour[0] != 0 and neighbour[0] != (height + 1) \
        and neighbour[1] != 0 and neighbour[1] != (width + 1) \
        and neighbour not in basin \
        and all_points[neighbour] != 9:  # not padding point, not already counted in basin, not 9
      if all_points[neighbour] > all_points[point]:
        basin.append(neighbour)
        basin_size = basin_size + 1
        calc_num_higher_points(neighbour)

basin_sizes = []
for point in low_points:
  basin_size = 1  # low point is part of basin
  basin = []
  calc_num_higher_points(point)
  basin_sizes.append(basin_size)

print(f"largest three basin sizes = {np.sort(basin_sizes)[-3:]}")
print(f"product = {np.prod(np.sort(basin_sizes)[-3:])}")