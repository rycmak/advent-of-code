file = open("input.txt")

total_points = 0

for card in file:
  winning_nums = card.split('|')[0].strip()
  winning_nums = winning_nums.split(':')[1].strip().split()
  my_nums = card.split('|')[1].strip().split()

  for i in range(len(winning_nums)):
    winning_nums[i] = int(winning_nums[i])
  for i in range(len(my_nums)):
    my_nums[i] = int(my_nums[i])

  matched_nums = set(winning_nums).intersection(set(my_nums))

  points = 2 ** (len(matched_nums) - 1) if len(matched_nums) > 0 else 0
  total_points += points

print(f"Total points = {total_points}")