from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from EsproFelli import app

async def send_id(update: Update, context: CallbackContext):
    chat_type = update.message.chat.type  # Check chat type
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id

    if chat_type == "private":  
        # Agar DM hai, toh sirf User ID bhejo
        await update.message.reply_text(f"{user_id}")
    else:  
        # Agar group hai, toh Chat ID + User ID dono bhejo
        await update.message.reply_text(f"🆔 *Chat ID:* `{chat_id}`\n👤 *User ID:* `{user_id}`", parse_mode="Markdown")

    app = Application.builder().token(BOT_TOKEN).build()

    # /id command ka handler
    app.add_handler(CommandHandler("id", send_id))

    print("Bot is running...")
   
