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
    if await is_admin(client, message):  # ✅ Admin hai to message delete nahi hoga
        return

    await message.delete()  # ❌ Non-admin ke link delete ho jayenge
    
    # Send warning message
    warning = await message.reply_text(
        f"⚠️ {message.from_user.mention} Links are not allowed!"
    )
    
    # Wait for 30 seconds and delete the warning message
    await asyncio.sleep(30)
    await warning.delete()

# /id command ka handler
@app.on_message(filters.command("id"))
async def send_id(client, message):
    chat_type = message.chat.type
    chat_id = message.chat.id
    user_id = message.from_user.id

    if chat_type == "private":
        # Agar DM hai, toh sirf User ID bhejo
        await message.reply_text(
            f"👤 *User ID:* `{user_id}`",
            parse_mode="markdown2"
        )
    else:
        # Agar group hai, toh Chat ID + User ID dono bhejo
        await message.reply_text(
            f"🆔 *Chat ID:* `{chat_id}`\n👤 *User ID:* `{user_id}`",
            parse_mode="markdown2"
        )
