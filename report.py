from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "Welcome to Branded Mass Report Bot!\nSelect an option below:",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("1 Report", callback_data="report_1")],
            [InlineKeyboardButton("5 Reports", callback_data="report_5")],
            [InlineKeyboardButton("9 Reports", callback_data="report_9")],
            [InlineKeyboardButton("Mass Report", callback_data="mass_report")]
        ])
    )

@Client.on_callback_query(filters.regex("report_"))
async def report_callback(client, callback_query):
    data = callback_query.data
    if data == "report_1":
        await callback_query.answer("1 Report Sent Successfully!")
    elif data == "report_5":
        await callback_query.answer("5 Reports Sent Successfully!")
    elif data == "report_9":
        await callback_query.answer("9 Reports Sent Successfully!")
    elif data == "mass_report":
        await callback_query.answer("Mass Reports Sent Successfully!")
