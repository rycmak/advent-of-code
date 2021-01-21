# Match each number on a ticket to a field; each field must have a valid number.
# Return product of all numbers belonging to departure* fields on my ticket.

# Strategy:
# Make rules dict with rule name as key and array of possible valid numbers as value.
# Make rules_positions dict with rule name as key and set of possible positions as value;
# initially, all positions are possible;
# but set will be gradually reduced via process of elimination by checking each ticket.
# At the end, each rule should be left with only one possible position.

data = []
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


def discard_invalid():
  valid_nums = set()
  valid_tickets = []

  for rule in rules:
    ranges = [range.strip() for range in rule.split(':')[1].strip().split("or")]
    for valid_range in ranges:
      valid_nums.update([x for x in range(int(valid_range.split('-')[0]), int(valid_range.split('-')[1]) + 1)])

  for ticket in nearby_tickets:
    if len([int(num) for num in ticket.split(',') if int(num) not in valid_nums]) == 0:
      valid_tickets.append(ticket)
  return valid_tickets
  

# Discard invalid tickets
valid_tickets = discard_invalid()

rules_dict = {}  # valid numbers for each rule
for rule in rules:
  rule_name = rule.split(':')[0].strip()
  ranges = [range.strip() for range in rule.split(':')[1].strip().split("or")]
  valid_nums = []
  for r in ranges:
    valid_nums = valid_nums + [x for x in range(int(r.split('-')[0]), int(r.split('-')[1]) + 1)]
  rules_dict[rule_name] = valid_nums

rules_pos_dict = {}  # possible positions for each rule; initially, all positions possible
for rule in rules:
  rules_pos_dict[rule.split(':')[0]] = list(range(len(rules)))

# Check each value on ticket and compare against each rule;
# if value not valid for given rule, remove its ticket position from rules_pos_dict[rule]
for ticket in valid_tickets:
  values = [int(x) for x in ticket.split(',')]
  for pos, value in enumerate(values):
    for rule, valid_values in rules_dict.items():
      if value not in valid_values:
        if pos in rules_pos_dict[rule]:
          rules_pos_dict[rule].remove(pos)


# Given each rule and its possible positions on ticket,
# first find rules with just one possible position.
# Remove these "taken" positions from all other rules.
# Repeat until each rule is left with just one possible position.
all_pos_found = all([len(pos_array) == 1 for pos_array in rules_pos_dict.values()])
while all_pos_found == False:
  for rule, pos_array in rules_pos_dict.items():
    if len(pos_array) == 1:  # if rule has just one possible position
      for key in rules_pos_dict.keys():
        if key != rule and pos_array[0] in rules_pos_dict[key]:
          rules_pos_dict[key].remove(pos_array[0])  # remove position from all but current rule
  all_pos_found = all([len(pos_array) == 1 for pos_array in rules_pos_dict.values()])


# Calculate product of departure values on my ticket
my_ticket = [int(x) for x in my_ticket.split(',')]
my_product = 1
for rule, pos in rules_pos_dict.items():
  if rule.split()[0] == "departure":
    my_product *= my_ticket[pos[0]]
print("My product = ", my_product)