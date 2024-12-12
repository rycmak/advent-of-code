with open("input.txt") as f:
  input = f.readline()

input = [int(x) for x in list(input)]

disk = []

fileId = 0

for i in range(len(input)):
  if i % 2 == 0:  # file block
    disk.extend([fileId] * input[i])
    fileId += 1
  else: # space block
    disk.extend(['.'] * input[i])

numSpaces = disk.count('.')

for i in range(numSpaces):
  if disk[len(disk)-1-i] != '.':
    s = disk.index('.')  # first space index in disk
    disk[s] = disk[len(disk)-1-i]
    disk[len(disk)-1-i] = '.'

checksum = 0
for i in range(len(disk) - numSpaces):
  checksum += i * disk[i]

print(checksum)