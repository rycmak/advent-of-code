file = open("input.txt", "r")

aim = 0
horizontal = 0
depth = 0

for direction in file:
  if direction.split(" ")[0] == "forward":
    horizontal += (int)(direction.split(" ")[1])
    depth += aim * (int)(direction.split(" ")[1])
  elif direction.split(" ")[0] == "down":
    aim += (int)(direction.split(" ")[1])
  elif direction.split(" ")[0] == "up":
    aim -= (int)(direction.split(" ")[1])

print(f"horizontal * depth = {horizontal * depth}")