import collections

datastream = ""

with open('input_test.txt') as file:
    datastream = file.readline().strip()

running_list = collections.deque([datastream[i] for i in range(14)])

char_processed = 14

for char in datastream[14:]:
  if all([running_list.count(running_list[i]) == 1 for i in range(14)]):
    print(f"First start-of-message marker detected; number of chars processed = {char_processed}")
    break
  else:
    running_list.popleft()
    running_list.append(char)
    char_processed += 1
