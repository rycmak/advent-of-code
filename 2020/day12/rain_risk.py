# Calculate Manhattan distance from starting point to finish

# Ferry starts off facing east;
# does not change direction unless instruction begins with 'R' or 'L'.
# Store no. of steps taken in each direction as a dict.
# At the end, sum up net no. of steps taken in N/S and E/W directions.

instructions = []
file = open("input.txt", "r")
for line in file:
  # Store each instruction as a tuple; e.g., ('N', 37)
  instructions.append((line.strip()[0], int(line.strip()[1:])))

steps = {'N': 0, 'E': 0, 'S': 0, 'W': 0}  # no. of steps taken in each direction
directions = ['N', 'E', 'S', 'W']
direction_index = 1  # initially facing 'E'
facing_direction = directions[direction_index]

for instruction in instructions:
  if instruction[0] == 'F':  # move forward in facing direction
    steps[facing_direction] += instruction[1]
  elif instruction[0] == 'L':  # turn left
    direction_index = (direction_index - int(instruction[1] / 90)) % 4
    facing_direction = directions[direction_index]
  elif instruction[0] == 'R':  # turn right
    direction_index = (direction_index + int(instruction[1] / 90)) % 4
    facing_direction = directions[direction_index]
  else:  # move N, E, S, or W
    direction = instruction[0]  
    steps[direction] += instruction[1]

manhattan_dist = abs(steps['N'] - steps['S']) + abs(steps['E'] - steps['W'])
print("Manhattan distance = ", manhattan_dist)