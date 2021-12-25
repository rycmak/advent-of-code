import numpy as np

file = open("input.txt", 'r')

octo_grid = np.zeros((10, 10), dtype=object)
height, width = octo_grid.shape

for i, line in enumerate(file):
  # Each octopus in the grid is a list
  # specifying energy level and whether it has flashed (True/False)
  octo_grid[i, :] = [[int(x), False] for x in list(line.replace('\n', ''))]

def step():
  for i in range(height):
    for j in range(width):
      octo_grid[i, j][0] += 1  # all energy levels increase by 1
      if octo_grid[i, j][0] > 9 and octo_grid[i, j][1] == False:
        octo_grid[i, j][1] = True  # flashed = True
        increase_neighbours_energies((i, j))  # increase neighbours' energies if necessary

  # Reset energy levels and flash statuses
  for i in range(height):
    for j in range(width):
      if octo_grid[i, j][1] == True:
        octo_grid[i, j] = [0, False]

def increase_neighbours_energies(point):
  for neighbour in neighbours(point):
    octo_grid[neighbour][0] += 1
    if octo_grid[neighbour][0] > 9 and octo_grid[neighbour][1] == False:
      octo_grid[neighbour][1] = True
      increase_neighbours_energies(neighbour)

def neighbours(point):
  # Return array of points that are neighbours (including diagonal) of point
  (i, j) = point
  adj_coords = [(i-1, j-1), (i-1, j), (i-1, j+1),
               (i, j-1), (i, j+1),
               (i+1, j-1), (i+1, j), (i+1, j+1)]
  return [x for x in adj_coords if x[0] >= 0 and x[0] < height
                               and x[1] >= 0 and x[1] < width]


octo_grid_synchronized = np.zeros((10, 10), dtype=object)
for i in range(height):
  for j in range(width):
    octo_grid_synchronized[(i, j)] = [0, False]

num_steps = 0
while (octo_grid == octo_grid_synchronized).all() == False:
  step()
  num_steps += 1

print(f"Number of steps to synchronization = {num_steps}")
