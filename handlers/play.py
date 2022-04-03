import os
from os import path
from pyrogram import Client, filters
from pyrogram.types import Message, Voice, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from callsmusic import callsmusic, queues
from callsmusic.callsmusic import client as USER
from helpers.admins import get_administrators
import requests
import aiohttp
from youtube_search import YoutubeSearch
import converter
from downloaders import youtube
from config import DURATION_LIMIT
from helpers.filters import command
from helpers.command import aditya 
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
import aiofiles
import ffmpeg
from PIL import Image, ImageFont, ImageDraw
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream


def transcode(filename):
    ffmpeg.input(filename).output("input.raw", format='s16le', acodec='pcm_s16le', ac=2, ar='48k').overwrite_output().run() 
    os.remove(filename)

# Convert seconds to mm:ss
def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


# Change image size
def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage

async def generate_cover(requested_by, title, views, duration, thumbnail):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("background.png", mode="wb")
                await f.write(await resp.read())
                await f.close()


    image1 = Image.open("./background.png")
    image2 = Image.open("etc/foreground.png")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save("temp.png")
    img = Image.open("temp.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("etc/font.otf", 32)
    draw.text((190, 550), f"Title: {title}", (255, 255, 255), font=font)
    draw.text(
(190, 590), f"Duration: {duration}", (255, 255, 255), font=font
    )
    draw.text((190, 630), f"Views: {views}", (255, 255, 255), font=font)
    draw.text((190, 670),
 f"Added By: {requested_by}",
 (255, 255, 255),
 font=font,
    )
    img.save("final.png")
    os.remove("temp.png")
    os.remove("background.png")



@Client.on_message(
    aditya(["/play", "*play", "play", "#", "@"])
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
async def play(_, message: Message):
    global que
    global useer

    lel = await message.reply("**Song Dhund Rha Hu Bhya Sabar Karo😅**")

    administrators = await get_administrators(message.chat)
    chid = message.chat.id

    try:
        user = await USER.get_me()
    except:
        user.first_name = "Esport_MusicX"
    usar = user
    wew = usar.id
    try:
        await _.get_chat_member(chid, wew)
    except:
        for administrator in administrators:
            if administrator == message.from_user.id:
                try:
                    invitelink = await _.export_chat_invite_link(chid)
                except:
                    await lel.edit(
                        "<b> 🤖Add Me As Admin In Your Group Sir✅ </b>")
                    return

                try:
                    await USER.join_chat(invitelink)
                    await USER.send_message(
                        message.chat.id, "** 🤨 Svagt Nahi Karoge Music Bot Join Kr Chuka Hai🥺**")

                except UserAlreadyParticipant:
                    pass
                except Exception:
                    await lel.edit(
                        f"<b> Flood Wait Please Wait More☹️ </b>\n𝙎𝙤𝙧𝙧𝙮 𝙖𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝙛𝙖𝙞𝙡𝙚𝙙 𝙩𝙤 𝙟𝙤𝙞𝙣 𝙮𝙤𝙪𝙧 𝙜𝙧𝙤𝙪𝙥😔😔.... 𝙥𝙡𝙚𝙖𝙨𝙚 𝙘𝙝𝙚𝙘𝙠 𝙖𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝙣𝙤𝙩 𝙗𝙖𝙣𝙣𝙚𝙙 𝙞𝙣 𝙮𝙤𝙪𝙧 𝙜𝙧𝙤𝙪𝙥✨✨🎸 :) ")
    try:
        await USER.get_chat(chid)
    except:
        await lel.edit(
            f"<i>Hey {user.first_name}, 😒𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝙣𝙤𝙩 𝙟𝙤𝙞𝙣 𝙩𝙝𝙞𝙨 𝙘𝙝𝙖𝙩 ........ 😁𝙨𝙖𝙮 𝙩𝙤 𝙖𝙙𝙢𝙞𝙣 𝙥𝙡𝙚𝙖𝙨𝙚 𝙨𝙚𝙣𝙙 /𝙥𝙡𝙖𝙮 𝙘𝙤𝙢𝙢𝙖𝙣𝙙 𝙛𝙞𝙧𝙨𝙩 𝙩𝙤 𝙟𝙤𝙞𝙣 𝙤𝙪𝙧 𝙍𝙊𝙔𝘼𝙡 𝘼𝙎𝙎𝙄𝙎𝙏𝘼𝙉𝙏🙄🙄 </i>")
        return
    
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"** 𝙎𝙤𝙣𝙜 𝙞𝙨 𝙇𝙊𝙉𝙂𝙀𝙍 𝙏𝙃𝘼𝙉 {DURATION_LIMIT} 𝙈𝙞𝙣𝙪𝙩𝙚𝙨 𝙖𝙧𝙚𝙣'𝙩 𝙖𝙡𝙡𝙤𝙬𝙚𝙙 𝙩𝙤 𝙥𝙡𝙖𝙮▶ ❤️🥀**"
            )

        file_name = get_file_name(audio)
        title = file_name
        thumb_name = "https://te.legra.ph/file/2f8b0a508e791cdfce57b.jpg"
        thumbnail = thumb_name
        duration = round(audio.duration / 60)
        views = "Locally added"

        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                            text="𝐂𝐡𝐚𝐧𝐧𝐞𝐥📡",
                            url=f"https://t.me/ROYALYSERBOT")
               ],
               [
                    InlineKeyboardButton(
                            text="ᏒᎧᎩᏗᏝᏰᎧᎩ🌟",
                            url=f"https://t.me/ROYALBOY_XD"),
                            
                    InlineKeyboardButton(
                            text="𝙎𝙐𝙋𝙋𝙊𝙍𝙏✨✨",
                            url=f"https://t.me/ROYALUBOT_SUPPORT")
               ],
               [
                        InlineKeyboardButton(
                            text="𝘿𝙀𝙑𝙀𝙇𝙊𝙋𝙀𝙍(LEGEND)❤️",
                            url=f"https://t.me/KartiK_KinG01")
                   
                ]
            ]
        )

        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name))
            else file_name
        )

    elif url:
        try:
            results = YoutubeSearch(url, max_results=1).to_dict()
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

            keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                            text="𝐂𝐡𝐚𝐧𝐧𝐞𝐥📡",
                            url=f"https://t.me/ROYALYSERBOT")
               ],
               [
                    InlineKeyboardButton(
                            text="ᏒᎧᎩᏗᏝᏰᎧᎩ🌟",
                            url=f"https://t.me/ROYALBOY_XD"),
                            
                    InlineKeyboardButton(
                            text="𝙎𝙐𝙋𝙋𝙊𝙍𝙏✨✨",
                            url=f"https://t.me/ROYALUBOT_SUPPORT")
               ],
               [
                        InlineKeyboardButton(
                            text="𝘿𝙀𝙑𝙀𝙇𝙊𝙋𝙀𝙍(LEGEND)👨‍💻",
                            url=f"https://t.me/KartiK_KinG01")
                   
                ]
            ]
        )

        except Exception as e:
            title = "NaN"
            thumb_name = "https://te.legra.ph/file/2f8b0a508e791cdfce57b.jpg"
            duration = "NaN"
            views = "NaN"
            keyboard = InlineKeyboardMarkup(
            [
                
                [
                    InlineKeyboardButton(
                            text="𝐂𝐡𝐚𝐧𝐧𝐞𝐥📡",
                            url=f"https://t.me/ROYALYSERBOT")
               ],
               [
                    InlineKeyboardButton(
                            text="ᏒᎧᎩᏗᏝᏰᎧᎩ🌟",
                            url=f"https://t.me/ROYALBOY_XD"),
                            
                    InlineKeyboardButton(
                            text="𝙎𝙐𝙋𝙋𝙊𝙍𝙏✨✨",
                            url=f"https://t.me/ROYALUBOT_SUPPORT")
               ],
               [
                        InlineKeyboardButton(
                            text="𝘿𝙀𝙑𝙀𝙇𝙊𝙋𝙀𝙍(LEGEND)👨‍💻",
                            url=f"https://t.me/KartiK_KinG01")
                   
                ]
            ]
        )

        if (dur / 60) > DURATION_LIMIT:
            await lel.edit(
                f"**𝙎𝙤𝙣𝙜 𝙞𝙨 𝙇𝙊𝙉𝙂𝙀𝙍 𝙏𝙃𝘼𝙉 {DURATION_LIMIT} 𝙈𝙞𝙣𝙪𝙩𝙚𝙨 𝙖𝙧𝙚𝙣'𝙩 𝙖𝙡𝙡𝙤𝙬𝙚𝙙 𝙩𝙤 𝙥𝙡𝙖𝙮▶ ❤️🥀**"
            )
            return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(youtube.download(url))
    else:
        if len(message.command) < 2:
            return await lel.edit(
                "𝙒𝙝𝙞𝙘𝙝 𝙨𝙤𝙣𝙜❤️🎶 𝙮𝙤𝙪 𝙬𝙖𝙣𝙩 𝙩𝙤 𝙡𝙞𝙨𝙩𝙚𝙣✨✨✨**"
            )
        await lel.edit("**🎵 𝙉𝙊𝙒 𝙋𝙇𝘼𝙔𝙄𝙉𝙂 𝙎𝙊𝙉𝙂𝙎🎶😁 𝙏𝙃𝘼𝙉𝙆𝙎 𝙁𝙊𝙍 𝙐𝙎𝙄𝙉𝙂 𝙊𝙐𝙍 𝙎𝙀𝙍𝙑𝙄𝘾𝙀....❤️**")
        query = message.text.split(None, 1)[1]
        # print(query)
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            await lel.edit(
                "**🌸 (･ัω･ั)𝙎𝙥𝙚𝙡𝙡𝙞𝙣𝙜 𝙥𝙧𝙤𝙗𝙡𝙚𝙢 𝙝𝙖𝙞 𝙖𝙖𝙥 𝙘𝙝𝙚𝙘𝙠 𝙠𝙧 𝙡𝙤 𝙚𝙠 𝙗𝙖𝙖𝙧😚.**"
            )
            print(str(e))
            return

        keyboard = InlineKeyboardMarkup(
            [
                
                [
                    InlineKeyboardButton(
                            text="𝐂𝐡𝐚𝐧𝐧𝐞𝐥📡",
                            url=f"https://t.me/ROYALYSERBOT")
               ],
               [
                    InlineKeyboardButton(
                            text="ᏒᎧᎩᏗᏝᏰᎧᎩ🌟",
                            url=f"https://t.me/ROYALBOY_XD"),
                            
                    InlineKeyboardButton(
                            text="𝙎𝙐𝙋𝙋𝙊𝙍𝙏✨✨",
                            url=f"https://t.me/ROYALUBOT_SUPPORT")
               ],
               [
                        InlineKeyboardButton(
                            text="𝘿𝙀𝙑𝙀𝙇𝙊𝙋𝙀𝙍(LEGEND)👨‍💻",
                            url=f"https://t.me/KartiK_KinG01")
                   
                ]
            ]
        )

        if (dur / 60) > DURATION_LIMIT:
            await lel.edit(
                f"**𝙎𝙤𝙣𝙜 𝙞𝙨 𝙇𝙊𝙉𝙂𝙀𝙍 𝙏𝙃𝘼𝙉 {DURATION_LIMIT} 𝙈𝙞𝙣𝙪𝙩𝙚𝙨 𝙖𝙧𝙚𝙣'𝙩 𝙖𝙡𝙡𝙤𝙬𝙚𝙙 𝙩𝙤 𝙥𝙡𝙖𝙮▶ ❤️🥀**"
            )
            return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(youtube.download(url))
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) in ACTV_CALLS:
        position = await queues.put(chat_id, file=file_path)
        await message.reply_photo(
            photo="final.png",
            caption="**𝙎𝙊𝙉𝙂 𝙋𝙊𝙎𝙄𝙏𝙄𝙊𝙉 😁** ** {}**".format(position),
            reply_markup=keyboard,
        )
    else:
        await callsmusic.pytgcalls.join_group_call(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        file_path,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )

        await message.reply_photo(
            photo="final.png",
            reply_markup=keyboard,
            caption="**R͆O͆Y͆A͆L͆-M͆U͆S͆I͆C͆X͆D͆ Now 😄 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 📀 𝐀𝐭 🤟 `{}`...**".format(
        message.chat.title
        ), )

    os.remove("final.png")
    return await lel.delete()
