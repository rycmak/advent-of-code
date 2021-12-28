file = open("input.txt", 'r')

rules = {}
pair_frequencies = {}

for i, line in enumerate(file):
  if i == 0:  # polymer template
    template = line.replace('\n', '')
  elif i > 1:  # rules start from line 3
    line = line.replace('\n', '').split(' -> ')
    rules[line[0]] = line[1]
    pair_frequencies[line[0]] = 0

for c in range(len(template) - 1):
  pair = template[c] + template[c+1]
  pair_frequencies[pair] += 1

letter_frequencies = {}
for c in template:
  if c in letter_frequencies.keys():
    letter_frequencies[c] += 1
  else:
    letter_frequencies[c] = 1

num_steps = 40
for i in range(num_steps):
  pair_frequencies_new = pair_frequencies.copy()
  for pair in pair_frequencies.keys():
    if pair_frequencies[pair] != 0:
      multiple = pair_frequencies[pair]  # how many times a given pair is in the sequence
      pair_frequencies_new[pair] -= multiple  # breaking this pair up, thus subtracting
      inserted_letter = rules[pair]  # insert new letter between the pair
      new_pair_1 = pair[0] + inserted_letter
      new_pair_2 = rules[pair] + pair[1]
      pair_frequencies_new[new_pair_1] += multiple  # increment new pairs
      pair_frequencies_new[new_pair_2] += multiple
      if inserted_letter in letter_frequencies.keys():  # increment new letter
        letter_frequencies[inserted_letter] += multiple
      else:
        letter_frequencies[inserted_letter] = multiple
  pair_frequencies = pair_frequencies_new

ordered_frequencies = sorted(letter_frequencies.values())
print(f"Most common - least common element = {ordered_frequencies[-1] - ordered_frequencies[0]}")
