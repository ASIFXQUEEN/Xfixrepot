from telethon import TelegramClient, events
import os
import time

client = TelegramClient('session', 
                       int(os.environ['API_ID']), 
                       os.environ['API_HASH']).start(bot_token=os.environ['BOT_TOKEN'])

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply("🚀 Bot Ready! Use /report @username reason")

@client.on(events.NewMessage(pattern='/report'))
async def report(event):
    try:
        args = event.text.split()
        if len(args) < 3:
            await event.reply("❌ Format: /report @username reason")
            return
        
        await client.send_report(
            entity=args[1],
            reason=" ".join(args[2:]),
            message="Reported via bot"
        )
        await event.reply(f"✅ Reported {args[1]}")
        time.sleep(10)  # Anti-ban
    except Exception as e:
        await event.reply(f"❌ Error: {str(e)}")

client.run_until_disconnected()
