import os

scaffolding = """# Advent of Code {year} - Day {day}

def solve_part_one(input):
    return 0

def solve_part_two(input):
    return 0
"""

def create_input_dirs(year):
    print(f"Creating directories for AoC {year}!")
    
    for i in range(1, 26, 1):
        try:
            path = f"{year}/{i}"
            os.makedirs(path)
            
            with open(f"{year}/{i}/solution.py", "w") as file:
                file.write(scaffolding.format(year = year, day = i))
        except Exception as error:
            print(f"Skipping directory creation: {path}")
            
def cache_input(data, year, day):
    with open(f"{year}/{day}/input.txt", "w") as file:
        file.write(data)
        
def fetch_input(year, day):
    with open(f"{year}/{day}/input.txt", "r") as file:
        return file.read()