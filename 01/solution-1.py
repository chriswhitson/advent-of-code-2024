import sys

with open(sys.argv[1]) as f:
    pairs = [list(map(int, line.split())) for line in f]
    columns = list(map(sorted, zip(*pairs)))
    print(sum(abs(a-b) for a,b in zip(*columns)))
    
    