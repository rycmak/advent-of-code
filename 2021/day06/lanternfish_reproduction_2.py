from collections import defaultdict

file = open("input.txt", 'r')

initial_fish = file.readline()
initial_fish = [int(i) for i in initial_fish.split(",")]

fish_dict = {}
for i in range(9):
  fish_dict[i] = 0

for timer in initial_fish:
  fish_dict[timer] += 1

def calc_num_fish(fish, days):
  current_day = 0
  while current_day < days:
    fish_dict_new = {}
    for i in range(9):
      fish_dict_new[i] = 0
    for timer in fish.keys():
      if timer == 0 or timer == 7:
        fish_dict_new[8] = fish[0]
        fish_dict_new[6] = fish[0] + fish[7]
      else:
        fish_dict_new[timer-1] = fish[timer]
    fish = fish_dict_new
    current_day += 1
  return sum(fish.values())

print(f"Number of fish = {calc_num_fish(fish_dict, 256)}")
