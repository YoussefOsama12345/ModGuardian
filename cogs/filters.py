"""
Filters Cog for ModGuardian Discord Bot.

This module provides automatic message moderation features including:
- Bad word filtering based on a loaded JSON word list
- Simple anti-spam detection based on repeated messages

It ensures a clean and safe server environment by monitoring user messages in real-time.
"""

import discord
from discord.ext import commands
from utils.bad_word_loader import load_bad_words

class Filters(commands.Cog):
    """
    A Cog for moderating server messages by filtering offensive language
    and detecting basic spam behavior.
    """

    def __init__(self, bot):
        """
        Initializes the Filters cog with the bot instance and loads the bad word list.

        Args:
            bot (commands.Bot): The Discord bot instance.
        """
        self.bot = bot
        self.message_cache = {}
        self.bad_words = load_bad_words()

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        """
        Listener for new messages. Filters out offensive language and repeated spam.

        Args:
            message (discord.Message): The message sent in a server channel.
        """
        if message.author.bot or not message.guild:
            return

        content_lower = message.content.lower()

        # 🚫 Bad word filter
        for word in self.bad_words:
            if word.strip() in content_lower:
                await message.delete()
                await message.channel.send(
                    f"🚫 {message.author.mention}, please avoid using inappropriate language!"
                )
                return

        # 🛑 Simple anti-spam detection: repeated messages
        user_id = message.author.id
        user_msgs = self.message_cache.get(user_id, [])
        user_msgs.append(message.content)

        # Keep only last 5 messages for comparison
        if len(user_msgs) > 5:
            user_msgs = user_msgs[-5:]

        self.message_cache[user_id] = user_msgs

        if user_msgs.count(message.content) >= 3:
            await message.delete()
            await message.channel.send(
                f"⚠️ {message.author.mention}, please avoid spamming the chat."
            )
            self.message_cache[user_id] = []

async def setup(bot):
    """
    Asynchronously adds the Filters cog to the bot.

    Args:
        bot (commands.Bot): The Discord bot instance.
    """
    await bot.add_cog(Filters(bot))
