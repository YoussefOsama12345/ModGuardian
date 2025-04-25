"""
Case model for assigning a unique moderation log number to each infraction.

This allows clean audit trails and structured logs, like "Case #42 — Mute".

Fields:
- case_id: Auto-incremented primary ID for each case
- guild_id: Server where the case was created
- infraction_id: FK linking to the related infraction
- case_number: Custom case number per guild
- status: Status of the case ("open", "closed", "appealed")
"""
