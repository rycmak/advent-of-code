file = open("input.txt", 'r')

positions = file.readline()
positions = [int(i) for i in positions.split(",")]

min_fuel = None
for p in positions:
  fuel = [abs(p - x) for x in positions]
  if min_fuel == None:
    min_fuel = sum(fuel)
  else:
    min_fuel = min(min_fuel, sum(fuel))

print(f"Min fuels = {min_fuel}")