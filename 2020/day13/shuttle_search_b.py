# Let first bus depart at timestamp T.  Find smallest T such that:
# each subsequent bus on list departs at the number of minutes 
# which matches its position (index) on the list.

# In other words:
# find smallest number T such that T + bus index
# is a multiple of bus_id for all buses.

import numpy as np
import copy

file = open("input.txt", "r")
for line in file:
  data = line.strip().split(',')

# Write each bus as tuple (t, bus_id) 
# where t is its index and also no. of minutes after T it should depart
all_buses = [(t, int(bus_id)) for t, bus_id in enumerate(data) if bus_id != 'x']
buses = copy.deepcopy(all_buses)

# Start T at max bus ID, since T cannot be smaller than this number
T = max([bus[1] for bus in buses])
time_found = False
increment_T = 1

while time_found == False:
  time_found = all([(T + t) % bus_id == 0 for t, bus_id in all_buses])
  if time_found: 
    print("Found! T = ", T)
    break
  # Try to increment T efficiently/smartly
  increment_T *= int(np.prod([bus_id for t, bus_id in buses if (T + t) % bus_id == 0]))
  bus_to_remove = [bus for bus in buses if (T + bus[0]) % bus[1] == 0]
  if bus_to_remove:
    buses = [bus for bus in buses if bus not in bus_to_remove]
  T += increment_T
