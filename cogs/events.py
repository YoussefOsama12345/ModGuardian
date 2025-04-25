"""
Events Cog for ModGuardian Discord Bot.

Handles server event listeners such as:
- Welcoming new members
- Logging member departures
- Global command error handling

This module improves the server experience and provides user-friendly feedback.
"""

import discord
from discord.ext import commands

class Events(commands.Cog):
    """Cog for handling server join/leave events and command errors."""

    def __init__(self, bot):
        """
        Initialize the Events cog with the bot instance.

        Args:
            bot (commands.Bot): The Discord bot instance.
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        """
        Send a welcome message when a member joins the server.

        Args:
            member (discord.Member): The member who joined.
        """
        welcome_channel = discord.utils.get(member.guild.text_channels, name='general') or member.guild.system_channel
        if welcome_channel:
            await welcome_channel.send(f"👋 Welcome {member.mention} to **{member.guild.name}**! Enjoy your stay!")

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        """
        Send a farewell message when a member leaves the server.

        Args:
            member (discord.Member): The member who left.
        """
        goodbye_channel = discord.utils.get(member.guild.text_channels, name='general') or member.guild.system_channel
        if goodbye_channel:
            await goodbye_channel.send(f"👋 **{member.name}** has left the server.")

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        """
        Handle command errors globally.

        Args:
            ctx (commands.Context): The context of the command.
            error (commands.CommandError): The error that occurred.
        """
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("🚫 You don’t have permission to use this command.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("⚠️ You missed a required argument.")
        elif isinstance(error, commands.CommandNotFound):
            pass 
        else:
            await ctx.send("❌ An unexpected error occurred.")
            raise error  

async def setup(bot):
    """Asynchronously add the Events cog to the bot."""
    await bot.add_cog(Events(bot))
