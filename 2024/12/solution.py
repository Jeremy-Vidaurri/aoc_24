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

# FOR LATER:
def check_diags(grid, row, col, target):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != target:
        return True
    return False
# diags are fucking up the seen 
# set up a separate function that checks diags without the seen set

def dfs2(grid, seen, values, row, col, target):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != target:
        return True
    if (row,col) in seen:
        return grid[row][col] != target

    seen.add((row,col))
    values[0] += 1

    left = dfs2(grid, seen, values, row, col-1, target)
    up = dfs2(grid, seen, values, row-1, col, target)
    right = dfs2(grid, seen, values, row, col+1, target)
    down = dfs2(grid, seen, values, row+1, col, target)

    leftD  = check_diags(grid, row+1, col-1, target)
    leftU  = check_diags(grid, row-1, col-1, target)
    rightD = check_diags(grid, row+1, col+1, target)
    rightU = check_diags(grid, row-1, col+1, target)

    valSides = ((1 & left) << 3) +((1 & up) << 2) + ((1 & right) << 1) + (1 & down)
    valDiag = ((1 & leftD) << 3) +((1 & leftU) << 2) + ((1 & rightD) << 1) + (1 & rightU)

    one_corner = set([0b1100, 0b0110, 0b0011, 0b1001])
    two_corners = set([0b1110, 0b1101, 0b1011, 0b0111]) 
    four_corners = set([0b1111])
    
# you can only have an inner corner if you have 2 adjacent sides or 1 side or no side
    one_edge = set([(0b1000, 0b0001), (0b1000, 0b0010), # Left is edge, top/bottom right does not match
                    (0b0100, 0b1000), (0b0100, 0b0010), # Top is edge, top left/right is matching 
                    (0b0010, 0b0100), (0b0010, 0b1000), # Right is edge, top/bottom right  is matching 
                    (0b0001, 0b0100), (0b0001, 0b0001)]) # Bottom is edge, down rght/left is matching
    
    one_edge_double = set([(0b1000, 0b0011), # Left is edge, top/bottom right does not match
                            (0b0100, 0b1010), # Top is edge, top left/right is matching 
                            (0b0010, 0b1100), # Right is edge, top/bottom right  is matching 
                            (0b0001, 0b0101),]) # Bottom is edge, down rght/left is matching
    two_edge = set([(0b1100, 0b0010), (0b0110, 0b1000), (0b0011, 0b0100), (0b1001, 0b0001)])

    #print(target, bin(valSides), row, col)
    if valSides in one_corner:
        #print("ONE CORNER", row, col)
        values[1] += 1
    elif valSides in two_corners:
        #print("TWO CORNER", row, col)
        values[1] += 2
    elif valSides in four_corners:
        #print("FOUR CORNER", row, col)
        values[1] += 4

    flag = False

    for s, d in one_edge_double:
        if s == valSides and d & valDiag == d:
           # print("ONE EDGE DOUBLE", row, col)
            values[1] += 2
            return False

    for s, d in one_edge:
        if s == valSides and d & valDiag == d:
            #print("ONE EDGE", row, col)
            values[1] += 1
            return False
        
    for s, d in two_edge:
        if s == valSides and d & valDiag == d:
            #print("TWO EDGE", row, col)
            values[1] += 1
            return False
        
    if valSides == 0 and valDiag != 0:
        #print("NO EDGE", row, col)
        while valDiag:

            values[1] += valDiag & 1
            valDiag >>= 1
        return False
    return False

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
            #print(char, values[0], values[1])

    return total
