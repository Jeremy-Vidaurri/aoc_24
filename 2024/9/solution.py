# Advent of Code 2024 - Day 9

def parse_input(input):
    for line in input:
        return [char for char in line]

def format_disk(disk_map):
    arr = []
    idx = 0
    for i, char in enumerate(disk_map):
        if i % 2 == 0:
            arr.extend([idx]*int(char))
            idx += 1
        else:
            arr.extend(['.']*int(char))

    return arr

def move_blocks(disk_map):
    start = 0
    end = len(disk_map) - 1

    while (start < end):
        if disk_map[start] != '.':
            start += 1
        elif disk_map[end] == '.':
            end -= 1
        else:
            disk_map[start] = disk_map[end]
            disk_map[end] = '.'
            start += 1
            end -= 1
    return disk_map
    
def calc_checksum(disk_map):
    result = 0
    for i in range(len(disk_map)):
        if disk_map[i] != '.':
            result += int(disk_map[i]) * i
    return result

def solve_part_one(input):
    disk_map = parse_input(input)
    formatted_disk = format_disk(disk_map)
    formatted_disk = move_blocks(formatted_disk)
    return calc_checksum(formatted_disk)

def get_file_length(disk_map, end):
    for i in range(end, -1, -1):
        if disk_map[i] != disk_map[end]:
            return end - i
    # Went through the whole list and it's all the same at this point
    return end + 1

def get_space_length(disk_map, start):
    for i in range(start, len(disk_map)):
        if disk_map[i] != '.':
            return i - start
    # Went through the whole list and it's all the same at this point
    return len(disk_map) - start

def update_block(disk_map, size, end):
    start = 0
    while start <= end - size:
        if disk_map[start] == ".":
            length = get_space_length(disk_map, start)
            if length >= size:
                for i in range(start, start+size):
                    disk_map[i] = disk_map[end]

                for i in range(end, end-size, -1):
                    disk_map[i] = '.'
                return disk_map

        start += 1
    return disk_map

def move_whole_blocks(disk_map):
    end = len(disk_map) - 1

    # No need to keep track of start
    while end >= 0:
        if disk_map[end] == '.':
            end -= 1
        else:
            length = get_file_length(disk_map, end)
            update_block(disk_map, length, end)
            end -= length
    # Find length of block and search for first empty block that has the same size
    return disk_map

def solve_part_two(input):
    disk_map = parse_input(input)
    formatted_disk = format_disk(disk_map)
    formatted_disk = move_whole_blocks(formatted_disk)
    return calc_checksum(formatted_disk)
