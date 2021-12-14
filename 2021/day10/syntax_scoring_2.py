file = open("input.txt", 'r')

open_brace = ['(', '[', '{', '<']
closed_brace_scores = {')': 1, ']': 2, '}': 3, '>': 4}
num_closed_braces = {')': 0, ']': 0, '}': 0, '>': 0}
match_open_brace_dict = {'(': ')', '[': ']', '{': '}', '<': '>'}
match_closed_brace_dict = {')': '(', ']': '[', '}': '{', '>': '<'}

scores = []

def calc_score(unmatched_open_braces):
  score = 0
  while unmatched_open_braces:
    matched_closed_brace = match_open_brace_dict[unmatched_open_braces.pop()]
    score = score * 5 + closed_brace_scores[matched_closed_brace]
  return score


for line in file:
  # treat line as a stack, reversed order so first elem pops out first
  line = list(line.replace('\n', ''))[::-1]
  # stack to hold each open brace that hasn't been matched with a closed brace
  matching_braces = []
  found_corrupt_brace = False
  while found_corrupt_brace != True:
    if not line:  # incomplete line; we only want corrupt lines
      scores.append(calc_score(matching_braces))
      break
    if line[-1] in open_brace:
      matching_braces.append(line.pop())
    else:  # it's a closed brace
      if match_closed_brace_dict[line[-1]] != matching_braces.pop():  # found non-matching brace
        num_closed_braces[line.pop()] += 1
        found_corrupt_brace = True
        break
      else:
        line.pop()

winning_score = sorted(scores)[len(scores) // 2]  # find middle score
print(f"winning score = {winning_score}")