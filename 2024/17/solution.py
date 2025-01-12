# Advent of Code 2024 - Day 17
import re
from copy import deepcopy
def parse_input(input):
    regs = []
    program = []
    for line in input:
        if not line:
            continue

        string = re.search("Register [ABC]: (\d+)", line)
        if string:
            regs.append(int(string.group(1)))
        else:
            string = re.search("Program: (.*)", line)
            program = [int(s) for s in string.group(1).split(',')]
    return regs, program

def fix_program(program):
    new_program = []
    for i in range(0,len(program),2):
        new_program.append([program[i],program[i+1]])
    return new_program

def run_operation(opcode, literal, index, regs, output):
    if literal <= 3:
        combo = literal
    elif literal <= 6:
        combo = regs[literal - 4]

    if opcode == 0:
        regs[0] = regs[0] // (2 ** combo)
        index += 1
    elif opcode == 1:
        regs[1] ^= literal
        index += 1
    elif opcode == 2:
        regs[1] = combo % 8
        index += 1
    elif opcode == 3:
        if regs[0] != 0:
            index = literal // 2
        else:
            index += 1
    elif opcode == 4:
        regs[1] ^= regs[2]
        index += 1
    elif opcode == 5:
        output.append(combo % 8)
        index += 1
    elif opcode == 6:
        regs[1] = regs[0] // (2 ** combo)
        index += 1
    elif opcode == 7:
        regs[2] = regs[0] // (2 ** combo)
        index += 1
    return output, index, regs

def solve_part_one(_input):
    regs, program = parse_input(_input)    
    program = fix_program(program)
    index = 0
    output = []
    while index < len(program):
        opcode, literal = program[index]
        output, index, regs = run_operation(opcode, literal, index, regs, output) 
    result = ','.join([str(n) for n in output]) 

    return result


def solve_part_two(_input):
    try:
        regs, _program = parse_input(_input)    
        program = fix_program(_program)
        for i in range(10, 20):
            regA = 8**i + 8**(i-8)
            tmp = deepcopy(regs)
            index = 0
            output = []
            tmp[0] = regA
            while index < len(program):
                opcode, literal = program[index]
                output, index, tmp = run_operation(opcode, literal, index, tmp, output) 
            result = ','.join([str(n) for n in output]) 
            print(i, result)
            if (result[:-1] == '0'):
                print(i, result)
                if result == '2,4,1,5,7,5,1,6,4,1,5,5,0,3,3,0':
                    break
    except Exception as e:
        print(i,e)
    return None
