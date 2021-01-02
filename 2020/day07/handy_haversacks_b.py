# How many individual bags inside a shiny gold bag?

# Find which direct inner colours (with multipliers) shiny gold contains
# Add this to total number of bags
# For each inner colour, recursively find its direct inner colours (with multipliers)
# Add to total number of bags
# Until reach inner colour that contains no other colour

import re

file = open("input.txt", "r")
rules_dict = {}
for rule in file:
  pattern = re.compile('(\d)*\s*([a-z]+ [a-z]+) bag')
  amount_colours = pattern.findall(rule.strip())
  # Dict with outer colour as key, tuple (amount(s), inner colour(s)) as value(s)
  rules_dict[amount_colours[0][1]] = []
  for num_colours in range(len(amount_colours[1:])):
    rules_dict[amount_colours[0][1]].append(amount_colours[num_colours + 1])
    if rules_dict[amount_colours[0][1]] == [('', 'no other')]:
      rules_dict[amount_colours[0][1]] = []

def count_inner_bags(colour, multiplier):
  multiplier = int(multiplier)
  global total_num_bags 
  total_num_bags += multiplier
  contains_inner = bool(rules_dict[colour])  # false if length of rule is 0; i.e., no inner colours
  while contains_inner == True:
    for amount_colour in rules_dict[colour]:
      count_inner_bags(amount_colour[1], multiplier * int(amount_colour[0]))
    break


total_num_bags = 0
count_inner_bags("shiny gold", 1)
print("Total number of bags inside a shiny gold bag: ", total_num_bags - 1)