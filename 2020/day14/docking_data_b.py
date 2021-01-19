# Store given values to 36-bit memory after applying current mask to memory address.
# Return sum of all values in memory.

# For each line in file, if mask -> set current_mask;
# else convert memory address into binary string and pad with zeros if necessary to make 36 bits.
# Create empty array to store possible addresses associated with current address.
# Apply mask to current memory address, where:
# if bitmask bit is 0, corresponding memory address bit is unchanged.
# if bitmask bit is 1, corresponding memory address bit is overwritten with 1.
# if bitmask bit is X, corresponding memory address bit is floating.
# Floating bit will take on both 0 and 1 -> creating two associated addresses.
# Total no. of associated addresses = 2^(no. of X's).
# Push each associated address to addresses array.
# Store current given value in dict as memory location/value pair for all associated addresses.

from itertools import product

memory = {}
current_mask = 36 * '0'  # set initial mask to 0 as 36-bit binary string

def apply_mask(mask, address):
  # Convert mask and address into array of bits, since strings are immutable
  mask = [bit for bit in mask]
  address = [bit for bit in address]
  x_positions = [i for i, bit in enumerate(mask) if bit == 'X']
  for i in range(len(mask)):
    if mask[i] != '0':
      address[i] = mask[i]
  return set_addresses(address, x_positions)
  

def set_addresses(address, positions):
  addresses = []
  # List possible combinations of 0's and 1's in positions marked 'X'
  # List should be of length 2^(no. of X's)
  zeros_ones = list(product(range(2), repeat=len(positions)))  # each combination in list is a tuple
  for combination in zeros_ones:
    for i, bit in enumerate(combination):
      address[positions[i]] = str(bit)
    addresses.append("".join(address))
  return addresses


file = open("input.txt", "r")
for line in file:
  if line.split('=')[0].strip() == "mask":
    current_mask = line.split('=')[1].strip()
  else:
    current_value = int(line.split('=')[1].strip())
    mem_id = int(line.split('=')[0].strip()[4:-1])
    binary_mem_id = str(bin(mem_id))[2:]
    binary_mem_id = (36 - len(binary_mem_id)) * '0' + binary_mem_id
    addresses = apply_mask(current_mask, binary_mem_id)  # list of associated addresses
    for address in addresses:
      memory[address] = current_value

print(sum([value for mem, value in memory.items()]))
