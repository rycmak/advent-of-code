reports = []
numSafeReports = 0

with open('input.txt', 'r') as f:
  for line in f:
    reports.append([int(x) for x in line.strip().split()])

def isAllIncreasingOrDecreasing(report):
  return all([report[i] < report[i+1] for i in range(len(report) - 1)]) \
    or all([report[i] > report[i+1] for i in range(len(report) - 1)])

def areAdjacentLevelsValid(report):
  return all([abs(report[i] - report[i+1]) <= 3 for i in range(len(report) - 1)])

def isSafe(report):
  return isAllIncreasingOrDecreasing(report) and areAdjacentLevelsValid(report)

for report in reports:
  if isSafe(report):
    numSafeReports += 1

print(f"Number of safe reports = {numSafeReports}")

