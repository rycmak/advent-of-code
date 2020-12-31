import re

all_passports = []
num_valid_passports = 0

def enter_passport_info(key_value_pairs, passport):
  for pair in key_value_pairs:
    key = pair.split(":")[0]
    value = pair.split(":")[1]
    passport[key] = value
  return passport

def valid_passport(passport):
  required_keys = ['byr', 'eyr', 'ecl', 'hcl', 'hgt', 'iyr', 'pid']
  if all(key in passport.keys() for key in required_keys):
    # check each key contains valid value
    return all(valid_value(key, value) for key, value in passport.items())

def valid_value(key, value):
  if key == 'byr':
    return (int(value) >= 1920 and int(value) <= 2002)
  elif key == 'iyr':
    return (int(value) >= 2010 and int(value) <= 2020)
  elif key == 'eyr':
    return (int(value) >= 2020 and int(value) <= 2030)
  elif key == 'hgt':
    return (value[-2:] == "cm" and int(value[:-2]) >= 150 and int(value[:-2]) <= 193) or \
           (value[-2:] == "in" and int(value[:-2]) >= 59 and int(value[:-2]) <= 76)
  elif key == 'hcl':
    return re.search('^#[0-9a-f]{6}$', value)
  elif key == 'ecl':
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
  elif key == 'pid':
    return re.search('^\d{9}$', value)
  elif key == 'cid':
    return True


# Run script
file = open("input.txt", "r")
passport_info = {}  # info for single passport
for line in file:
  if line.strip() != "":
    key_value_pairs = line.strip().split(" ") 
    passport_info = enter_passport_info(key_value_pairs, passport_info)
  else:
    # pass passport_info to all_passports
    all_passports.append(passport_info)
    # prepare empty dict for next passport
    passport_info = {}

# Don't forget to process final passport in file!
# (It is not processed by "else" statement above.)
all_passports.append(passport_info)

for passport in all_passports:
  if valid_passport(passport):
    num_valid_passports += 1

print("Number of valid passports = ", num_valid_passports)
