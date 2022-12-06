import collections

datastream = ""

with open('input.txt') as file:
    datastream = file.readline().strip()

running_list = collections.deque([datastream[i] for i in range(4)])

char_processed = 4

for char in datastream[4:]:
  if all([running_list.count(running_list[i]) == 1 for i in range(4)]):
    print(f"First start-of-message marker detected; number of chars processed = {char_processed}")
    break
  else:
    running_list.popleft()
    running_list.append(char)
    char_processed += 1