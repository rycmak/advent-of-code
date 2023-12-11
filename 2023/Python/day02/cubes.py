file = open("input.txt")

bag = {
  "red": 12,
  "green": 13,
  "blue": 14
}

possible_ids = []

for game in file:
  game = game.strip()
  id = int(game.split(':')[0][5:])
  subsets = game.split(':')[1].split(';')
  impossible = False
  for subset in subsets:
    if impossible == True:
      break
    cubes = subset.strip().split(',')
    for cube in cubes:
      if impossible == True:
        break
      number = int(cube.strip().split()[0])
      colour = cube.strip().split()[1]
      if number > bag[colour]:
        impossible = True
  if impossible == False:
    possible_ids.append(id)

print(f"Sum of possibe game IDs = {sum(possible_ids)}")
