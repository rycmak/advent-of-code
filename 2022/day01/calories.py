file = open("input.txt", 'r')

calories_per_elf = [0]  # initialize first elf with 0 calories

for line in file:
  # if not a new elf, add to that elf's calorie count
  if line != "\n":
    calories_per_elf[-1] += int(line)
  # otherwise, append new elf to array
  else:
    calories_per_elf.append(0)

print(f"Max calories carried by an elf is {max(calories_per_elf)}")