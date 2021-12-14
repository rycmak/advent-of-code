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

risk_levels = []

for i in range(1, height + 1):
  for j in range(1, width + 1):
      neighbours = [all_points[i, j-1], all_points[i, j+1], all_points[i-1, j], all_points[i+1, j]]
      if all([all_points[i, j] < x for x in neighbours]):
        risk_levels.append(all_points[i, j] + 1)

print(f"Sum of risk levels = {sum(risk_levels)}")
