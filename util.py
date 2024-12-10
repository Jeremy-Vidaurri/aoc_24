import os

scaffolding = """
# Advent of Code {year} - Day {day}

def solve_part_one(input):
    return None

def solve_part_two(input):
    return None
"""

def create_daily_dirs(year: str) -> None:
    """
    Creates daily directories for the AoC year. This includes a parent directory `year` along with daily directories containing a scaffolded `solution.py`
    
    Args:
        year (str): AoC year
        
    Returns:
        None
        
    Raises:
        None

    """
    print(f"Creating daily directories for AoC {year}!")
    
    for i in range(1, 26, 1):
        try:
            path = f"{year}/{i}"
            os.makedirs(path)
            
            with open(f"{year}/{i}/solution.py", "w") as file:
                file.write(scaffolding.format(year = year, day = i))
        except Exception as error:
            print(f"Skipping directory creation: {path} ({error})")
            
def cache_input(data: str, year: str, day: str) -> None:
    """
    Writes puzzle input data to disk. Saves to `year/day/year_day_input.txt`

    Args:
        data (str): response from AoC API request
        year (str): puzzle year
        day (str): puzzle day

    Returns:
        None

    Raises:
        None
    """
    
    print(f"Attempting to cache puzzle input...")
    
    try:
        with open(f"{year}/{day}/{year}_{day}_input.txt", "w") as file:
            file.write(data)
    except Exception as error:
        print(f"Failed to cache puzzle input: {error}")
        
def fetch_input(year: str, day: str) -> str:
    """
    Reads puzzle input from file. File must exist at `year/day/year_day_input.txt`

    Args:
        year (str): puzzle year
        day (str): puzzle day

    Returns:
        str: The contents of the file

    Raises:
        None
    """
    
    print(f"Attempting to fetch puzzle input...")
    
    try:
        with open(f"{year}/{day}/{year}_{day}_input.txt", "r") as file:
            return file.read()
    except Exception as error:
        print(f"Failed to fetch puzzle input: {error}")
    
def fetch_sample_input(year: str, day: str) -> str:
    """
    Reads sample puzzle input from file. This typically is copy-pasted directly from AoC problem description. File must exist at `year/day/sample_input.txt`

    Args:
        year (str): puzzle year
        day (str): puzzle day

    Returns:
        str: The contents of the file

    Raises:
        None
    """
    
    print(f"Attempting to fetch sample puzzle input...")
    
    try:
        with open(f"{year}/{day}/sample_input.txt", "r") as file:
            return file.read()
    except Exception as error:
        print(f"Failed to fetch sample puzzle input: {error}")
    
def in_bounds_2d(x: int, y: int, width: int, height: int) -> bool:
    """
    Check if a particular coord is within the bounds of a 2D list

    Args:
        x (int): X coord
        y (int): Y coord
        width (int): width of 2D list
        height (int): height of 2D list

    Returns:
        bool: The result of the check.

    Raises:
        None
    """
    
    print(f"Checking if coord is in bounds x: {x}, y: {y}, width: {width}, height: {height}")

    return 0 <= x < width and 0 <= y < height

def in_bounds(index: int, length: int) -> bool:
    """
    Check if a particular index is within the bounds of a list

    Args:
        index (int): index of list
        length (int): length of list

    Returns:
        bool: The result of the check.

    Raises:
        None
    """
    
    print(f"Checking if index is in bounds index: {index}, length: {length}")

    return 0 <= index <= length
