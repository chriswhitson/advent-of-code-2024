import sys
from collections import Counter

with open(sys.argv[1]) as f:
    pairs = [list(map(int, line.split())) for line in f]
    col1, col2 = list(zip(*pairs))
    counts1 = Counter(col1)
    counts2 = Counter(col2)
    result = 0
    for a,b in counts1.items():
        result += a*b*counts2[a]
    print(result)
    
    
    
    
    