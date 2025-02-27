from pyrogram import Client, filters
from pyrogram.types import Message
import re
import asyncio
from EsproFelli import app

# Function to check if user is admin
async def is_admin(client, message: Message):
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    return chat_member.status in ["administrator", "creator"]

# Regular expression to detect all types of links
LINK_REGEX = r"(https?://\S+|www\.\S+|t\.me/\S+|telegram\.me/\S+)"

# Filter messages containing links (excluding admins)
@app.on_message(filters.text & filters.regex(LINK_REGEX) & ~filters.me)
async def delete_links(client, message: Message):
    if not await is_admin(client, message):  # Check if user is NOT an admin
        await message.delete()  # Delete the message
        
        # Send warning message
        warning = await message.reply_text(f"⚠️ {message.from_user.mention} Links are not allowed!")
        
        # Wait for 30 seconds and delete the warning message
        await asyncio.sleep(30)
        await warning.delete()

# Delete new member join messages
@app.on_message(filters.new_chat_members)
async def delete_join_message(client: Client, message: Message):
    try:
        await message.delete()
        print(f"Deleted join message in {message.chat.id}")
    except Exception as e:
        print(f"Error deleting join message: {e}")

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
