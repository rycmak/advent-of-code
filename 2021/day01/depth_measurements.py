# file = open("input.txt", "r")

# count = 0
# previous = None
# for num in file:
#   # num = int(num)
#   current = int(num)

#   if previous is not None:
#     if current > previous:
#       count += 1
#   previous = current

# print(count)
# file.close()


with open('input.txt','r') as f:
  nums = [int(i.replace('\n', '')) for i in f]

count = 0
for i in range(1, len(nums)):
  if nums[i] > nums[i-1]:
    count += 1

print(count)