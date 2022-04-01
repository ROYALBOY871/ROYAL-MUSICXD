import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/ee0aa83dc223b8bf6da02.jpg",
        caption=f"""*🎸✨✨𝘽𝙀𝙎𝙏 🎧𝙈𝙐𝙎𝙄𝘾 𝘽𝙊𝙏🎧 𝘽𝙔 𝙍𝙊𝙔𝘼𝙇𝘽𝙊𝙔_𝙓𝘿 𝙃𝙄𝙂𝙃 𝙌𝙐𝘼𝙇𝙄𝙏𝙔 𝙈𝙐𝙎𝙄𝘾🎶🎶 𝙒𝙄𝙏𝙃 𝙉𝙊 𝙇𝘼𝙂 && 𝙉𝙚𝙬 𝙂𝙀𝙉𝙀𝙍𝘼𝙏𝙄𝙊𝙉👨‍💻 𝘼𝘿𝙑𝘼𝙉𝘾𝙀𝘿 𝘽𝙊𝙏 𝙒𝙞𝙩𝙝 𝙢𝙖𝙣𝙮 𝙛𝙚𝙖𝙩𝙪𝙧𝙚𝙨✨✨🎸

       ⭕𝙎𝙪𝙥𝙥𝙤𝙧𝙩:-  @ROYALUBOT_SUPPORT

       ⭕𝘾𝙍𝙀𝘼𝙏𝙊𝙍:- @ROYALBOY_XD

       ⭕𝘾𝙝𝙖𝙣𝙣𝙚𝙡:- @ROYALYSERBOT

       ⭕𝙊𝙒𝙉𝙀𝙍:- @ROYALBOY_XD

       ⭕𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧:- @KartiK_KinG01

🌟👨‍🎤𝙅𝙊𝙄𝙉 𝙊𝙐𝙍 𝙏𝙀𝘼𝙈 𝙉𝙊𝙒 𝙁𝙊𝙍 𝘾𝙃𝘼𝙏𝙏𝙄𝙉𝙂💌 𝙅𝙊𝙄𝙉 - @ved_maitrich007
   𝙄𝙛 𝙔𝙤𝙪 𝙣𝙚𝙚𝙙 𝙖𝙣𝙮 𝙝𝙚𝙡𝙥 𝙩𝙝𝙚𝙣 𝙠𝙞𝙣𝙙𝙡𝙮 𝙘𝙤𝙣𝙩𝙖𝙘𝙩 𝙩𝙤 [👨‍💻𝙇𝙀𝙂𝙀𝙉𝘿👨‍💻](t.me/KartiK_KinG01)**""",
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
