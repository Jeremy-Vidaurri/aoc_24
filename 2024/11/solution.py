# Advent of Code 2024 - Day 11
import math
import collections

def process(arr:collections.deque):
    length = len(arr)
    for _ in range(length):
        num = arr.popleft()
        if num == 0:
            
            arr.append(1)
        elif (int(math.log10(num)) + 1) % 2 == 0:
            
            digits = int(math.log10(num)) + 1
            arr.append(num // 10**(digits//2))
            arr.append(num % 10**(digits//2))
        else:
            arr.append(num * 2024)
    return arr

def solve_part_one(input):
    arr = collections.deque([int(line) for line in input[0].strip().split()])
    for _ in range(25):
        arr = process(arr)
    return len(arr)

mapping = {}

def tree_process(num, depth):
    if depth == -1:
        return 1
    if num in mapping and mapping[num][depth] != -1:
        return mapping[num][depth]
    
    if num not in mapping:
        mapping[num] = [-1] * 75

    if num == 0:
        mapping[num][depth] = tree_process(num + 1, depth - 1)
    elif (int(math.log10(num)) + 1) % 2 == 0: # Fancy way of check even digit count
        digits = int(math.log10(num)) + 1
        mapping[num][depth] = tree_process(num // 10**(digits//2), depth-1) + tree_process(num % 10**(digits//2), depth-1)
    else:
        mapping[num][depth] = tree_process(num*2024, depth-1)
    return mapping[num][depth]

def solve_part_two(input):
    arr = [int(line) for line in input[0].strip().split()]
    result = 0
    for num in arr:
        result += tree_process(num, 74)
    print(mapping[0])
    return result
