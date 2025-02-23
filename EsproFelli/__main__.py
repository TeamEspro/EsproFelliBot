from EsproFelli import app, LOG
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup , CallbackQuery 


BOT_IMAGE = "https://graph.org/file/865e24f1e90cd1c0b0979-29505f50adbd375b7c.jpg"



@app.on_message(filters.command("start"))
async def start(_,msg):
    await msg.reply_photo(
        photo=f"{BOT_IMAGE}",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
Hɪ I'ᴍ A Aᴅᴠᴀɴᴄᴇ Cʜᴀᴛ.\n\n Nᴀᴍᴇ Is 𝐅єℓℓι [•ᴧғᴋ•] Fᴏʀᴍ Iɴᴅɪᴀ \n\n ✔ I'ᴍ A Aʀᴛɪғɪᴄɪᴀʟ Iɴᴛᴇʟʟɪɢᴇɴᴄᴇ\n\n/ᴄʜᴀᴛʙᴏᴛ - [ᴏɴ/ᴏғғ] Tʜɪs Cᴏᴍᴍᴀɴᴅ Usᴇ Oɴʟʏ Aɴʏ Gʀᴏᴜᴘ

💕Jᴜsᴛ Aᴅᴅ Mᴇ » Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ Aɴᴅ 
EɴJᴏʏ Sᴜᴘᴇʀ Qᴜᴀʟɪᴛʏ Cʜᴀᴛ
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✚ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ✚", url=f"https://t.me/FelliChatBot?startgroup=true")
                ]
                
           ]
        ),
    )



if __name__ == "__main__":
    LOG.info("started")
    app.run()

