# If the launcher starts off with a positive y velocity vy, 
# then it will eventually fall back down to y=0 at velocity
# -(vy + 1).  For the next downward step to not overshoot 
# the target area, the max y velocity downward should be 
# vy + 1 = abs(target_y_min)
# i.e., vy = abs(target_y_min) - 1

# Launched upward at vy = abs(target_y_min) - 1
# the probe will reach a max height of 
# (abs(target_y_min) - 1) + (abs(target_y_min) - 2) + ... 0
# = (abs(target_y_min) - 1) * abs(target_y_min) / 2

# Example target_y_min = -10
# Actual target_y_min = -260
target_y_min = -260

max_height = (abs(target_y_min) - 1) * abs(target_y_min) / 2
print(f"Max height = {max_height}")