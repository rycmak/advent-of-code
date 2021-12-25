import numpy as np

file = open("input_test.txt", 'r')

dots = []
instructions = []
instruction = False
x_max = 0
y_max = 0

for line in file:
  line = line.replace('\n', '')
  if len(line) == 0:
    instruction = True
  elif instruction == True:
    line = line.split()[2].split('=')
    instructions.append((line[0], line[1]))
  else:
    line = line.split(',')
    dots.append((int(line[1]), int(line[0])))
    x_max = max(x_max, dots[-1][1])
    y_max = max(y_max, dots[-1][0])

grid = np.zeros((y_max + 1, x_max + 1))
for dot in dots:
  grid[dot] = 1

def y_fold(y_fold_line):
  global grid
  global y_max
  print(f"y_max = {y_max}")
  sub_grid = grid[(y_fold_line+1):(y_max+1), :]
  new_grid = np.zeros((y_max - y_fold_line, grid.shape[1]))
  print(f"new grid size = {new_grid.shape}")
  for y in range(y_max - y_fold_line):
    print(f"y = {y}")
    new_grid[y, :] = sub_grid[y_max - y_fold_line - y - 1, :]  # why -1 here???
  grid = grid[:y_fold_line, :]
  y_max = grid.shape[0] - 1
  grid[(y_max+1-new_grid.shape[0]):y_max+1, :] = grid[(y_max+1-new_grid.shape[0]):y_max+1, :] + new_grid
  # print(grid)

def x_fold(x_fold_line):
  global grid
  global x_max
  print(f"gridsize = {grid.shape}, x_max = {x_max}, x_fold_line = {x_fold_line} ")
  sub_grid = grid[:, (x_fold_line+1):(x_max+1)]
  print(f"subgrid.shape = {sub_grid.shape}")
  new_grid = np.zeros((grid.shape[0], (x_max - x_fold_line)))
  print(f"new_grid.shape = {new_grid.shape}")
  for x in range(x_max - x_fold_line):
    new_grid[:, x] = sub_grid[:, x_max - x_fold_line - x - 1]  # why -1 here???
  grid = grid[:, :x_fold_line]
  x_max = grid.shape[1] - 1
  grid[:, (x_max+1-new_grid.shape[1]):x_max+1] = grid[:, (x_max+1-new_grid.shape[1]):x_max+1] + new_grid
  # print(grid)

first_fold = instructions[0]
if first_fold[0] == 'y':  # horizontal fold
  y_fold_line = int(first_fold[1])
  y_fold(y_fold_line)
elif first_fold[0] == 'x':  # vertical fold
  x_fold_line = int(first_fold[1])
  x_fold(x_fold_line)

num_dots = np.count_nonzero(grid)
print(f"Number of dots = {num_dots}")
