file = open("input.txt", 'r')

action_names = {
  "A": "Rock",
  "B": "Paper",
  "C": "Scissors",
}

action_scores = {
  "Rock": 1,
  "Paper": 2,
  "Scissors": 3
}

result_names = {
  "X": "lose",
  "Y": "draw",
  "Z": "win"
}

result_scores = {
  "win": 6,
  "draw": 3,
  "lose": 0
}

action_to_use = {
  "Rock": {"win": "Paper", "draw": "Rock", "lose": "Scissors"},
  "Paper": {"win": "Scissors", "draw": "Paper", "lose": "Rock"},
  "Scissors": {"win": "Rock", "draw": "Scissors", "lose": "Paper"}
}

my_total_score = 0

for round in file:
  elf_action = action_names[round[0]]
  desired_result = result_names[round[2]]
  my_total_score += (result_scores[desired_result]
                        + action_scores[action_to_use[elf_action][desired_result]])

print(f"My total score = {my_total_score}")