file = open("input.txt", 'r')

positions = file.readline()
positions = [int(i) for i in positions.split(",")]
position_range = list(range(min(positions), max(positions) + 1))

min_fuel = None
for p in position_range:
  # print(f"p = {p}")
  diffs = [abs(p - x) for x in positions]
  # Formula for 1 + 2 + ... + n = n * (n + 1) / 2
  fuel = [d * (d + 1) / 2 for d in diffs]
  if min_fuel == None:
    min_fuel = sum(fuel)
  else:
    min_fuel = min(min_fuel, sum(fuel))
  print(f"fuel = {sum(fuel)}")

print(f"Min fuels = {min_fuel}")