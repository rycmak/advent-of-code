import re

input = ""

with open("input.txt") as f:
  for line in f:
    input += line

matches = re.findall(r'mul\((\d+,\d+)\)|(do\(\))|(don\'t\(\))', input)

# print(matches)
# [('2,4', '', ''), ('', "don't()", ''), ('5,5', '', ''), ('11,8', '', ''), ('', '', 'do()'), ('8,5', '', '')]

sum = 0
do = True

for match in matches:
  if match[0]:
    if do:
      sum += int(match[0].split(',')[0]) * int(match[0].split(',')[1])
  elif match[1]:
    do = True
  elif match[2]:
    do = False

print(sum)