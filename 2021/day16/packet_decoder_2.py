file = open("input.txt")
binary_string = '' 
for line in file:
  binary_string += str(bin(int(line.strip(), 16)))[2:].zfill(len(line) * 4)

packet_start_index = 0
versions = []
packets_hierarchy_dict = {}

def get_packet_value_and_end_index_if_no_subpackets(index):
  global binary_string
  binary_substring = binary_string[index:]
  num_binary_groups = 0
  number = ''  # number is concatenation of all the binary groups (which together represent one number)
  last_binary_group = False
  while last_binary_group == False:
    number += binary_substring[(num_binary_groups * 5 + 7):(num_binary_groups * 5 + 11)]
    if binary_substring[num_binary_groups * 5 + 6] == '0':  # final binary group starts with 0
      last_binary_group = True
    num_binary_groups += 1
  value = int(number, base=2)
  end_index = index + num_binary_groups * 5 + 5
  return value, end_index

def get_parsed_packet_end_index(index):
  if binary_string[index:] == '0' * len(binary_string[index:]):  # only leftover zeros
    return len(binary_string) - 1  # entire data packet has been parsed
  version = int(binary_string[index:index+3], 2)
  versions.append(version)
  type_id = int(binary_string[index+3:index+6], 2)
  packets_hierarchy_dict[index] = {}
  packets_hierarchy_dict[index]["type_id"] = type_id
  if type_id == 4:  # packet contains just one binary number
    value, end_index = get_packet_value_and_end_index_if_no_subpackets(index)
    packets_hierarchy_dict[index]["value"] = value
    return end_index
  else:  # operator packet containing subpackets
    packets_hierarchy_dict[index]["subpackets"] = []
    length_type_id = int(binary_string[index+6], 2)
    if length_type_id == 0:  # next 15 bits represent total bit length of following subpackets
      subpacket_bit_length = int(binary_string[index+7:index+22], 2)
      next_packet_start_index = index + 3 + 3 + 1 + 15 + subpacket_bit_length
      next_subpacket_start_index = index + 22
      while (next_subpacket_start_index < next_packet_start_index):
        packets_hierarchy_dict[index]["subpackets"].append(next_subpacket_start_index)
        next_subpacket_start_index = get_parsed_packet_end_index(next_subpacket_start_index) + 1
      return next_packet_start_index - 1
    elif length_type_id == 1:
      num_subpackets = int(binary_string[index+7:index+18], 2)
      num_subpackets_parsed = 0
      next_subpacket_start_index = index + 18
      while num_subpackets_parsed < num_subpackets:
        packets_hierarchy_dict[index]["subpackets"].append(next_subpacket_start_index)
        next_subpacket_start_index = get_parsed_packet_end_index(next_subpacket_start_index) + 1
        num_subpackets_parsed += 1
      return next_subpacket_start_index - 1

while packet_start_index < len(binary_string):
  packet_end_index = get_parsed_packet_end_index(packet_start_index)
  packet_start_index = packet_end_index + 1

packet_indices = sorted(packets_hierarchy_dict.keys(), reverse=True)
packet_values = {}  # store packet values instead of indices
for index in packet_indices:
  type_id = packets_hierarchy_dict[index]["type_id"]
  if type_id == 4:
    packet_values[index] = packets_hierarchy_dict[index]["value"]
  elif type_id == 0:
    sum_values = 0
    for subpacket in packets_hierarchy_dict[index]["subpackets"]:
      sum_values += packet_values[subpacket]
    packet_values[index] = sum_values
  elif type_id == 1:
    product_values = 1
    for subpacket in packets_hierarchy_dict[index]["subpackets"]:
      product_values *= packet_values[subpacket]
    packet_values[index] = product_values
  elif type_id == 2:
    subpacket_values = []
    for subpacket in packets_hierarchy_dict[index]["subpackets"]:
      subpacket_values.append(packet_values[subpacket])
    packet_values[index] = min(subpacket_values)
  elif type_id == 3:
    subpacket_values = []
    for subpacket in packets_hierarchy_dict[index]["subpackets"]:
      subpacket_values.append(packet_values[subpacket])
    packet_values[index] = max(subpacket_values)
  elif type_id == 5:
    packet_values[index] = 1 if \
      packet_values[packets_hierarchy_dict[index]["subpackets"][0]] > \
        packet_values[packets_hierarchy_dict[index]["subpackets"][1]] \
    else 0
  elif type_id == 6:
    packet_values[index] = 1 if \
      packet_values[packets_hierarchy_dict[index]["subpackets"][0]] < \
        packet_values[packets_hierarchy_dict[index]["subpackets"][1]] \
    else 0
  elif type_id == 7:
    packet_values[index] = 1 if \
      packet_values[packets_hierarchy_dict[index]["subpackets"][0]] == \
        packet_values[packets_hierarchy_dict[index]["subpackets"][1]] \
    else 0
  else:
    pass

print(f"Outermost packet value = {packet_values[0]}")