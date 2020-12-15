import numpy as np

file = open("input.txt", "r")
nums = []
for num in file:
  # num = int(num)
  nums.append(int(num))
file.close()

nums = np.array(nums)
for i in range(len(nums)):
  for j in range(i, len((nums))):
    if nums[i] + nums[j] == 2020:
      print("i: %i, num: %i" % (i, nums[i]))
      print("j: %i, num: %i" % (j, nums[j]))
