# Given a list of rules, find how many bag colours can contain one shiny gold bag

# Assume all colour descriptors contain 2 words (e.g., "mirrored chartreuse")
# pattern = re.compile('([a-z]+ [a-z]+) bag')
# For each rule, get colours = pattern.findall(rule) => returns array
# First colour in array = outermost colour; others are inner colours
# Make a dict with outer colour as key, inner colours as values
# For shiny gold as inner colour, find all possible dict keys (direct outer colours)
# Recursively, for each key above find all possible dict keys that can contain it
# If this key does not also appear as a value elsewhere, then it is the outermost colour.
# Make all possible outer colours a set and count its members

import re

file = open("input.txt", "r")
rules_dict = {}
for rule in file:
  pattern = re.compile('([a-z]+ [a-z]+) bag')
  colours = pattern.findall(rule.strip())
  # Dict with outer colour as key, inner colour(s) as value(s)
  rules_dict[colours[0]] = colours[1:]

# Find key(s) (outer colour(s)) associated with each value (inner colour) in array
def find_outer_colours(colours):
  all_outer_colours = set()
  for colour in colours:
    outermost = False
    while outermost == False:
      # outer colours than can contain colour
      outer_colours = [outer for outer, inner in rules_dict.items() if colour in inner]
      if outer_colours:
        for outer_colour in outer_colours:
          contains_shiny_gold.add(outer_colour)
        find_outer_colours(outer_colours)  # repeat recursively for each outer colour
        break
      else:
        # reached outermost colour for current sequence
        contains_shiny_gold.add(colour)
        outermost = True

contains_shiny_gold = set()
find_outer_colours(["shiny gold"])
print("Number of colours that can contain shiny gold: ", len(contains_shiny_gold))

# An alternative approach would be to find all colours that occur only once in input file.
# These are so-called "stop colours" -- no other colours can be outside of it.
# So we can recurse over each colour until we reach a stop colour, then count number of steps

# Or probably this is the type of problem where graphs (nodes and edges) would be appropriate...