from pyrogram import Client, filters
from pyrogram.types import Message
from EsproFelli import app

# Dictionary to store last welcome message ID per chat
last_welcome_message = {}

@app.on_message(filters.new_chat_members)
async def welcome(client: Client, message: Message):
    chat_id = message.chat.id

    # If there's a previous welcome message, delete it
    if chat_id in last_welcome_message:
        try:
            await client.delete_messages(chat_id, last_welcome_message[chat_id])
        except Exception as e:
            print(f"Error deleting message: {e}")

    # Generate welcome message
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

        # Send new welcome message and store its ID
        sent_message = await client.send_message(chat_id, welcome_text)
        last_welcome_message[chat_id] = sent_message.message_id
