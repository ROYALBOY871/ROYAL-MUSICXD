""" broadcast & statistic collector """

# Copyright (C) 2021 By adityaProject
# Originally written by aditya on github
# Broadcast function


import asyncio
import traceback
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant
from helpers.filters import command
from callsmusic.callsmusic import client as aditya
from config import SUDO_USERS
from helpers.decorators import sudo_users_only


@Client.on_message(filters.command(["gcast"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`𝙎𝙏𝘼𝙍𝙏𝙄𝙉𝙂 𝙏𝙊 𝘽𝙍𝙊𝘼𝘿𝘾𝘼𝙎𝙏𝙄𝙉𝙂 ...`")
        if not message.reply_to_message:
            await wtf.edit("**__Ƥɭɘɑsɘ Ʀɘƥɭy Ƭø ɑ Mɘssɑʛɘ Ƭø Stɑɤt Ɓɤøɑɗƈɑst ...__**")
            return
        lmao = message.reply_to_message.text
        async for dialog in aditya.iter_dialogs():
            try:
                await aditya.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`Ɓɤøɑɗƈɑstɩŋʛ` \n\n**Sɘŋt Ƭø:** `{sent}` Ƈɦɑts \n**Fɑɩɭɘɗ Iŋ:** {failed} chats")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"`𝙂𝘾𝘼𝙎𝙏 𝙎𝙐𝘾𝘾𝙀𝙎𝙎𝙁𝙐𝙇` \n\n**𝙎𝙚𝙣𝙩 𝙩𝙤:** `{sent}` CHATS \n**FAILED IN:** {failed} CHATS")
