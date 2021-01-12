# 'F' moves ship to waypoint specified no. of times.
# N, E, S, W instructions move waypoint specified no. of steps from ship.
# L or R rotates waypoint anticlockwise or clockwise around ship

# Waypoint is relative to ship -- if ship moves, waypoint moves with it.
# Waypoint initial position relative to ship: 10 units E, 1 unit N

# For waypoint, store its coords relative to ship as a dict.
# For ship, store no. of steps taken in each direction as a dict.
# At the end, sum up net no. of steps taken in N/S and E/W directions.

instructions = []
file = open("input.txt", "r")
for line in file:
  # Store each instruction as a tuple; e.g., ('N', 37)
  instructions.append((line.strip()[0], int(line.strip()[1:])))

steps = {'N': 0, 'E': 0, 'S': 0, 'W': 0}  # no. of steps taken in each direction by ship
directions = ['N', 'E', 'S', 'W']
waypoint_coords = {'N': 1, 'E': 10, 'S': 0, 'W': 0}  # initial waypoint coords relative to ship

def calc_waypoint_coords(instruction):
  global direction_index_1, direction_index_2  # current waypoint direction
  waypoint_coords[instruction[0]] += instruction[1]
  if waypoint_coords['E'] - waypoint_coords['W'] >= 0:
    waypoint_coords['E'] = waypoint_coords['E'] - waypoint_coords['W']
    waypoint_coords['W'] = 0
    direction_index_1 = 1  # set waypoint to have E component
  elif waypoint_coords['E'] - waypoint_coords['W'] < 0:
    waypoint_coords['W'] = waypoint_coords['W'] - waypoint_coords['E']
    waypoint_coords['E'] = 0
    direction_index_1 = 3  # set waypoint to have W component
  if waypoint_coords['N'] - waypoint_coords['S'] >= 0:
    waypoint_coords['N'] = waypoint_coords['N'] - waypoint_coords['S']
    waypoint_coords['S'] = 0
    direction_index_2 = 0  # set waypoint to have N component
  elif waypoint_coords['N'] - waypoint_coords['S'] < 0:
    waypoint_coords['S'] = waypoint_coords['S'] - waypoint_coords['N']
    waypoint_coords['N'] = 0
    direction_index_2 = 2  # set waypoint to have S component

def rotate_waypoint(instruction):
  direction = instruction[0]
  degrees = instruction[1]
  global direction_index_1, direction_index_2  # current waypoint direction
  if direction == 'L':
    new_direction_index_1 = (direction_index_1 - int(degrees / 90)) % 4
    new_direction_index_2 = (direction_index_2 - int(degrees / 90)) % 4
  else:  # 'clockwise'
    new_direction_index_1 = (direction_index_1 + int(degrees / 90)) % 4
    new_direction_index_2 = (direction_index_2 + int(degrees / 90)) % 4
  # Store previous waypoint units before overwriting with new ones:
  last_waypoint_units_1 = waypoint_coords[directions[direction_index_1]]
  last_waypoint_units_2 = waypoint_coords[directions[direction_index_2]]
  # Set units in all directions to 0
  waypoint_coords[directions[direction_index_1]] = 0
  waypoint_coords[directions[direction_index_2]] = 0
  # Fill waypoint units for new directions
  waypoint_coords[directions[new_direction_index_1]] = last_waypoint_units_1
  waypoint_coords[directions[new_direction_index_2]] = last_waypoint_units_2

  direction_index_1 = new_direction_index_1
  direction_index_2 = new_direction_index_2


for instruction in instructions:
  if instruction[0] == 'F':  # move ship to waypoint specified number of times 
    for key in waypoint_coords.keys():
      steps[key] += waypoint_coords[key] * instruction[1]
  elif instruction[0] == 'L' or instruction[0] == 'R':  # rotate waypoint around ship
    rotate_waypoint(instruction)
  else:  # move waypoint
    calc_waypoint_coords(instruction)

manhattan_dist = abs(steps['N'] - steps['S']) + abs(steps['E'] - steps['W'])
print("Manhattan distance = ", manhattan_dist)