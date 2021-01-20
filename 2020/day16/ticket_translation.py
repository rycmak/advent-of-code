# Check if each number on each ticket belongs to allowed set (given in rules).
# Return sum of all invalid numbers.

# Strategy:
# Get allowed numbers from all rules and put them into a set.
# For each number on each ticket, check if in set;
# if not, add to running error sum.

data = []
error_sum = 0
index = 0

file = open("input.txt", "r")
for line in file:
  data.append(line.strip())
  if line.strip() == "your ticket:":
    ticket_index = index
  elif line.strip() == "nearby tickets:":
    nearby_index = index
  index += 1

rules = data[:ticket_index - 1]
my_ticket = data[ticket_index + 1]
nearby_tickets = data[nearby_index + 1:]

valid_nums = set()

for rule in rules:
  ranges = [range.strip() for range in rule.split(':')[1].strip().split("or")]
  for valid_range in ranges:
    valid_nums.update([x for x in range(int(valid_range.split('-')[0]), int(valid_range.split('-')[1]) + 1)])

for ticket in nearby_tickets:
  error_sum += sum([int(num) for num in ticket.split(',') if int(num) not in valid_nums])

print("Error rate = ", error_sum)
