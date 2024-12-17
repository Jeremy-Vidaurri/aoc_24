# Advent of Code 2024 - Day 16

class nodes():
    def __init__(self):
        self.nodes = set()
    
    def find_node(self, row, col):
        for node in self.nodes:
            if node.row == row and node.col == col:
                return node
        return None

class node():
    def __init__(self, row, col):
        self.neighbors = [[None] * 2] * 4 # 2d array with (node, distance) in order of N E S W
        self.minCost = float('inf')
        self.row = row
        self.col = col

    def __hash__(self):
        return hash((self.row, self.col))

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

def is_intersection(grid, row, col):
    if grid[row + 1][col] == '.' and grid[row][col + 1] == '.' or\
        grid[row - 1][col] == '.' and grid[row][col + 1] == '.' or\
        grid[row + 1][col] == '.' and grid[row][col - 1] == '.' or\
        grid[row - 1][col] == '.' and grid[row][col - 1] == '.':
        return True
    return False

def find_end(grid, startRow, startCol, dirRow, dirCol):
    newRow = startRow + dirRow
    newCol = startCol + dirCol
    while grid[newRow][newCol] != '#':
        if is_intersection(grid, newRow, newCol):
            return max(abs(newRow - startRow), abs(newCol - startCol))
        newRow += dirRow
        newCol += dirCol
    return max(abs(newRow - startRow - dirRow), abs(newCol - startCol - dirCol))


def grid_to_graph(grid, starting_node):
    dirs = [(-1,0), (0,1), (1, 0), (0,-1)]
    
    queue = [starting_node]
    node_set = nodes()
    ending_node = None

    while len(queue) != 0:
        cur = queue.pop(0)
        #print(cur.row, cur.col)
        node_set.nodes.add(cur)
        if grid[cur.row][cur.col] == 'E':
            ending_node = cur

        for i, (dirRow, dirCol) in enumerate(dirs):
            #print(cur.neighbors[i])
            if cur.neighbors[i][0]:
                continue

            dist = find_end(grid, cur.row, cur.col, dirRow, dirCol)
            if dist == 0:
                continue

            newRow = cur.row + dist * dirRow
            newCol = cur.col + dist * dirCol
            existing_node = node_set.find_node(newRow, newCol)
            if existing_node:
                cur.neighbors[i] = [existing_node, dist]
                existing_node.neighbors[(i + 2) % 4] = [cur,dist]
            else:
                new_node = node(cur.row + dist * dirRow, cur.col + dist * dirCol)
                cur.neighbors[i] = [new_node, dist]
                new_node.neighbors[(i + 2) % 4] = [cur,dist]
                queue.append(new_node)
                
    return starting_node, ending_node, node_set

def find_path(start,grid):
    node_arr = [(start,1)]
    while node_arr:
        n, cur_dir = node_arr.pop(0)
        #print(n.row, n.col, n.minCost, cur_dir)
        for i, (node_neighbor, dist_neighbor) in enumerate(n.neighbors):
            if not node_neighbor or (i + 2) % 4 == cur_dir:
                # Don't go nowhere
                continue
            if i != cur_dir and dist_neighbor + n.minCost + 1000 < node_neighbor.minCost:
                node_neighbor.minCost = dist_neighbor + n.minCost + 1000
                node_arr.append((node_neighbor,i))
            elif dist_neighbor + n.minCost < node_neighbor.minCost:
                node_neighbor.minCost = dist_neighbor + n.minCost
                node_arr.append((node_neighbor,i))

def solve_part_one(input):
    _grid = [line.strip() for line in input]
    grid = [[char for char in row] for row in _grid]
    start = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                start = node(i,j)
                break
    start.minCost = 0
    start, end, node_set = grid_to_graph(grid, start)
    
    find_path(start, grid)
    # for n in node_set.nodes:
    #     grid[n.row][n.col] = 'O'
    #     if n.neighbors[0][0]:
    #         print(n.neighbors[0])
    #         grid[n.row - 1][n.col] = '^'
    #     if n.neighbors[1][0]:
    #         grid[n.row][n.col+1] = '>'
    #     if n.neighbors[2][0]:
    #         grid[n.row + 1][n.col] = 'v'
    #     if n.neighbors[3][0]:
    #         grid[n.row][n.col - 1] = '<'
    # for _row in grid:
    #     print(''.join(_row))

    print(end.minCost)


    return None

def solve_part_two(input):
    return None
