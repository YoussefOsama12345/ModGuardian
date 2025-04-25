"""
User model for tracking Discord users within a specific guild.

Each entry represents a user in a server and stores basic state flags such as
mute or ban status. Used for real-time checks and moderation history context.

Fields:
- user_id: Discord user ID
- guild_id: Discord server ID
- is_banned: Boolean indicating if user is currently banned
- is_muted: Boolean indicating if user is currently muted
- last_seen: Timestamp of last interaction (optional for logging)
"""