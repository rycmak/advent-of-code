# Find first number in given list
# that is not the sum of two of the preceding 25 numbers

file = open("input.txt", "r")
numbers = []
for line in file: 
  numbers.append(int(line.strip()))

def find_additive_pair(index):
  for first_index in range(index - 25, index - 1):
    for second_index in range(first_index, index):
      if (numbers[first_index] + numbers[second_index] == numbers[index]
          and numbers[first_index] != numbers[second_index]):
        return True
  return False

for index in range(len(numbers))[25:]:
  if find_additive_pair(index) == False:
    print("First non-conforming number: ", numbers[index])
    break
