input = []
inputCopy = []

with open("input.txt") as f:
  row = 0
  for line in f:
    if line.find('^') != -1:
      currentPos = (row, line.find('^'))
    input.append(list(line.strip()))
    inputCopy.append(list(line.strip()))
    row += 1

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

count = 0

for i in range(numRows):
  for j in range(numCols):
    if inputCopy[i][j] == 'X':
      count += 1

print(count)
