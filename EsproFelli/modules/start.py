from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup , CallbackQuery 
from EsproFelli import app

BOT_IMAGE = "https://telegra.ph/file/f1aca953494a6c4a4ad87.jpg"



@bot.on_message(filters.command("start") & filters.private)
async def start_(client: Client, message: Message):
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
                        "✚ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ✚", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )
