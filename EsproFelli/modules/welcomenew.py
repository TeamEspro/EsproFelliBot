from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CommandHandler, CallbackContext

TOKEN = "7734465358:AAGMuYNK4DSMq8i7W5HofNa6WHr6xtbgRIU"

async def welcome(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        await update.message.reply_text(f"Welcome {member.first_name} to the group! 🎉")

def main():
    app = Application.builder().token(TOKEN).build()
    
    # New members ke liye handler
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
    
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()