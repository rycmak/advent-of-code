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
  print("Bool: ", all(key in passport.keys() for key in required_keys))
  return all(key in passport.keys() for key in required_keys)

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