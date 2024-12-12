# Advent of Code 2024 - Day 12
def dfs(grid, seen, values, row, col, target):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != target:
        values[1] += 1
        return
    if (row,col) in seen:
        return 

    seen.add((row,col))
    values[0] += 1

    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    for dirR, dirC in dirs:
        newR = row + dirR
        newC = col + dirC
        dfs(grid,seen,values,newR,newC,target)
    return

def solve_part_one(input):
    _grid = [line.strip() for line in input]
    grid = [[char for char in row] for row in _grid]
    seen_sets = {}
    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            char = grid[row][col]
            if char not in seen_sets:
                seen_sets[char] = set()
            values = [0,0]
            
            if (row, col)  in seen_sets[char]:
                continue
            
            dfs(grid, seen_sets[char], values, row, col, char)
            total += values[0] * values[1]

    return total

def dfs2(grid, seen, values, row, col, target):

    return 0

def solve_part_two(input):
    _grid = [line.strip() for line in input]
    grid = [[char for char in row] for row in _grid]
    seen_sets = {}
    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            char = grid[row][col]
            if char not in seen_sets:
                seen_sets[char] = set()

            values = [0,0]
            
            if (row, col)  in seen_sets[char]:
                continue
            
            dfs2(grid, seen_sets[char], values, row, col, char)
            total += values[0] * values[1]
            print(char, values[0], values[1])

    return total
