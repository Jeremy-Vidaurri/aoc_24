# Advent of Code 2024 - Day 15
from copy import deepcopy

def parse_input(input):
    grid = []
    moves = []
    for line in input:
        if line == '':
            continue
        if line[0] == "#":
            sublist = []
            for val in line.strip():
                sublist.append(val)
            grid.append(sublist)
        else:
            for move in line:
                moves.append(move)
    return grid, moves

def find_robot(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                return (i, j)
    return (-1, -1)
dirs = {
    'v': (1, 0),
    '^': (-1, 0),
    '<': (0, -1),
    '>': (0, 1)
}
def can_push_boxes(grid, deltaRow, deltaCol, row, col):
    while True:
        row += deltaRow
        col += deltaCol
        if grid[row][col] == '.':
            return True, row, col
        elif grid[row][col] == '#':
            return False, row, col

def simulate_movement(grid, move, row, col):
    # Translate the move into useful directions
    deltaRow, deltaCol = dirs[move]
    newRow = row + deltaRow
    newCol = col + deltaCol
    #print(row, col, newRow, newCol)

    if grid[newRow][newCol] == "O":
        # Box in the way, we need to check if there's a wall behind it
        has_space, emptyRow, emptyCol = can_push_boxes(grid, deltaRow, deltaCol, row, col)
        if has_space:
            grid[emptyRow][emptyCol] = 'O'
            grid[newRow][newCol] = '@'
            grid[row][col] = '.'
    elif grid[newRow][newCol] == '#':
        # Can't do anything,  there's a wall
        pass
    else:
        # Nothing in our way, let's get moving
        grid[newRow][newCol] = '@'
        grid[row][col] = '.'

    return grid

def solve_part_one(input):
    grid, moves = parse_input(input)
    result = 0
    for move in moves:
        row, col = find_robot(grid)
        simulate_movement(grid, move, row, col)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                result += i * 100 + j
    
    return result

def expand_grid(grid):
    new_grid = []
    for row in grid:
        sublist = []
        for val in row:
            if val == '#':
                sublist.append('#')
                sublist.append('#')
            elif val == 'O':
                sublist.append('[')
                sublist.append(']')
            elif val == '.':
                sublist.append('.')
                sublist.append('.')
            else:
                sublist.append('@')
                sublist.append('.')
        new_grid.append(sublist)
    return new_grid

def can_push_boxes_2(grid, deltaRow, deltaCol, row, col):
    if deltaCol != 0:
        while True:
            col += deltaCol
            if grid[row][col] == '.':
                return True, row, set([col])
            elif grid[row][col] == '#':
                return False, row, set([col])
    cols_to_check = set()

    if row + deltaRow == '[':
        cols_to_check.add(col)
        cols_to_check.add(col + 1)
    else:
        cols_to_check.add(col)
        cols_to_check.add(col - 1)

    while True:
        row += deltaRow
        good = 0
        tmp = cols_to_check.copy()
        for check_column in tmp:
            if grid[row][check_column] == '#':
                return False, -1, set()
            elif grid[row][check_column] =='[':
                cols_to_check.add(check_column + 1)
            elif grid[row][check_column] ==']':
                cols_to_check.add(check_column - 1)
            else:
                good += 1
        if good == len(cols_to_check):
            #print(row)
            return True, row, cols_to_check

def move_multiple_boxes(grid, starting_row, ending_row, startingCol):
    #print(starting_row, ending_row)
    if ending_row > starting_row:
        delta = 1
    else:
        delta = -1

    tmp_grid = deepcopy(grid)

    columns = set()
    columns.add(startingCol)
    if grid[starting_row][startingCol] =='[':
        columns.add(startingCol + 1)
    elif grid[starting_row][startingCol] ==']':
        columns.add(startingCol - 1)
    moved = set()
    for row in range(starting_row, ending_row, delta):
        tmp = columns.copy()
        for col in tmp:
            #print(grid[row][col], row, col)
            if grid[row][col] == '[' or grid[row][col] == ']':
                tmp_grid[row + delta][col] = grid[row][col]
                #print(tmp_grid[row + delta][col])
                if (row - delta, col) not in moved:
                    #print(row, col, delta, starting_row)
                    tmp_grid[row][col] = '.'

            moved.add((row, col))
            if grid[row + delta][col] =='[':
                columns.add(col + 1)
            elif grid[row + delta][col] ==']':
                columns.add(col - 1)
        
    return deepcopy(tmp_grid)

def simulate_movement_2(grid, move, row, col):
    # Translate the move into useful directions
    deltaRow, deltaCol = dirs[move]
    newRow = row + deltaRow
    newCol = col + deltaCol
    #print(row, col, newRow, newCol)
    #print(move)
    # for _row in grid:
    #     print(''.join(_row))
    if grid[newRow][newCol] == "[" or grid[newRow][newCol] == ']':
        # Box in the way, we need to check if there's a wall behind it
        has_space, emptyRow, columns = can_push_boxes_2(grid, deltaRow, deltaCol, row, col)
        if has_space:
            if deltaCol != 0:
                emptyCol = columns.pop()
                grid[emptyRow].pop(emptyCol)
                grid[emptyRow].insert(col, '.')
            else:
                grid = move_multiple_boxes(grid, newRow, emptyRow, col)
                grid[newRow][col] = '@'
                grid[row][col] = '.'
                # for _row in grid:
                #     print('DEBUG',''.join(_row))
    elif grid[newRow][newCol] == '#':
        # Can't do anything,  there's a wall
        pass
    else:
        # Nothing in our way, let's get moving
        grid[newRow][newCol] = '@'
        grid[row][col] = '.'

    return grid

def solve_part_two(input):
    init_grid, moves = parse_input(input)
    grid = expand_grid(init_grid)

    result = 0
    for move in moves:
        #print(move)
        row, col = find_robot(grid)
        grid = simulate_movement_2(grid, move, row, col)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '[':
                result += i * 100 + j
    
    for row in grid:
        print(''.join(row))

    print(result)

    return None
