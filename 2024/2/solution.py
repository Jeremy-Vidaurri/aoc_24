# Advent of Code 2024 - Day 2

def solve_part_one(input):
    total_safe = 0
    
    for line in input:
        parts = list(map(int, line.split()))
        pointer = 0
        last_num = -1
        is_increasing = None
        safe = True
        
        while pointer < len(parts) and safe == True:
            if last_num == -1:
                last_num = parts[pointer]
                pointer += 1
                continue
            elif parts[pointer] == last_num:
                safe = False
                continue
                
            if is_increasing == None:
                if abs(parts[pointer] - last_num > 3):
                    safe = False
                    break
                elif parts[pointer] > last_num:
                    is_increasing = True
                else:
                    is_increasing = False
                    
            if (parts[pointer] - last_num > 3 and is_increasing == True) or (parts[pointer] < last_num and is_increasing == True):
                safe = False
                break
            elif (parts[pointer] - last_num < -3 and is_increasing == False) or (parts[pointer] > last_num and is_increasing == False):
                safe = False
                break
            
            last_num = parts[pointer]
            pointer += 1
                
        if safe == True:
            total_safe += 1       
        
    return total_safe

def solve_part_two(input):
    total_safe = 0     
        
    return total_safe
