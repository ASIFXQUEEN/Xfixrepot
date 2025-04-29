# plugins/make_config.py

import json
from pyrogram import Client, filters
from pyrogram.types import Message, ReplyKeyboardRemove
from info import Config, Txt

@Client.on_message(filters.private & filters.user(Config.OWNER) & filters.command("make_config"))
async def make_config(client: Client, message: Message):
    try:
        await message.reply_text("Send the Username of the Group or Channel (without @):", reply_to_message_id=message.id)

        username = await client.ask(
            chat_id=message.chat.id,
            text="Enter username (without @):",
            filters=filters.text,
            timeout=60
        )

        target = username.text.strip().replace("@", "")

        data = {
            "Target": target
        }

        with open("config.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        await message.reply_text(
            f"Configuration Saved Successfully!\nTarget: @{target}",
            reply_to_message_id=message.id,
            reply_markup=ReplyKeyboardRemove()
        )

    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")
