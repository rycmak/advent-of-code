file = open("input.txt", "r")

depths = []
previous = None
for depth in file:
  depths.append(int(depth))

count = 0
previous = None
for i in range(len(depths) - 2):
  current = sum(depths[i:i+3])
  if previous is not None:
    if current > previous:
      count += 1
  previous = current

file.close()

print(count)