# Pseudo code:
# assume original map is narrow (has more rows than columns)
# transform map to array
# no. of steps downwards = no. of rows
# no. of map copies = ceil((no. of steps downwards - 1) * 3 / no. of columns)
# start at (i, j) = (0, 0)
# move across to (i + 3, j + 1)
# if element == '#', increment num_trees

# Let's try to do this without using numpy ;-p
# NB: If using numpy, could make use of concatenate, hstack, etc.
# to stack (repeat) copies of original map to the right.
# But without numpy, we'll try to use zip instead...


file = open("input.txt", "r")
map_original = []  # will be a 2D array containing original map
num_rows = 0
for line in file:
  num_rows += 1
  map_original.append(list(line.strip()))

map_full = map_original  # map_full will be a 2D array containing full (repeated) map
num_copies = int((num_rows - 1) * 3 / len(map_original[0])) + 1  # if using numpy, use np.ceil instead of +1
for i in range(num_copies):
  # append map_full with copy of map_original
  map_full = [(map_full + map_original) for map_full, map_original in zip(map_full, map_original)]


# start at position (0, 0)
column = 0
row = 0
num_trees = 0
while row < (num_rows - 1):
  column += 3
  row += 1
  if map_full[row][column] == "#":
    num_trees += 1

print("num_trees", num_trees)
