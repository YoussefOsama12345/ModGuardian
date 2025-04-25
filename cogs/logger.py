"""
Logger Cog for ModGuardian Discord Bot.

This module listens to message deletion and edits, and logs them to a specific channel.
It provides transparency and moderation support by tracking chat history.

Environment Variable:
- LOG_CHANNEL_ID: The ID of the channel where logs will be sent.
"""

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID", 0))

class Logger(commands.Cog):
    """
    A Cog for logging deleted and edited messages in a server.
    Sends detailed embeds to the configured log channel.
    """

    def __init__(self, bot):
        """
        Initialize the Logger cog with the bot instance.

        Args:
            bot (commands.Bot): The Discord bot instance.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        """
        Listener that triggers when a message is deleted.
        Logs the content, author, and channel to the log channel.

        Args:
            message (discord.Message): The deleted message object.
        """
        if message.author.bot or not message.guild:
            return

        log_channel = self.bot.get_channel(LOG_CHANNEL_ID)
        if log_channel:
            embed = discord.Embed(
                title="🗑️ Message Deleted",
                description=f"**Author:** {message.author.mention}\n**Channel:** {message.channel.mention}",
                color=discord.Color.red()
            )
            embed.add_field(name="Content", value=message.content or "*(no content)*", inline=False)
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        """
        Listener that triggers when a message is edited.
        Logs the old and new content, author, and channel to the log channel.

        Args:
            before (discord.Message): The original message.
            after (discord.Message): The edited message.
        """
        if before.author.bot or not before.guild:
            return

        if before.content == after.content:
            return  # Skip if no content changed (e.g., embed-only change)

        log_channel = self.bot.get_channel(LOG_CHANNEL_ID)
        if log_channel:
            embed = discord.Embed(
                title="✏️ Message Edited",
                description=f"**Author:** {before.author.mention}\n**Channel:** {before.channel.mention}",
                color=discord.Color.orange()
            )
            embed.add_field(name="Before", value=before.content or "*(no content)*", inline=False)
            embed.add_field(name="After", value=after.content or "*(no content)*", inline=False)
            await log_channel.send(embed=embed)

async def setup(bot):
    """
    Asynchronously adds the Logger cog to the bot.

    Args:
        bot (commands.Bot): The Discord bot instance.
    """
    await bot.add_cog(Logger(bot))
