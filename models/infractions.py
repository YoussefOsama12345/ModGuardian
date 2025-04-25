"""
Infraction model for storing moderation actions.

Used to track warnings, kicks, bans, and mutes. Each infraction includes the
moderator, user, reason, type of infraction, and duration (if applicable).

Fields:
- user_id: ID of the user receiving the infraction
- guild_id: Server where the infraction occurred
- moderator_id: ID of the moderator who issued it
- type: Type of infraction ("warn", "mute", "ban", "kick")
- reason: Optional explanation for the action
- issued_at: When the action was issued
- duration_seconds: Duration of the action (e.g., temp mute)
- active: Whether the infraction is still active
"""
