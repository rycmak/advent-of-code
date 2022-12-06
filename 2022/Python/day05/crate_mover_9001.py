file = open("input.txt", 'r')

instructions = []
rows = []

for line in file:
  if line == '\n':
    continue
  elif list(line)[1] == '1':
    num_stacks = int(list(line.strip())[-1])
  elif (line.split()[0] != "move"):
    rows.append(list(line))
  else:
    instructions.append([int(line.strip().split(' ')[i]) for i in [1, 3, 5]])

stacks = []

for row in reversed(rows):
  for i in range(num_stacks):
    if len(stacks) < (i + 1):
      stacks.append([])
    if (row[(i * 4) + 1]) != ' ':
      stacks[i].append(row[(i * 4) + 1])

for instruction in instructions:
  num_crates_to_move = instruction[0]
  from_stack = instruction[1] - 1  # index starts at 0
  to_stack = instruction[2] - 1
  stacks[to_stack].extend(stacks[from_stack][-num_crates_to_move:])
  stacks[from_stack] = stacks[from_stack][0:-num_crates_to_move]

for stack in stacks:
  print(stack)

top_crates = ""
for stack in stacks:
  top_crates += stack.pop()

print(f"Crate on top of each stack is {top_crates}")