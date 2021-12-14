file = open("input.txt", "r")

binaries = []
for binary in file:
  binaries.append(binary.replace('\n', ''))

file.close()

# Find length of each binary; assume all binaries in each input file has the same length
binary_length = len(binaries[0])

sum_bits_per_position = [sum(int(binary[i]) for binary in binaries) for i in range(binary_length)]

gamma_bits = ['0' if sum_bits_per_position[i] < len(binaries) / 2 else '1' for i in range(binary_length)]
gamma_binary = int("".join(gamma_bits), 2)

epsilon_bits = ['0' if sum_bits_per_position[i] > len(binaries) / 2 else '1' for i in range(binary_length)]
epsilon_binary = int("".join(epsilon_bits), 2)

print(f"Power consumption = {gamma_binary * epsilon_binary}")