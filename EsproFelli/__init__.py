# EsproFelli/__init__.py
from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config




class app(Client):
    def __init__(self):
        super().__init__(
            name="app",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.DEFAULT,
        )



from EsproFelli.modules.felli import felli_function
from EsproFelli.modules.wel import welcome_message
from EsproFelli.modules.tagall import tag_all
