import re

with open("input.txt") as f:
  input = f.readline()

input = [int(x) for x in list(input)]

disk = []
fileBlocks = []  # [(fileId, startIndex, blockSize)]

fileId = 0
startIndex = 0

for i in range(len(input)):
  if i % 2 == 0:  # file block
    disk.extend([fileId] * input[i])
    fileBlocks.append((fileId, startIndex, input[i]))
    fileId += 1
  else: # space block
    disk.extend('.' * input[i])
  startIndex += input[i]

fileBlocks.reverse()

for n, fileBlock in enumerate(fileBlocks):
  print(n)
  fileId = fileBlock[0]
  fileStartIndex = fileBlock[1]
  fileSize = fileBlock[2]
  for i in range(len(disk)):
    if i < fileStartIndex and all([disk[i+j] == '.' for j in range(fileSize)]):  # enough space
      for k in range(fileSize):
        disk[i+k] = fileId
        disk[fileStartIndex+k] = '.'
      break

checksum = 0

for i in range(len(disk)):
  if disk[i] != '.':
    checksum += i * disk[i]

print(checksum)
