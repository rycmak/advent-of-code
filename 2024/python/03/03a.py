import re

input = ""

with open("input.txt") as f:
  for line in f:
    input += line

matches = re.findall(r'mul\((\d+,\d+)\)', input)

sum = 0

for match in matches:
  sum += int(match.split(',')[0]) * int(match.split(',')[1])

print(sum)