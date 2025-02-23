from pyrogram import Client, filters
from pyrogram.types import Message
from EsproFelli import app


@app.on_message(filters.command("id"))
def id_command(client: Client, message: Message):
    chat_type = message.chat.type  # Chat ka type check karein

    if chat_type == "private":
        # DM me sirf user ka ID send hoga
        user_id = message.from_user.id
        message.reply_text(f"**Your ID:** `{user_id}`")  # Sirf user ID bhejna hai
    elif chat_type in ["group", "supergroup"]:
        # Group ya Supergroup me sirf group ka ID send hoga
        chat_id = message.chat.id
        message.reply_text(f"**Group ID:** `{chat_id}`")  # Sirf group ID bhejna hai

