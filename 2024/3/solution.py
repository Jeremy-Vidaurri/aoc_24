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
    queue = []
    sum = 0
    single_string = ""

    for line in input:
        single_string += line.strip()
    
    pattern = r"(do\(\))|(don\'t\(\))|(mul\(\d+,\d+\))"

    queue.extend(x.group() for x in re.finditer(pattern, single_string))

    currentMode = 'do'
    for string in queue:
        if "don't()" in string:
            currentMode = "dont"
        elif "do()" in string:
            currentMode = "do"
        elif currentMode == "do":
            sum += multiply(string)

    return sum
