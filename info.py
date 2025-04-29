class Config:
    OWNER = 5099049612
    SUDO = [5099049612]


class Txt:
    START_TXT = """Hey {},

I am a Branded Mass Report Bot.

Use /help to see available commands."""
    
    HELP_TXT = """
<b>Available Commands:</b>

/start - Start the bot
/help - Show help message
/report - Start reporting
/make_config - Make target config
"""

    REPORT_CHOICE = """<b>Choose Report Reason:</b>

1. Child Abuse
2. Copyrighted Content
3. Impersonation
4. Irrelevant Geogroup
5. Illegal Drug
6. Violence
7. Offensive Personal Detail
8. Pornography
9. Spam
"""

    SEND_NO_OF_REPORT_MSG = "How many times should I report the target <b>@{}</b>?"
