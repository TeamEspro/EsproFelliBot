from telethon import TelegramClient, events
from EsproFelli import app

# Initialize the client
bot = TelegramClient('bot_session', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Event to welcome new members
@bot.on(events.ChatAction)
async def welcome_new_member(event):
    if event.user_joined or event.user_added:
        for user in event.action_message.action.users:
            user_obj = await bot.get_entity(user)
            full_name = user_obj.first_name + (" " + user_obj.last_name if user_obj.last_name else "")
            user_id = user_obj.id
            username = f"@{user_obj.username}" if user_obj.username else "No Username"
            
            welcome_message = f"🎉 **Welcome to the Group!** 🎉\n\n👤 **Full Name:** {full_name}\n🔹 **User ID:** {user_id}\n🔹 **Username:** {username}\n\n📢 **Enjoy & Follow the Rules!**"
            
            await event.reply(welcome_message)


# modules/wel.py

def welcome_message():
    return "👋 Welcome to EsproFelli!"

if __name__ == "__main__":
    print(welcome_message())

