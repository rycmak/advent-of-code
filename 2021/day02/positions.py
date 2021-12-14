file = open("input.txt", "r")

horizontal = 0
depth = 0

for direction in file:
  if direction.split(" ")[0] == "forward":
    horizontal += (int)(direction.split(" ")[1])
  elif direction.split(" ")[0] == "down":
    depth += (int)(direction.split(" ")[1])
  elif direction.split(" ")[0] == "up":
    depth -= (int)(direction.split(" ")[1])

print(f"horizontal = {horizontal}\ndepth = {depth}")
print(f"horizontal * depth = {horizontal * depth}")
