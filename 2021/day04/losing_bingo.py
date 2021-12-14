import numpy as np

file = open("input.txt", 'r')

random_numbers = []
boards = []
boards_marked = []
board_num = -1  # index to keep track of which board in boards; no board at beginning

for i, line in enumerate(file):
  if i == 0:
    random_numbers = [int(x) for x in line.replace('\n', '').split(',')]
  else:
    if i % 6 != 1:  # not a blank line
      if i % 6 == 2:  # first line of new board
        board_num += 1
        boards.append(np.zeros((5, 5)))
        boards_marked.append(np.full((5, 5), "unmarked", dtype=object))
      
      line_num = i % 6 - 2
      # If line_num becomes negative, it is the last line (row index 4) of each board
      line_num = line_num if line_num >= 0 else 4
      
      boards[board_num][line_num, :] = [int(x) for x in line.split()]

file.close()

wins_tracker = ["not_won"] * len(boards)

def has_won(board):
  for i in range(5):
    if ((list(board[i, :]) == ['marked' for k in range(5)])
          or (list(board[:, i]) == ['marked' for k in range(5)])):
      return True
  return False

def found_losing_board():
  for i, board in enumerate(boards_marked):
    if has_won(board):
      wins_tracker[i] = "won"
  return wins_tracker.count("not_won") == 1

def mark_number_on_board(board_index, rand_num):
  boards_marked[board_index][np.where(boards[board_index] == rand_num)] = "marked"

def calc_score(board_index, board, rand_num):
  print(f"sum = {sum(boards[board_index][np.where(boards_marked[board_index] == 'unmarked')])}")
  print(f"rand_num = {rand_num}")
  score = sum(boards[board_index][np.where(boards_marked[board_index] == "unmarked")]) * rand_num
  print(f"Final score = {score}")

def continue_for_losing_board(board_index, rand_num_index):
  losing_board = boards[board_index]
  losing_board_marker = boards_marked[board_index]
  rand_num = random_numbers[rand_num_index]
  if has_won(losing_board_marker) == True:
    calc_score(board_index, losing_board, random_numbers[rand_num_index - 1])
  else:
    mark_number_on_board(board_index, rand_num)
    continue_for_losing_board(board_index, rand_num_index + 1)

for rand_num_index, rand_num in enumerate(random_numbers):
  for board_index in range(len(boards)):
    mark_number_on_board(board_index, rand_num)
  if found_losing_board():
    losing_board_index = wins_tracker.index("not_won")
    continue_for_losing_board(losing_board_index, rand_num_index + 1)
