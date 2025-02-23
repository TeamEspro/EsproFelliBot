from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CommandHandler, CallbackContext
from EsproFelli import app

async def welcome(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        await update.message.reply_text(f"Welcome {member.first_name} to the group! 🎉")

    app = Application.builder().token(BOT_TOKEN).build()
    
    # New members ke liye handler
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
    
    print("Bot is running...")
    
