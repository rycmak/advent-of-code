file = open("input.txt")
binary_string = '' 
for line in file:
  binary_string += str(bin(int(line.strip(), 16)))[2:].zfill(len(line) * 4)

packet_start_index = 0
versions = []
packets_hierarchy_dict = {}

def get_packet_end_index_if_no_subpackets(index):
  global binary_string
  binary_substring = binary_string[index:]
  num_binary_groups = 0
  number = ''  # number is concatenation of all the binary groups (together represent one number)
  last_binary_group = False
  while last_binary_group == False:
    number += str(int(binary_substring[(num_binary_groups * 5 + 7):(num_binary_groups * 5 + 11)], 2))
    if binary_substring[num_binary_groups * 5 + 6] == '0':  # final binary group starts with 0
      last_binary_group = True
    num_binary_groups += 1
    end_index = index + num_binary_groups * 5 + 5
  return end_index

def get_parsed_packet_end_index(index):
  if binary_string[index:] == '0' * len(binary_string[index:]):  # only leftover zeros
    return len(binary_string) - 1  # entire data packet has been parsed
  version = int(binary_string[index:index+3], 2)
  versions.append(version)
  type_id = int(binary_string[index+3:index+6], 2)
  if type_id == 4:  # packet contains just one binary number
    packets_hierarchy_dict[index] = None
    return get_packet_end_index_if_no_subpackets(index)
  else:  # operator packet containing subpackets
    packets_hierarchy_dict[index] = []
    length_type_id = int(binary_string[index+6], 2)
    if length_type_id == 0:  # next 15 bits represent total bit length of following subpackets
      subpacket_bit_length = int(binary_string[index+7:index+22], 2)
      next_packet_start_index = index + 3 + 3 + 1 + 15 + subpacket_bit_length
      next_subpacket_start_index = index + 22
      while (next_subpacket_start_index < next_packet_start_index):
        packets_hierarchy_dict[index].append(next_subpacket_start_index)
        next_subpacket_start_index = get_parsed_packet_end_index(next_subpacket_start_index) + 1
      return next_packet_start_index - 1
    elif length_type_id == 1:
      num_subpackets = int(binary_string[index+7:index+18], 2)
      num_subpackets_parsed = 0
      next_subpacket_start_index = index + 18
      while num_subpackets_parsed < num_subpackets:
        packets_hierarchy_dict[index].append(next_subpacket_start_index)
        next_subpacket_start_index = get_parsed_packet_end_index(next_subpacket_start_index) + 1
        num_subpackets_parsed += 1
      return next_subpacket_start_index - 1

while packet_start_index < len(binary_string):
  packet_end_index = get_parsed_packet_end_index(packet_start_index)
  packet_start_index = packet_end_index + 1

print(f"Sum of versions = {sum(versions)}")