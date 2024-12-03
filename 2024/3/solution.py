# Advent of Code 2024 - Day 3
import re

def multiply(mul):
    mul_pattern = "\d+,\d+"
    numbers = re.findall(mul_pattern, mul)[0].split(',')
    return int(numbers[0]) * int(numbers[1])

def solve_part_one(input):
    parts = []
    for line in input:
        pattern = "mul\(\d+,\d+\)"
        found = re.findall(pattern, line)
        parts.extend(found)

    sum = 0

    for mul in parts:
        mul_pattern = "\d+,\d+"
        numbers = re.findall(mul_pattern, mul)[0].split(',')
        sum += int(numbers[0]) * int(numbers[1])
    return sum

def solve_part_two(input):
    queue_do = []
    queue_dont = []
    queue_mult = []
    sum = 0
    single_string = ""

    for line in input:
        single_string += line.strip()
    
    pattern_do = "do\(\)"
    pattern_dont = "don\'t\(\)"
    pattern_mult = "mul\(\d+,\d+\)"

    queue_do.extend(x.span() for x in re.finditer(pattern_do, single_string))
    queue_dont.extend(x.span() for x in re.finditer(pattern_dont, single_string))
    queue_mult.extend([x.span(), x.group()] for x in re.finditer(pattern_mult, single_string))
    currentMode = 'do'

    for (start, end), string in queue_mult:
        while (queue_do and start > queue_do[0][0]) or (queue_dont and start > queue_dont[0][0]):
            if queue_do and start > queue_do[0][0]:
                queue_do.pop(0)
                currentMode = 'do'
            if queue_dont and start > queue_dont[0][0]:
                queue_dont.pop(0)
                currentMode = 'dont'
        if currentMode == 'do':
            #print("MULT")
            #print(start,end)
            sum += multiply(string)

    return sum
