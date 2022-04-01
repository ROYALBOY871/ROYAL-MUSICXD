import os
import requests
import aiohttp
import yt_dlp

from pyrogram import filters, Client
from youtube_search import YoutubeSearch

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


@Client.on_message(filters.command('song') & ~filters.private & ~filters.channel)
def song(client, message):

    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"

    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply("𝙍𝙊𝙔𝘼𝙇-𝙈𝙐𝙎𝙄𝘾𝙓𝘿🎧 𝙋𝙍𝙊𝘾𝙀𝙎𝙎𝙄𝙉𝙂 𝙏𝙊 𝘿𝙊𝙒𝙉𝙇𝙊𝘼𝘿 𝙏𝙃𝙀 𝙎𝙊𝙉𝙂.........❤️")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)


        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        m.edit(
            "𝙎𝙤𝙣𝙜 🌠 𝙉𝙤𝙩 𝙁𝙤𝙪𝙣𝙙😔 "
        )
        print(str(e))
        return
    m.edit("𝙍𝙊𝙔𝘼𝙇-𝙈𝙐𝙎𝙄𝘾𝙓𝘿🎧 𝙋𝙍𝙊𝘾𝙀𝙎𝙎𝙄𝙉𝙂 𝙏𝙊 𝘿𝙊𝙒𝙉𝙇𝙊𝘼𝘿 𝙏𝙃𝙀 𝙎𝙊𝙉𝙂.........❤️")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = "**🎵 𝙐𝙋𝙇𝙊𝘼𝘿𝙀𝘿 𝘽𝙔✨- [👨‍💻𝙇𝙀𝙂𝙀𝙉𝘿👨‍💻](https://t.me/KartiK_KinG01) ❤️**"
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, thumb=thumb_name, parse_mode='md', title=title, duration=dur)
        m.delete()
    except Exception as e:
        m.edit("**𝙔𝙤𝙪𝙏𝙪𝙗𝙚 𝙚𝙧𝙧𝙤𝙧 ❌ 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐎𝐰𝐧𝐞𝐫 🥀 [👨‍💻 𝙇𝙀𝙂𝙀𝙉𝘿 👨‍💻](https://t.me/KartiK_KinG01) ❤️**")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)