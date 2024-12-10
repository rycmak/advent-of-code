import copy

input = []
inputCopy = []
obstaclePositions = []

with open("input.txt") as f:
  row = 0
  for line in f:
    if line.find('^') != -1:
      originalPos = (row, line.find('^'))
    input.append(list(line.strip()))
    inputCopy.append(list(line.strip()))
    row += 1

currentPos = originalPos

numRows = len(input)
numCols = len(input[0])
inputCopy[currentPos[0]][currentPos[1]] = 'X'


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
currentDirectionIndex = 0  # current direction to move is (-1, 0)

def getNextDirectionIndex():
  global currentDirectionIndex
  nextDirectionIndex = (currentDirectionIndex + 1) % 4  # there are 4 possible directions
  currentDirectionIndex = nextDirectionIndex
  return currentDirectionIndex

def getNextPos(currentPos, currentDirection):
  return tuple(map(lambda x, y: x + y, currentPos, currentDirection))

def isValid(nextPos):
  if nextPos[0] >=0 and nextPos[0] < numRows \
    and nextPos[1] >= 0 and nextPos[1] < numCols:
    return True
  return False


nextPos = getNextPos(currentPos, directions[currentDirectionIndex])

while isValid(nextPos):
  if input[nextPos[0]][nextPos[1]] == '.' or input[nextPos[0]][nextPos[1]] == '^':
    currentPos = nextPos
    inputCopy[currentPos[0]][currentPos[1]] = 'X'
    nextPos = getNextPos(currentPos, directions[currentDirectionIndex])
  elif input[nextPos[0]][nextPos[1]] == '#':
    nextPos = getNextPos(currentPos, directions[getNextDirectionIndex()])
  

for i in range(numRows):
  for j in range(numCols):
    if inputCopy[i][j] == 'X':
      if i == originalPos[0] and j == originalPos[1]:
        continue
      obstaclePositions.append((i, j))


# Now we have found all possible positions to place obstacles
# Reset all position and direction variable
# Traverse the map again, each time with a new obstacle in place

count = 0
numObstacle = 0

for obstaclePos in obstaclePositions:
  numObstacle += 1
  print(f"numObstacle = {numObstacle}")
  currentPos = originalPos
  currentDirectionIndex = 0  # current direction to move is (-1, 0)
  inputCopy = copy.deepcopy(input)
  inputCopy[obstaclePos[0]][obstaclePos[1]] = '#'
  traversed = [[set() for i in range(numCols)] for j in range(numRows)]
  traversed[currentPos[0]][currentPos[1]].add(currentDirectionIndex)
  nextPos = getNextPos(currentPos, directions[currentDirectionIndex])
  while isValid(nextPos):
    # Check if nextPos has been traversed with current direction before
    if currentDirectionIndex in traversed[nextPos[0]][nextPos[1]]:
      count += 1
      break
    if inputCopy[nextPos[0]][nextPos[1]] == '.' or inputCopy[nextPos[0]][nextPos[1]] == '^':
      currentPos = nextPos
      traversed[currentPos[0]][currentPos[1]].add(currentDirectionIndex)
      nextPos = getNextPos(currentPos, directions[currentDirectionIndex])
    elif inputCopy[nextPos[0]][nextPos[1]] == '#':
      nextPos = getNextPos(currentPos, directions[getNextDirectionIndex()])

print(count)


