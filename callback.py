# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ✅ • يسمح لك بالبحث عن الموسيقي والفيديو وتشغيلها في المجموعات من خلال المحادثه الصوتيه في تليجرام**

💡 **اكتشف جميع أوامر الروبوت وكيفية عملها من خلال النقر على زر الأوامر »📚**

🔖 **لمعرفة كيفية استخدام هذا الروبوت ، الرجاء النقر فوق الزر »🎧 كيفية الأستخدام !**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ 🎞 اضَِٖـفٍُ آلٓبَٰـۄټِٖ إلٓيَ مج ـمۄعَِٰټِٖـڪ 🎞 ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("🎧 ڪيَفٍُيَـة آس๋͜ټِٖخدآم هذآ آلٓرۄبَٰـۄټِٖ 🎧", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 آلٓأۄآمــر 📚", callback_data="cbcmds"),
                    InlineKeyboardButton("👨‍💻 لٓلٓأس๋͜‏ټِٖـفٍُس๋͜‏ـآࢪآټِٖ 👩‍💻", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "🎥 ج ـرۄبَٰ آلٓدعَِٰـم 🎥", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 قٍُنـآة آلٓس๋͜‏ـۄࢪس๋͜‏  📣", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "♔↯ ᴅᴇᴠ • ʙᴀʀʟᴏ ↯♔", url="https://t.me/bar_lo0o0"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **الدليل الأساسي لأستخدام هذا الروبوت:**

1.) **أولا أضفني إلي مجموعتك.**
2.) **بعد ذلك ، قم بترقيتي كمسؤول ومنح جميع الأذونات باستثناء المسؤول المجهول.**
3.) **بعد ترقيتي ، اكتب /reload في المجموعة لتحديث بيانات المسؤول.**
4.) **أضف @{ASSISTANT_NAME} لمجموعتك أو اكتب /userbotjoin لدعوه الحساب المساعد.**
5.) **قم بتشغيل محادثة الفيديو أولاً قبل البدء في تشغيل الفيديو / الموسيقى.**
6.) **في بعض الأحيان ، يتم إعادة تحميل الروبوت باستخدام /reload يمكن أن يساعدك الأمر في حل بعض المشكلات.**

📌 **إذا لم ينضم المستخدم bot إلى دردشة الفيديو ، فتأكد من تشغيل دردشة الفيديو بالفعل ، أو اكتب /userbotleave ثم اكتب /userbotjoin مره اخرى.**

💡 **إذا كانت لديك أسئلة متابعة حول هذا الروبوت ، فيمكنك إخباره من خلال دردشة الدعم الخاصة بي هنا: @{GROUP_SUPPORT}**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **اضغط على الزر أدناه لقراءة الشرح ومشاهدة قائمة الأوامر المتاحة! !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 Sudo Cmd", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 آلٓأۄآمــر", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
      f"""🏮 أهلا عزيزي هذه هي الأوامر الأساسية للروبوت

» /mplay (اسم الأغنية / رابط) - تشغيل الموسيقى على دردشة الفيديو
» /vplay (اسم / رابط الفيديو) - تشغيل الفيديو على دردشة الفيديو
» /vstream - تشغيل فيديو مباشر من yt live / m3u8
» /playlist - تظهر لك قائمة التشغيل
» /video (استعلام) - تنزيل الفيديو من youtube
» /song (استعلام) - تنزيل أغنية من youtube
» /lyric (استعلام) - قص الأغنية الغنائية
» /search (استعلام) - ابحث عن رابط فيديو youtube

» /ping - إظهار حالة البوت بينغ
» /uptime - إظهار حالة وقت تشغيل الروبوت
» /alive - عرض معلومات الروبوت على قيد الحياة (في مجموعة)

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the admin commands:

» /pause - pause the stream
» /resume - resume the stream
» /skip - switch to next stream
» /stop - stop the streaming
» /vmute - mute the userbot on voice chat
» /vunmute - unmute the userbot on voice chat
» /volume `1-200` - adjust the volume of music (userbot must be admin)
» /reload - reload bot and refresh the admin data
» /userbotjoin - invite the userbot to join group
» /userbotleave - order userbot to leave from group

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the sudo commands:

» /rmw - clean all raw files
» /rmd - clean all downloaded files
» /sysinfo - show the system information
» /update - update your bot to latest version
» /restart - restart your bot
» /leaveall - order userbot to leave from all group

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **settings of** {query.message.chat.title}\n\n⏸ : pause stream\n▶️ : resume stream\n🔇 : mute userbot\n🔊 : unmute userbot\n⏹ : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()
