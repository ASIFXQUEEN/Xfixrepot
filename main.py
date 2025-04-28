from telethon import TelegramClient, events, types
from config import Config
import os
import json
import asyncio

# Initialize
client = TelegramClient('massreport', Config.API_ID, Config.API_HASH).start(bot_token=Config.BOT_TOKEN)

# Account Manager
def load_accounts():
    if os.path.exists(Config.ACCOUNTS_FILE):
        with open(Config.ACCOUNTS_FILE) as f:
            return json.load(f)
    return {}

def save_accounts(accounts):
    with open(Config.ACCOUNTS_FILE, 'w') as f:
        json.dump(accounts, f)

# Owner Check
async def is_owner(event):
    return event.sender_id == Config.OWNER_ID

# Commands
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    if not await is_owner(event): return
    await event.reply("""
👑 **Owner Menu**:
• /addacc - Add session
• /rmacc - Remove session
• /listacc - Account list
• /report - Mass report tool
""")

@client.on(events.NewMessage(pattern='/addacc'))
async def add_account(event):
    if not await is_owner(event): return
    await event.reply("📤 Send the session string (telethon/pyrogram)")
    
    try:
        session_msg = await client.wait_for(
            events.NewMessage(from_users=Config.OWNER_ID),
            timeout=60
        )
        accounts = load_accounts()
        accounts[str(len(accounts)+1)] = session_msg.text
        save_accounts(accounts)
        await event.reply(f"✅ Account {len(accounts)} added!")
    except Exception as e:
        await event.reply(f"❌ Error: {str(e)}")

@client.on(events.NewMessage(pattern='/rmacc'))
async def remove_account(event):
    if not await is_owner(event): return
    accounts = load_accounts()
    if not accounts:
        return await event.reply("❌ No accounts stored!")
    
    await event.reply(f"🔢 Accounts: {', '.join(accounts.keys())}\nReply with number to remove")
    
    try:
        num_msg = await client.wait_for(
            events.NewMessage(from_users=Config.OWNER_ID),
            timeout=30
        )
        if num_msg.text not in accounts:
            return await event.reply("❌ Invalid number!")
        
        del accounts[num_msg.text]
        save_accounts(accounts)
        await event.reply("✅ Account removed!")
    except Exception as e:
        await event.reply(f"❌ Error: {str(e)}")

@client.on(events.NewMessage(pattern='/listacc'))
async def list_accounts(event):
    if not await is_owner(event): return
    accounts = load_accounts()
    if not accounts:
        return await event.reply("❌ No accounts stored!")
    
    msg = "📋 Active Accounts:\n"
    for num, session in accounts.items():
        msg += f"{num}. {session[:15]}...\n"
    await event.reply(msg)

@client.on(events.NewMessage(pattern='/report'))
async def report_tool(event):
    if not await is_owner(event): return
    
    # Reason selection
    reasons = {
        "1": "Spam", "2": "Violence",
        "3": "Child Abuse", "4": "Illegal"
    }
    await event.reply("""
📢 Report Reason:
1. Spam
2. Violence
3. Child Abuse
4. Illegal
Reply with number (1-4)""")
    
    try:
        # Get reason
        reason_msg = await client.wait_for(
            events.NewMessage(from_users=Config.OWNER_ID),
            timeout=30
        )
        reason = reasons.get(reason_msg.text.strip())
        if not reason: return await event.reply("❌ Invalid choice!")
        
        # Get target
        await event.reply("👤 Reply to target message")
        target_msg = await client.wait_for(
            events.NewMessage(from_users=Config.OWNER_ID),
            timeout=30
        )
        target = await target_msg.get_reply_message()
        
        # Get count
        await event.reply("🔢 Report count (1-50):")
        count_msg = await client.wait_for(
            events.NewMessage(from_users=Config.OWNER_ID),
            timeout=30
        )
        count = min(50, max(1, int(count_msg.text)))
        
        # Execute reports
        success = 0
        for i in range(count):
            try:
                await client.send_report(
                    entity=target.sender_id,
                    reason=reason,
                    message=f"Report {i+1}/{count}"
                )
                success += 1
                await event.reply(f"✅ {i+1}/{count} sent")
                await asyncio.sleep(15)  # Anti-ban
            except:
                await asyncio.sleep(30)
        
        await event.reply(f"📊 Results:\nTotal: {count}\nSuccess: {success}")
        
    except Exception as e:
        await event.reply(f"❌ Error: {str(e)}")

client.run_until_disconnected()
