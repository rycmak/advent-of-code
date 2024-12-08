xmasArray = []

with open("input.txt") as f:
  for line in f:
    xmasArray.append(list(line.strip()))

numRows = len(xmasArray)
numCols = len(xmasArray[0])
steps = [(0,1), (0,-1), (1,-1), (1,0), (1,1), (-1,-1), (-1,0), (-1,1)]

def isXmas(i, j):
  if i > 0 and i < (numRows - 1) and j > 0 and j < (numCols - 1):
    if xmasArray[i-1][j-1] == 'M' and xmasArray[i+1][j+1] == 'S' and xmasArray[i-1][j+1] == 'M' and xmasArray[i+1][j-1] == 'S' \
    or xmasArray[i-1][j-1] == 'M' and xmasArray[i+1][j+1] == 'S' and xmasArray[i-1][j+1] == 'S' and xmasArray[i+1][j-1] == 'M' \
    or xmasArray[i-1][j-1] == 'S' and xmasArray[i+1][j+1] == 'M' and xmasArray[i-1][j+1] == 'M' and xmasArray[i+1][j-1] == 'S' \
    or xmasArray[i-1][j-1] == 'S' and xmasArray[i+1][j+1] == 'M' and xmasArray[i-1][j+1] == 'S' and xmasArray[i+1][j-1] == 'M':
      return True
  else:
    return False
 
count = 0

for i in range(numRows):
  for j, char in enumerate(xmasArray[i]):
    if char == 'A' and isXmas(i, j):
      count += 1

print(count)