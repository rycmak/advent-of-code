file = open("input.txt")

sorted_hands = []

def make_hand_dict(hand):
  hand_dict = {}
  for card in hand:
    if card in hand_dict.keys():
      hand_dict[card] += 1
    else:
      hand_dict[card] = 1
  return hand_dict

def get_hand_type(hand):
  hand_dict = make_hand_dict(hand)
  if 5 in hand_dict.values():
    return "Five of a kind"
  elif 4 in hand_dict.values():
    return "Four of a kind"
  elif 3 in hand_dict.values() and 2 in hand_dict.values():
    return "Full house"
  elif 3 in hand_dict.values():
    return "Three of a kind"
  elif list(hand_dict.values()).count(2) == 2:
    return "Two pair"
  elif 2 in hand_dict.values():
    return "One pair"
  else:
    return "High card"

def is_lower_type(new_type, old_type):
  if new_type == "Five of a kind":
    return False
  elif new_type == "Four of a kind" and old_type != "Five of a kind":
    return False
  elif new_type == "Full house" and old_type not in ["Five of a kind", "Four of a kind"]:
    return False
  elif new_type == "Three of a kind" and old_type not in ["Five of a kind", "Four of a kind", "Full house"]:
    return False
  elif new_type == "Two pair" and old_type not in ["Five of a kind", "Four of a kind", "Full house", "Three of a kind"]:
    return False
  elif new_type == "One pair" and old_type not in ["Five of a kind", "Four of a kind", "Full house", "Three of a kind", "Two pair"]:
    return False
  else:
    return True

def is_lower_strength(new_hand, old_hand):
  cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
  strengths = range(14, 1, -1)
  card_strengths = {}
  for i, card in enumerate(cards):
    card_strengths[card] = strengths[i]
  for i, card in enumerate(new_hand):
    if card_strengths[new_hand[i]] == card_strengths[old_hand[i]]:
      continue
    return True if card_strengths[new_hand[i]] < card_strengths[old_hand[i]] else False

def is_lower_rank(new_hand, old_hand):
  new_hand_type = get_hand_type(new_hand)
  old_hand_type = get_hand_type(old_hand)
  if new_hand_type != old_hand_type:
    return True if is_lower_type(new_hand_type, old_hand_type) else False
  else:
    return True if is_lower_strength(new_hand, old_hand) else False

def sort_hands(hand, bid):
  for i, sorted_hand in enumerate(sorted_hands):
    if is_lower_rank(hand, sorted_hand[0]):
      if i == len(sorted_hands) - 1:
        sorted_hands.append((hand, bid))
        return
      else:
        continue
    else:
      sorted_hands.insert(i, (hand, bid))
      return

for line in file:
  hand = [c for c in line.split()[0].strip()]
  bid = int(line.split()[1].strip())
  if not sorted_hands:
    sorted_hands.append((hand, bid))
  else:
    sort_hands(hand, bid)

total_winnings = 0
sorted_hands.reverse()
for rank, (hand, bid) in enumerate(sorted_hands):
  total_winnings += (rank + 1) * bid

print(f"Total winnings = {total_winnings}")