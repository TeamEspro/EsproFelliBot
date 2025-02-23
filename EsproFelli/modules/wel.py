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
        
        username = f"@{member.username}" if member.username else "No Username"
        user_id = member.id

        welcome_text = f"""
👋 Welcome, {full_name}!
🆔 ID: {user_id}
🔗 Username: {username}

We're happy to have you here! 🎉
"""

        # Message group me send hoga bina kisi reply ke
        await client.send_message(message.chat.id, welcome_text)
