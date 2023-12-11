import re

file = open("input.txt")

digits = [str(digit) for digit in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
calibration_values = []

def words2nums(line):
  line = re.sub('one', 'o1e', line)
  line = re.sub('two', 't2o', line)
  line = re.sub('three', 't3e', line)
  line = re.sub('four', 'f4r', line)
  line = re.sub('five', 'f5e', line)
  line = re.sub('six', 's6x', line)
  line = re.sub('seven', 's7n', line)
  line = re.sub('eight', 'e8t', line)
  line = re.sub('nine', 'n9e', line)
  return line


def get_first_and_last_digits(line):
  for char in list(line):
    if char in digits:
      num = char
      for char2 in list(reversed(list(line))):
        if char2 in digits:
          num += char2
          calibration_values.append(int(num))
          break
      break

for line in file:
  print(f"line = {line}")
  line = line.strip()
  numbers_only = words2nums(line)
  print(f"numbers_only = {numbers_only}")
  get_first_and_last_digits(numbers_only)


print(f"Calibration values = {calibration_values}")
print(f"Sum = {sum(calibration_values)}")