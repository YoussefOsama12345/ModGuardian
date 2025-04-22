"""
Bad Word Loader Utility for ModGuardian Bot.

This module provides a function to load a list of banned or filtered words
from a JSON file. It is used by the Filters Cog to perform automatic
message moderation.

Expected file: data/bad_words.json
Format: A JSON array of strings (bad words).
"""

import json

def load_bad_words(path="data/bad_words.json"):
    """
    Load a list of bad words from a JSON file.

    Args:
        path (str): Path to the bad words JSON file. Defaults to "data/bad_words.json".

    Returns:
        list: A list of bad words to be used for content filtering.
              Returns an empty list if the file is not found.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
