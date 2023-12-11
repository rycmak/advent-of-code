file = open("input.txt")

# For each card, find number of matching numbers.
# Make dict with card number as key, number of cards (starting with 1) as value.
# For each card, add value of subsequent cards with number of matching numbers.
# Sum all values in dict.

cards = {}
num_matches = []
num_cards = 0

for card in file:
  num_cards += 1
  winning_nums = card.split('|')[0].strip()
  winning_nums = winning_nums.split(':')[1].strip().split()
  my_nums = card.split('|')[1].strip().split()

  for i in range(len(winning_nums)):
    winning_nums[i] = int(winning_nums[i])
  for i in range(len(my_nums)):
    my_nums[i] = int(my_nums[i])

  num_matched = len(set(winning_nums).intersection(set(my_nums)))
  num_matches.append(num_matched)

  cards[num_cards] = 1

for i in range(num_cards):
  num_matched = num_matches[i]
  for j in range(num_matched):
    cards[i+j+2] += cards[i+1]

print(f"Total number of cards = {sum(cards.values())}")
