# Find contiguous set of numbers that sum to 258585477 (index 593)
# Return sum of smallest and largest numbers in set

# Naive strategy:
# Notice that all numbers after 258585477 in input are larger (check)
# so we will only test preceding numbers (indices before 593).
# Work backwards (since larger numbers tend to occur later)
# and sum first two preceding numbers.
# If sum is too small, include next preceding number and test.
# If sum is too large, remove first preceding number and test.
# Repeat until equality.


file = open("input.txt", "r")
numbers = []
for line in file: 
  numbers.append(int(line.strip()))

# First, check that all numbers after index 593 are larger than 258585477
# So that we only have to worry about indices up to 593
target_number = 258585477
target_index = 593
print("Need only check from indices preceding 593: %s" 
    % all(numbers[index] > target_number 
      for index in range(target_index + 1, len(numbers))))  # prints True

# Let's start with the two numbers immediately preceding 258585477
nums_to_sum = [numbers[target_index - 1], numbers[target_index - 2]]

for i in range(target_index - 3, -1, -1):  # index backwards until 0, unless sequence is found
  while sum(nums_to_sum) > target_number:
    # remove first number in list until sum is smaller than target
    del nums_to_sum[0]
  if sum(nums_to_sum) == target_number:
    print("Sum of smallest and largest numbers = ", min(nums_to_sum) + max(nums_to_sum))
    break
  # Sum is too small; add next preceding number to list
  nums_to_sum.append(numbers[i])  




