import json
from pathlib import Path
from datetime import datetime

CONFIG_FILE = Path("config.json")

def load():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
        
    return {}

def save(data):
    with open(CONFIG_FILE, "w") as file:
        json.dump(data, file, indent = 4)
        
def get_config(key):
    state = load()
    return state.get(key)

def set_config(key, value):
    state = load()
    state[key] = value
    save(state)
    
def update_last_outbound_api_call_time():
    set_config("last_outbound_api_call_time", datetime.now().isoformat())