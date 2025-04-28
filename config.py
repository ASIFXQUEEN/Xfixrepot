import os
import json

class Config:
    # Telegram API
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    
    # Owner
    OWNER_ID = 6909450415  # Your ID
    
    # Account Storage
    ACCOUNTS_FILE = "accounts.json"
    
    # Proxy
    PROXY = None  # {"host":"1.1.1.1","port":80,"scheme":"socks5"}
