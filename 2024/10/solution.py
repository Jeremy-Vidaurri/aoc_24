# Advent of Code 2024 - Day 10

def dfs(grid, startX, startY):
    stack = [(startX,startY)]
    visited = set()
    dirs = [(0,1),(1,0),(-1,0),(0,-1)]
    count = 0

    while stack:
        x, y = stack.pop()
        visited.add((x,y))
        if grid[x][y] == 9:
            count += 1
        for dirX, dirY in dirs:
            newX = dirX + x
            newY = dirY + y

            if newX < 0 or newX >= len(grid) or \
            newY < 0 or newY >= len(grid[0]) or \
            (newX,newY) in visited or \
            grid[newX][newY] - grid[x][y] != 1:
                continue
            stack.append((newX,newY))
    return count

def solve_part_one(input):
    _grid = [line.strip() for line in input]
    grid = [[int(char) for char in row] for row in _grid]
    result = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                result += dfs(grid, i, j)
    return result

def dfs_2(grid, startX, startY):
    stack = [(startX,startY)]
    visited = set()
    dirs = [(0,1),(1,0),(-1,0),(0,-1)]
    count = 0

    while stack:
        x, y = stack.pop()
        visited.add((x,y))
        if grid[x][y] == 9:
            count += 1
        for dirX, dirY in dirs:
            newX = dirX + x
            newY = dirY + y

            if newX < 0 or newX >= len(grid) or \
            newY < 0 or newY >= len(grid[0]) or \
            grid[newX][newY] - grid[x][y] != 1:
                continue
            stack.append((newX,newY))
    return count

def solve_part_two(input):
    _grid = [line.strip() for line in input]
    grid = [[int(char) for char in row] for row in _grid]
    result = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                result += dfs_2(grid, i, j)
    return result
