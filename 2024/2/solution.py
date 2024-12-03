# Advent of Code 2024 - Day 2

def is_safe(report, dir):
    for i in range(len(report) - 1):
        if (int(report[i+1]) - int(report[i]) > 3 or int(report[i+1]) - int(report[i]) <= 0) and dir == 1:
            return False
        if (int(report[i+1]) - int(report[i]) < -3 or int(report[i+1]) - int(report[i]) >= 0) and dir == -1:
            return False
    return True

def solve_part_one(input):
    safe_total = 0

    for line in input:
        line_split = line.split(' ')
        dir = 1 if int(line_split[0]) < int(line_split[1]) else -1 if int(line_split[0]) > int(line_split[1]) else 0

        # Even line
        if dir == 0:
            continue

        safe_total += 1 if is_safe(line_split, dir) else 0

    return safe_total

def brute_force(report):
    for i in range(len(report)):
        tmp = report.pop(i)
        dir = 1 if int(report[0]) < int(report[1]) else -1 if int(report[0]) > int(report[1]) else 0
        if (dir != 0 and is_safe(report, dir)):
            return True
        report.insert(i, tmp)
    return False

def solve_part_two(input):
    safe_total = 0
    for line in input:
        line_split = line.split(' ')

        safe_total += 1 if brute_force(line_split) else 0
    return safe_total

        
