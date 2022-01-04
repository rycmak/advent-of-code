# input_test = {"target area": {'x': "20..30", 'y':"-10..-5"}}
# input_actual = {"target area": {'x': "25..67", 'y':"-260..-200"}}

import numpy as np
import math
from itertools import product

x_min = 25
x_max = 67
y_min = -260
y_max = -200

target_x = list(range(x_min, x_max + 1))
target_y = list(range(y_min, y_max + 1))
target_area = list(product(target_x, target_y))

# To avoid brute-forcing unnecessary x coordinates, we will try to find 
# minimum viable vx, which is the smallest vx for which:
# vx * (vx + 1) / 2 >= min(target_x)
# which we can solve using the quadratic equation:
# vx = (sqrt(1 + 8 * min(target_x)) - 1) / 2

vx_min =  math.ceil((np.sqrt(1 + 8 * min(target_x)) - 1) / 2)
vx_range = list(range(vx_min, max(target_x) + 1))
vy_range = list(range(min(target_y), abs(min(target_y)) + 1))
v_range = list(product(vx_range, vy_range))
v_valid = []

for v in v_range:
  vx = v[0]
  vy = v[1]

  x = 0
  y = 0

  while (x, y) not in target_area:
    x += vx
    y += vy
    if (x, y) in target_area:
      v_valid.append(v)
      break
    if x > max(target_x) or y < min(target_y):
      # print(f"Breaking: {(vx, vy)}")
      break
    if vx > 0:
      vx -= 1
    elif vx < 0:
      vx += 1
    else:
      vx = 0
    vy -= 1

print(f"Number of valid velocities = {len(v_valid)}")