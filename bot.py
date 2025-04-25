"""
Main entry point for the ModGuardian Discord bot.

Responsibilities:
- Loads configuration from settings.py
- Initializes the bot instance with required intents
- Dynamically loads all command and event cogs from the /cogs folder
- Starts the bot and handles connection lifecycle
"""

import discord
from discord.ext import commands
import os
import asyncio
from config import settings

INTENTS = discord.Intents.all()
INTENTS.message_content = True     
INTENTS.members = True  

bot = commands.Bot(command_prefix=settings.COMMAND_PREFIX, intents=INTENTS)

@bot.event
async def on_ready():
    """
    Event triggered when the bot successfully connects to Discord.

    Prints a confirmation message with bot username and ID.
    """
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")
    print("💬 Bot is now running...")

async def load_cogs():
    """
    Dynamically loads all Python cog modules from the ./cogs directory.

    Each .py file in /cogs is assumed to be a valid Cog extension.
    """
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"🔧 Loaded cog: {filename}")

async def main():
    try:
        async with bot:
            await load_cogs()
            await bot.start(settings.BOT_TOKEN)
    except Exception as e:
        print("🔥 An error occurred:", e)

asyncio.run(main())
