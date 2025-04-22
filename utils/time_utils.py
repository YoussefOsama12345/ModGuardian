"""
Time Utilities for ModGuardian Bot.

Provides utility functions for parsing human-readable duration strings
(e.g., "10m", "2h") into their equivalent time in seconds. Used for
temporary mutes and scheduled moderation tasks.
"""

def parse_duration(duration_str: str) -> int:
    """
    Parse a duration string into seconds.

    Supported time suffixes:
        - 's' for seconds
        - 'm' for minutes
        - 'h' for hours
        - 'd' for days

    If the suffix is missing or invalid, defaults to 60 (minutes).
    If parsing fails, defaults to 600 seconds (10 minutes).

    Args:
        duration_str (str): The duration string (e.g., "10m", "2h").

    Returns:
        int: The duration in seconds.
    """
    units = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    try:
        unit = duration_str[-1]
        amount = int(duration_str[:-1])
        return amount * units.get(unit, 60)  # default to minutes
    except Exception:
        return 600  # fallback to 10 minutes
