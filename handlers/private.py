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
        caption=f"""**ð¥ Êá´ÊÊá´, Éª á´á´ Êá´É¢á´É´á´ á´á´ê±Éªá´ Êá´á´
Éª á´á´ sá´á´á´Ê Òá´sá´ á´ á´ á´Êá´Êá´Ê
Êá´á´ Òá´Ê á´á´Êá´É¢Êá´á´ É¢Êá´á´á´s á´á´ á´Êá´Ê á´á´á´Éªá´ á´É´á´ á´ Éªá´á´á´ sá´É´É¢..

âââââââââââââââââââ
â sá´á´á´á´Êá´ âºâº @ROYALUBOT_SUPPORT
â á´á´á´á´á´á´s âºâº @ROYALYSERBOT
â á´Êá´á´á´á´Ê âºâº @ROYALBOY_XD
â á´á´á´ á´Êá´á´á´Ê âºâº @ItsMeViju
â á´á´¡É´á´Ê âºâº @KartiK_KinG01
âââââââââââââââââââ

[Join Here For Chit Chat ð](https://t.me/ved_maitrich007)
   ð ÉªÒ Êá´á´ Êá´á´ á´ á´É´Ê Ç«á´á´sá´Éªá´É´s á´Êá´É´
á´á´ á´á´ á´Ê [Êá´É¢á´É´á´ á´á´¡É´á´Ê](t.me/KartiK_KinG01) ...**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "â â° Aá´á´ Má´ Tá´ Yá´á´Ê GÊá´á´á´ â± â", url=f"https://t.me/KING_OTP_BOT?startgroup=true")
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
                        "ððð ðððð Join - ", url=f"https://t.me/ROYALYSERBOT")
                ]
            ]
        ),
    )
