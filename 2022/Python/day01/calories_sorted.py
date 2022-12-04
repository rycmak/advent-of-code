file = open("input.txt", 'r')

calories_per_elf = [0]  # initialize first elf with 0 calories

for line in file:
  # if not a new elf, add to that elf's calorie count
  if line != "\n":
    calories_per_elf[-1] += int(line)
  # otherwise, append new elf to array
  else:
    calories_per_elf.append(0)

calories_sorted = sorted(calories_per_elf, reverse=True)

print(f"Total calories carried by top 3 elves is {sum(calories_sorted[0:3])}")