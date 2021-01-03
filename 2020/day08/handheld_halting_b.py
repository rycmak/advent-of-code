# Change one operation in boot code from jmp -> nop or nop -> jmp
# so that program will run from first line and terminate
# after trying to run instruction after last line

# Strategy:
# Find first line with jmp and change it to nop
# Run program to see if it loops back on itself
# If yes, then reverse boot code change
# Find second line with jmp and change it to nop, and so on...
# Until we find a program that tries to run code[(last index + 1)]
# If cannot find such a program, begin process again with changing nop to jmp

# NB:
# a.copy() creates only a shallow copy!
# For deep copy, import copy and use copy.deepcopy(a)

import copy

file = open("input.txt", "r")
boot_code = []
for line in file:
  boot_code.append(line.strip().split())
  boot_code[-1].append(False)

jmp_nop_indices = [index for index in range(len(boot_code)) if boot_code[index][0] == 'jmp'
                    or boot_code[index][0] == 'nop']

def run_program(boot_code_version):
  # Return whether program terminated properly, and if so, the accumulator
  # Success happens when we reach index = len(boot_code_version)
  # Failure happens when we reach a line that has already been executed
  accumulator = 0
  boot_code_index = 0
  while True:
    boot_code_changed[boot_code_index][2] = True  # set "executed" for this line to True
    instruction = boot_code_changed[boot_code_index][0]
    if instruction == "acc":
      accumulator += int(boot_code_changed[boot_code_index][1])
      boot_code_index += 1
    elif instruction == "jmp":
      boot_code_index += int(boot_code_changed[boot_code_index][1])
    else:  # instruction == "nop"
      boot_code_index += 1
    if boot_code_index == len(boot_code_changed):
      success = True
      return success, accumulator
    executed = boot_code_changed[boot_code_index][2]  # check if next line has already been executed
    if executed: 
      return False, accumulator


success = False
while success == False:
  for index in jmp_nop_indices:
    boot_code_changed = copy.deepcopy(boot_code)
    if boot_code_changed[index][0] == "jmp":
      boot_code_changed[index][0] = "nop"
    else:
      boot_code_changed[index][0] = "jmp"
    success, accumulator = run_program(boot_code_changed)
    if success:
      print("Success! Accumulator = %s" % accumulator)
      break
  if success == False:
    print("Doomed to fail ad infinitum :-(")
  break             
