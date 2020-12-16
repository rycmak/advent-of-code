file = open("input.txt", "r")

num_valid = 0

for line in file:
  # policy = part before colon
  policy = line.strip().split(":")[0]
  # get min/max number allowed for given letter
  min_max = policy.split(" ")[0]
  letter = policy.split(" ")[1]
  min = int(min_max.split("-")[0])
  max = int(min_max.split("-")[1])
  
  # password = part after colon
  password = line.strip().split(":")[1]

  # check if password contains between min and max of given letter
  if password.count(letter) >= min and password.count(letter) <= max:
    num_valid += 1

print("Number of valid passwords = ", num_valid)