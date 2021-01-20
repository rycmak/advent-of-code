# Same as part 1, but now find 30,000,000th number!

# Given input list of numbers, consider last number:
# if this is its first occurrence, next number is 0;
# else, find previous index before last when it occurred
# and subtract from last index -> set as next number.
# Find 30,000,000th number.

# Strategy:
# Large lists seem inefficient for this problem...
# Since for each number we only need to know its last index,
# we don't need to keep a list with entire history of all numbers.
# Instead, store each unique number as key in dict, with value = last index.
# This way, we can quickly look up last index of latest number, 
# and subtract it from current index to obtain next number.


N = 30000000
nums = "1,17,0,10,18,11,6"
nums = [int(i) for i in nums.split(',')]
last_num = nums[-1]
nums = nums[:-1]

index = 0
nums_dict = {}
for num in nums:
  nums_dict[num] = index
  index += 1

while index < (N - 1):
  try:
    last_index = nums_dict[last_num]
  except KeyError:
    last_index = None
  if last_index is not None:
    next_num = index - last_index
  else:
    next_num = 0
  nums_dict[last_num] = index
  last_num = next_num
  index += 1
  
print("30000000th number is", last_num)
