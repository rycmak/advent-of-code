import numpy as np

file = open("input.txt", 'r')
grid_max = 4000000

sensors = []
beacons = []
distances = []
coverage = {}  # dict with rows as keys, and column ranges with no beacons as values

for line in file:
  sensor_x = int(line.split(":")[0].split("at")[1].split(",")[0].split("=")[1].strip())
  sensor_y = int(line.split(":")[0].split("at")[1].split(",")[1].split("=")[1].strip())
  sensors.append((sensor_x, sensor_y))

  beacon_x = int(line.split(":")[1].split("at")[1].split(",")[0].split("=")[1].strip())
  beacon_y = int(line.split(":")[1].split("at")[1].split(",")[1].split("=")[1].strip())
  beacons.append((beacon_x, beacon_y))

  distances.append(abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y))


def add_coverage(row_num, covered_range):
  coverage[row_num].append(covered_range)
  new_row_coverage = []
  for covered_segment in sorted(coverage[row_num], key=lambda pair: pair[0]):
    if new_row_coverage and new_row_coverage[-1][-1] + 1 >= covered_segment[0]:
      new_row_coverage[-1] = range(new_row_coverage[-1][0], 
                                    max(new_row_coverage[-1][-1], covered_segment[-1]) + 1)
    else:
      new_row_coverage.append(covered_segment)
  coverage[row_num] = new_row_coverage


for i in range(len(sensors)):
  print(f"i = {i}")
  for y in range(sensors[i][1]-distances[i], sensors[i][1]+distances[i]+1):
    covered_range = range(sensors[i][0]-(distances[i]-abs(sensors[i][1]-y)), 
                            sensors[i][0]+(distances[i]-abs(sensors[i][1]-y))+1)
    if y in coverage:
      add_coverage(y, covered_range)
    else:
      coverage[y] = [covered_range]


distress_beacon_row_num = [row_num for row_num in coverage.keys() 
                  if (len(coverage[row_num]) > 1 and row_num >= 0 and row_num <= grid_max)]
if len(distress_beacon_row_num) == 1:
  distress_beacon_row_num = distress_beacon_row_num[0]
  covered_ranges = coverage[distress_beacon_row_num]
  if len(covered_ranges) == 2:
    distress_beacon_col_num = covered_ranges[0][-1] + 1
    tuning_freq = distress_beacon_col_num * 4000000 + distress_beacon_row_num
    print(f"Tuning frequency of distress beacon = {tuning_freq}")
  else:
    print("Oh no, something is not right as there seems to be more than one column "\
        "that could contain the distress beacon!")
else:
    print("Oh no, something is not right as there seems to be more than one row "\
        "that could contain the distress beacon!")