file = open("input_test.txt", 'r')

initial_fish = file.readline()
initial_fish = [int(i) for i in initial_fish.split(",")]

def calc_num_fish(fish, days):
  current_day = 0
  while current_day < days:
    print(current_day)
    # print(f"fish array = {fish}")
    num_zeros = fish.count(0)
    fish = [x - 1 if x > 0 else 6 for x in fish]
    fish.extend([8 for x in range(num_zeros)])
    current_day += 1
  return len(fish)

print(f"Number of fish = {calc_num_fish(initial_fish, 256)}")
    
