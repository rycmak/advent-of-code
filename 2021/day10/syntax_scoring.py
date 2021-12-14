file = open("input.txt", 'r')

open_brace = ['(', '[', '{', '<']
closed_brace_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
num_closed_braces = {')': 0, ']': 0, '}': 0, '>': 0}
matching_brace_dict = {')': '(', ']': '[', '}': '{', '>': '<'}

for line in file:
  # treat line as a stack, reversed order so first elem pops out first
  line = list(line.replace('\n', ''))[::-1]
  # stack to hold each open brace that hasn't been matched with a closed brace
  matching_braces = []
  found_corrupt_brace = False
  while found_corrupt_brace != True:
    if not line: break  # incomplete line; we only want corrupt lines
    if line[-1] in open_brace:
      matching_braces.append(line.pop())
    else:  # it's a closed brace
      if matching_brace_dict[line[-1]] != matching_braces.pop():  # found non-matching brace
        num_closed_braces[line.pop()] += 1
        found_corrupt_brace = True
        break
      else:
        line.pop()

score = sum([closed_brace_scores[x] * num_closed_braces[x] for x in closed_brace_scores.keys()])
print(f"score = {score}")
    