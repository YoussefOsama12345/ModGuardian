"""
InfractionService

Handles creation, querying, and expiration of moderation actions such as 
warnings, mutes, bans, and kicks. This service is responsible for managing 
the core logic of user discipline across the guild.

Responsibilities:
- Add new infractions to the database
- Track active punishments (e.g., temp mutes)
- Expire infractions after their duration
- Retrieve user infraction history
"""
