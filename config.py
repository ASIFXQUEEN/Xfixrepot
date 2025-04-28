import os

class Config:
    # Telegram (Required)
    API_ID = int(os.environ.get("API_ID", 12345))  # my.telegram.org se
    API_HASH = os.environ.get("API_HASH", "")      # my.telegram.org se
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")    # @BotFather se
    
    # Owner
    OWNER_ID = int(os.environ.get("OWNER_ID", 123456789))  # @userinfobot se apna ID lein
    
    # Proxy (Optional)
    PROXY = None  # {"host":"1.1.1.1", "port":80, "scheme":"socks5"}
