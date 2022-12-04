# In Python, ord() converts a single char
# into an int representing a Unicode char
# ord('a') = 97, ord('z') = 122
# ord('A') = 65, ord('Z') = 90

small_letters = 'abcdefghijklmnopqrstuvwxyz'
dict_small_letters = {}
for letter in small_letters:
  dict_small_letters[letter] = ord(letter) - 96

capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dict_capital_letters = {}
for letter in capital_letters:
  dict_capital_letters[letter] = ord(letter) - 38

dict_items_priorities = {**dict_small_letters, **dict_capital_letters}

sum_badges_priorities = 0

file = open("input.txt", 'r')

group_items = []

for rucksack in file:
  if len(group_items) < 3:
    group_items.append(set(list(rucksack.strip())))
    if len(group_items) == 3:
      group_badge = group_items[0].intersection(group_items[1], group_items[2])
      sum_badges_priorities += dict_items_priorities[group_badge.pop()]
      group_items = []

print(f"Sum of badge priorities = {sum_badges_priorities}")