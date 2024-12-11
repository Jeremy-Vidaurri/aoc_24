import os

scaffolding = """# Advent of Code {year} - Day {day}

def solve_part_one(input):
    return None

def solve_part_two(input):
    return None
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
        
        print(f"Successfully cached puzzle input.")
    except Exception as error:
        print(f"Failed to cache puzzle input: {error}")
        
def cache_leaderboard(data: list[Participant]) -> None:
    """
    Writes private leaderboard data to disk. Saves to `leaderboard.txt`

    Args:
        data (str): Parsed response from AoC API

    Returns:
        None

    Raises:
        Exception
            Encountered error while writing to disk
    """
    
    print(f"Attempting to cache private leaderboard data...")
    
    participant_data = [participant.to_json() for participant in data]
    
    try:
        with open("leaderboard.txt", "w") as file:
            json.dump(participant_data, file, indent = 4)
            
        print(f"Successfully cached private leaderboard data.")
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
        FileNotFoundError
            File does not exist
    """
    
    print(f"Attempting to fetch cached puzzle input...")
    
    try:
        with open(f"{year}/{day}/{year}_{day}_input.txt", "r") as file:
            print(f"Successfully fetched cached puzzle input.")
            return file.read()
    except FileNotFoundError:
        print(f"{year}/{day}/{year}_{day}_input.txt not found.")
        
def fetch_leaderboard() -> list[Participant]:
    """
    Reads private leaderboard data from file. File must exist at `leaderboard.txt`

    Args:
        None

    Returns:
        list[Participant]: List of participant data

    Raises:
        FileNotFoundError
            File does not exist
        JSONDecodeError
            Fle contains malformed JSON data
    """
    
    print("Attempting to fetch cached private leaderboard data...")
    
    try:
        with open("leaderboard.txt", "r") as file:
            data = json.load(file)
            
        print("Successfully fetched cached private leaderboard data.")
        return [Participant.load(participant) for participant in data]
    except FileNotFoundError:
        print(f"leaderboard.txt not found. Returning an empty list.")
        return []
    except json.JSONDecodeError:
        print(f"leaderboard.txt contains invalid JSON. Returning an empty list.")
    
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
            print("Successfully fetched cached sample puzzle input.")
            return file.read()
    except Exception as error:
        print(f"Failed to fetch sample puzzle input: {error}")
    
def in_bounds_2d(x: int, y: int, width: int, height: int) -> bool:
    """
    Check if a particular coord is within the bounds of a 2D list

    Args:
        x (int): x coord
        y (int): y coord
        width (int): width of 2D list
        height (int): height of 2D list

    Returns:
        bool: The result of the check.

    Raises:
        None
    """

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

    return 0 <= index <= length

def get_middle_object(data: list[any]) -> any:
    """
    Gets object in the middle of the list. Because this is done with integer division, if the length of the list has even parity this function will return the right side of the two middle objects

    Args:
        data (list[any]): list

    Returns: 
        any: object in the middle of the list

    Raises:
        None
    """
    
    return data[int(len(data) / 2)]

def fetch_neighbors_2d(data: list[list[any]], x: int, y: int) -> set[any]:
    """
    Get the neighbors of a coordinate in a 2D list.

    Args:
        data (list[list[any]]): 2D list
        x (int): x coord
        y (int): y coord

    Returns:
        set[any]: The unique neighbors of the given coordinate

    Raises:
        None
    """
    
    neighbors = set()
    width = len(data[0])
    height = len(data)

    # Up
    dx, dy = 0, -1
    if in_bounds_2d(x + dx, y + dy, width, height):
        neighbors.add((x + dx, y + dy))

    # Down
    dx, dy = 0, 1 
    if in_bounds_2d(x + dx, y + dy, width, height):
        neighbors.add((x + dx, y + dy))

    # Left
    dx, dy = -1, 0
    if in_bounds_2d(x + dx, y + dy, width, height):
        neighbors.add((x + dx, y + dy))

    # Right
    dx, dy = 1, 0
    if in_bounds_2d(x + dx, y + dy, width, height):
        neighbors.add((x + dx, y + dy))

    return neighbors

def fetch_neighbors_2d(data: list[list[any]], coords: tuple[int, int]) -> set[any]:
    """
    Get the neighbors of a coordinate in a 2D list.

    Args:
        data (list[list[any]]): 2D list
        coords (tuple[int, int]): x and y coordinates

    Returns:
        set[any]: The unique neighbors of the given coordinate

    Raises:
        None
    """
    
    return fetch_neighbors_2d(data, coords[0], coords[1])