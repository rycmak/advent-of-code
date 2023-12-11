file = open("input.txt")

for line in file:
  if line.split(':')[0] == "Time":
    times = list(line.split(':')[1].strip().split())
    times = [int(time) for time in times]
  else:
    dists = list(line.split(':')[1].strip().split())
    dists = [int(dist) for dist in dists]

margins = 1

for i, time in enumerate(times):
  margin = 0
  for t in range(time):
    dist = t * (time - t)
    if dist > dists[i]:
      margin += 1
  margins *= margin

print(f"Margins = {margins}")
