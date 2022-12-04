file = open("input.txt", 'r')

num_containing_pairs = 0

for pair in file:
  assignments = pair.strip().split(',')
  min_max_pairs = [[int(x) for x in elf.split('-')] for elf in assignments]
  if ((min(min_max_pairs[0]) >= min(min_max_pairs[1]) 
        and max(min_max_pairs[0]) <= max(min_max_pairs[1]))
        or ((min(min_max_pairs[0]) <= min(min_max_pairs[1]) 
        and max(min_max_pairs[0]) >= max(min_max_pairs[1])))):
          num_containing_pairs += 1

print(f"Number of assignment pairs with one range fully containing the other = {num_containing_pairs}")