import numpy as np

file = open("input.txt", 'r')
row_of_interest = 2000000

sensors = []
beacons = []
distances = []

for line in file:
  sensor_x = int(line.split(":")[0].split("at")[1].split(",")[0].split("=")[1].strip())
  sensor_y = int(line.split(":")[0].split("at")[1].split(",")[1].split("=")[1].strip())
  sensors.append((sensor_x, sensor_y))

  beacon_x = int(line.split(":")[1].split("at")[1].split(",")[0].split("=")[1].strip())
  beacon_y = int(line.split(":")[1].split("at")[1].split(",")[1].split("=")[1].strip())
  beacons.append((beacon_x, beacon_y))

  distances.append(abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y))

no_beacons = []

for i in range(len(sensors)):
  for y in range(sensors[i][1]-distances[i], sensors[i][1]+distances[i]+1):
    if y == row_of_interest:
      for x in range(sensors[i][0]-(distances[i]-abs(sensors[i][1]-y)), 
                      sensors[i][0]+(distances[i]-abs(sensors[i][1]-y))+1):
        no_beacons.append((x, y))

no_beacons_in_row = [pos for pos in no_beacons if pos[1] == row_of_interest]
num_beacons_in_row = len(set([pos for pos in beacons if pos[1] == row_of_interest]))

print(f"Number of positions that cannot contain a beacon = {len(set(no_beacons_in_row)) - num_beacons_in_row}")
