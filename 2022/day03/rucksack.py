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

sum_duplicate_items_priorities = 0

file = open("input.txt", 'r')

for rucksack in file:
  len_compartment = int(len(rucksack) / 2)
  compartment_1 = rucksack[0:len_compartment]
  compartment_2 = rucksack[len_compartment:len(rucksack)]
  for item in compartment_2:
    if item in compartment_1:
      sum_duplicate_items_priorities += dict_items_priorities[item]
      break

print(f"Sum of duplicate items' priorities = {sum_duplicate_items_priorities}")