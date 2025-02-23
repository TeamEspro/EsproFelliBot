from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
import random
from EsproFelli import app

# Alag-alag messages ka ek list
custom_messages = [
    "Hey {name}, kaise ho? 😊",
    "{name}, aaj ka din kaisa ja raha hai? 🌸",
    "Hello {name}, tum kya kar rahe ho? 🤔",
    "{name}, aaj kuch naya seekha kya? 🚀",
    "Kya haal hain {name}? 🎉",
    "Aree {name}, kab mil rahe ho? 😎",
    "{name}, tumhari favorite movie kaunsi hai? 🍿",
    "Suno {name}, koi mazedar joke sunao! 😆",
    "Aaj ka weather kaisa hai {name}? ☀️🌧️",
    "{name}, life me naye goals kya hain? 🏆",
    "Good morning {name}, aaj ka kya plan hai? ☀️",
    "{name}, tumhara favorite gaana kaunsa hai? 🎵",
    "Coffee ya chai, {name}? ☕",
    "Biryani ya pizza, {name}? 🍕",
    "Aaj ka mood kaisa hai {name}? 😄",
    "{name}, kya tumhe gaming pasand hai? 🎮",
    "Aaj kis topic pe baat karein {name}? 💬",
    "Weekend plans kya hain {name}? 🏖️",
    "{name}, tumhare liye motivation quote: 'Dream Big!' ✨",
    "Coding ya music, {name}? 🤖🎶",
    "Kitni baje soye the {name}? 😴",
    "{name}, cricket ya football? ⚽🏏",
    "Aaj tumne kya interesting padha? 📖",
    "{name}, kya tumhe traveling pasand hai? ✈️",
    "Sabse zyada maza kab aaya {name}? 😆",
    "Aaj ka best moment kya tha {name}? 🌟",
    "Tumhare favorite YouTuber kaun hain {name}? 📺",
    "Aaj ka challenge: 10 push-ups kar lo {name}! 💪",
    "Tumhare sapne ka city kaunsa hai {name}? 🌆",
    "Joke sunao {name}, hasi chahiye! 😂",
    "Kya tumhe coding ya designing pasand hai {name}? 🎨💻"
]

@app.on_message(filters.command("tagall") & filters.group)
async def tag_all_members(client: Client, message: Message):
    chat_id = message.chat.id
    members = []

    async for member in client.get_chat_members(chat_id):
        if not member.user.is_deleted and not member.user.is_bot:  # Ignore deleted accounts & bots
            members.append(member.user)

    if not members:
        await message.reply("⚠ Koi member nahi mila!")
        return

    await message.reply(f"🔹 Total {len(members)} members ko tag kiya ja raha hai...")

    for i, member in enumerate(members, start=1):
        try:
            # Randomly ek message select karega
            msg_text = random.choice(custom_messages).format(name=member.mention)
            await message.reply_text(msg_text)
            await asyncio.sleep(3)  # Avoid rate limit
        except Exception as e:
            print(f"Error sending message to {member.first_name}: {e}")

    await message.reply("✅ Sabhi members ko successfully tag kar diya gaya!")

# modules/tagall.py

def ritik():
    return "📌 Tagging all members..."

print(ritik())
