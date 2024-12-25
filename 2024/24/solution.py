# Advent of Code 2024 - Day 24
import re
from copy import deepcopy

def parse_input(input):
    gates_section = False
    init_values = {}
    ops = []


    for line in input:
        line = line.strip()
        if line == '':
            gates_section = True
        elif not gates_section:
            pattern = "(.*): (\d+)"
            text = re.search(pattern,line)
            init_values[text.group(1)] = int(text.group(2))
        else:
            pattern = "(.*) (AND|OR|XOR) (.*) -> (.*)"
            text = re.search(pattern,line)
            ops.append((text.group(1), text.group(2), text.group(3), text.group(4)))
        
    return init_values, ops

# Ops may be out of order. Maybe pop the ones that are used and continue looping over ops until size of dict remains the same?
def run_ops(values, ops: list):
    while len(ops) != 0:
        tmp = deepcopy(ops)
        for reg1, op, reg2, dest in tmp:
            if reg1 not in values or reg2 not in values:
                continue
            if op == 'AND':
                values[dest] = values[reg1] & values[reg2]
            elif op == 'OR':
                values[dest] = values[reg1] | values[reg2]
            elif op == 'XOR':
                values[dest] = values[reg1] ^ values[reg2]
            else:
                assert(False) # Hmm?
            ops.remove((reg1, op, reg2, dest))
    return values
def solve_part_one(input):
    values, ops = parse_input(input)
    values = run_ops(values, ops)
    result = 0
    for reg in sorted(values.keys())[::-1]:
        if reg[0] == 'z':
            print(reg)
            result <<= 1
            result += values[reg]
    print(result)

    return None

def solve_part_two(input):
    return None
