from collections import defaultdict

file = open("input.txt", 'r')

connections_dict = defaultdict(list)

for line in file:
  line = line.replace('\n', '').split('-')
  connections_dict[line[0]].append(line[1])
  connections_dict[line[1]].append(line[0])

# For example 1, connections_dict looks like this:
# {'start': ['A', 'b'], 'A': ['start', 'c', 'b', 'end'], 'b': ['start', 'A', 'd', 'end'], 
# 'c': ['A'], 'd': ['b'], 'end': ['A', 'b']}

all_paths = []

def find_path(point, path):
  global all_paths
  current_path = path.copy()
  if point == "end":
    current_path.append("end")
    all_paths.append(current_path)
  elif (point == point.lower() and point not in current_path) or (point == point.upper()):
    current_path.append(point)
    for x in connections_dict[point]:
      find_path(x, current_path)

for x in connections_dict["start"]:
  find_path(x, ["start"])

print(f"Number of paths = {len(all_paths)}")
  