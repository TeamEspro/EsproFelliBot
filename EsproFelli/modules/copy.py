import os
import dns.resolver
from EsproFelli import app
from pyrogram import Client, filters
from pymongo import MongoClient
from pyrogram.enums import ChatAction  # ✅ Correct way to use ChatAction Enum

# ✅ DNS Resolver Fix for MongoDB
dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ["8.8.8.8", "8.8.4.4"]


# ✅ MongoDB Setup
MONGO_URI = "mongodb+srv://rogip74246:fCM4fkn8jWv9zizJ@ritikraj.mylvo.mongodb.net/?retryWrites=true&w=majority"

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    client.admin.command('ping')  # MongoDB Connection Test
    print("✅ MongoDB Connection Successful!")
except Exception as e:
    print(f"❌ MongoDB Connection Failed: {e}")
    exit()  # Agar connection fail ho to program exit kar de

db = client["telegram_bot"]  # Database ka naam
collection = db["message_replies"]  # Collection ka naam

# ✅ Pyrogram Bot Setup
app = Client("auto_reply_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.group & filters.reply)
def save_reply(client, message):
    """ Messages aur replies ko store karega """
    if message.reply_to_message:
        original_text = message.reply_to_message.text
        reply_text = message.text
        
        # Agar message ya reply "/" se start hota hai to ignore kare
        if original_text and reply_text and not original_text.startswith("/") and not reply_text.startswith("/"):
            collection.update_one(
                {"message": original_text},
                {"$set": {"reply": reply_text}},
                upsert=True
            )
            message.reply_text("✅ Reply saved!")

@app.on_message(filters.group & filters.text)
def auto_reply(client, message):
    """ Saved replies ko check karega aur respond karega """
    if not message.text.startswith("/"):  # Agar message "/" se start hota hai to ignore kare
        stored_reply = collection.find_one({"message": message.text})
        if stored_reply:
            client.send_chat_action(message.chat.id, ChatAction.TYPING)  # ✅ Corrected Chat Action
            message.reply_text(stored_reply["reply"])
