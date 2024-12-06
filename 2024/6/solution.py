# Advent of Code 2024 - Day 6
import copy
def progress(arr, row, col, dirX, dirY):
    if row + dirY < 0 or row + dirY >= len(arr) or col + dirX < 0 or col + dirX >= len(arr[0]):
            return arr, 0, 0
    while arr[row + dirY][col + dirX] == '#':
        if dirY != 0:
            dirX = 1 if dirY == -1 else -1
            dirY = 0
        elif dirX != 0:
            dirY = -1 if dirX == -1 else 1
            dirX = 0
        if row + dirY < 0 or row + dirY >= len(arr) or col + dirX < 0 or col + dirX >= len(arr[0]):
            return arr, 0, 0

    arr[row] = arr[row][:col] + "." + arr[row][col+1:]
    arr[row+dirY] = arr[row+dirY][:col+dirX] + "^" + arr[row+dirY][col+dirX+1:]

    return arr, dirX, dirY

def progress_2(arr, row, col, dirX, dirY):
    distinct_pos = set()

    if row + dirY < 0 or row + dirY >= len(arr) or col + dirX < 0 or col + dirX >= len(arr[0]):
            return False
    while not(row + dirY < 0 or row + dirY >= len(arr) or col + dirX < 0 or col + dirX >= len(arr[0])):
        if (row, col, dirX, dirY) in distinct_pos:
            return True
        distinct_pos.add((row,col, dirX, dirY))
        while arr[row + dirY][col + dirX] != '#':
            row += dirY
            col += dirX
            if row + dirY < 0 or row + dirY >= len(arr) or col + dirX < 0 or col + dirX >= len(arr[0]):
                return False
            

        while arr[row + dirY][col + dirX] == '#':
            if dirY != 0:
                dirX = 1 if dirY == -1 else -1
                dirY = 0
            elif dirX != 0:
                dirY = -1 if dirX == -1 else 1
                dirX = 0
            if row + dirY < 0 or row + dirY >= len(arr) or col + dirX < 0 or col + dirX >= len(arr[0]):
                return False

    return False

def find_guard(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "^":
                guardRow, guardCol = row, col
                return guardRow, guardCol
    return -1, -1 # Happens if no guard is found

def solve_part_one(input):
    grid = [line.strip() for line in input]
    dirX, dirY = 0, -1
    distinct_pos = set()

    while not(dirX == 0 and dirY == 0):
        guardRow, guardCol = find_guard(grid)
        if guardRow == -1:
            break
        
        grid, dirX, dirY = progress(grid, guardRow, guardCol, dirX, dirY)
        #print(grid, dirX, dirY)
    return len(distinct_pos)

def help(grid):
    
    dirX, dirY = 0, -1
    guardRow, guardCol = find_guard(grid)
    
    return progress_2(grid, guardRow, guardCol, dirX, dirY)

def solve_part_two(input):
    count = 0
    _grid = [line.strip() for line in input]
    grid = [[char for char in row] for row in _grid]

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "#" or grid[row][col] == "^":
                continue
            #print(row, col)
            new_try = copy.deepcopy(grid)
            new_try[row][col] = '#'
            #print(new_try)
            worked = help(new_try)

            if worked:
                count +=1 
                #print(count)
    return count
    
