import numpy as np

file = open("input.txt", 'r')

height_map = []

for line in file:
  height_map.append([ord(x) for x in list(line.strip())])

height_map = np.array(height_map)

def can_move_to(new_x, new_y, current_height):
  if (new_x >= 0 and new_x < height_map.shape[0]
      and new_y >= 0 and new_y < height_map.shape[1]
      and height_map[new_x, new_y] <= current_height + 1
      and visited[new_x, new_y] == 0):
    return True
  else:
    return False

def get_next_steps(current_x, current_y, current_height):
  # check if able to move up
  if can_move_to(current_x-1, current_y, current_height):
    steps[-1].append((current_x-1, current_y))
    visited[current_x-1, current_y] = 1
  # check if able to move down
  if can_move_to(current_x+1, current_y, current_height):
    steps[-1].append((current_x+1, current_y))
    visited[current_x+1, current_y] = 1
  # check if able to move left
  if can_move_to(current_x, current_y-1, current_height):
    steps[-1].append((current_x, current_y-1))
    visited[current_x, current_y-1] = 1
  # check if able to move right
  if can_move_to(current_x, current_y+1, current_height):
    steps[-1].append((current_x, current_y+1))
    visited[current_x, current_y+1] = 1

start_S = np.where(height_map == ord('S'))
start_a = np.where(height_map == ord('a'))
height_map[start_S] = ord('a')  # convert height at S to be same as 'a'
end = np.where(height_map == ord('E'))
destination_height = height_map[end] = ord('z') + 1  # convert destination height to be one more than 'z'
start_positions = [(start_S[0][0], start_S[1][0])]
for pos in range(0, len(start_a[0])):
  start_positions.append((start_a[0][pos], start_a[1][pos]))

num_steps_per_path = []

for start in start_positions:
  visited = np.zeros((height_map.shape))
  visited[start] = 1
  steps = [[start]]
  destination_reached = False

  while not destination_reached:
    steps.append([])
    for pos in steps[-2]:
      get_next_steps(pos[0], pos[1], height_map[pos])
    if destination_height in [height_map[pos] for pos in steps[-1]]:
      destination_reached = True
      num_steps_per_path.append(len(steps) - 1)
    if not steps[-1]:  # no way to reach destination
      break

print(f"Fewest steps to move from a to E = {min(num_steps_per_path)}")

