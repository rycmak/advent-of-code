input = []

with open("input.txt") as f:
  for line in f:
    input.append(line.strip())

splitIndex = input.index('')

rules = {}

for i in range(splitIndex):
  val1 = int(input[i].split('|')[0])
  val2 = int(input[i].split('|')[1])

  if val1 in rules:
    rules[val1]["occursBefore"].append(val2)
  else:
    rules[val1] = {"occursBefore": [val2]}


def isCorrect(update):
  for i, page in enumerate(update):
    for j, pageAfter in enumerate(update[(i+1):]):
      if pageAfter in rules:
        if page in rules[pageAfter]["occursBefore"]:
          return False
  return True

def fix(update):
  for i, page in enumerate(update):
    for j, pageAfter in enumerate(update[(i+1):]):
      if pageAfter in rules:
        if page in rules[pageAfter]["occursBefore"]:
          # page order violates rules, so swap ordering
          update[i], update[i+1+j] = pageAfter, page
          fix(update)
          break
  return update


middlePages = []

for i in range(splitIndex+1, len(input)):
  update = [int(page) for page in input[i].split(',')]
  if not isCorrect(update):
    middlePages.append(fix(update)[int(len(update)/2)])

print(sum(middlePages))
