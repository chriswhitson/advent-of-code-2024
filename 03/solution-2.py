import sys
import re

with open(sys.argv[1]) as f:
    memory = f.readlines()
    
muls = [mul for line in memory for mul in re.findall("mul\((\d{1,3}),(\d{1,3})\)|(don't)\(\)|(do)\(\)", line)]

enabled = True
result = 0
for a, b, dont, do in muls:
    if dont:
        enabled = False
    elif do:
        enabled = True
    elif enabled:
        result += int(a) * int(b)

print(result)