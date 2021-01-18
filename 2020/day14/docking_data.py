# Store given values to 36-bit memory after applying current mask.
# Return sum of all current values in memory.

# For each line in file, if mask -> set current_mask;
# else convert value into binary string and pad with zeros if necessary to make 36 bits.
# Compare each value bit with mask bit and convert to mask bit if they're different.
# Convert value to decimal and store in dict as memory location/value pair.

memory = {}
current_mask = 36 * '0'  # set initial mask to 0 as 36-bit binary string

def apply_mask(mask, value):
  # Convert mask and value strings into array, since strings are immutable
  mask = [bit for bit in mask]
  value = [bit for bit in value]
  for i in range(len(mask)):
    if mask[i] != 'X':
      value[i] = mask[i]
  return "".join(value)


file = open("input.txt", "r")
for line in file:
  if line.split('=')[0].strip() == "mask":
    current_mask = line.split('=')[1].strip()
  else:  # memory/value pair
    mem_id = int(line.split('=')[0].strip()[4:-1])
    value = int(line.split('=')[1].strip())
    binary_string = str(bin(value))[2:]
    binary_string = (36 - len(binary_string)) * '0' + binary_string  # pad with 0's
    masked_value = apply_mask(current_mask, binary_string)
    memory[mem_id] = int(masked_value, 2)

print(sum([value for key, value in memory.items()]))
