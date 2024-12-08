left_col = []
right_col = []
similarity = []

with open('input_example.txt', 'r') as f:
    for line in f:
        left_col.append(int(line.strip().split()[0]))
        right_col.append(int(line.strip().split()[1]))

for i in range(len(left_col)):
    n = left_col[i]
    freq = len([x for x in right_col if x == n])
    similarity.append(n * freq)

print(sum(similarity))