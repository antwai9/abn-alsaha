# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @bar_lo0o0 © Rocks
# Owner BARLO


import re
import asyncio

from config import ASSISTANT_NAME, BOT_USERNAME, IMG_1, IMG_2, GROUP_SUPPORT
from rocksdriver.filters import command, other_filters
from rocksdriver.queues import QUEUE, add_to_queue
from rocksdriver.asad import call_py, user
from pyrogram import Client
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped
from youtubesearchpython import VideosSearch


def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1)
        for r in search.result()["result"]:
            ytid = r["id"]
            if len(r["title"]) > 34:
                songname = r["title"][:70]
            else:
                songname = r["title"]
            url = f"https://www.youtube.com/watch?v={ytid}"
        return [songname, url]
    except Exception as e:
        print(e)
        return 0


async def ytdl(link):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        "bestaudio",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if stdout:
        return 1, stdout.decode().split("\n")[0]
    else:
        return 0, stderr.decode()


@Client.on_message(command(["play", f"play@{BOT_USERNAME}"]) & other_filters)
async def play(c: Client, m: Message):
    replied = m.reply_to_message
    chat_id = m.chat.id
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("❤️ ʜᴇᴀʀᴛ ❤️", url=f"https://t.me/bar_lo0o0o0o0o"),
                InlineKeyboardButton("👨‍‍👧‍👦 ɢʀᴏᴜᴘ 👨‍👧‍👦", url=f"https://t.me/{GROUP_SUPPORT}"),
            ]
        ]
    )
    if m.sender_chat:
        return await m.reply_text("**ʏᴏᴜ'ʀᴇ ᴀɴ __Aɴᴏɴʏᴍᴏᴜs Aᴅᴍɪɴ__ !\n\n» ʀᴇᴠᴇʀᴛ ʙᴀᴄᴋ ᴛᴏ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ ғʀᴏᴍ ᴀᴅᴍɪɴ ʀɪɢʜᴛs.**")
    try:
        aing = await c.get_me()
    except Exception as e:
        return await m.reply_text(f"**Eʀʀᴏʀ**:\n\n{e}")
    a = await c.get_chat_member(chat_id, aing.id)
    if a.status != "administrator":
        await m.reply_text(
            f"💡 Tᴏ ᴜsᴇ ᴍᴇ, I ɴᴇᴇᴅ ᴛᴏ ʙᴇ ᴀɴ **Aᴅᴍɪɴɪsᴛʀᴀᴛᴏʀ** ᴡɪᴛʜ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ **ᴘᴇʀᴍɪssɪᴏɴs**:\n\n» ❌ __Dᴇʟᴇᴛᴇ ᴍᴇssᴀɢᴇs__\n» ❌ __Rᴇsᴛʀɪᴄᴛ ᴜsᴇʀs__\n» ❌ __Aᴅᴅ ᴜsᴇʀs__\n» ❌ __Mᴀɴᴀɢᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ__\n\nDᴀᴛᴀ ɪs **ᴜᴘᴅᴀᴛᴇᴅ** ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴀғᴛᴇʀ ʏᴏᴜ **ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ**"
        )
        return
    if not a.can_manage_voice_chats:
        await m.reply_text(
            "**ᴍɪssɪɴɢ ʀᴇϙᴜɪʀᴇᴅ ᴘᴇʀᴍɪssɪᴏɴ:**" + "\n\n» ❌ **__Mᴀɴᴀɢᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ__**"
        )
        return
    if not a.can_delete_messages:
        await m.reply_text(
            "**ᴍɪssɪɴɢ ʀᴇϙᴜɪʀᴇᴅ ᴘᴇʀᴍɪssɪᴏɴ:**" + "\n\n» ❌ **__Dᴇʟᴇᴛᴇ ᴍᴇssᴀɢᴇs__**"
        )
        return
    if not a.can_invite_users:
        await m.reply_text("**ᴍɪssɪɴɢ ʀᴇϙᴜɪʀᴇᴅ ᴘᴇʀᴍɪssɪᴏɴ**:" + "\n\n» ❌ **__Aᴅᴅ ᴜsᴇʀs__**")
        return
    try:
        ubot = (await user.get_me()).id
        b = await c.get_chat_member(chat_id, ubot)
        if b.status == "kicked":
            await m.reply_text(
                f"@{ASSISTANT_NAME} **ɪs ʙᴀɴɴᴇᴅ ɪɴ ɢʀᴏᴜᴘ** {m.chat.title}\n\n» **ᴜɴʙᴀɴ ᴛʜᴇ ᴜsᴇʀʙᴏᴛ ғɪʀsᴛ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ.**"
            )
            return
    except UserNotParticipant:
        if m.chat.username:
            try:
                await user.join_chat(m.chat.username)
            except Exception as e:
                await m.reply_text(f"❌ **ᴜsᴇʀʙᴏᴛ ғᴀɪʟᴇᴅ ᴛᴏ ᴊᴏɪɴ**\n\n**ʀᴇᴀsᴏɴ**: `{e}`")
                return
        else:
            try:
                user_id = (await user.get_me()).id
                link = await c.export_chat_invite_link(chat_id)
                if "+" in link:
                    link_hash = (link.replace("+", "")).split("t.me/")[1]
                    await ubot.join_chat(link_hash)
                await c.promote_member(chat_id, user_id)
            except UserAlreadyParticipant:
                pass
            except Exception as e:
                return await m.reply_text(
                    f"❌ **ᴜsᴇʀʙᴏᴛ ғᴀɪʟᴇᴅ ᴛᴏ ᴊᴏɪɴ**\n\n**ʀᴇᴀsᴏɴ**: `{e}`"
                )
    if replied:
        if replied.audio or replied.voice:
            suhu = await replied.reply("📥 **Dᴏᴡɴʟᴏᴀᴅɪɴɢ ᴀᴜᴅɪᴏ...**")
            dl = await replied.download()
            link = replied.link
            if replied.audio:
                if replied.audio.title:
                    songname = replied.audio.title[:70]
                else:
                    if replied.audio.file_name:
                        songname = replied.audio.file_name[:70]
                    else:
                        songname = "Audio"
            elif replied.voice:
                songname = "Voice Note"
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await suhu.delete()
                await m.reply_photo(
                    photo=f"{IMG_1}",
                    caption=f"💡 **ᴛʀᴀᴄᴋ ᴀᴅᴅᴇᴅ ᴛᴏ ǫᴜᴇᴜᴇ »** `{pos}`\n\n🏷 **ɴᴀᴍᴇ:** [{songname[:10]}]({link})\n💭 **ᴄʜᴀᴛ:** `{chat_id}`\n🎧 **ʀᴇǫᴜᴇsᴛ ʙʏ:** {requester}",
                reply_markup=keyboard,
                )
            else:
             try:
                await suhu.edit("🔄 **Jᴏɪɴɪɴɢ ᴠᴄ...**")
                await call_py.join_group_call(
                    chat_id,
                    AudioPiped(
                        dl,
                    ),
                    stream_type=StreamType().local_stream,
                )
                add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await suhu.delete()
                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                await m.reply_photo(
                    photo=f"{IMG_2}",
                    caption=f"💡 **ᴀᴜᴅɪᴏ sᴛʀᴇᴀᴍɪɴɢ sᴛᴀʀᴛᴇᴅ**\n\n🏷 **ɴᴀᴍᴇ:** [{songname[:10]}]({url})\n💡 **sᴛᴀᴛᴜs:** `Playing`\n🎧 **ʀᴇǫᴜᴇsᴛ ʙʏ:** {requester}",
                    reply_markup=keyboard,
              )
             except Exception as e:
                await suhu.delete()
                await m.reply_text(f"🚫 **Eʀʀᴏʀ**:\n\n» {e}")
        else:
            if len(m.command) < 2:
                await m.reply(
                    "**» ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ᴀᴜᴅɪᴏ ғɪʟᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇᴛʜɪɴɢ ᴛᴏ sᴇᴀʀᴄʜ.**"
                )
            else:
                suhu = await c.send_message(chat_id, "🔎 **Sᴇᴀʀᴄʜɪɴɢ...**")
                query = m.text.split(None, 1)[1]
                search = ytsearch(query)
                if search == 0:
                    await suhu.edit("❌ **Nᴏ ʀᴇsᴜʟᴛ ғᴏᴜɴᴅ.**")
                else:
                    songname = search[0]
                    url = search[1]
                    veez, ytlink = await ytdl(url)
                    if veez == 0:
                        await suhu.edit(f"❌ yt-dl **Issᴜᴇs ᴅᴇᴛᴇᴄᴛᴇᴅ**\n\n» `{ytlink}`")
                    else:
                        if chat_id in QUEUE:
                            pos = add_to_queue(
                                chat_id, songname, ytlink, url, "Audio", 0
                            )
                            await suhu.delete()
                            requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                            await m.reply_photo(
                                photo=f"{IMG_1}",
                                caption=f"💡 **sᴏɴɢ ᴀᴅᴅᴇᴅ ᴛᴏ ǫᴜᴇᴜᴇ »** `{pos}`\n\n🏷 **ɴame:** [{songname[:10]}]({url})\n🎧 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {requester}",
                                reply_markup=keyboard,
                            )
                        else:
                            try:
                                await suhu.edit("🔄 **Jᴏɪɴɪɴɢ ᴠᴄ...**")
                                await call_py.join_group_call(
                                    chat_id,
                                    AudioPiped(
                                        ytlink,
                                    ),
                                    stream_type=StreamType().local_stream,
                                )
                                add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                                await suhu.delete()
                                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                                await m.reply_photo(
                                    photo=f"{IMG_2}",
                                    caption=f"💡 **ᴍᴜsɪᴄ sᴛʀᴇᴀᴍɪɴɢ sᴛᴀʀᴛᴇᴅ.**\n\n🏷 **ɴᴀᴍᴇ:** [{songname[:10]}]({url})\n💡 **sᴛᴀᴛᴜs:** `Playing`\n🎧 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {requester}",
                                    reply_markup=keyboard,
                                )
                            except Exception as ep:
                                await suhu.delete()
                                await m.reply_text(f"🚫 **Eʀʀᴏʀ**: `{ep}`")

    else:
        if len(m.command) < 2:
            await m.reply(
                    "**» ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ᴀᴜᴅɪᴏ ғɪʟᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇᴛʜɪɴɢ ᴛᴏ sᴇᴀʀᴄʜ.**"
                )
        else:
            suhu = await c.send_message(chat_id, "🔎 **Sᴇᴀʀᴄʜɪɴɢ...**")
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            if search == 0:
                await suhu.edit("❌ **Rᴇsᴜʟᴛ ɴᴏᴛ ғᴏᴜɴᴅ.**")
            else:
                songname = search[0]
                url = search[1]
                veez, ytlink = await ytdl(url)
                if veez == 0:
                    await suhu.edit(f"❌ yt-dl **ɪssᴜᴇs ᴅᴇᴛᴇᴄᴛᴇᴅ**\n\n» `{ytlink}`")
                else:
                    if chat_id in QUEUE:
                        pos = add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                        await suhu.delete()
                        requester = (
                            f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                        )
                        await m.reply_photo(
                            photo=f"{IMG_1}",
                            caption=f"💡 **ᴛʀᴀᴄᴋ ᴀᴅᴅᴇᴅ ᴛᴏ ǫᴜᴇᴜᴇ »** `{pos}`\n\n🏷 **ɴᴀᴍᴇ:** [{songname[:10]}]({url})\n🎧 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {requester}",
                            reply_markup=keyboard,
                        )
                    else:
                        try:
                            await suhu.edit("🔄 **Jᴏɪɴɪɴɢ ᴠᴄ...**")
                            await call_py.join_group_call(
                                chat_id,
                                AudioPiped(
                                    ytlink,
                                ),
                                stream_type=StreamType().local_stream,
                            )
                            add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                            await suhu.delete()
                            requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                            await m.reply_photo(
                                photo=f"{IMG_2}",
                                caption=f"💡 **Mᴜsɪᴄ sᴛʀᴇᴀᴍɪɴɢ sᴛᴀʀᴛᴇᴅ.**\n\n🏷 **ɴᴀᴍᴇ:** [{songname[:10]}]({url})\n💡 **sᴛᴀᴛᴜs:** `Playing`\n🎧 **ʀᴇǫᴜᴇsᴛ ʙʏ:** {requester}",
                                reply_markup=keyboard,
                            )
                        except Exception as ep:
                            await suhu.delete()
                            await m.reply_text(f"🚫 **Eʀʀᴏʀ**: `{ep}`")


# stream is used for live streaming only


@Client.on_message(command(["stream", f"stream@{BOT_USERNAME}"]) & other_filters)
async def stream(c: Client, m: Message):
    chat_id = m.chat.id
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("❤️ ʜᴇᴀʀᴛ ❤️", url=f"https://t.me/bar_lo0o0o0o0o"),
                InlineKeyboardButton("👨‍‍👧‍👦 ɢʀᴏᴜᴘ 👨‍👧‍👦", url=f"https://t.me/{GROUP_SUPPORT}"),
            ]
        ]
    )
    if m.sender_chat:
         return await m.reply_text("**ʏᴏᴜ'ʀᴇ ᴀɴ __Aɴᴏɴʏᴍᴏᴜs Aᴅᴍɪɴ__ !\n\n» ʀᴇᴠᴇʀᴛ ʙᴀᴄᴋ ᴛᴏ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ ғʀᴏᴍ ᴀᴅᴍɪɴ ʀɪɢʜᴛs.**")
    try:
        aing = await c.get_me()
    except Exception as e:
        return await m.reply_text(f"*Eʀʀᴏʀ**:\n\n{e}")
    a = await c.get_chat_member(chat_id, aing.id)
    if a.status != "administrator":
        await m.reply_text(
            f"💡 Tᴏ ᴜsᴇ ᴍᴇ, I ɴᴇᴇᴅ ᴛᴏ ʙᴇ ᴀɴ **Aᴅᴍɪɴɪsᴛʀᴀᴛᴏʀ** ᴡɪᴛʜ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ **ᴘᴇʀᴍɪssɪᴏɴs**:\n\n» ❌ __Dᴇʟᴇᴛᴇ ᴍᴇssᴀɢᴇs__\n» ❌ __Rᴇsᴛʀɪᴄᴛ ᴜsᴇʀs__\n» ❌ __Aᴅᴅ ᴜsᴇʀs__\n» ❌ __Mᴀɴᴀɢᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ__\n\nDᴀᴛᴀ ɪs **ᴜᴘᴅᴀᴛᴇᴅ** ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴀғᴛᴇʀ ʏᴏᴜ **ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ**"
        )
        return
    if not a.can_manage_voice_chats:
        await m.reply_text(
            "**ᴍɪssɪɴɢ ʀᴇϙᴜɪʀᴇᴅ ᴘᴇʀᴍɪssɪᴏɴ:**" + "\n\n» ❌ **__Mᴀɴᴀɢᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ__**"
        )
        return
    if not a.can_delete_messages:
        await m.reply_text(
            "**ᴍɪssɪɴɢ ʀᴇϙᴜɪʀᴇᴅ ᴘᴇʀᴍɪssɪᴏɴ:**" + "\n\n» ❌ **__Dᴇʟᴇᴛᴇ ᴍᴇssᴀɢᴇs__**"
        )
        return
    if not a.can_invite_users:
        await m.reply_text("**ᴍɪssɪɴɢ ʀᴇϙᴜɪʀᴇᴅ ᴘᴇʀᴍɪssɪᴏɴ**:" + "\n\n» ❌ **__Aᴅᴅ ᴜsᴇʀs__**")
        return
    try:
        ubot = (await user.get_me()).id
        b = await c.get_chat_member(chat_id, ubot)
        if b.status == "kicked":
            await m.reply_text(
                f"@{ASSISTANT_NAME} **ɪs ʙᴀɴɴᴇᴅ ɪɴ ɢʀᴏᴜᴘ** {m.chat.title}\n\n» **ᴜɴʙᴀɴ ᴛʜᴇ ᴜsᴇʀʙᴏᴛ ғɪʀsᴛ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ.**"
            )
            return
    except UserNotParticipant:
        if m.chat.username:
            try:
                await user.join_chat(m.chat.username)
            except Exception as e:
                await m.reply_text(f"❌ **ᴜsᴇʀʙᴏᴛ ғᴀɪʟᴇᴅ ᴛᴏ ᴊᴏɪɴ**\n\n**ʀᴇᴀsᴏɴ**: `{e}`")
                return
        else:
            try:
                user_id = (await user.get_me()).id
                link = await c.export_chat_invite_link(chat_id)
                if "+" in link:
                    link_hash = (link.replace("+", "")).split("t.me/")[1]
                    await ubot.join_chat(link_hash)
                await c.promote_member(chat_id, user_id)
            except UserAlreadyParticipant:
                pass
            except Exception as e:
                return await m.reply_text(
                    f"❌ **ᴜsᴇʀʙᴏᴛ ғᴀɪʟᴇᴅ ᴛᴏ ᴊᴏɪɴ**\n\n**reason**: `{e}`"
                )

    if len(m.command) < 2:
        await m.reply("» **ɢɪᴠᴇ ᴍᴇ ᴀ live-link/m3u8 url/youtube ʟɪɴᴋ ᴛᴏ sᴛʀᴇᴀᴍ**.")
    else:
        link = m.text.split(None, 1)[1]
        suhu = await c.send_message(chat_id, "🔄 **Pʀᴏᴄᴇssɪɴɢ ʟɪᴠᴇ sᴛʀᴇᴀᴍ...**")

        regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
        match = re.match(regex, link)
        if match:
            asad, livelink = await ytdl(link)
        else:
            livelink = link
            asad = 1

        if asad == 0:
            await suhu.edit(f"❌ yt-dl **ɪssᴜᴇs ᴅᴇᴛᴇᴄᴛᴇᴅ**\n\n» `{livelink}`")
        else:
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, "Radio", livelink, link, "Audio", 0)
                await suhu.delete()
                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                await m.reply_photo(
                    photo=f"{IMG_1}",
                    caption=f"💡 **ᴛʀᴀᴄᴋ ᴀᴅᴅᴇᴅ ᴛᴏ ǫᴜᴇᴜᴇ »** `{pos}`\n\n🎧 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {requester}",
                    reply_markup=keyboard,
                )
            else:
                try:
                    await suhu.edit("🔄 **Jᴏɪɴɪɴɢ ᴠᴄ...**")
                    await call_py.join_group_call(
                        chat_id,
                        AudioPiped(
                            livelink,
                        ),
                        stream_type=StreamType().live_stream,
                    )
                    add_to_queue(chat_id, "Radio", livelink, link, "Audio", 0)
                    await suhu.delete()
                    requester = (
                        f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                    )
                    await m.reply_photo(
                        photo=f"{IMG_2}",
                        caption=f"💡 **[Music live]({link}) stream started.**\n\n💭 **Chat:** `{chat_id}`\n💡 **Status:** `Playing`\n🎧 **Request by:** {requester}",
                        reply_markup=keyboard,
                    )
                except Exception as ep:
                    await suhu.delete()
                    await m.reply_text(f"🚫 error: `{ep}`")