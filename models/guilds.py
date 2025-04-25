"""
Guild (Server) configuration model.

Stores customizable settings for each server the bot is in. This includes
logging channels, custom command prefixes, bad word filters, and mute role IDs.

Fields:
- guild_id: Unique Discord server ID
- command_prefix: Prefix used for commands in this guild (default "!")
- log_channel_id: Channel to send moderation logs
- mute_role_id: ID of the role used to mute users
- bad_words: List of bad words specific to this guild
"""
