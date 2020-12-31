# Take first 7 chars and string translate F -> 0, B-> 1
# Convert binary to decimal: int('binary_number', 2)

# Take last 3 chars and string translate L -> 0, R-> 1


# Convert given string to row number in decimal
# Using str.translate() instead of regex substitution as apparently former is faster:
# https://docs.python.org/3/howto/regex.html
def decimal_row(binary_string):
  translation = {70: '0', 66: '1'}  # in unicode, 'F' = 70, 'B' = 66
  return int(binary_string.translate(translation), 2)

# Convert given string to column number in decimal
def decimal_column(binary_string):
  translation = {76: '0', 82: '1'}  # in unicode, 'L' = 76, 'R' = 82
  return int(binary_string.translate(translation), 2)


# Run script
seat_ids = []

file = open("input.txt", "r")
for line in file:
  binary_id = line.strip()
  row = decimal_row(binary_id[:-3])
  column = decimal_column(binary_id[-3:])
  seat_id = row * 8 + column
  seat_ids.append(seat_id)

# Use set difference to find missing seat_id within sequence
# Idea from https://stackoverflow.com/a/16974075/2108880
seat_ids = sorted(seat_ids)
lowest = seat_ids[0]
highest = seat_ids[-1]
print("Missing seat ID: ", set(range(lowest, highest + 1)).difference(seat_ids))