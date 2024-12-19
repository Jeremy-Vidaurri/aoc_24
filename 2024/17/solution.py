# Advent of Code 2024 - Day 17
import re
import copy
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


def recursion(cur_num, digit_place, program, regs, _program):
    print(cur_num, digit_place)
    if digit_place == -1:
        if cur_num == int(','.join([str(n) for n in program])):
            return cur_num
        else:
            return -1
        

    for i in range(cur_num, cur_num+8**(digit_place+1), 8**(digit_place-1)):
        print(i)
        index = 0
        output = []
        tmp = copy.deepcopy(regs)
        tmp[0] = i
        while index < len(program):
            opcode, literal = program[index]
            output, index, regs = run_operation(opcode, literal, index, tmp, output) 
        if _program[digit_place-1:] == output[digit_place-1:]:
            print(output, cur_num)
            check = cur_num + recursion(cur_num + i, digit_place - 1, program, regs, _program)
    
    return -1


def solve_part_two(_input):
    regs, _program = parse_input(_input)    
    program = fix_program(_program)
    print(recursion(0o1000000000000000,16,program, regs,_program))
    return None
