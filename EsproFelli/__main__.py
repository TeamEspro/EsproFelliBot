from EsproFelli import app, LOG
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup , CallbackQuery 


BOT_IMAGE = "https://telegra.ph/file/f1aca953494a6c4a4ad87.jpg"



@app.on_message(filters.command("start"))
async def start(_,msg):
    await message.reply_photo(
        photo=f"{BOT_IMAGE}",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
Hɪ I'ᴍ A Aᴅᴠᴀɴᴄᴇ 𝐇ocαηє [•ᴧғᴋ•].\n\n Nᴀᴍᴇ Is 𝐇ocαηє [•ᴧғᴋ•] Fᴏʀᴍ Iɴᴅɪᴀ \n\n ✔ I'ᴍ A Aʀᴛɪғɪᴄɪᴀʟ Iɴᴛᴇʟʟɪɢᴇɴᴄᴇ\n\n/ᴄʜᴀᴛʙᴏᴛ - [ᴏɴ/ᴏғғ] Tʜɪs Cᴏᴍᴍᴀɴᴅ Usᴇ Oɴʟʏ Aɴʏ Gʀᴏᴜᴘ

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


print("Bot running...")
