"""
Entrypoint script for running the ModGuardian bot.

This script imports and executes the `main()` function from the bot module,
which starts the Discord bot using the provided settings and loaded cogs.

Usage:
    python run.py
"""

from bot import main

if __name__ == "__main__":
    main()
