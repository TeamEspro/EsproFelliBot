import os
import logging 
from pyrogram import Client
from config import Config 

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOG = logging.getLogger(__name__)


ENV = bool(os.environ.get("ENV",False))

if ENV:
    API_ID=int(os.environ.get("API_ID",""))
    API_HASH=str(os.environ.get("API_HASH",""))
    BOT_TOKEN=str(os.environ.get("BOT_TOKEN",""))
    MONGO_URL =str(os.environ.get("MONGO_URL", ""))
    SUDO = list(int(i) for i in os.environ.get("SUDO", "6693611573").split(" "))
    START_IMG=str(os.environ.get("START_IMG",""))
    BOT_ID=int(os.environ.get("BOT_ID",""))
    BOT_USERNAME=str(os.environ.get("BOT_USERNAME",""))
    BOT_NAME=str(os.environ.get("BOT_NAME",""))

else:
    API_ID=Config.API_ID
    API_HASH=Config.API_HASH
    BOT_TOKEN=Config.BOT_TOKEN
    MONGO_URL=Config.MONGO_URL
    SUDO=Config.SUDO
    START_IMG=Config.START_IMG
    BOT_ID=Config.BOT_ID
    BOT_USERNAME=Config.BOT_USERNAME
    BOT_NAME=Config.BOT_NAME



app=Client(
    "BOT",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="EsproFelli.modules")
     )

LOG.info("starting the bot....")

