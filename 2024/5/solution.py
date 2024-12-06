# Advent of Code 2024 - Day 5
def validate(num, arr, seen):
    for a in arr:
        if a in seen:
            #print(a,'\n\n')
            #print(f"{num}|{a}")
            return False
    return True
        
def solve_part_one(input):
    before = {}
    for line in input:
        if '|' not in line:
            break
        be,af = line.split('|')
        if be not in before:
            before[be] = []
        before[be].append(af)

    count = 0
    for line_no, line in enumerate(input):
        if ',' not in line:
            continue
        
        order = line.split(',')
        seen = set()
        for num in order:
            seen.add(num)
            #print(num, before.get(num,[]))
            if num in before:
                valid = validate(num, before[num], seen)
                
                if not valid:
                    #print(line_no)
                    break
            
        else:
            mid_val = int(order[(len(order)-1)//2])
            count += mid_val
        
                
    return count

def issue(num, arr, seen):
    for a in arr:
        if a in seen:
            return a
    return ""
    


def is_still_bad(order, rules):
    seen = set()
    for num in order:
        seen.add(num)
        #print(num, before.get(num,[]))
        if num in rules:
            valid = validate(num, rules[num], seen)
            
            if not valid:
                return True, issue(num, rules[num], seen)
    return False, ""

def solve_part_two(input):
    before = {}
    for line in input:
        if '|' not in line:
            break
        be,af = line.split('|')
        if be not in before:
            before[be] = []
        before[be].append(af)

    count = 0
    for line_no, line in enumerate(input):
        if ',' not in line:
            continue
        
        order = line.split(',')
        seen = set()
        for num in order:
            seen.add(num)
            if num in before:
                valid = validate(num, before[num], seen)
                
                if not valid:
                    while True:
                        is_bad, issue = is_still_bad(order, before)
                        if not is_bad:
                            mid_val = int(order[(len(order)-1)//2])
                            count += mid_val
                            break
                        order.append(order.pop(order.index(issue)))
                    break

    return count
