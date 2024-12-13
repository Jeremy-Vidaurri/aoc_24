# Advent of Code 2024 - Day 13
import re

def parse_input(input):
    arr = []
    sublist = []
    for line in input:
        if "Button A" in line:
            sublist = []
            a_amount_X = re.search("X\+(\d*)", line)
            a_amount_X = a_amount_X.group(1)
            a_amount_Y = re.search("Y\+(\d*)", line)
            a_amount_Y = a_amount_Y.group(1)
            sublist.append([int(a_amount_X), int(a_amount_Y)])
        elif "Button B" in line:
            b_amount_X = re.search("X\+(\d*)", line)
            b_amount_X = b_amount_X.group(1)
            b_amount_Y = re.search("Y\+(\d*)", line)
            b_amount_Y = b_amount_Y.group(1)
            sublist.append([int(b_amount_X), int(b_amount_Y)])
        elif "Prize" in line:
            prize_X = re.search("X\=(\d*)", line)
            prize_X = prize_X.group(1)
            prize_Y = re.search("Y\=(\d*)", line)
            prize_Y = prize_Y.group(1)
            sublist.append([int(prize_X), int(prize_Y)])
        else:
            arr.append(sublist)
    return arr


# FOR LATER:
#   * Switch to using a dict
#       - Have the key be a string with runningX:runningY
#       - This will help reduce space greatly 

def backtrack(game, runningX, runningY, cache, tokens):
    (aX, aY), (bX, bY), (prizeX, prizeY) = game
    if runningX > prizeX or runningY > prizeY:
        return -1 # Not possible with this configuration
    if runningX == prizeX and runningY == prizeY:
        return 1
    if cache[runningX][runningY] != float('inf'):
        return cache[runningX][runningY]
    
    pressA = backtrack(game, runningX + aX, runningY + aY, cache, tokens + 1)
    pressB = backtrack(game, runningX + bX, runningY + bY, cache, tokens + 3)
    cache[runningX][runningY] = min(pressA, pressB)

    if cache[runningX][runningY] != -1:
        cache[runningX][runningY] += 1

    return cache[runningX][runningY]


def solve_part_one(input):
    games = parse_input(input)
    result = 0
    for game in games:
        _, _, (prizeX, prizeY) = game
        cache = [[float('inf')] * (prizeY+1)] * (prizeX+1)
        backtrack(game, 0, 0, cache, 0)
        result += cache[prizeX][prizeY]
    return result

def solve_part_two(input):
    return None
