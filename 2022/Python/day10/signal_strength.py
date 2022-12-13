file = open("input.txt", 'r')

cycle = 1
register = 1
cycles_to_check = [20, 60, 100, 140, 180, 220]
signal_strengths = []

def check_signal(cycle_num):
  global cycle
  if cycle in cycles_to_check:
    signal_strengths.append(cycle_num * register)
  cycle += 1

for line in file:
  print(f"cycle = {cycle}, register = {register}")
  if (line.startswith("noop")):
    check_signal(cycle)
  else:
    check_signal(cycle)
    check_signal(cycle)
    increment = int(line.strip().split()[1])
    register += increment

print(f"Sum of signal strengths = {sum(signal_strengths)}")
print(signal_strengths)