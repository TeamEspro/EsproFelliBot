from pyrogram import Client, filters
from pyrogram.types import Message
from EsproFelli import app

# Welcome message function
@app.on_message(filters.new_chat_members)
async def welcome(client: Client, message: Message):
    for member in message.new_chat_members:
        full_name = member.first_name
        if member.last_name:
            full_name += f" {member.last_name}"

        user_id = member.id

        # Mention user using MarkdownV2 format
        mention = f"[{full_name}](tg://user?id={user_id})"

        # Escape special characters for MarkdownV2
        welcome_text = f"""
👋 Welcome {mention}!
🎉 We're happy to have you here!
"""

        await message.reply_text(welcome_text, parse_mode="markdown2")  # Correct parse mode
