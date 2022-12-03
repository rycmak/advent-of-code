file = open("input.txt", 'r')

action_names = {
  "A": "Rock",
  "B": "Paper",
  "C": "Scissors",
  "X": "Rock",
  "Y": "Paper",
  "Z": "Scissors"
}

action_scores = {
  "Rock": 1,
  "Paper": 2,
  "Scissors": 3
}

me_vs_elf_scores = {
  "Rock": {"Rock": 3, "Paper": 0, "Scissors": 6},
  "Paper": {"Rock": 6, "Paper": 3, "Scissors": 0},
  "Scissors": {"Rock": 0, "Paper": 6, "Scissors": 3}
}

my_total_score = 0

for round in file:
  elf_action = action_names[round[0]]
  my_action = action_names[round[2]]
  my_total_score += (action_scores[my_action] + me_vs_elf_scores[my_action][elf_action])

print(f"My total score = {my_total_score}")