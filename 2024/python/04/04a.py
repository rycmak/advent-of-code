xmasArray = []

with open("input.txt") as f:
  for line in f:
    xmasArray.append(list(line.strip()))

numRows = len(xmasArray)
numCols = len(xmasArray[0])
steps = [(0,1), (0,-1), (1,-1), (1,0), (1,1), (-1,-1), (-1,0), (-1,1)]

def numXmas(i, j):
  numXmas = 0
  xmasSubstring = "MAS"
  for step in steps:
    for k, char in enumerate(xmasSubstring):
      k = k + 1
      nextStep = tuple(k * s for s in step)
      nextPosition = getNextPosition(i, j, nextStep)
      if isInArray(nextPosition) and xmasArray[nextPosition[0]][nextPosition[1]] == char:
        if char == 'S':
          numXmas += 1
          break
        continue
      else:
        break
  return numXmas

def getNextPosition(i, j, nextStep):
  return tuple(map(lambda a, b: a + b, (i,j), nextStep))

def isInArray(position):
  return position[0] >= 0 and position[0] < numCols \
     and position[1] >= 0 and position[1] < numRows

count = 0

for i in range(numRows):
  for j, char in enumerate(xmasArray[i]):
    if char == 'X':
      count += numXmas(i, j)

print(count)