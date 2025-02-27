from pyrogram import Client, filters
from pyrogram.types import Message


# Dictionary to store last welcome message ID per chat
last_welcome_message = {}

# Delete new member join messages
@app.on_message(filters.new_chat_members)
async def handle_new_members(client: Client, message: Message):
    chat_id = message.chat.id

    # Delete the join message
    try:
        await message.delete()
        print(f"Deleted join message in {chat_id}")
    except Exception as e:
        print(f"Error deleting join message: {e}")

    # If there's a previous welcome message, delete it
    if chat_id in last_welcome_message:
        try:
            await client.delete_messages(chat_id, last_welcome_message[chat_id])
        except Exception as e:
            print(f"Error deleting old welcome message: {e}")

    # Generate and send new welcome message
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

        try:
            sent_message = await client.send_message(chat_id, welcome_text)
            last_welcome_message[chat_id] = sent_message.id  # Fix: Use 'id' instead of 'message_id'
        except Exception as e:
            print(f"Error sending welcome message: {e}")

# Delete left member messages
@app.on_message(filters.left_chat_member)
async def delete_leave_message(client: Client, message: Message):
    try:
        await message.delete()
        print(f"Deleted leave message in {message.chat.id}")
    except Exception as e:
        print(f"Error deleting leave message: {e}")

# Delete video chat (voice chat) start/stop messages
@app.on_message(filters.service)
async def delete_vc_message(client: Client, message: Message):
    try:
        await message.delete()
        print(f"Deleted voice chat message in {message.chat.id}")
    except Exception as e:
        print(f"Error deleting voice chat message: {e}")
