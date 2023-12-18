file = open("input.txt")

network = {}

count = 0
for line in file:
  if count == 0:
    left_right = list(line.strip())
    directions = [0 if x == 'L' else 1 for x in left_right]
  elif count >= 2:
    node = line.split('=')[0].strip()
    network[node] = []
    network[node].append(line.split('=')[1].split(',')[0].strip()[1:])
    network[node].append(line.split('=')[1].split(',')[1].strip()[0:-1])
  count += 1

done = False
current_node = 'AAA'
num_steps = 0

while not done:
  for direction in directions:
    num_steps += 1
    current_node = network[current_node][direction]
    if current_node == 'ZZZ':
      print(f"Number of steps = {num_steps}")
      done = True
      break
