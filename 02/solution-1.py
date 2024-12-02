import sys

with open(sys.argv[1]) as f:
    reports = [list(map(int, line.split())) for line in f]
    
def is_safe(report):
    diff = 0
    for i in range(0,len(report) - 1):
        next_diff = report[i+1] - report[i]
        if (1 < abs(next_diff) > 3 or next_diff == 0) or (diff < 0 and next_diff > 0) or (diff > 0 and next_diff < 0):
            return False
        diff = next_diff
    return True

print(sum(is_safe(report) for report in reports))
