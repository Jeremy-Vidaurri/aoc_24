# Advent of Code 2024 - Day 13
import re
import numpy as np

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
    arr.append(sublist)
    return arr

def try_solution(game):
    (aX, aY), (bX,bY), (prizeX, prizeY) = game
    aCount = 0
    while aCount < 100:
        bCount = (prizeX - prizeY - aCount*(aX-aY)) // (bX-bY)
        curX = aCount * aX + bCount * bX
        curY = aCount * aY + bCount * bY
        if curX == prizeX and curY == prizeY:
            return aCount, bCount
        aCount += 1
    return -1, -1


def solve_part_one(input):
    games = parse_input(input)
    result = 0
    for game in games:
        aCount, bCount = try_solution(game)

        if aCount >= 0 and bCount >= 0:
            #print(aCount, bCount)
            result += aCount * 3 + bCount
        
    return result

def try_with_start(game, startX):
    (aX, aY), (bX,bY), (prizeX, prizeY) = game
    prizeX += 10000000000000
    prizeY += 10000000000000
    aCount = startX
    while aCount - startX < 4:
        print
        bCount = (prizeX - prizeY - aCount*(aX-aY)) // (bX-bY)
        curX = aCount * aX + bCount * bX
        curY = aCount * aY + bCount * bY
        if curX == prizeX and curY == prizeY:
            return aCount, bCount
        aCount += 1
    return -1, -1

def solve_part_two(input):
    games = parse_input(input)
    result = 0
    for game in games:
        (aX, aY), (bX,bY), (prizeX, prizeY) = game
        left = np.array([[aX, bX], [aY, bY]])
        right = np.array([prizeX + 10000000000000, prizeY + 10000000000000])
        solution = np.linalg.solve(left,right)

        aCount, bCount = try_with_start(game, int(solution[0]) - 1)
        if aCount >= 0 and bCount >= 0:
            #print(aCount, bCount)
            result += aCount * 3 + bCount
    print(result)
    return None
