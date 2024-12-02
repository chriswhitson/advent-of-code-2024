import sys

with open(sys.argv[1]) as f:
    puzzle = [list(line) for line in f]

def count_xmas(x,y):
    count = 0
    if puzzle[y][x] != 'X':
        return 0
    if x >= 3 and puzzle[y][x-1] == 'M' and puzzle[y][x-2] == 'A' and puzzle[y][x-3] == 'S':
        count += 1
    if x < len(puzzle[y]) - 3 and puzzle[y][x+1] == 'M' and puzzle[y][x+2] == 'A' and puzzle[y][x+3] == 'S':
        count += 1
    if y >= 3 and puzzle[y-1][x] == 'M' and puzzle[y-2][x] == 'A' and puzzle[y-3][x] == 'S':
        count += 1
    if y < len(puzzle) - 3 and puzzle[y+1][x] == 'M' and puzzle[y+2][x] == 'A' and puzzle[y+3][x] == 'S':
        count += 1
        
    if x >= 3 and y >= 3 and puzzle[y-1][x-1] == 'M' and puzzle[y-2][x-2] == 'A' and puzzle[y-3][x-3] == 'S':
        count += 1 
    if x >= 3 and y < len(puzzle) - 3 and puzzle[y+1][x-1] == 'M' and puzzle[y+2][x-2] == 'A' and puzzle[y+3][x-3] == 'S':
        count += 1
    if x < len(puzzle[y]) and y >= 3 and puzzle[y-1][x+1] == 'M' and puzzle[y-2][x+2] == 'A' and puzzle[y-3][x+3] == 'S':
        count += 1 
    if x < len(puzzle[y]) - 3 and y < len(puzzle) - 3 and puzzle[y+1][x+1] == 'M' and puzzle[y+2][x+2] == 'A' and puzzle[y+3][x+3] == 'S':
        count += 1
    
    return count
    
    
xmas_count = sum(count_xmas(x,y) for y in range(len(puzzle)) for x in range(len(puzzle[y])))
print(xmas_count)