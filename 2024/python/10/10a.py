input = []

with open("input.txt") as f:
  for line in f:
    input.append([int(x) for x in list(line.strip())])

numRows = len(input)
numCols = len(input[0])

trailheads = {}

def isValid(pos):
  return pos[0] >= 0 and pos[0] < numRows and pos[1] >= 0 and pos[1] < numCols

def findTrail(start, currentPos, currentLevel):
  if currentLevel == 9:
    trailheads[start].add(currentPos)
    return
  nextPos = [(currentPos[0]-1, currentPos[1]),\
             (currentPos[0]+1, currentPos[1]),\
             (currentPos[0], currentPos[1]-1),\
             (currentPos[0], currentPos[1]+1)]
  for pos in nextPos:
    if isValid(pos) and input[pos[0]][pos[1]] == currentLevel + 1:
      findTrail(start, pos, currentLevel + 1)    


for i in range(numRows):
  for j in range(numCols):
    if input[i][j] == 0:
      trailheads[(i,j)] = set()
      findTrail(start=(i, j), currentPos=(i, j), currentLevel=0)

scores = 0
for trail in trailheads.keys():
  scores += len(trailheads[trail])

print(scores)