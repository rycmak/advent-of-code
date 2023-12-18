import numpy as np

file = open("input.txt")

network = {}
a_nodes = set()
z_nodes = set()

count = 0
for line in file:
  if count == 0:
    left_right = list(line.strip())
    directions = [0 if x == 'L' else 1 for x in left_right]
  elif count >= 2:
    node = line.split('=')[0].strip()
    if node[2] == 'A':
      a_nodes.add(node)
    if node[2] == 'Z':
      z_nodes.add(node)
    network[node] = []
    network[node].append(line.split('=')[1].split(',')[0].strip()[1:])
    network[node].append(line.split('=')[1].split(',')[1].strip()[0:-1])
  count += 1

node_steps = {}  # dict containing each node ending in 'A' and num steps to reach node ending in 'Z'
for node in a_nodes:
  done = False
  num_steps = 0
  current_node = node
  while not done:
    for direction in directions:
      num_steps += 1
      next_node = network[current_node][direction]
      if next_node in z_nodes:  # reached a node ending in 'Z'
        node_steps[node] = num_steps
        done = True  # assume we will not reach a different 'Z' node if we continued
        break
      current_node = next_node

print(f"Number of steps = {np.lcm.reduce(list(node_steps.values()))}")
