# Advent of Code 2024 - Day 20
import util
# Have an array that keeps track of the current steps it would take to get to the end
# At each spot, sheck if moving two spots illegally would save enough time.

def get_base_times(start, grid, current_steps):
    startRow, startCol = start
    queue = [(startRow,startCol,0)]
    dirs = [(-1,0), (0,1), (1, 0), (0,-1)]
    seen = set()
    seen.add(start)
    total_steps = 0
    while len(queue) != 0:
        curRow, curCol, steps = queue.pop(0)
        total_steps = max(total_steps, steps)
        current_steps[curRow][curCol] = steps
        for dirRow, dirCol in dirs:
            newRow = curRow + dirRow 
            newCol = curCol + dirCol
            if newRow >= len(grid) or newCol >= len(grid[0]) or newRow < 0 or newCol < 0 or (newRow, newCol) in seen or grid[newRow][newCol] == '#':
                continue
            
            queue.append((newRow, newCol, steps + 1))
            seen.add((newRow,newCol))
    return total_steps


def try_cheat(grid, curRow, curCol, current_steps):
    # Take the current score
    # Move twice in each direction
    # If it ends up in a '.', the cheat saves new score - (current score + 2)
    # Return an array of each possible cheat saving.
    #   Should result in at most 8 values
    curSteps = current_steps[curRow][curCol]
    possible_ends = [(-2,0),(2,0),(0,-2),(0,2),(1,1),(-1,1),(-1,-1),(1,-1)]
    cheat_scores = []
    for dRow, dCol in possible_ends:
        newRow = curRow + dRow
        newCol = curCol + dCol
        if newRow < 0 or newRow >= len(grid) or newCol < 0 or newCol >= len(grid[0]) or grid[newRow][newCol] == '#':
            continue
        newSteps = current_steps[newRow][newCol]

        cheat_save = newSteps - (curSteps + 2)
        cheat_scores.append(cheat_save)

    return cheat_scores


def solve_part_one(input):
    _grid = [line.strip() for line in input]
    grid = [[char for char in row] for row in _grid]
    current_steps = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    start = (0,0)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'S':
                start = (row,col)

    total_steps = get_base_times(start, grid, current_steps)
    cheats = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if total_steps - current_steps[row][col] < 100 or current_steps[row][col] == -1:
                continue
            cheat_checks = try_cheat(grid, row, col, current_steps)
            cheats.extend(cheat_checks)
    result = 0
    for val in cheats:
        if val >= 100:
            result += 1
    return result

def get_steps_map(start, current_steps, grid):
    startRow, startCol = start
    queue = [(startRow,startCol,0)]
    dirs = [(-1,0), (0,1), (1, 0), (0,-1)]
    seen = set()
    seen.add(start)
    step_map = {}
    total_steps = 0
    while len(queue) != 0:
        curRow, curCol, steps = queue.pop(0)
        step_map[steps] = (curRow, curCol)
        total_steps = max(total_steps, steps)
        current_steps[curRow][curCol] = steps
        for dirRow, dirCol in dirs:
            newRow = curRow + dirRow 
            newCol = curCol + dirCol
            if newRow >= len(grid) or newCol >= len(grid[0]) or newRow < 0 or newCol < 0 or (newRow, newCol) in seen or grid[newRow][newCol] == '#':
                continue
            
            queue.append((newRow, newCol, steps + 1))
            seen.add((newRow,newCol))
    return total_steps, step_map

def try_cheat_2(cur_steps, step_map, total_steps):
    cheats = []
    curRow, curCol = step_map[cur_steps]
    for i in range(cur_steps + 100, total_steps+1):
        checkRow, checkCol = step_map[i]
        diff = abs(checkRow - curRow) + abs(checkCol - curCol)
        if diff <= 20:
            cheats.append(i - (cur_steps + diff))
    return cheats

def solve_part_two(input):
    _grid = [line.strip() for line in input]
    grid = [[char for char in row] for row in _grid]
    current_steps = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    start = (0,0)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'S':
                start = (row,col)
    cheats = []
    total_steps, step_map = get_steps_map(start, current_steps, grid)
    #print(step_map)
    result = 0
    for i in range(total_steps - 101):
        cheats.extend(try_cheat_2(i, step_map, total_steps))

    for val in cheats:
        if val >= 100:
            result += 1
    print(result)
    return None
