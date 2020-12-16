file = open("input.txt", "r")

num_valid = 0

for line in file:
  # policy = part before colon
  policy = line.strip().split(":")[0]
  # get the two possible positions for given letter
  pos = policy.split(" ")[0]
  letter = policy.split(" ")[1]
  pos1 = int(pos.split("-")[0])
  pos2 = int(pos.split("-")[1])
  
  # password = part after colon
  password = line.split(":")[1].strip()

  # check if password contains given letter in exactly one position
  if ((password[pos1 - 1] == letter and password[pos2 - 1] != letter) or
     (password[pos1 - 1] != letter and password[pos2 - 1] == letter)):
     num_valid += 1

print("Number of valid passwords = ", num_valid)