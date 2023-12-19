file = open("input.txt")

sequences = []

for line in file:
  seq = line.split()
  seq = [int(x.strip()) for x in seq]
  sequences.append(seq)

extrapolated_values = []

def extrapolate_value(diffs):
  diffs.reverse()
  for i in range(len(diffs) - 1):
    new_value = diffs[i][-1] + diffs[i+1][-1]
    diffs[i+1].append(new_value)
  return diffs[-1][-1]

for seq in sequences:
  diffs = [seq]  # will contain lists of differences, starting with original seq
  level = 0
  all_zeros = False
  while not all_zeros:
    diff = []
    for i in range(len(diffs[level]) - 1):
      diff.append(diffs[level][i+1] - diffs[level][i])
    diffs.append(diff)
    level += 1
    if all([x == 0 for x in diff]):
      all_zeros = True
      diffs[-1].append(0)  # padding with extra zero to prepare for next step
      extrapolated_values.append(extrapolate_value(diffs))

print(f"Sum of extrapolated_values = {sum(extrapolated_values)}")
