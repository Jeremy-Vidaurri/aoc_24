import json
from pathlib import Path
from datetime import datetime

CONFIG_FILE = Path("config.json")
    
def get_config(key: str) -> str | dict:
    """
    Gets value from config file

    Args:
        key (str): Config value to get

    Returns:
        Config value

    Raises:
        FileNotFoundError
            Config file not found. Returns empty dict.
        JSONDecodeError
            Config file contains malformed JSON
    """
    
    try:
        state = _load()
        return state.get(key)
    except FileNotFoundError:
        print("Config file not found")
        return {}
    except json.JSONDecodeError:
        print("Config file contains malformed JSON")
        return {}

def set_config(key: str, value: str | dict) -> None:
    """
    Sets values in config file

    Args:
        key (str): Config value to set
        value (str | dict): Value of configuration

    Returns:
        None

    Raises:
        FileNotFoundError
            Config file not found. Returns empty dict.
        JSONDecodeError
            Config file contains malformed JSON
    """
    
    try:
        state = _load()
        state[key] = value
        _to_json(state)
    except FileNotFoundError:
        print("Config file not found")
    except json.JSONDecodeError:
        print("Config file contains malformed JSON")
    
def update_last_outbound_api_call_time() -> None:
    """
    Updates last outbound API call time in config file to current time. This is used to throttle input data requests.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """
    
    set_config("last_outbound_api_call_time", datetime.now().isoformat())
    
def update_last_leaderboard_api_call_time() -> None:
    """
    Updates last outbound leaderboard API call time in config file to current time. This is used to throttle private leaderboard requests.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """
    
    set_config("last_leaderboard_api_call_time", datetime.now().isoformat())
    
# ---------- Internal Functions ----------

def _load():
    with open(CONFIG_FILE, "r") as file:
        return json._load(file)

def _to_json(data):
    with open(CONFIG_FILE, "w") as file:
        json.dump(data, file, indent = 4)