import sys

with open(sys.argv[1]) as f:
    puzzle = [list(line) for line in f]
    
def is_xmas(x,y):
    if puzzle[y][x] != 'A':
        return False
    if x == 0 or x == len(puzzle[y]) - 1 or y == 0 or y == len(puzzle) - 1:
        return False
    if puzzle[y-1][x-1] == 'M' and puzzle[y-1][x+1] == 'M' and puzzle[y+1][x-1] == 'S' and puzzle[y+1][x+1] == 'S':
        return True
    if puzzle[y-1][x-1] == 'S' and puzzle[y-1][x+1] == 'S' and puzzle[y+1][x-1] == 'M' and puzzle[y+1][x+1] == 'M':
        return True
    if puzzle[y-1][x-1] == 'M' and puzzle[y-1][x+1] == 'S' and puzzle[y+1][x-1] == 'M' and puzzle[y+1][x+1] == 'S':
        return True
    if puzzle[y-1][x-1] == 'S' and puzzle[y-1][x+1] == 'M' and puzzle[y+1][x-1] == 'S' and puzzle[y+1][x+1] == 'M':
        return True
    return False
    
xmas_count = sum(is_xmas(x,y) for y in range(len(puzzle)) for x in range(len(puzzle[y])))
print(xmas_count)