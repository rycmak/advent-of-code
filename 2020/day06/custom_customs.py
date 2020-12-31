# Count number of distinct questions answered by each group
# Sum these counts

answers_all_groups = 0

file = open("input.txt", "r")
group_answers = []
for line in file:
  if line.strip() != "":
    # add answers to same group
    group_answers.append(line.strip())
  else:
    # before starting on new group, tally previous group's answers
    answers_all_groups += len(set("".join(group_answers)))
    group_answers = []

# Don't forget to process last group!
# (not processed by else statement above)
answers_all_groups += len(set("".join(group_answers)))

print("Sum of group answers = ", answers_all_groups)