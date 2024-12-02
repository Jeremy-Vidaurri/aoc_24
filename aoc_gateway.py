import requests
import os
import config_manager
from models import Participant
from datetime import datetime
from bs4 import BeautifulSoup

def fetch_input(year, day):
    print(f"Fetching input data for day {day} ({year})...")
    
    if os.path.exists(f"{year}/{day}/{year}_{day}_input.txt"):
        raise Exception(f"Input data for day {day} ({year}) already cached.")
    
    if minutes_since_last_outbound_call() < int(config_manager.get_config("outbound_api_call_throttle")):
        raise Exception(f"Cancelling AoC endpoint request; the last request was too recent.")
    
    url = f"https://adventofcode.com/{year}/day/{day}/input"

    response = requests.get(url, headers = fetch_headers())
    
    config_manager.update_last_outbound_api_call_time()

    if response.status_code == 200:
        data = response.text
        return data
    else:
        raise Exception(f"AoC endpoint request failed. Status code: {response.status_code}")
    
def submit_answer(year, day, part, answer):
    print(f"Submiting answer ({answer}) for day {day} - part {part} puzzle ({year})...")
    
    url = f"https://adventofcode.com/{year}/day/{day}/answer"
    payload = {
        "level": part,
        "answer": answer
    }
    
    response = requests.post(url, headers = fetch_headers(), data = payload)
    
    if response.status_code == 200:
        data = response.text
        return parse_answer_response(data)
    else:
        raise Exception(f"AoC endpoint request failed. Status code: {response.status_code}")
    
def fetch_leaderboard():
    print(f"Fetching private leaderboard stats...")
    
    response = requests.get(config_manager.get_config("private_leaderboard_url"), headers = fetch_headers())
    
    if response.status_code == 200:
        participants = []
        
        soup = BeautifulSoup(response.text, 'html.parser')
        priv_board_rows = soup.find_all(class_ = 'privboard-row')
        priv_board_rows = priv_board_rows[1:]
        
        for row in priv_board_rows:
            participant = Participant()
            
            # Parse the participant's name
            name_div = row.find(class_ = 'privboard-name')
            if name_div:
                name_text = name_div.get_text()
                if '(AoC++)' in name_text:
                    name_text = name_text.replace(' (AoC++)', '')
                participant.name = name_text
            
            # Parse the participant's number of stars
            two_star_divs = row.find(class_ = 'privboard-star-both')
            one_star_divs = row.find(class_ = 'privboard-star-firstonly')
            
            total_stars = 0
            
            if two_star_divs:
                total_stars += 2 * len(two_star_divs)
                
            if one_star_divs:
                total_stars += len(one_star_divs)
            
            participant.stars = total_stars
            
            # Parse the participant's leaderboard position
            position = None
  
            position_div = row.find(class_ = 'privboard-position')
            if position_div and participant.stars > 0:
                position_text = position_div.get_text()
                position_text = position_text.replace(')', '')
                
                position = int(position_text)
                
            participant.position = position
            
            participants.append(participant)
            
        return participants
            
    else:
        raise Exception(f"AoC endpoint request failed. Status code: {response.status_code}") 
    
def minutes_since_last_outbound_call():
    last_call_str = config_manager.get_config("last_outbound_api_call_time")
    last_call = datetime.fromisoformat(last_call_str)
    current_time = datetime.now()
    time_difference = current_time - last_call
    return time_difference.total_seconds() / 60

def fetch_headers():
    return {
        "User-Agent": config_manager.get_config("user_data")["user_agent"],
        "Cookie": os.getenv("AOC_COOKIE")
    }
    
def parse_answer_response(response):
    soup = BeautifulSoup(response, 'html.parser')
    
    article = soup.find('article')
    paragraph = article.find('p')
    result = paragraph.get_text()
    
    if "Did you already complete it?" in result:
        result = "Puzzle already completed!"
    elif "That's the right answer!" in result:
        result = "Correct answer!"
    elif "That's not the right answer." in result:
        result = "Wrong answer!"
    elif "your answer is too high" in result:
        result = "Submitted answer is ABOVE the expected answer..."
        
    return result