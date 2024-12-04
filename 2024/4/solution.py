# Advent of Code 2024 - Day 4
import re
def horizontal_count(line):
    return len(re.findall('(XMAS)', line)) + len(re.findall('(SAMX)', line))

def solve_part_one(input):
    total = 0
    for line in input:
        total += horizontal_count(line)

    for i in range(len(input) - 3):
        for j in range(len(input[i])):
            if input[i][j] == 'X' and input[i+1][j] == 'M' and input[i+2][j] == 'A' and input[i+3][j] == 'S' or \
                input[i][j] == 'S' and input[i+1][j] == 'A' and input[i+2][j] == 'M' and input[i+3][j] == 'X':
                total += 1
    
    for i in range(len(input) - 3):
        for j in range(len(input[i]) - 3):
            if input[i][j] == 'X' and input[i+1][j+1] == 'M' and input[i+2][j+2] == 'A' and input[i+3][j+3] == 'S' or \
                input[i][j] == 'S' and input[i+1][j+1] == 'A' and input[i+2][j+2] == 'M' and input[i+3][j+3] == 'X':
                total += 1
    for i in range(len(input) - 3):
        for j in range(3, len(input[i])):
            if input[i][j] == 'X' and input[i+1][j-1] == 'M' and input[i+2][j-2] == 'A' and input[i+3][j-3] == 'S' or \
                input[i][j] == 'S' and input[i+1][j-1] == 'A' and input[i+2][j-2] == 'M' and input[i+3][j-3] == 'X':
                total += 1
    return total

def solve_part_two(input):
    total = 0
    for i in range(1,len(input) - 1):
        for j in range(1, len(input[i]) - 1):
            if (input[i-1][j-1] == 'M' and input[i][j] == 'A' and input[i+1][j+1] == 'S' or \
                input[i-1][j+1] == 'S' and input[i][j] == 'A' and input[i+1][j+1] == 'M') and \
                (input[i-1][j+1] == 'M' and input[i][j] == 'A' and input[i+1][j-1] == 'S' or \
                input[i-1][j+1] == 'S' and input[i][j] == 'A' and input[i+1][j-1] == 'M'):
                total +=1 
    return total
