from pyrogram import Client, filters
from EsproFelli import app


@app.on_message(filters.command("id"))
def id_command(client, message):
    if message.chat.type == "private":
        # Agar private chat me command aayi hai, toh user ka ID bhejna hai
        user_id = message.from_user.id
        message.reply_text(f"Your User ID: `{user_id}`")
    else:
        # Agar group me command aayi hai, toh group ka ID bhejna hai
        chat_id = message.chat.id
        message.reply_text(f"Group ID: `{chat_id}`")

