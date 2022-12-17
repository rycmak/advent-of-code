file = open("input.txt", 'r')

left_packets = []
right_packets = []

line_num = 1
for line in file:
  if line_num % 3 == 1:
    left_packets.append(eval(line))
  elif line_num % 3 == 2:
    right_packets.append(eval(line))
  line_num += 1

def is_correct_order(left, right):
  if (type(left) == int and type(right) == int):
    if left < right:
      return True
    if left > right:
      return False
  elif (type(left) == int and type(right) == list):
    return is_correct_order([left], right)
  elif (type(left) == list and type(right) == int):
    return is_correct_order(left, [right])
  elif (type(left) == list and type(right) == list):
    if (len(left) <= len(right)):
      for i in range(0, len(left)):
        is_correct = is_correct_order(left[i], right[i])
        if is_correct is None:
          continue
        else:
          return is_correct
      if (len(left) < len(right)):
        return True
    else:
      for i in range(0, len(right)):
        is_correct = is_correct_order(left[i], right[i])
        if is_correct is None:
          continue
        else:
          return is_correct
      return False

sum_indices = 0

for i in range(0, len(left_packets)):
  if is_correct_order(left_packets[i], right_packets[i]):
    sum_indices += (i + 1)

print(f"Sum of indices of pairs in correct order = {sum_indices}")