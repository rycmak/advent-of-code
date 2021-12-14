file = open("input.txt", 'r')

def num_common_letters(string1, string2):
  return len(list(set(list(string1)).intersection(list(string2))))

def get_digit(value_string):
  for key, value in digit_dict.items():
    if value_string == value:
      return key

output_numbers = []

for line in file:
  input = line.replace('\n', '').split("|")[0].strip().split(" ")
  output = line.replace('\n', '').split("|")[1].strip().split(" ")
  input = [set(list(x)) for x in input]
  output = [set(list(x)) for x in output]
  
  digit_dict = {}
  
  for digit in input:
    # print(f"digit = {digit}")
    if len(digit) == 2:
      digit_dict[1] = digit
    elif len(digit) == 3:
      digit_dict[7] = digit
    elif len(digit) == 4:
      digit_dict[4] = digit
    elif len(digit) == 7:
      digit_dict[8] = digit

  for digit in input:
    # print(f"digit = {digit}")
    if len(digit) == 5:  # could be 2, 3, 5
      if num_common_letters(digit, digit_dict[4]) == 2:
        digit_dict[2] = digit
      elif num_common_letters(digit, digit_dict[1]) == 2:
        digit_dict[3] = digit
      else:
        digit_dict[5] = digit
    elif len(digit) == 6:  # could be 0, 6, 9
      if num_common_letters(digit, digit_dict[4]) == 4:
        digit_dict[9] = digit
      elif num_common_letters(digit, digit_dict[7]) == 2:
        digit_dict[6] = digit
      else:
        digit_dict[0] = digit

  output_digits = ""
  for digit_string in output:
    digit = get_digit(digit_string)
    output_digits += str(digit)
  output_numbers.append(int(output_digits))

print(f"Sum of output = {sum(output_numbers)}")
