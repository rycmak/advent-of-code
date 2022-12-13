import numpy as np

file = open("input.txt", 'r')

cycle = 0
register = 1
sprite = [0, 1, 2]

screen_width = 40
screen_height = 6
screen = [['.'] * screen_width] * screen_height
screen = np.array(screen).reshape(screen_height, screen_width)

def draw_pixel(cycle_num):
  global cycle
  pixel_row = int(cycle_num / screen_width)
  pixel_col = cycle_num % screen_width
  if pixel_col in sprite:
    screen[pixel_row, pixel_col] = '#'
  else:
    screen[pixel_row, pixel_col] = '.'
  cycle += 1

for line in file:
  if (line.startswith("noop")):
    draw_pixel(cycle)
  else:
    draw_pixel(cycle)
    draw_pixel(cycle)
    increment = int(line.strip().split()[1])
    register += increment
    sprite = [register - 1, register, register + 1]

print(screen)