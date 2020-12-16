import numpy as np
import timeit

file = open("input.txt", "r")
nums = []
for num in file:
  # num = int(num)
  nums.append(int(num))
file.close()

nums = np.array(nums)

# Method 1 for finding two numbers that sum to 2020
def find_nums1(nums_array):
  for i in range(len(nums_array)):
    for j in range(i, len((nums_array))):
      if nums_array[i] + nums_array[j] == 2020:
        print("i: %i, num: %i" % (i, nums_array[i]))
        print("j: %i, num: %i" % (j, nums_array[j]))

# Time Method 1
test1 = '''
def test1():
  return find_nums1(nums)
'''
time1 = timeit.timeit(stmt=test1)
print("time1: %f" % time1)


# Method 2 for finding two numbers that sum to 2020
def find_nums2(nums_array):
  for i in range(len(nums_array)):
    match = [y for y in nums_array[(i + 1):] if y + nums_array[i] == 2020]
    if len(match) > 0:
      print("i: %i, num: %i" % (i, nums_array[i]))
      print("match: ", match)

# Time Method 2
test2 = '''
def test2():
  return find_nums2(nums)
'''
time2 = timeit.timeit(test2)
print("time2: %f" % time2)
