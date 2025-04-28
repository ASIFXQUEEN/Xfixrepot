from pyrogram import (
    Client,
    __version__
)
from pyrogram.raw.all import layer
from info import Config
import logging
from datetime import datetime
import logging.config
import os
from pytz import timezone
from aiohttp import web
from plugins import web_server
import pyromod

# Logging Configuration
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="ReportBot",
            in_memory=True,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins={'root': 'plugins'}
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        
        # Bot Information
        self.mention = me.mention
        self.username = me.username
        
        # Web Server Setup
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        
        try:
            await web.TCPSite(app, bind_address, Config.PORT).start()
            logging.info(f"✅ {me.first_name} with Pyrogram v{__version__} (Layer {layer}) started on {me.username}")
            
            # Notification to Owner
            if Config.OWNER:
                await self.send_message(
                    Config.OWNER,
                    f"**__{me.first_name} Is Started Successfully! ✨__**"
                )
        except Exception as e:
            logging.error(f"Failed to start web server: {str(e)}")
            raise

    async def stop(self, *args):
        await super().stop()
        logging.info("Bot Stopped ⛔")

if __name__ == "__main__":
    bot = Bot()
    bot.run()
