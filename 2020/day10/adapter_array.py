# Sort a list of joltage adaptors,
# find occurrences of 1-jolt and 3-jolt differences,
# and calculate product of these two numbers.
# Note: need to add 0 to beginning of list (outlet joltage)
# as well as (max adaptor joltage + 3) (device joltage).

# Strategy 1:
# Find differences between each consecutive pair in list
# and find numbers of 1's and 3's separately.
# Strategy 2:
# Make a new list by shifting original to the right by 1 place;
# pad new list on left by 0, and original list on right by 0.
# Calculate differences of two lists element-by-element;
# take differences[second_index:last_index] and find numbers of 1's and 3's

# Let's go with Strategy 2:

import copy
from operator import sub
from collections import Counter

joltages = [0]  # first, include outlet joltage

file = open("input.txt", "r")
for line in file:
  joltages.append(int(line.strip()))

joltages.sort()
joltages.append(max(joltages) + 3)
joltages_shifted = copy.deepcopy(joltages)
joltages_shifted.insert(0, 0)  # insert 0 at beginning of shifted list
joltages.append(0)  # insert 0 at end of original list

joltages_diff = list(map(sub, joltages, joltages_shifted))[1:-1]

joltage_counter = Counter(joltages_diff)
print("Product of number of 1's and number of 3's = ", joltage_counter[1] * joltage_counter[3])
