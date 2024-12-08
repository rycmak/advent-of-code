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

def isSafeAfterDampening(report):
  for i in range(len(report)):
    copy = report.copy()
    del copy[i]
    if isSafe(copy):
      return True
  return False

for report in reports:
  if isSafe(report) or isSafeAfterDampening(report):
    numSafeReports += 1

print(f"Number of safe reports = {numSafeReports}")
