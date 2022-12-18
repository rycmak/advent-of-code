import numpy as np

file = open("input.txt", 'r')

grid_shape = (600, 650)
grid = np.full(grid_shape, '.')

sand_source = (0, 500)

for path_string in file:
  coords_string = [line.strip() for line in path_string.split("->")]
  path = [tuple(map(int, coord.split(","))) for coord in coords_string]
  for i in range(len(path) - 1):
    start_horizontal = min(path[i][1], path[i+1][1])
    end_horizontal = max(path[i][1], path[i+1][1])
    start_vertical = min(path[i][0], path[i+1][0])
    end_vertical = max(path[i][0], path[i+1][0])
    grid[start_horizontal:end_horizontal+1, start_vertical:end_vertical+1] = '#'

left_edge = min(np.where(grid == '#')[1])
right_edge = max(np.where(grid == '#')[1])
bottom_edge = max(np.where(grid == '#')[0])
floor = bottom_edge + 2

grid[floor, :] = '#'


def get_next_pos(current_pos):
  if grid[current_pos[0]+1, current_pos[1]] == '.':
    return (current_pos[0]+1, current_pos[1])
  elif grid[current_pos[0]+1, current_pos[1]-1] == '.':
    return (current_pos[0]+1, current_pos[1]-1)
  elif grid[current_pos[0]+1, current_pos[1]+1] == '.':
    return (current_pos[0]+1, current_pos[1]+1)
  else:
    return current_pos


def get_sand_stop_pos():
  current_pos = sand_source
  while current_pos[0] < floor:
    next_pos = get_next_pos(current_pos)
    if next_pos == current_pos:
      break
    else:
      current_pos = next_pos
  return current_pos


units_of_sand = 0

while True:
  sand_stop_pos = get_sand_stop_pos()
  units_of_sand += 1
  if sand_stop_pos == sand_source:  # source is blocked
    break
  if sand_stop_pos[0] == (floor - 1):  # reached rest position on floor
    grid[sand_stop_pos] = 'o'
    continue
  grid[sand_stop_pos] = 'o'

print(f"Units of sand = {units_of_sand}")
