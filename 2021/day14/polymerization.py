file = open("input.txt", 'r')

rules = {}

for i, line in enumerate(file):
  if i == 0:  # polymer template
    template = line.replace('\n', '')
  elif i > 1:  # rules start from line 3
    line = line.replace('\n', '').split(' -> ')
    rules[line[0]] = line[1]

num_steps = 10
for i in range(num_steps):
  new_template = template[0]
  for c in range(len(template) - 1):
    pair = template[c] + template[c+1]
    if pair in rules.keys():
      new_template += rules[pair] + template[c+1]
  template = new_template

letter_frequencies = {}
for c in template:
  if c in letter_frequencies.keys():
    letter_frequencies[c] += 1
  else:
    letter_frequencies[c] = 1

ordered_frequencies = sorted(letter_frequencies.values())
print(f"Most common - least common element = {ordered_frequencies[-1] - ordered_frequencies[0]}")
