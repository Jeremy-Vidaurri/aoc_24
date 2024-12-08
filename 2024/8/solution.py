# Advent of Code 2024 - Day 8

def find_antennas(grid):
    ant_locs = {}

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '.':
                continue

            if grid[row][col] not in ant_locs:
                ant_locs[grid[row][col]] = set()

            ant_locs[grid[row][col]].add((row,col))
    return ant_locs

def find_possible_antinodes_1(locs):
    possible_locs = set()
    for row1, col1 in locs:
        for row2, col2 in locs:
            if row1 == row2 and col1 == col2:
                continue
            slope_row = row2-row1
            slope_col = col2-col1
            possible_locs.add((row1-slope_row, col1-slope_col))
            possible_locs.add((row2+slope_row, col2+slope_col))

    return possible_locs

def solve_part_one(input):
    _grid = [line.strip() for line in input]
    grid = [[char for char in row] for row in _grid]
    ant_locs = find_antennas(grid)
    antinodes_locs = set()

    for ant in ant_locs.keys():
        possible_locs = find_possible_antinodes_1(ant_locs[ant])
        for row, col in possible_locs:
            # location is oob
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                continue
            antinodes_locs.add((row,col))
    return len(antinodes_locs)

def find_possible_antinodes_2(size, locs):
    possible_locs = set()

    for row1, col1 in locs:
        for row2, col2 in locs:
            if row1 == row2 and col1 == col2:
                continue
            slope_row = row2-row1
            slope_col = col2-col1
            
            curRow = row1
            curCol = col1
            while (curRow - slope_row >= 0 and curRow - slope_row < size) and (curCol - slope_col >= 0 and curCol - slope_col < size):
                possible_locs.add((curRow-slope_row, curCol-slope_col))
                curRow -= slope_row
                curCol -= slope_col
            curRow = row2
            curCol = col2
            while (curRow + slope_row >= 0 and curRow + slope_row < size) and (curCol + slope_col >= 0 and curCol + slope_col < size):
                possible_locs.add((curRow+slope_row, curCol+slope_col))
                curRow += slope_row
                curCol += slope_col

    return possible_locs

def solve_part_two(input):
    _grid = [line.strip() for line in input]
    grid = [[char for char in row] for row in _grid]
    ant_locs = find_antennas(grid)
    antinodes_locs = set()
    size = len(grid)
    result  = 0


    for ant in ant_locs.keys():
        possible_locs = find_possible_antinodes_2(size,ant_locs[ant])
        result += len(ant_locs[ant])
        for row, col in possible_locs:
            antinodes_locs.add((row,col))

        for row, col in ant_locs[ant]:
            antinodes_locs.add((row,col))
    return len(antinodes_locs)