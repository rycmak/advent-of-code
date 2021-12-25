import numpy as np

file = open("input.txt", 'r')

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
  sub_grid = grid[(y_fold_line+1):(y_max+1), :]
  new_grid = np.zeros((y_max - y_fold_line, grid.shape[1]))
  for y in range(y_max - y_fold_line):
    new_grid[y, :] = sub_grid[y_max - y_fold_line - y - 1, :]
  grid = grid[:y_fold_line, :]
  y_max = grid.shape[0] - 1
  grid[(y_max+1-new_grid.shape[0]):y_max+1, :] = grid[(y_max+1-new_grid.shape[0]):y_max+1, :] + new_grid

def x_fold(x_fold_line):
  global grid
  global x_max
  sub_grid = grid[:, (x_fold_line+1):(x_max+1)]
  new_grid = np.zeros((grid.shape[0], (x_max - x_fold_line)))
  for x in range(x_max - x_fold_line):
    new_grid[:, x] = sub_grid[:, x_max - x_fold_line - x - 1]  # why -1 here???
  grid = grid[:, :x_fold_line]
  x_max = grid.shape[1] - 1
  grid[:, (x_max+1-new_grid.shape[1]):x_max+1] = grid[:, (x_max+1-new_grid.shape[1]):x_max+1] + new_grid

for i, fold in enumerate(instructions):
  if fold[0] == 'y':  # horizontal fold
    y_fold_line = int(fold[1])
    y_fold(y_fold_line)
  elif fold[0] == 'x':  # vertical fold
    x_fold_line = int(fold[1])
    x_fold(x_fold_line)


letters = np.full(grid.shape, '.', dtype=object)
letters[np.where(grid > 0)] = '#'
print(letters)

# ['#' '#' '#' '.' '.' '#' '.' '.' '#' '.' '.' '#' '#' '.' '.' '#' '.' '.' '.' '.' '#' '#' '#' '.' '.' '.' '#' '#' '.' '.' '#' '#' '#' '.' '.' '.' '#' '#' '.' '.']
# ['#' '.' '.' '#' '.' '#' '.' '.' '#' '.' '#' '.' '.' '#' '.' '#' '.' '.' '.' '.' '#' '.' '.' '#' '.' '#' '.' '.' '#' '.' '#' '.' '.' '#' '.' '#' '.' '.' '#' '.']
# ['#' '.' '.' '#' '.' '#' '#' '#' '#' '.' '#' '.' '.' '#' '.' '#' '.' '.' '.' '.' '#' '.' '.' '#' '.' '#' '.' '.' '.' '.' '#' '.' '.' '#' '.' '#' '.' '.' '#' '.']
# ['#' '#' '#' '.' '.' '#' '.' '.' '#' '.' '#' '#' '#' '#' '.' '#' '.' '.' '.' '.' '#' '#' '#' '.' '.' '#' '.' '.' '.' '.' '#' '#' '#' '.' '.' '#' '#' '#' '#' '.']
# ['#' '.' '#' '.' '.' '#' '.' '.' '#' '.' '#' '.' '.' '#' '.' '#' '.' '.' '.' '.' '#' '.' '#' '.' '.' '#' '.' '.' '#' '.' '#' '.' '#' '.' '.' '#' '.' '.' '#' '.']
# ['#' '.' '.' '#' '.' '#' '.' '.' '#' '.' '#' '.' '.' '#' '.' '#' '#' '#' '#' '.' '#' '.' '.' '#' '.' '.' '#' '#' '.' '.' '#' '.' '.' '#' '.' '#' '.' '.' '#' '.']