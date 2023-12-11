import re

file = open("input.txt")

# Find coords of each symbol *, and store in dict.
# Find all coords of numbers.
# For each number, find whether it is adjacent to *.
# Assume each number is adjacent to at most one *.
# Record number against corresponding * in dict.
# At the end, for each * in dict, if it has exactly 2 adjacent numbers, calc gear ratio.

engine_map = []
numbers_coords = []  # (x, y, length, num) of each number on map
star_with_adj_nums = {}
gear_ratios = []
count = 0

for line in file:
  line = line.strip()
  engine_map.append(line)
  for star in re.finditer("\*", line):  # find any stars in line
    star_with_adj_nums[(count, star.start())] = []
  for num in re.finditer("\d{1,3}", line):  # find any 1- to 3-digit numbers in line
    numbers_coords.append((count, num.start(), num.end()-num.start(), int(num.group())))
  count += 1

star_coords = list(star_with_adj_nums.keys())

map_width = len(engine_map[0])
map_height = len(engine_map)

def get_adj_star(num_coord):
  y_start = num_coord[1] - 1 if num_coord[1] > 0 else 0
  y_end = num_coord[1] + num_coord[2] if num_coord[1] + num_coord[2] < map_width - 1 else map_width - 1
  x_start = num_coord[0] - 1 if num_coord[0] > 0 else 0
  x_end = num_coord[0] + 1 if num_coord[0] + 1 < map_height - 1 else map_height - 1
  for y in range(y_start, y_end + 1):
    for x in range(x_start, x_end + 1):
      if (x, y) in star_coords:
        return (x, y)

for num_coord in numbers_coords:
  star_coord = get_adj_star(num_coord)
  if star_coord:
    star_with_adj_nums[star_coord].append(num_coord[3])

for star in star_with_adj_nums:
  if len(star_with_adj_nums.get(star)) == 2:
    gear_ratio = star_with_adj_nums[star][0] * star_with_adj_nums[star][1]
    gear_ratios.append(gear_ratio)

print(f"Sum of gear ratios = {sum(gear_ratios)}")