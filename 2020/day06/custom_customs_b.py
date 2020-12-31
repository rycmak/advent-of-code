# Count number of common questions answered by everyone in each group
# Sum these counts

answers_all_groups = 0

file = open("input.txt", "r")
group_first_person = True
group_common_answers = {}
for line in file:
  if line.strip() != "":
    if group_first_person:
      # Questions answered by first person in group
      group_common_answers = set(line.strip())
    else:
      group_common_answers = group_common_answers.intersection(set(line.strip()))
    group_first_person = False
  else:
    # before starting on new group, tally previous group's common answers
    answers_all_groups += len(group_common_answers)
    group_common_answers = {}
    group_first_person = True

# Don't forget to process last group!
# (not processed by else statement above)
answers_all_groups += len(group_common_answers)

print("Sum of group answers = ", answers_all_groups)