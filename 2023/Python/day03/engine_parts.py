import re

file = open("input.txt")

engine_map = []
numbers_coords = []  # (x, y, length, num) of each number on map
symbols_coords = []  # (x, y) of each symbol on map
count = 0

for line in file:
  line = line.strip()
  engine_map.append(line)
  for symbol in re.finditer("[^\d.]", line):  # find any symbols in line
    symbols_coords.append((count, symbol.start()))
  for num in re.finditer("\d{1,3}", line):  # find any 1- to 3-digit numbers in line
    numbers_coords.append((count, num.start(), num.end()-num.start(), int(num.group())))
  count += 1

map_width = len(engine_map[0])
map_height = len(engine_map)

def is_symbol_adjacent(num_coord):
  y_start = num_coord[1] - 1 if num_coord[1] > 0 else 0
  y_end = num_coord[1] + num_coord[2] if num_coord[1] + num_coord[2] < map_width - 1 else map_width - 1
  x_start = num_coord[0] - 1 if num_coord[0] > 0 else 0
  x_end = num_coord[0] + 1 if num_coord[0] + 1 < map_height - 1 else map_height - 1
  for y in range(y_start, y_end + 1):
    for x in range(x_start, x_end + 1):
      if (x, y) in symbols_coords:
        return True  # assume each engine part number is in contact with at most one symbol

engine_part_nums = []

for num_coord in numbers_coords:
  if is_symbol_adjacent(num_coord):
    engine_part_nums.append(num_coord[3])

print(f"Sum of engine part numbers = {sum(engine_part_nums)}"p)