file = open("input.txt")

seed_soil_map = {}
soil_fert_map = {}
fert_water_map = {}
water_light_map = {}
light_temp_map = {}
temp_humid_map = {}
humid_loc_map = {}

seed_ranges = []

for line in file:
  line = line.strip()
  if line == "":
    continue
  if line[0:6] == "seeds:":
    seed_nums = list(line.split(':')[1].strip().split())
    seed_nums = [int(seed) for seed in seed_nums]
    for i in range(len(seed_nums)):
      if i % 2 == 0:
        seed_min = seed_nums[i]
      else:
        seed_max = seed_min + seed_nums[i]
        seed_ranges.append((seed_min, seed_max))
    continue
  if line[-4:] == "map:":
    mapping = list(line.split()[0].strip().split('-'))
    source =  mapping[0]
    continue

  line = list(line.split())
  line = [int(num) for num in line]
  dest_start = line[0]
  source_start = line[1]
  map_range = line[2]
  
  if source == "seed":
    seed_soil_map[(source_start, source_start+map_range)] = dest_start
  elif source == "soil":
    soil_fert_map[(source_start, source_start+map_range)] = dest_start
  elif source == "fertilizer":
    fert_water_map[(source_start, source_start+map_range)] = dest_start
  elif source == "water":
    water_light_map[(source_start, source_start+map_range)] = dest_start
  elif source == "light":
    light_temp_map[(source_start, source_start+map_range)] = dest_start
  elif source == "temperature":
    temp_humid_map[(source_start, source_start+map_range)] = dest_start
  elif source == "humidity":
    humid_loc_map[(source_start, source_start+map_range)] = dest_start


def get_split_source_ranges(source_range, source_dest_map):
  split_ranges = [source_range]
  split_ranges_with_map_info = []
  while split_ranges:
    current_range = split_ranges[0]
    del split_ranges[0]

    for mappable_range in sorted(source_dest_map.keys()):
      if current_range[0] > mappable_range[1]:
        continue  # go to next range in source_dest_map.keys
      if current_range[1] < mappable_range[0]:
        split_range_with_map_info = (current_range[0], current_range[1] - current_range[0], "no map")
        split_ranges_with_map_info.append(split_range_with_map_info)
        return split_ranges_with_map_info  # no more source ranges to map
      if current_range[0] >= mappable_range[0] and current_range[1] < mappable_range[1]:
        split_range_with_map_info = (current_range[0], current_range[1] - current_range[0], mappable_range)
        split_ranges_with_map_info.append(split_range_with_map_info)
        break  # go to next range in split_ranges
      if (current_range[0] >= mappable_range[0] and 
          current_range[0] < mappable_range[1] and 
          current_range[1] >= mappable_range[1]):
        split_range_with_map_info = (current_range[0], mappable_range[1] - current_range[0], mappable_range)
        split_ranges_with_map_info.append(split_range_with_map_info)
        split_range = (mappable_range[1], current_range[1])
        split_ranges.insert(0, split_range)
        break  # now deal with split_range that was split from current_range (i.e., split_ranges[0])
      if (current_range[0] < mappable_range[0] and
          current_range[1] >= mappable_range[0] and
          current_range[1] < mappable_range[1]):
        split_range_1_with_map_info = (current_range[0], mappable_range[0] - current_range[0], "no map")
        split_ranges_with_map_info.append(split_range_1_with_map_info)
        split_range_2_with_map_info = (mappable_range[0], current_range[1] - mappable_range[0], mappable_range)
        split_ranges_with_map_info.append(split_range_2_with_map_info)
        break  # this current_range is done; go deal with next range in split_range (split_ranges[0])
      if current_range[0] < mappable_range[0] and current_range[1] >= mappable_range[1]:
        split_range_1_with_map_info = (current_range[0], mappable_range[0] - current_range[0], "no map")
        split_ranges_with_map_info.append(split_range_1_with_map_info)
        split_range_2_with_map_info = (mappable_range[0], mappable_range[1] - mappable_range[0], mappable_range)
        split_ranges_with_map_info.append(split_range_2_with_map_info)
        split_range_3 = (mappable_range[1], current_range[1])
        split_ranges.insert(0, split_range_3)
        break  # now deal with split_range_3 that was split from current_range (i.e., split_ranges[0])
  
  if not split_ranges_with_map_info:
    split_ranges_with_map_info.append((source_range[0], source_range[1] - source_range[0], "no map"))
  return split_ranges_with_map_info


def get_mapped_ranges(source_ranges, source_dest_map):
  dest_ranges = []
  for source_range in source_ranges:
    if source_range[2] == "no map":
      dest_ranges.append((source_range[0], source_range[0] + source_range[1]))
    else:
      mappable_range = source_range[2]
      dest_range_start = source_dest_map[mappable_range] + (source_range[0] - mappable_range[0])
      dest_range_end = source_dest_map[mappable_range] + (source_range[0] - mappable_range[0]) + source_range[1]
      dest_ranges.append((dest_range_start, dest_range_end))
  return dest_ranges

source_dest_maps = [seed_soil_map, soil_fert_map, fert_water_map, 
                    water_light_map, light_temp_map, temp_humid_map, humid_loc_map]

source_ranges = seed_ranges

for source_dest_map in source_dest_maps:
  all_source_ranges = []
  for source_range in sorted(source_ranges):
    # split source range into list of mappable source ranges: [(source_start, range, source_dest_map.key), (...), ...]
    split_ranges = get_split_source_ranges(source_range, source_dest_map)
    for split_range in split_ranges:
      all_source_ranges.append(split_range)
  mapped_dest_ranges = get_mapped_ranges(all_source_ranges, source_dest_map)
  source_ranges = mapped_dest_ranges  # mapped destination ranges becomes new source ranges

  if source_dest_map == humid_loc_map:
    print(f"Lowest location = {sorted(mapped_dest_ranges)[0][0]}")
    break


# # Test function get_split_source_ranges()
# source_range = (10, 20)
# source_dest_map = {
#   (5, 8): 13,
#   (9, 11): 20,
#   (14, 17): 1,
#   (19, 23): 100,
#   (25, 30): 200
# }
# test_results = get_split_source_ranges(source_range, source_dest_map)
# print(f"test_results = {test_results}")
# # IT WORKS!!
