file = open("input.txt")

digits = [str(digit) for digit in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
calibration_values = []

for line in file:
  line = line.strip()
  for char in list(line):
    if char in digits:
      num = char
      for char2 in list(reversed(list(line))):
        if char2 in digits:
          num += char2
          calibration_values.append(int(num))
          break
      break
  continue

print(f"Calibration values = {calibration_values}")
print(f"Sum = {sum(calibration_values)}")