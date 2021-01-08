# Instead of checking whether immediate adjacent seats are occupied,
# now should check if an empty seat does not "see" any occupied seats in all eight directions
# before becoming occupied;
# and an occupied seat should "see" 5 or more occupied seats before being vacant.

# Below is a highly-inefficient solution,
# which, given a seat, finds all seats in each of the 8 directions,
# then takes the first in each direction as the visible seat that it "sees" in that direction.
# A more efficient solution would just find the first visible seat in each direction.

import copy

seats = []  # list of lists; each list is a row
file = open("input.txt", "r")
for line in file:
  seats.append(list(line.strip()))

reference = copy.deepcopy(seats)
num_rows = len(reference)
num_cols = len(reference[0])

def find_visible_seats(row, col):
  visible_seats = [next(iter([(row, col - i) for i in range(1, col + 1) if reference[row][col - i] != '.']), None)] + \
                  [next(iter([(row, col + i) for i in range(1, num_cols - col) if reference[row][col + i] != '.']), None)] + \
                  [next(iter([(row - i, col) for i in range(1, row + 1) if reference[row - i][col] != '.']), None)] + \
                  [next(iter([(row + i, col) for i in range(1, num_rows - row) if reference[row + i][col] != '.']), None)] + \
                  [next(iter([(row - i, col - i) for i in range(1, min(row + 1, col + 1)) if reference[row - i][col - i] != '.']), None)] + \
                  [next(iter([(row - i, col + i) for i in range(1, min(row + 1, num_cols - col)) if reference[row - i][col + i] != '.']), None)] + \
                  [next(iter([(row + i, col - i) for i in range(1, min(num_rows - row, col + 1)) if reference[row + i][col - i] != '.']), None)] + \
                  [next(iter([(row + i, col + i) for i in range(1, min(num_rows - row, num_cols - col)) if reference[row + i][col + i] != '.']), None)]
  return visible_seats

def check_empty_visible(row, col):
  visible_seats = find_visible_seats(row, col)
  if all([reference[seat[0]][seat[1]] != '#' for seat in visible_seats if seat is not None]):
    return '#'
  else:
    return 'L'

def check_occupied_visible(row, col):
  visible_seats = find_visible_seats(row, col)
  visible_seats = find_visible_seats(row, col)
  if sum([reference[seat[0]][seat[1]] == '#' for seat in visible_seats if seat is not None]) >= 5:
    return 'L'
  else:
    return '#'

# Iterations
stabilized = False
num_iterations = 0
while stabilized == False:
  num_iterations += 1
  seats = []
  for row in range(num_rows):
    seats_row = []
    for col in range(num_cols):
      if reference[row][col] == 'L':
        seats_row.append(check_empty_visible(row, col))
      elif reference[row][col] == '#':
        seats_row.append(check_occupied_visible(row, col))
      else:
        seats_row.append(reference[row][col])
    seats.append(seats_row)
  # After all rows have been processed, check if anything has changed:
  stabilized = seats == reference
  if stabilized:
    print("No. of iterations: ", num_iterations)
    print("No. of occupied seats = ", sum(seat.count('#') for seat in seats))
    break
  else:
    reference = copy.deepcopy(seats)
