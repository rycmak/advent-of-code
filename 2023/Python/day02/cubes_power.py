file = open("input.txt")

powers = []

for game in file:
  min_colours = {
  "red": 0,
  "green": 0,
  "blue": 0
  }
  subsets = game.strip().split(':')[1].split(';')
  for subset in subsets:
    cubes = subset.strip().split(',')
    for cube in cubes:
      number = int(cube.strip().split()[0])
      colour = cube.strip().split()[1]
      min_colours[colour] = max(min_colours[colour], number)
  power = min_colours["red"] * min_colours["green"] * min_colours["blue"]
  powers.append(power)

print(sum(powers))