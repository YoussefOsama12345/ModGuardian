"""
MessageLogService

Logs deleted and edited messages to support audit trails and moderation
transparency within Discord servers.

Responsibilities:
- Save deleted messages with author, channel, and timestamp
- Save edited messages with before/after content
- Retrieve message logs for analysis or embeds
"""
