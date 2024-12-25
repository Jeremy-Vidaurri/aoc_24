# Advent of Code 2024 - Day 25
def parse_input(input):
    arr = []
    subarr = []
    for line in input:
        line = line.strip()

        if line == '':
            arr.append(subarr)
            subarr = []
        else:
            subarr.append([char for char in line])
    arr.append(subarr)
    return arr       

def separate_grids(grids):
    keys = []
    locks = []
    for grid in grids:
        if grid[0][0] == '#':
            locks.append(grid)
        else:
            keys.append(grid)
    return keys, locks

def get_size(grid):
    length = [0,0,0,0,0]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '#':
                length[col] += 1
    return length

def key_fits(key_size, lock_size):
    for i in range(len(key_size)):
        if key_size[i] + lock_size[i] > 7:
            return False
    return True

def solve_part_one(input):
    grids = parse_input(input)
    keys, locks = separate_grids(grids)
    result = 0
    for key in keys:
        for lock in locks:
            key_size = get_size(key)
            lock_size = get_size(lock)
            if key_fits(key_size, lock_size):
                result += 1
    return result

def solve_part_two(input):
    return None
