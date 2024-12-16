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
                return True, row, set(), col
            elif grid[row][col] == '#':
                return False, row, set(), col
            
    boxes = set()

    if grid[row + deltaRow][col] == '[':
        boxes.add((row + deltaRow, col))
    elif grid[row + deltaRow][col] == ']':
        boxes.add((row + deltaRow, col-1))

    empty_row = row + deltaRow
    
    while True:
        tmp = boxes.copy()
        for box in tmp:
            if deltaRow == 1:
                empty_row = max(empty_row, box[0])
            else:
                empty_row = min(empty_row, box[0])
            newRow = box[0] + deltaRow
            
            if grid[newRow][box[1]] == '#' or grid[newRow][box[1] + 1] == '#':
                return False, -1, set(), -1
            
            if grid[newRow][box[1]] == '[':
                boxes.add((newRow, box[1]))
            elif grid[newRow][box[1]] == ']':
                boxes.add((newRow, box[1] - 1))
            if grid[newRow][box[1] + 1] == '[':
                boxes.add((newRow, box[1] + 1))
            
        if len(boxes) == len(tmp):
            #print(boxes)
            #print(empty_row)
            return True, empty_row + deltaRow, boxes, -1


def move_multiple_boxes(grid, boxes: set, emptyRow, deltaRow):
    diff = len(grid)
    for box in boxes:
        boxRow, boxCol = box
        grid[boxRow][boxCol] = '.'
        grid[boxRow][boxCol+1] = '.' # Boxes tracks left side
        diff = min((emptyRow - boxRow) * deltaRow, diff)

    for box in boxes:
        boxRow, boxCol = box

        grid[boxRow + diff * deltaRow][boxCol] = '['
        grid[boxRow + diff * deltaRow][boxCol + 1] = ']'

    # New idea:
    #   - Keep track of the left side of the boxes that need to be moved (will gather in can_push_boxes)
    #   - Keep track of the row that the last box will be inserted into
    #   - Simply copy/paste boxes into the appropriate row
    #       - Beforehand, replace their positions with . so we don't override afterwards
    return grid

def simulate_movement_2(grid, move, row, col):
    # Translate the move into useful directions
    deltaRow, deltaCol = dirs[move]
    newRow = row + deltaRow
    newCol = col + deltaCol
    #print(row, col, newRow, newCol)
    # print(move)
    # for _row in grid:
    #     print(''.join(_row))
    #input('')
    if grid[newRow][newCol] == "[" or grid[newRow][newCol] == ']':
        # Box in the way, we need to check if there's a wall behind it
        has_space, emptyRow, boxes, emptyCol = can_push_boxes_2(grid, deltaRow, deltaCol, row, col)
        if has_space:
            if deltaCol != 0:
                grid[emptyRow].pop(emptyCol)
                grid[emptyRow].insert(col, '.')
            else:
                grid = move_multiple_boxes(grid, boxes, emptyRow, deltaRow)
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
    
    # for row in grid:
    #     print(''.join(row))

    return result
