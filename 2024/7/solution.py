# Advent of Code 2024 - Day 7
import copy

def brute_force(target, arr, cur_total):
    if len(arr) == 0:
        return target == cur_total

    num = int(arr.pop(0))
    add = brute_force(target, copy.deepcopy(arr), cur_total+num)
    mul = brute_force(target, copy.deepcopy(arr), cur_total*num)
    
    return add or mul

def brute_force_concat(target, arr, cur_total):
    if len(arr) == 0:
        return target == cur_total
    if cur_total >= target:
        return False
    num = int(arr.pop(0))
    if brute_force_concat(target, copy.deepcopy(arr), cur_total+num):
        return True
    if brute_force_concat(target, copy.deepcopy(arr), cur_total*num):
        return True
    combined = int(str(cur_total) + str(num))
    if brute_force_concat(target, copy.deepcopy(arr), combined):
        return True

def solve_part_one(input):
    lines = [line for line in input]
    count = 0
    for line in lines:
        split = line.split()
        split[0] = split[0][:-1] # Remove the ':' at the end
        target = int(split.pop(0))
        if brute_force(target, split, 0):
            count += target
    return count

def solve_part_two(input):
    lines = [line for line in input]
    count = 0
    for line in lines:
        split = line.split()
        split[0] = split[0][:-1] # Remove the ':' at the end
        target = int(split.pop(0))
        if brute_force_concat(target, split, 0):
            count += target
    return count
