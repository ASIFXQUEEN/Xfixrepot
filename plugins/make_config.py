from pyrogram import Client, filters
from pyrogram.types import Message

# Temporary storage for configs, can be replaced with DB
user_configs = {}

@Client.on_message(filters.command("make_config"))
async def make_config_handler(client, message: Message):
    await message.reply("Send the Username of the Group or Channel (without @):")

    # Define a one-time listener for the next message from this user
    @Client.on_message(filters.text & filters.user(message.from_user.id))
    async def get_username(client, msg):
        username = msg.text.strip()
        user_configs[message.from_user.id] = username
        await msg.reply(f"Config saved for @{username}")
        client.remove_handler(get_username, group=1)  # Remove listener to prevent multiple calls
