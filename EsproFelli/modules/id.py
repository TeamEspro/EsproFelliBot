from pyrogram import Client, filters
from EsproFelli import app


@app.on_message(filters.command("id"))
def id_command(client, message):
    if message.chat.type == "private":
        # DM me command ka reply
        user_id = message.from_user.id
        message.reply_text(f"**Your ID:** `{user_id}`")
    else:
        # Group me command ka reply
        chat_id = message.chat.id
        message.reply_text(f"**Group ID:** `{chat_id}`")
