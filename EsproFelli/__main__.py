from EsproFelli.__init__ import app

import asyncio

# Telegram Bot API Library
from pyrogram import Client

# Bot Configuration


# Function to send message on start
async def send_start_message():
    await bot.send_message(chat_id=OWNER_ID, text="✅ Bot Started Successfully!")

# Bot Start Event
@app.on_message()
async def start_bot(_, message):
    print("Bot is running...")
    
# Running the bot
async def main():
    async with app:
        await send_start_message()  # Send start message to owner

app.run(main())

# EsproFelli/main.py

# Absolute Import ka use karein

from EsproFelli.modules.felli import felli_function
from EsproFelli.modules.wel import welcome_message


# Functions ko call karein
app = app()

print(felli_function())
print(welcome_message())


