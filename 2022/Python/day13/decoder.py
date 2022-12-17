file = open("input.txt", 'r')

packets = []
ordered_packets = [[[2]], [[6]]]

line_num = 1
for line in file:
  if line_num % 3 == 1:
    packets.append(eval(line))
  elif line_num % 3 == 2:
    packets.append(eval(line))
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


for packet in packets:
  for i in range(0, len(ordered_packets)):
    ordered = is_correct_order(packet, ordered_packets[i])
    if ordered is True:
      ordered_packets.insert(i, packet)
      break
    if i == (len(ordered_packets) - 1):
      ordered_packets.append(packet)

print(f"Decoder key = {(ordered_packets.index([[2]]) + 1) * (ordered_packets.index([[6]]) + 1)}")