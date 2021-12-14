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

winning_board_num = None

def has_winning_board():
  for k, board in enumerate(boards_marked):
    for i in range(5):
      if ((list(board[i, :]) == ['marked' for k in range(5)])
        or (list(board[:, i]) == ['marked' for k in range(5)])):
        global winning_board_num
        winning_board_num = k
        return True
  return False

def calc_winning_score():
  for i in random_numbers:
    for j, board in enumerate(boards):
      boards_marked[j][np.where(board == i)] = "marked"
    if has_winning_board():
      return sum(boards[winning_board_num][np.where(boards_marked[winning_board_num]
                   == "unmarked")]) * i

print(f"Winning score = {calc_winning_score()}")
