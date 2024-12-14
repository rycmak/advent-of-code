from itertools import combinations

input = []

with open("input.txt") as f:
  for line in f:
    input.append(list(line.strip()))

numRows = len(input)
numCols = len(input[0])

# Record positions of antennas
antennas = {}
for i in range(numRows):
  for j in range(numCols):
    x = input[i][j]
    if x != '.':
      if x in antennas.keys():
        antennas[x].append((i, j))
      else:
        antennas[x] = [(i, j)]

nodes = set()

def isPositionInMap(x, y):
  return x >= 0 and x < numRows and y >= 0 and y < numCols

def setNodes(key, ant1, ant2):
  dist = (abs(ant1[0] - ant2[0]), abs(ant1[1] - ant2[1]))
  if ant1[0] > ant2[0] and ant1[1] > ant2[1]:
    if isPositionInMap((ant1[0] + dist[0]), (ant1[1] + dist[1])):
      nodes.add(((ant1[0] + dist[0]), (ant1[1] + dist[1])))
    if isPositionInMap((ant2[0] - dist[0]), (ant2[1] - dist[1])):
      nodes.add(((ant2[0] - dist[0]), (ant2[1] - dist[1])))
  elif ant1[0] > ant2[0] and ant1[1] < ant2[1]:
    if isPositionInMap((ant1[0] + dist[0]), (ant1[1] - dist[1])):
      nodes.add(((ant1[0] + dist[0]), (ant1[1] - dist[1])))
    if isPositionInMap((ant2[0] - dist[0]), (ant2[1] + dist[1])):
      nodes.add(((ant2[0] - dist[0]), (ant2[1] + dist[1])))
  elif ant1[0] < ant2[0] and ant1[1] < ant2[1]:
    if isPositionInMap((ant1[0] - dist[0]), (ant1[1] - dist[1])):
      nodes.add(((ant1[0] - dist[0]), (ant1[1] - dist[1])))
    if isPositionInMap((ant2[0] + dist[0]), (ant2[1] + dist[1])):
      nodes.add(((ant2[0] + dist[0]), (ant2[1] + dist[1])))
  elif ant1[0] < ant2[0] and ant1[1] > ant2[1]:
    if isPositionInMap((ant1[0] - dist[0]), (ant1[1] + dist[1])):
      nodes.add(((ant1[0] - dist[0]), (ant1[1] + dist[1])))
    if isPositionInMap((ant2[0] + dist[0]), (ant2[1] - dist[1])):
      nodes.add(((ant2[0] + dist[0]), (ant2[1] - dist[1])))
  
for key in antennas.keys():
  combs = list(combinations(antennas[key], 2))  # pair combinations
  for comb in combs:
    ant1, ant2 = comb[0], comb[1]
    setNodes(key, ant1, ant2)

print(len(nodes))
