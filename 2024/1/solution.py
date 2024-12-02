# Advent of Code 2024 - Day 1

def solve_part_one(input):
    left = []
    right = []

    for line in input:
        split = line.split(" ")
        left.append(int(split[0]))
        right.append(int(split[-1]))

    left.sort()
    right.sort()

    dist = 0
    for i in range(len(left)):
        dist += abs(left[i] - right[i])

    return dist

def solve_part_two(input):
    left = []
    right = []

    for line in input:
        split = line.split(" ")
        left.append(int(split[0]))
        right.append(int(split[-1]))

    set_left = set(left)
    dict_right = {}

    for val in right:
        dict_right[val] = dict_right.get(val, 0) + 1

    similarity = 0
    for val in set_left:
        if val in dict_right:
            similarity += val * dict_right[val]

    return similarity