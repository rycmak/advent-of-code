left_col = []
right_col = []
dist = []

with open('input.txt', 'r') as f:
    for line in f:
        left_col.append(int(line.strip().split()[0]))
        right_col.append(int(line.strip().split()[1]))

left_col.sort()
right_col.sort()

for i in range(len(left_col)):
    dist.append(abs(left_col[i] - right_col[i]))

print(sum(dist))