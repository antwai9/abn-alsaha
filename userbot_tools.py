# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @bar_lo0o0 © Rocks
# Owner BARLO




import asyncio
from rocksdriver.asad import user
from pyrogram.types import Message
from pyrogram import Client, filters
from config import BOT_USERNAME, SUDO_USERS
from rocksdriver.filters import command, other_filters
from pyrogram.errors import UserAlreadyParticipant
from rocksdriver.decorators import authorized_users_only, sudo_users_only


@Client.on_message(
    command(["join", f"join@{BOT_USERNAME}"]) & ~filters.private & ~filters.bot
)
@authorized_users_only
async def join_chat(c: Client, m: Message):
    chat_id = m.chat.id
    try:
        invite_link = await m.chat.export_invite_link()
        if "+" in invite_link:
            link_hash = (invite_link.replace("+", "")).split("t.me/")[1]
            await user.join_chat(f"https://t.me/joinchat/{link_hash}")
        await m.chat.promote_member(
            (await user.get_me()).id,
            can_manage_voice_chats=True
        )
        return await user.send_message(chat_id, "✅ **Usᴇʀʙᴏᴛ ᴊᴏɪɴᴅ ᴛʜᴇ ᴄʜᴀᴛ**")
    except UserAlreadyParticipant:
        admin = await m.chat.get_member((await user.get_me()).id)
        if not admin.can_manage_voice_chats:
            await m.chat.promote_member(
                (await user.get_me()).id,
                can_manage_voice_chats=True
            )
            return await user.send_message(chat_id, "✅ **Usᴇʀʙᴏᴛ ᴀʟʀᴇᴀᴅʏ ɪɴ ᴄʜᴀᴛ**")
        return await user.send_message(chat_id, "✅ **Usᴇʀʙᴏᴛ ᴀʟʀᴇᴀᴅʏ ɪɴ ᴄʜᴀᴛ**")


@Client.on_message(command(["userbotleave",
                            f"leave@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
@authorized_users_only
async def leave_chat(_, m: Message):
    chat_id = m.chat.id
    try:
        await user.leave_chat(chat_id)
        return await _.send_message(
            chat_id,
            "✅ **Usᴇʀʙᴏᴛ ʟᴇᴀᴠᴇᴅ ᴛʜᴇ ᴄʜᴀᴛ**",
        )
    except UserNotParticipant:
        return await _.send_message(
            chat_id,
            "❌ **Usᴇʀʙᴏᴛ ᴀʟʀᴇᴀᴅʏ ʟᴇᴀᴠᴇ ᴛʜᴇ ᴄʜᴀᴛ**",
        )


@Client.on_message(command(["leaveall", f"leaveall@{BOT_USERNAME}"]))
@sudo_users_only
async def leave_all(client, message):
    if message.from_user.id not in SUDO_USERS:
        return

    left = 0
    failed = 0
    lol = await message.reply("🔄 **ᴜsᴇʀʙᴏᴛ** leaving all chats !")
    async for dialog in USER.iter_dialogs():
        try:
            await USER.leave_chat(dialog.chat.id)
            left += 1
            await lol.edit(
                f"Userbot leaving all group...\n\nLeft: {left} chats.\nFailed: {failed} chats."
            )
        except BaseException:
            failed += 1
            await lol.edit(
                f"Userbot leaving...\n\nLeft: {left} chats.\nFailed: {failed} chats."
            )
        await asyncio.sleep(0.7)
    await client.send_message(
        message.chat.id, f"✅ Left from: {left} chats.\n❌ Failed in: {failed} chats."
    )
