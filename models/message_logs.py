"""
Message log model to store edited or deleted messages.

Used to help moderators audit changes, especially for abuse of edits or
attempts to delete inappropriate content.

Fields:
- message_id: Original message ID
- user_id: Author of the message
- guild_id: Server where message was sent
- channel_id: Channel where message was sent
- action: "edited" or "deleted"
- original_content: Before edit or deletion
- edited_content: After edit (if applicable)
- timestamp: When the log was recorded
"""
