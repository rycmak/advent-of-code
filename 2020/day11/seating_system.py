# Given seating map with marked with empty seats 'L' and floor '.',
# find final state of map by iterating with following rules:
# 1. If a seat is empty (L) and there are no occupied seats adjacent to it, 
#    the seat becomes occupied.
# 2. If a seat is occupied (#) and four or more seats adjacent to it are also occupied, 
#    the seat becomes empty.
# 3. Otherwise, the seat's state does not change.

import copy

seats = []  # list of lists; each list is a row
file = open("input.txt", "r")
for line in file:
  seats.append(list(line.strip()))

reference = copy.deepcopy(seats)
num_rows = len(reference)
num_cols = len(reference[0])

def find_adjacent_seats(row, col):
  if row == 0:
    if col == 0:  # top left corner
      return [(row, col + 1), (row + 1, col + 1), (row + 1, col)]
    elif col == (num_cols - 1):  # top right corner
      return [(row, col - 1), (row + 1, col - 1), (row + 1, col)]
    else:  # top row non-corner
      return [(row, col - 1), (row, col + 1), (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
  elif row == (num_rows - 1) : 
    if col == 0:  # bottom left corner
      return [(row, col + 1), (row - 1, col + 1), (row - 1, col)]
    elif col == (num_cols - 1):  # bottom right corner
      return [(row, col - 1), (row - 1, col - 1), (row - 1, col)]
    else:  # bottom row non-corner
      return [(row, col - 1), (row, col + 1), (row - 1, col - 1), (row - 1, col), (row - 1, col + 1)]
  elif col == 0:  # left edge
    return [(row - 1, col), (row + 1, col), (row - 1, col + 1), (row, col + 1), (row + 1, col + 1)]
  elif col == (num_cols - 1):  # right edge
    return [(row - 1, col), (row + 1, col), (row - 1, col - 1), (row, col - 1), (row + 1, col - 1)]
  else:
    return [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1), 
            (row, col - 1), (row, col + 1), (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
  

def check_adjacent_empty(row, col):
  # print("CHECK_ADJ_EMPTY: ", reference[row][col])
  adjacent_seats = find_adjacent_seats(row, col)
  if all([reference[seat[0]][seat[1]] != '#' for seat in adjacent_seats]):
    return '#'
  else:
    return 'L'

def check_adjacent_occupied(row, col):
  # print("CHECK_ADJ_OCC: ", reference[row][col])
  adjacent_seats = find_adjacent_seats(row, col)
  if sum([reference[seat[0]][seat[1]] == '#' for seat in adjacent_seats]) >= 4:
    return 'L'
  else:
    return '#'


# Iterations
seats = []
stabilized = False
num_iterations = 0
while stabilized == False:
  num_iterations += 1
  seats = []
  for row in range(num_rows):
    seats_row = []
    for col in range(num_cols):
      if reference[row][col] == 'L':
        seats_row.append(check_adjacent_empty(row, col))
      elif reference[row][col] == '#':
        seats_row.append(check_adjacent_occupied(row, col))
      else:
        seats_row.append(reference[row][col])
    # print("SEATS_ROW: ", seats_row)
    seats.append(seats_row)
  # After all rows have been processed, check if anything has changed:
  stabilized = seats == reference
  if stabilized:
    print("No. of iterations: ", num_iterations)
    print("No. of occupied seats = ", sum(seat.count('#') for seat in seats))
    break
  else:
    reference = copy.deepcopy(seats)
  

