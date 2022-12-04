file = open("input.txt", 'r')

num_overlapping_pairs = 0

for pair in file:
  assignments = pair.strip().split(',')
  min_max_pairs = [[int(x) for x in elf.split('-')] for elf in assignments]
  if not ((min(min_max_pairs[0])) > max(min_max_pairs[1])
      or (max(min_max_pairs[0])) < min(min_max_pairs[1])):
      num_overlapping_pairs += 1

print(f"Number of overlapping assignment pairs = {num_overlapping_pairs}")