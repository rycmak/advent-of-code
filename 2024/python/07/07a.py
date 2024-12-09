from itertools import product

testVals = []
eqns = []

with open("input.txt") as f:
  for line in f:
    testVals.append(int(line.split(':')[0].strip()))
    eqns.append([int(x) for x in line.split(':')[1].strip().split()])

operators = ['+', '*']

result = 0

for k in range(len(eqns)):
  eqn = eqns[k]
  # print(f"eqn = {eqn}")
  length = len(eqn)
  operatorCombinations = list(product(operators, repeat=(length-1)))
  # print(f"opCombs = {operatorCombinations}")
  for opComb in operatorCombinations:
    tempResult = eqn[0]
    for i in range(length-1):
      if opComb[i] == '+':
        tempResult += eqn[i+1]
        # print(f"in +: temp = {tempResult}")
      else:
        tempResult *= eqn[i+1]
        # print(f"in *: temp = {tempResult}")
    if tempResult == testVals[k]:
      result += testVals[k]
      break


print(result)