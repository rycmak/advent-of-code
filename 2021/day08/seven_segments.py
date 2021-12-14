file = open("input.txt", 'r')

count = 0

for line in file:
  output = line.replace('\n', '').split("|")[1].strip()
  for x in output.split(" "):
    if len(x) in [2, 3, 4, 7]:
      count += 1

print(f"Count = {count}")