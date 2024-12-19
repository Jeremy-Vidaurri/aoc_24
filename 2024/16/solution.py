# Advent of Code 2024 - Day 16
import heapq
import util

def solve(startRow, startCol, grid, endRow, endCol):
    queue = [(0, startRow,startCol, 0)] #cost, row, col, dir
    heapq.heapify(queue)
    dirs = [(0,1), (1, 0), (0,-1),(-1,0)]
    costs = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]    
    costs[startRow][startCol] = 0
    seen = set()
    while len(queue) != 0:
        curCost, curRow, curCol, curDir = heapq.heappop(queue)
        seen.add((curRow, curCol, curDir))
        for newDir, (dirRow, dirCol) in enumerate(dirs):
            newRow = curRow + dirRow 
            newCol = curCol + dirCol
            if not util.in_bounds_2d(newCol, newRow, len(grid[0]), len(grid)) or grid[newRow][newCol] == '#' or (newDir + 2) % 4 == curDir or (newRow, newCol, newDir) in seen:
                continue

            if newDir != curDir:
                costs[newRow][newCol] = min(costs[newRow][newCol], curCost + 1001)
                heapq.heappush(queue, (curCost + 1001, newRow, newCol, newDir))
            elif newDir == curDir:
                costs[newRow][newCol] = min(costs[newRow][newCol], curCost + 1)
                heapq.heappush(queue, (curCost + 1, newRow, newCol, newDir))

    return costs[endRow][endCol]

def solve_part_one(input):
    print("Starting part 1")
    _grid = [line.strip() for line in input]
    grid = [[char for char in row] for row in _grid]
    startRow, startCol, endRow, endCol = 0,0,0,0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                startRow, startCol = i,j
            if grid[i][j] == 'E':
                endRow, endCol = i,j
            
            if startRow * startCol * endRow * endCol != 0:
                break
    score = solve(startRow, startCol, grid, endRow, endCol)

    print(score)

    return None

def solve_part_two(input):
    return None
