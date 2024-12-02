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

safe_reports = 0
for report in reports:
    if is_safe(report):
        safe_reports += 1
    else:
        for i in range(len(report)):
            if is_safe(report[:i] + report[i+1:]):
                safe_reports += 1
                break
print(safe_reports)