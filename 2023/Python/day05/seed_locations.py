file = open("input.txt")

source = ""
seed_soil_map = {}
soil_fert_map = {}
fert_water_map = {}
water_light_map = {}
light_temp_map = {}
temp_humid_map = {}
humid_loc_map = {}

for line in file:
  line = line.strip()
  if line == "":
    continue
  if line[0:6] == "seeds:":
    seeds = list(line.split(':')[1].strip().split())
    seeds = [int(seed) for seed in seeds]
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

lowest_loc = None

for seed in seeds:
  soil = None
  for seed_range in seed_soil_map.keys():
    if seed >= seed_range[0] and seed < seed_range[1]:
      soil = seed_soil_map[seed_range] + (seed - seed_range[0])
      break
  soil = seed if soil is None else soil
  
  fert = None
  for soil_range in soil_fert_map.keys():
    if soil >= soil_range[0] and soil < soil_range[1]:
      fert = soil_fert_map[soil_range] + (soil - soil_range[0])
      break
  fert = soil if fert is None else fert
  
  water = None
  for fert_range in fert_water_map.keys():
    if fert >= fert_range[0] and fert < fert_range[1]:
      water = fert_water_map[fert_range] + (fert - fert_range[0])
      break
  water = fert if water is None else water

  light = None
  for water_range in water_light_map.keys():
    if water >= water_range[0] and water < water_range[1]:
      light = water_light_map[water_range] + (water - water_range[0])
      break
  light = water if light is None else light

  temp = None
  for light_range in light_temp_map.keys():
    if light >= light_range[0] and light < light_range[1]:
      temp = light_temp_map[light_range] + (light - light_range[0])
      break
  temp = light if temp is None else temp

  humid = None
  for temp_range in temp_humid_map.keys():
    if temp >= temp_range[0] and temp < temp_range[1]:
      humid = temp_humid_map[temp_range] + (temp - temp_range[0])
      break
  humid = temp if humid is None else humid

  loc = None
  for humid_range in humid_loc_map.keys():
    if humid >= humid_range[0] and humid < humid_range[1]:
      loc = humid_loc_map[humid_range] + (humid - humid_range[0])
      break
  loc = humid if loc is None else loc
  
  if lowest_loc is None:
    lowest_loc = loc
  else:
    lowest_loc = loc if loc < lowest_loc else lowest_loc

print(f"Lowest location = {lowest_loc}")
