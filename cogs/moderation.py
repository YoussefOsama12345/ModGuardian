"""
Moderation Cog for ModGuardian Discord Bot.

Provides core moderation commands:
- Kick
- Ban
- Mute (with optional duration)
- Unmute

This module helps moderators enforce server rules and manage member behavior.
"""

import discord
from discord.ext import commands
from discord.ext.commands import Context
import asyncio
import os
from dotenv import load_dotenv
from utils.time_utils import parse_duration

# Load environment variables from .env
load_dotenv()

# Name of the mute role, default is "Muted"
MUTE_ROLE_NAME = os.getenv("MUTE_ROLE_NAME", "Muted")

class Moderation(commands.Cog):
    """
    A Cog for managing moderation commands like kick, ban, mute, and unmute.
    """

    def __init__(self, bot):
        """
        Initialize the Moderation cog with the bot instance.

        Args:
            bot (commands.Bot): The Discord bot instance.
        """
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx: Context, member: discord.Member, *, reason=None):
        """
        Kick a member from the server.

        Args:
            ctx (Context): The command context.
            member (discord.Member): The member to be kicked.
            reason (str, optional): The reason for the kick.
        """
        await member.kick(reason=reason)
        await ctx.send(f"👢 {member.mention} has been kicked. Reason: {reason or 'No reason provided'}")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx: Context, member: discord.Member, *, reason=None):
        """
        Ban a member from the server.

        Args:
            ctx (Context): The command context.
            member (discord.Member): The member to be banned.
            reason (str, optional): The reason for the ban.
        """
        await member.ban(reason=reason)
        await ctx.send(f"⛔ {member.mention} has been banned. Reason: {reason or 'No reason provided'}")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx: Context, member: discord.Member, duration: str = "10m"):
        """
        Temporarily mute a member by assigning the mute role.

        Args:
            ctx (Context): The command context.
            member (discord.Member): The member to be muted.
            duration (str, optional): Duration for the mute (e.g., "10m", "1h").
        """
        mute_role = discord.utils.get(ctx.guild.roles, name=MUTE_ROLE_NAME)
        if not mute_role:
            mute_role = await ctx.guild.create_role(name=MUTE_ROLE_NAME)
            for channel in ctx.guild.channels:
                await channel.set_permissions(mute_role, send_messages=False, speak=False)

        await member.add_roles(mute_role)
        await ctx.send(f"🔇 {member.mention} has been muted for {duration}")

        seconds = parse_duration(duration)
        await asyncio.sleep(seconds)

        if mute_role in member.roles:
            await member.remove_roles(mute_role)
            await ctx.send(f"🔊 {member.mention} has been unmuted after {duration}")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx: Context, member: discord.Member):
        """
        Unmute a member by removing the mute role.

        Args:
            ctx (Context): The command context.
            member (discord.Member): The member to be unmuted.
        """
        mute_role = discord.utils.get(ctx.guild.roles, name=MUTE_ROLE_NAME)
        if mute_role and mute_role in member.roles:
            await member.remove_roles(mute_role)
            await ctx.send(f"🔊 {member.mention} has been unmuted.")
        else:
            await ctx.send("⚠️ That user is not muted.")

async def setup(bot):
    """
    Asynchronously adds the Moderation cog to the bot.

    Args:
        bot (commands.Bot): The Discord bot instance.
    """
    await bot.add_cog(Moderation(bot))
