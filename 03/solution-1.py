import sys
import re

with open(sys.argv[1]) as f:
    memory = f.readlines()
    
muls = (mul for line in memory for mul in re.findall("mul\((\d{1,3}),(\d{1,3})\)", line))
result = sum(int(a) * int(b) for a,b in muls)
print(result)