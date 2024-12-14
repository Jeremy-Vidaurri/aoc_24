# Advent of Code 2024 - Day 14
import re
def parse_input(input):
    robots = []
    for line in input:
        robot_info = re.search("p=(\d+),(\d+) v=(-*\d+),(-*\d+)", line)
        robots.append([int(robot_info.group(1)), int(robot_info.group(2)), int(robot_info.group(3)), int(robot_info.group(4))])
    return robots

    

def solve_part_one(input):
    rowCount = 103
    colCount = 101
    robots = parse_input(input)
    quads = [0,0,0,0]

    # Figure out which rows/cols to not account for
    midRow = 51
    midCol = 50

    for robot in robots:
        posX, posY, velX, velY = robot
        for i in range(100):
            posX = (posX + velX) % colCount
            posY = (posY + velY) % rowCount
        if posX == midCol or posY == midRow:
            continue
        
        if posX < midCol and posY < midRow:
            #print("TL", posY, posX)
            quads[0] += 1
        elif posX > midCol and posY < midRow:
            #print("BL", posY, posX)
            quads[1] += 1
        elif posX > midCol and posY > midRow:
            #print("BR", posY, posX)
            quads[2] += 1
        elif posX < midCol and posY > midRow:
            #print("TR", posY, posX)
            quads[3] += 1
        else:
            print("UHHHHH", posY, posX)
    
        
    total = quads[0] * quads[1] * quads[2] * quads[3]
    return total

def makeGrid(robots):
    rob_set = set([(posX, posY) for posX, posY, _, _ in robots])
    grid = []
    for i in range(103):
        row = []
        for j in range(101):
            if (i, j) in rob_set:
                row.append('X')
            else:
                row.append('.')
        grid.append(''.join(row))
    for row in grid:
        print(row)


def simulate_step(robots):
    rowCount = 103
    colCount = 101
    for robot in robots:
        posX, posY, velX, velY = robot
        robot[0] = (posX + velX) % colCount
        robot[1] = (posY + velY) % rowCount
        
def solve_part_two(input_list):
    robots = parse_input(input_list)
    iteration = 0
    for i in range(63):
        simulate_step(robots)

    while True:
        print(f"Iteration: {iteration}")
        makeGrid(robots)
        input(" ")
        for i in range(103):
            simulate_step(robots)
        iteration += 1

    

    return None
