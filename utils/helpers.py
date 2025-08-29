# utils/helpers.py

import json
import random

def load_quotes(file_path):
    """
    Load quotes from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file containing quotes.
    
    Returns:
        dict: A dictionary with moods as keys and lists of quotes as values.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            quotes_dict = json.load(f)
        return quotes_dict
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: {file_path} is not a valid JSON.")
        return {}

def get_quote_by_mood(quotes_dict, mood):
    """
    Select a random quote for the given mood.
    
    Args:
        quotes_dict (dict): Dictionary of quotes categorized by mood.
        mood (str): User's current mood.
    
    Returns:
        str: A randomly selected quote or a message if mood not found.
    """
    mood = mood.lower()  # make it case-insensitive
    if mood in quotes_dict:
        return random.choice(quotes_dict[mood])
    else:
        return "Sorry, no quotes available for this mood."
