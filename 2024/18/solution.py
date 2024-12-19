# Advent of Code 2024 - Day 18
from collections import defaultdict

def parse_input(input):
    blocks = set()
    for i, line in enumerate(input):
        x, y = line.strip().split(',')
        blocks.add((int(y),int(x)))
        print(y,x, i)
        if i == 1023:
            return blocks
    return blocks

def bfs(block_map, size):
    queue = [(0,0,0)]
    dirs = [(-1,0), (0,1), (1, 0), (0,-1)]
    seen = set()
    seen.add((0,0))
    while len(queue) != 0:
        curRow, curCol, steps = queue.pop(0)
        if curRow == size and curCol == size:
            return steps
        
        for dirRow, dirCol in dirs:
            newRow = curRow + dirRow 
            newCol = curCol + dirCol
            if newRow > size or newCol > size or newRow < 0 or newCol < 0 or (newRow, newCol) in seen or (newRow, newCol) in block_map:
                continue
            
            queue.append((newRow, newCol, steps + 1))
            seen.add((newRow,newCol))


def visualize_grid(size, blocks):
    grid = []
    for y in range(size):
        row = ""
        for x in range(size):
            row += '.' if (y,x) not in blocks else 'X'
        grid.append(row)

    for row_2 in grid:
        print(row_2)

def solve_part_one(_input):
    size = 70
    blocks = parse_input(_input)
    result = bfs(blocks, size)
    return result

def parse_input_2(input):
    block_map = defaultdict(set) # step:[blocks]
    for i, line in enumerate(input):
        x, y = line.strip().split(',')
        block_map[i+1] = block_map[i+1].union(block_map[i])
        block_map[i+1].add((int(y),int(x)))
    return block_map

def bfs_2(block_map, size, blocks_fallen):
    queue = [(0,0,0)]
    dirs = [(-1,0), (0,1), (1, 0), (0,-1)]
    seen = set()
    seen.add((0,0))
    fallen_blocks = block_map[blocks_fallen]
    while len(queue) != 0:
        curRow, curCol, steps = queue.pop(0)
        if curRow == size and curCol == size:
            return -1
        
        for dirRow, dirCol in dirs:
            newRow = curRow + dirRow 
            newCol = curCol + dirCol
            if newRow > size or newCol > size or newRow < 0 or newCol < 0 or (newRow, newCol) in seen or (newRow, newCol) in fallen_blocks:
                continue
            
            queue.append((newRow, newCol, steps + 1))
            seen.add((newRow,newCol))
    return blocks_fallen


def solve_part_two(_input):
    size = 70
    blocks = parse_input_2(_input)
    result = -1
    for i in range(1024, len(blocks)):
        result = bfs_2(blocks, size, i)
        if result != -1:
            print(result)
            break
    print(blocks[result].symmetric_difference(blocks[result-1]))
    return None
