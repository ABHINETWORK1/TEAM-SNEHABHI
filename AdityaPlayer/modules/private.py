# SNEHABHI SERVER (Telegram bot project )
# Copyright (C)  SNEHABHI SERVER

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging
from AdityaPlayer.modules.msg import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from AdityaPlayer.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL,BOT_USERNAME
logging.basicConfig(level=logging.INFO)

@Client.on_message(filters.private & filters.incoming & filters.command(['start']))
def _start(client, message):
    client.send_message(message.chat.id,
        text=tr.START_MSG.format(message.from_user.first_name, message.from_user.id),
        parse_mode="markdown",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💫 𝙼𝙰𝚂𝚃𝙸 𝙶𝚁𝙾𝚄𝙿 👈", url=f"https://t.me/LIVE_LIKE_LIFE")],
                [
                    InlineKeyboardButton(
                        "💫𝙾𝚆𝙽𝙴𝚁 𝙺𝙸𝙽𝙶✨", url=f"https://t.me/SNEHU_IS_MINE")
                ],[
                    InlineKeyboardButton(
                        "💫𝙾𝚆𝙽𝙴𝚁 𝚀𝚄𝙴𝙴𝙽✨", url=f"HTTP://T.ME/ABHI_IS_MINE")
                ],[
                    InlineKeyboardButton(
                         "💫𝚂𝚄𝙿𝙿𝙾𝚁T✨", url=f"https://t.me/SNEHABHI_SERVER")
                    InlineKeyboardButton(
                         "💫 𝙲𝙷𝙰𝙽𝙽𝙴𝙻✨", url=f"http://t.me/ABHI_NETWORK1")
                ]     
             ]    
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        f"""**SNEHABHI SERVER IS Oɴʟɪɴᴇ ✅**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💫𝚂𝚄𝙿𝙿𝙾𝚁𝚃 ✨", url=f"https://t.me/SNEHABHI_SERVER"
                    )
                ]
            ]
        ),
    )


@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = '▶️', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = f"https://t.me/SNEHABHI_SERVER"
        button = [
            [InlineKeyboardButton("💫 𝙼𝙰𝚂𝚃𝙸 𝙶𝚁𝙾𝚄𝙿 👈", url=f"https://t.me/LIVE_LIKE_LIFE")],
            [InlineKeyboardButton(text = '🌐 Ʋƥɗɑʈɘs', url=f"https://t.me/ABHI_NETWORK1"),
             InlineKeyboardButton(text = '💫𝚂𝚄𝙿𝙿𝙾𝚁𝚃 ✨', url=f"https://t.me/SNEHABHI_SERVER")],
            [InlineKeyboardButton(text = '💫𝙾𝚆𝙽𝙴𝚁 𝙺𝙸𝙽𝙶✨', url=f"https://t.me/SNEHU_IS_MINE")],
            [InlineKeyboardButton(text = '💫𝙾𝚆𝙽𝙴𝚁 𝚀𝚄𝙴𝙴𝙽✨', url=f"HTTP://T.ME/ABHI_IS_MINE")],
            [InlineKeyboardButton(text = '◀️', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '◀️', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '▶️', callback_data = f"help+{pos+1}")
            ],
        ]
    return button

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""**🙋‍ Ɦɘɭɭø, I ɑɱ ɑɳ Ʌɗⱱɑɳƈɘɗ Ƥrɘɱɩʋɱ Ɱʉsɩƈ Ƥɭɑƴɘr Ɓøʈ Ƈrɘɑʈɘɗ Ɓƴ [SNEHU & ABHI ](t.me/SNEHABHI_SERVER). I Ƈɑɳ Ƥɭɑƴ Ɱʉsɩƈ ɩɳ Yøʋr Ƭɘɭɘʛrɑɱ Ƈɦɑɳɳɘɭ ør Ɠrøuƥ Vøɩƈɘ Ƈɦɑʈ ...**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💫 𝙼𝙰𝚂𝚃𝙸 𝙶𝚁𝙾𝚄𝙿 👈", url=f"https://t.me/LIVE_LIKE_LIFE"
                    )
                ]
            ]
        ),
    )


