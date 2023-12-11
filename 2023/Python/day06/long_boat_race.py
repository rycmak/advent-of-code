import numpy as np

file = open("input.txt")

for line in file:
  if line.split(':')[0] == "Time":
    time = ""
    times = list(line.split(':')[1].strip().split())
    for t in times:
      time += t
    time = int(time)
    
  else:
    dist = ""
    dists = list(line.split(':')[1].strip().split())
    for d in dists:
      dist += d
    dist = int(dist)

margin = 0

# The long way -- do the loop
# for t in range(time):
#   print(t)
#   d = t * (time - t)
#   if d > dist:
#     margin += 1

# The short way -- solve quadratic equation
# t * (time - t) > dist
# t^2 - t*time + dist < 0
# t = (time +/- sqrt(time^2 - 4*dist)) / 2

t1 = np.ceil((time - np.sqrt(time**2 - 4*dist)) / 2)
t2 = np.floor((time + np.sqrt(time**2 - 4*dist)) / 2)

margin = (t2 - t1) + 1

print(f"Margin = {margin}")