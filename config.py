import os

class Config:
    # Telegram API (Get from my.telegram.org)
    API_ID = int(os.environ.get("API_ID", 12345))  
    API_HASH = os.environ.get("API_HASH", "your_api_hash_here")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_bot_token_here")

    # Owner Settings
    OWNER_ID = 6909450415  # 👈 Your ID hardcoded
    PROXY = None  # {"host":"1.1.1.1", "port":80, "scheme":"socks5"}
