file = open("input.txt")

grid = []
stepped = []  # contains coords aleady stepped on
num_rows = 0

for line in file:
  grid_line = list(line.strip())
  grid.append(grid_line)
  if 'S' in grid_line:
    start = (num_rows, grid_line.index('S'))
  num_rows += 1

num_cols = len(grid[0])

for i in range(num_rows):
  stepped.append([False for j in range(num_cols)])

def get_direction_and_position(current):
  direction, pipe = None, None
  
  # Try going north:
  if (grid[current[0]][current[1]] in ['|', 'L', 'J', 'S'] and
      stepped[current[0]-1][current[1]] == False):
    if current[0] > 1 and grid[current[0]-1][current[1]] == '|':
      direction, current, pipe = "north", (current[0]-1, current[1]), '|'
      return direction, current, pipe
    elif current[0] > 0 and current[1] > 0 and grid[current[0]-1][current[1]] == '7':
      direction, current, pipe = "west", (current[0]-1, current[1]), '7'
      return direction, current, pipe
    elif current[0] > 0 and current[1] < num_cols - 1 and grid[current[0]-1][current[1]] == 'F':
      direction, current, pipe = "east", (current[0]-1, current[1]), 'F'
      return direction, current, pipe
 
  # Or try going west
  if (grid[current[0]][current[1]] in ['-', '7', 'J', 'S'] and 
      stepped[current[0]][current[1]-1] == False):
    if current[1] > 1 and grid[current[0]][current[1]-1] == '-':
      direction, current, pipe = "west", (current[0], current[1]-1), '-'
      return direction, current, pipe
    elif current[0] < num_rows - 1 and current[1] > 0 and grid[current[0]][current[1]-1] == 'F':
      direction, current, pipe = "south", (current[0], current[1]-1), 'F'
      return direction, current, pipe
    elif current[0] > 0 and current[1] > 0 and grid[current[0]][current[1]-1] == 'L':
      direction, current, pipe = "north", (current[0], current[1]-1), 'L'
      return direction, current, pipe

  # Or try going south
  if (grid[current[0]][current[1]] in ['|', '7', 'F', 'S'] and
      stepped[current[0]+1][current[1]] == False):
    if current[0] < num_rows - 2 and grid[current[0]+1][current[1]] == '|':
      direction, current, pipe = "south", (current[0]+1, current[1]), '|'
      return direction, current, pipe
    elif current[0] < num_rows - 1 and current[1] < num_cols - 1 and grid[current[0]+1][current[1]] == 'L':
      direction, current, pipe = "east", (current[0]+1, current[1]), 'L'
      return direction, current, pipe
    elif current[0] < num_rows - 1 and current[1] > 0 and grid[current[0]+1][current[1]] == 'J':
      direction, current, pipe = "west", (current[0]+1, current[1]), 'J'
      return direction, current, pipe

  # If none of the above work, try going east
  if (grid[current[0]][current[1]] in ['-', 'L', 'F', 'S'] and
      stepped[current[0]][current[1]+1] == False):
    if current[1] < num_cols - 2 and grid[current[0]][current[1]+1] == '-':
      direction, current, pipe = "east", (current[0], current[1]+1), '-'
      return direction, current, pipe
    elif current[0] > 0 and current[1] < num_cols - 1 and grid[current[0]][current[1]+1] == 'J':
      direction, current, pipe = "north", (current[0], current[1]+1), 'J'
      return direction, current, pipe
    elif current[0] < num_rows - 1 and current[1] < num_cols - 1 and grid[current[0]][current[1]+1] == '7':
      direction, current, pipe = "south", (current[0], current[1]+1), '7'
      return direction, current, pipe

current = start
loop = [(current[0], current[1])]  # will contain coords of loop
num_steps = 0

while True:
  stepped[current[0]][current[1]] = True
  direction, next, pipe = get_direction_and_position(current)
  current = next
  loop.append((current[0], current[1]))
  stepped[current[0]][current[1]] = True
  num_steps += 1
  if pipe == 'S':
    break
  if direction == "north":
    next = (next[0]-1, next[1])
  elif direction == "west":
    next = (next[0], next[1]-1)
  elif direction == "south":
    next = (next[0]+1, next[1])
  elif direction == "east":
    next = (next[0], next[1]+1)
  current = next
  num_steps += 1
  if grid[current[0]][current[1]] == 'S':
    break
  loop.append((current[0], current[1]))

grid[start[0]][start[1]] = 'L'  # manually inputting this for now

in_loop = 0  # number of tiles within loop
ex_loop = 0  # number of tiles outside loop

for i, row in enumerate(grid):
  for j, pipe in enumerate(row):
    if (i, j) not in loop:
      # tile is not part of loop;
      # go east and find how many times loop is crossed
      num_crossing = 0
      loop_segment = [p for p in loop if p[0] == i and p[1] > j]  # points in row i that form part of loop
      bend = None
      for seg in sorted(loop_segment):
        if grid[seg[0]][seg[1]] == '|':
          num_crossing += 1
          continue
        if grid[seg[0]][seg[1]] == 'L':
          bend = 'L'
          continue
        if grid[seg[0]][seg[1]] == 'F':
          bend = 'F'
          continue
        if grid[seg[0]][seg[1]] == 'J':
          if bend == 'L':
            num_crossing += 2
            bend = None
          elif bend == 'F':
            num_crossing += 1
            bend = None
          continue
        if grid[seg[0]][seg[1]] == '7':
          if bend == 'L':
            num_crossing += 1
            bend = None
          elif bend == 'F':
            num_crossing += 2
            bend = None
          continue
      # if given point crosses the loop in a given direction an even number of times
      # then it is outside the loop
      if num_crossing % 2 == 0:
        ex_loop += 1
      else:
        in_loop += 1

print(f"Number of tiles enclosed by loop = {in_loop}")
