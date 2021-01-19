# Given input list of numbers, consider last number:
# if this is its first occurrence, next number is 0;
# else, find previous index before last when it occurred
# and subtract from last index -> set as next number.
# Find 2020th number.

# Strategy:
# While length of list < 2020, get last number (N) on list.
# Create new list with last number removed, then reverse this list.
# Find index of N; if found, append this index to end of original list;
# else, append 0.


nums = "1,17,0,10,18,11,6"
nums = [int(i) for i in nums.split(',')]

while len(nums) < 2020:
  last_num = nums[-1]
  reversed_nums = nums[:-1][::-1]  # not including last number
  try:
    last_index = reversed_nums.index(last_num)
  except ValueError:
    last_index = None
  if last_index is not None:
    # index = len(nums) - 1 - last_index - 1
    # nums.append(len(nums) - 1 - index)
    nums.append(last_index + 1)
  else:
    nums.append(0)
  
print("2020th number is", nums[-1])