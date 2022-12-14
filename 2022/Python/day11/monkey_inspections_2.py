file = open("input.txt", 'r')

class Monkey:
  pass

def get_operand(operand):
  if operand == "old":
    return "old"
  else:
    return int(operand)

def operate(operator, operand_1, operand_2):
  if operand_2 == "old":
    operand_2 = operand_1
  if operator == '+':
    return int(operand_1) + int(operand_2)
  elif operator == '-':
    return int(operand_1) - int(operand_2)
  elif operator == '*':
    return int(operand_1) * int(operand_2)

monkeys = []
line_num = 1
all_divisors = 1

for line in file:
  if line_num % 7 == 1:
    monkey_num = int(line.strip()[7:-1])
    monkeys.append(Monkey())
    monkeys[monkey_num].num_items_inspected = 0
  elif line_num % 7 == 2:
    items = line.split(':')[1].strip().split(',')
    items = [int(item) for item in items]
    monkeys[monkey_num].items = items
  elif line_num % 7 == 3:
    [operator, operand] = line.split('=')[1].strip().split()[1:]
    monkeys[monkey_num].operator = operator
    monkeys[monkey_num].operand = get_operand(operand)
  elif line_num % 7 == 4:
    divisor = int(line.split("by")[1].strip())
    monkeys[monkey_num].divisor = divisor
    all_divisors *= divisor
  elif line_num % 7 == 5:
    monkeys[monkey_num].monkey_true = int(line.split("monkey")[1].strip())
  elif line_num % 7 == 6:
    monkeys[monkey_num].monkey_false = int(line.split("monkey")[1].strip())
  line_num += 1

for round in range(0, 10000):
  for monkey in monkeys:
    for item in monkey.items:
      worry_level = int(operate(monkey.operator, item, monkey.operand)) % all_divisors
      if worry_level % monkey.divisor == 0:
        monkeys[monkey.monkey_true].items.append(worry_level)
      else:
        monkeys[monkey.monkey_false].items.append(worry_level)
      monkey.num_items_inspected += 1
      monkey.items = monkey.items[1:]

num_items_inspected = sorted([monkey.num_items_inspected for monkey in monkeys], reverse=True)
print(f"Monkey business level = {num_items_inspected[0] * num_items_inspected[1]}")

