# Given a timestamp (large number), find the bus ID (factor)
# that has a multiple closest to (and larger than) timestamp.
# Return bus ID * (multiple - timestamp).

data = []
file = open("input.txt", "r")
for line in file:
  data.append(line.strip())

timestamp = int(data[0])
buses = [int(bus_id) for bus_id in data[1].split(',') if bus_id != 'x']

# First arrival time after timestamp for each bus
first_buses = [((timestamp // bus) + 1) * bus for bus in buses]

time_diffs = [first_bus - timestamp for first_bus in first_buses]
min_time = [(i, time) for i, time in enumerate(time_diffs) if time == min(time_diffs)]
# Extract (index, min_time) from array above
min_time_index, min_time = min_time[0][0], min_time[0][1]
first_bus = buses[min_time_index]

print("Time till next bus: ", min_time)
print("Time * bus ID = ", min_time * first_bus)
