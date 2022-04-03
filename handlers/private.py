import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c79c552994c222362d80e.jpg",
        caption=f"""**💥 ʜᴇʟʟᴏ, ɪ ᴀᴍ ʟᴇɢᴇɴᴅ ᴍᴜꜱɪᴄ ʙᴏᴛ
ɪ ᴀᴍ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ
ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs ᴛᴏ ᴘʟᴀʏ ᴀᴜᴅɪᴏ ᴀɴᴅ ᴠɪᴅᴇᴏ sᴏɴɢ..

═══════════════════
★ sᴜᴘᴘᴏʀᴛ ›› @ROYALUBOT_SUPPORT
★ ᴜᴘᴅᴀᴛᴇs ›› @ROYALYSERBOT
★ ᴄʀᴇᴀᴛᴏʀ ›› @ROYALBOY_XD
★ ᴅᴇᴠᴇʟᴏᴘᴇʀ ›› @ItsMeViju
★ ᴏᴡɴᴇʀ ›› @KartiK_KinG01
═══════════════════

[Join Here For Chit Chat 😁](https://t.me/ved_maitrich007)
   💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ
ᴅᴍ ᴛᴏ ᴍʏ [ʟᴇɢᴇɴᴅ ᴏᴡɴᴇʀ](t.me/KartiK_KinG01) ...**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ❱ ➕", url=f"https://t.me/KING_OTP_BOT?startgroup=true")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/afc66f54a8c2a2002ec3a.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙁𝙊𝙍 𝙍𝙀𝙋𝙊 Join - ", url=f"https://t.me/ROYALYSERBOT")
                ]
            ]
        ),
    )
