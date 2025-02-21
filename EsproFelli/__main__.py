from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config
class app(Client):
    def __init__(self):
       
        super().__init__(
            name="EsproMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )



# EsproFelli/main.py

# Absolute Import ka use karein

from modules.felli import felli_function
from modules.wel import welcome_message
from modules.tagall import tag_all

# Functions ko call karein

print(felli_function())
print(welcome_message())
print(tag_all())
