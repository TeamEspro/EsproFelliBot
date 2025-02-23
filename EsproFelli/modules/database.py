from pyrogram import Client, filters, idle
from pymongo import MongoClient
import random


MONGO_URL = "mongodb+srv://rogip74246:fCM4fkn8jWv9zizJ@ritikraj.mylvo.mongodb.net/?retryWrites=true&w=majority&appName=ritikraj"


db = MongoClient(MONGO_URL)["chatbot_db"]
settings, responses = db["settings"], db["responses"]

# ✅ Function to Check Admin
async def is_admin(chat_id, user_id):
    return user_id in [m.user.id async for m in bot.get_chat_members(chat_id, filter="administrators")]

# ✅ Enable/Disable Chatbot
@bot.on_message(filters.command(["chatbot on", "chatbot off"]) & filters.group)
async def toggle_chatbot(client, message):
    if not await is_admin(message.chat.id, message.from_user.id):
        return await message.reply_text("❌ You are not an admin!")
    
    status = "on" in message.text
    settings.update_one({"chat_id": message.chat.id}, {"$set": {"enabled": status}}, upsert=True)
    await message.reply_text(f"✅ Chatbot {'enabled' if status else 'disabled'}!")

# ✅ Respond to Messages & Save Replies (Ignore "/" wale words)
@bot.on_message(filters.text & ~filters.command() & ~filters.bot)
async def chatbot_response(client, message):
    chat_id, user_text = message.chat.id, message.text.strip()

    # 🛑 Ignore "/" se start hone wale words
    if user_text.startswith("/"):
        return

    # 🛑 Check if chatbot is enabled
    if not settings.find_one({"chat_id": chat_id, "enabled": True}):
        return

    # 🔹 If message is a reply, save it in the database
    if message.reply_to_message:
        responses.insert_one({"question": message.reply_to_message.text, "answer": user_text})
        return await message.reply_text("✅ Response saved!")

    # 🔹 Check if a reply exists for this message
    reply = responses.find_one({"question": user_text})
    if reply:
        await message.reply_text(reply["answer"])
    else:
        await message.reply_text("🤖 Mujhe ye nahi pata, mujhe sikhao! (Reply karo)")

