# Find value of accumulator after following a series of steps
#
# Turn each line in input to a list where:
# Index 0: tuple(instruction type (acc, jmp, or nop), integer argument)
# Index 1: contains boolean executed for whether this instruction has already been run
# OR
# Index 1: array containing step number(s) which runs this instruction
# Push this list into a super-list (of lists) called boot_code
# 
# Initialize accumulator = 0
# Initialize boot_code_index = 0 (which boot code line currently running)
# Start from first index in boot_code
# Before running each instruction, check if executed
# If executed, stop and return accumulater
# Otherwise:
# Set executed = True for instruction
# If instruction type == acc, then increment accumulator by argument, 
#   and go to next list (increment boot_code_line)
# If instruction type == jmp, then increment boot_code_line by argument
# If instruction type == nop, then increment boot_code_line by 1

boot_code = []
file = open("input.txt", "r")
for line in file:
  boot_code.append(line.strip().split())
  boot_code[-1].append(False)

accumulator = 0
boot_code_index = 0
while True:
  boot_code[boot_code_index][2] = True  # set "executed" for this line to True
  instruction = boot_code[boot_code_index][0]
  if instruction == "acc":
    accumulator += int(boot_code[boot_code_index][1])
    boot_code_index += 1
  elif instruction == "jmp":
    boot_code_index += int(boot_code[boot_code_index][1])
  else:  # instruction == "nop"
    boot_code_index += 1
  executed = boot_code[boot_code_index][2]  # check if next line has already been executed
  if executed: break

print("accumulator = ", accumulator)