file = open("input.txt")

binaries = []
for binary in file:
  binaries.append(binary.replace('\n', ''))
file.close()

# Find length of each binary; assume all binaries in each input file has the same length
binary_length = len(binaries[0])

# Find 02 rating
def get_only_numbers_with_most_common_bit(binary_array, bit_position):
  # Find most common bit in bit_position
  # Return only numbers with most common bit in bit_position
  if len(binary_array) == 1 or bit_position == binary_length:
    return binary_array[0]
  else:
    sum_bits_in_position = sum([int(binary[bit_position]) for binary in binary_array])
    if sum_bits_in_position < (len(binary_array) - sum_bits_in_position):  # 0 is most common bit in bit_position
      return get_only_numbers_with_most_common_bit(
        [x for x in binary_array if x[bit_position] == '0'], bit_position + 1)
    else:  # 1 is most common bit in bit_position, or 0 and 1 equally common
      return get_only_numbers_with_most_common_bit(
        [x for x in binary_array if x[bit_position] == '1'], bit_position + 1)

def get_only_numbers_with_least_common_bit(binary_array, bit_position):
  # Find least common bit in bit_position
  # Return only numbers with least common bit in bit_position
  if len(binary_array) == 1 or bit_position == binary_length:
    return binary_array[0]
  else:
    sum_bits_in_position = sum([int(binary[bit_position]) for binary in binary_array])
    if sum_bits_in_position < len(binary_array) / 2:  # 0 is most common bit in bit_position
      return get_only_numbers_with_least_common_bit(
        [x for x in binary_array if x[bit_position] == '1'], bit_position + 1)
    else:  # 1 is most common bit in bit_position, or 0 and 1 equally common
      return get_only_numbers_with_least_common_bit(
        [x for x in binary_array if x[bit_position] == '0'], bit_position + 1)

o2_rating = int(get_only_numbers_with_most_common_bit(binaries, 0), 2)

co2_rating = int(get_only_numbers_with_least_common_bit(binaries, 0), 2)

print(f"Life support rating = {o2_rating * co2_rating}")


