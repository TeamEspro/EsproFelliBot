
from EsproFelli import app
from pyrogram import Client, filters

# Function to handle new member joins
@app.on_message(filters.new_chat_members)
def welcome_new_member(client, message):
    for member in message.new_chat_members:
        full_name = member.first_name
        if member.last_name:
            full_name += f" {member.last_name}"
        username = f"@{member.username}" if member.username else "No Username"
        user_id = member.id

        welcome_text = (
            f"👋 Welcome, {full_name}!\n"
            f"🆔 User ID: `{user_id}`\n"
            f"📛 Username: {username}\n"
            f"🎉 Enjoy your stay in this group!"
        )

        message.reply_text(welcome_text, parse_mode="markdown")


# modules/wel.py

def welcome_message():
    return "👋 Welcome to EsproFelli!"

if __name__ == "__main__":
    print(welcome_message())

