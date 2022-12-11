import numpy as np

file = open("input.txt", 'r')

grid_size = 500

visited = np.zeros((grid_size, grid_size))

knots_pos = [(int(grid_size/2), int(grid_size/2)) for i in range(0, 10)]
visited[knots_pos[-1]] = 1

def is_touching(a, b):
  if (a[0] == b[0]):
    if abs(a[1] - b[1]) <= 1:
      return True
  if (a[1] == b[1]):
    if abs(a[0] - b[0]) <= 1:
      return True
  if ((abs(a[0] - b[0]) == 1) and (abs(a[1] - b[1]) == 1)):
    return True
  return False

def get_new_following_pos(a, b):
  if (a[0] == b[0]):
    if (a[1] - b[1]) > 1:
      return (b[0], b[1]+1)
    elif (b[1] - a[1]) > 1:
      return (b[0], b[1]-1)
  if (a[1] == b[1]):
    if (a[0] - b[0]) > 1:
      return (b[0]+1, b[1])
    elif (b[0] - a[0]) > 1:
      return (b[0]-1, b[1])
  if (a[0] - b[0] >= 1):
    if (a[1] - b[1] >= 2):
      return (b[0]+1, b[1]+1)
    if (b[1] - a[1] >= 2):
      return (b[0]+1, b[1]-1)
  if (b[0] - a[0] >= 1):
    if (a[1] - b[1] >= 2):
      return (b[0]-1, b[1]+1)
    if (b[1] - a[1] >= 2):
      return (b[0]-1, b[1]-1)
  if (a[1] - b[1] >= 1):
    if (a[0] - b[0] >= 2):
      return (b[0]+1, b[1]+1)
    if (b[0] - a[0] >= 2):
      return (b[0]-1, b[1]+1)
  if (b[1] - a[1] >= 1):
    if (a[0] - b[0] >= 2):
      return (b[0]+1, b[1]-1)
    if (b[0] - a[0] >= 2):
      return (b[0]-1, b[1]-1)

def move_knots():
  for knot in range(1, 10):
    if not is_touching(knots_pos[knot-1], knots_pos[knot]):
      knots_pos[knot] = get_new_following_pos(knots_pos[knot-1], knots_pos[knot])
  visited[knots_pos[-1]] = 1
  
for line in file:
  dir = line.strip().split()[0]
  steps = int(line.strip().split()[1])
  if dir == "R":
    for step in range(0, steps):
      knots_pos[0] = (knots_pos[0][0], knots_pos[0][1]+1)
      move_knots()
  elif dir == "L":
    for step in range(0, steps):
      knots_pos[0] = (knots_pos[0][0], knots_pos[0][1]-1)
      move_knots()
  elif dir == "U":
    for step in range(0, steps):
      knots_pos[0] = (knots_pos[0][0]-1, knots_pos[0][1])
      move_knots()
  elif dir == "D":
    for step in range(0, steps):
      knots_pos[0] = (knots_pos[0][0]+1, knots_pos[0][1])
      move_knots()

print(f"The tail visited {int(visited.sum())} positions at least once.")