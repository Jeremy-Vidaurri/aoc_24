import aoc_gateway
import importlib
import util
import os
import config_manager
import time

def create_dirs():
    year = config_manager.get_config("year")
    
    # If this year's directory exists, we likely ran this successfully already.
    if not os.path.exists(f"{year}/"):
        util.create_input_dirs(year)

def fetch_input():
    year = config_manager.get_config("year")
    day = config_manager.get_config("day")
    
    try:
        response = aoc_gateway.fetch_input(year, day)
        util.cache_input(response, year, day)
    except Exception as error:
        print(error)

def run_solution():
    year = config_manager.get_config("year")
    day = config_manager.get_config("day")
    part = config_manager.get_config("part")
    
    # Dynamically fetch the appropriate solution module
    try:
        module_name = f"{year}.{day}.solution"
        solution_module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        print(f"Solution for {year} day {day} not found")
    
    input_data = util.fetch_input(year, day).splitlines()
    
    if part == 1:
        start_time = time.perf_counter()
        result = solution_module.solve_part_one(input_data)
        end_time = time.perf_counter()
        
        execution_time = end_time - start_time
        print(f"Solution execution time: {execution_time * 1000:.3f} ms")
        
        response = aoc_gateway.submit_answer(year, day, part, result)
        print(response)
    elif part == 2:
        start_time = time.perf_counter()
        result = solution_module.solve_part_two(input_data)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Solution execution time: {execution_time * 1000:.3f} ms")
        
        response = aoc_gateway.submit_answer(year, day, part, result)
        print(response)
        
def print_leaderboard():
    participants = aoc_gateway.fetch_leaderboard()
    for participant in participants:
        position_str = "N/A " if participant.position == None else str(participant.position) + ') '
        print(f"{position_str:<5} {participant.name:<25} {str(participant.stars) + '★':<5}")

def main():
    display_leaderboard = config_manager.get_config("display_leaderboard")
    if display_leaderboard:  
        print_leaderboard()
    
    # Create scaffolded directories and solution files
    create_dirs()
    
    # Fetch input data from Advent of Code website and cache data on disk
    fetch_input()
    
    # Run solution!
    run_solution()

if __name__ == "__main__":
    main()