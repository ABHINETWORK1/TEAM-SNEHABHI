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
                        "π« πΌπ°πππΈ πΆππΎππΏ π", url=f"https://t.me/LIVE_LIKE_LIFE")],
                [
                    InlineKeyboardButton(
                        "π«πΎππ½π΄π πΊπΈπ½πΆβ¨", url=f"https://t.me/SNEHU_IS_MINE")
                ],[
                    InlineKeyboardButton(
                        "π«πΎππ½π΄π πππ΄π΄π½β¨", url=f"HTTP://T.ME/ABHI_IS_MINE")
                ],[
                    InlineKeyboardButton(
                         "π«πππΏπΏπΎπTβ¨", url=f"https://t.me/SNEHABHI_SERVER"),
                    InlineKeyboardButton(
                         "π« π²π·π°π½π½π΄π»β¨", url=f"http://t.me/ABHI_NETWORK1")
                ]     
             ]    
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        f"""**SNEHABHI SERVER IS OΙ΄ΚΙͺΙ΄α΄ β**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π«πππΏπΏπΎππ β¨", url=f"https://t.me/SNEHABHI_SERVER"
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
            [InlineKeyboardButton(text = 'βΆοΈ', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = f"https://t.me/SNEHABHI_SERVER"
        button = [
            [InlineKeyboardButton("π« πΌπ°πππΈ πΆππΎππΏ π", url=f"https://t.me/LIVE_LIKE_LIFE")],
            [InlineKeyboardButton(text = 'π Ζ²Ζ₯ΙΙΚΙs', url=f"https://t.me/ABHI_NETWORK1"),
             InlineKeyboardButton(text = 'π«πππΏπΏπΎππ β¨', url=f"https://t.me/SNEHABHI_SERVER")],
            [InlineKeyboardButton(text = 'π«πΎππ½π΄π πΊπΈπ½πΆβ¨', url=f"https://t.me/SNEHU_IS_MINE")],
            [InlineKeyboardButton(text = 'π«πΎππ½π΄π πππ΄π΄π½β¨', url=f"HTTP://T.ME/ABHI_IS_MINE")],
            [InlineKeyboardButton(text = 'βοΈ', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = 'βοΈ', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = 'βΆοΈ', callback_data = f"help+{pos+1}")
            ],
        ]
    return button

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""**πβ κͺΙΙ­Ι­ΓΈ, I ΙΙ± ΙΙ³ ΙΙβ±±ΙΙ³ΖΙΙ Ζ€rΙΙ±Ι©ΚΙ± β±?ΚsΙ©Ζ Ζ€Ι­ΙΖ΄Ιr ΖΓΈΚ ΖrΙΙΚΙΙ ΖΖ΄ [SNEHU & ABHI ](t.me/SNEHABHI_SERVER). I ΖΙΙ³ Ζ€Ι­ΙΖ΄ β±?ΚsΙ©Ζ Ι©Ι³ YΓΈΚr Ζ¬ΙΙ­ΙΚrΙΙ± ΖΙ¦ΙΙ³Ι³ΙΙ­ ΓΈr ΖrΓΈuΖ₯ VΓΈΙ©ΖΙ ΖΙ¦ΙΚ ...**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π« πΌπ°πππΈ πΆππΎππΏ π", url=f"https://t.me/LIVE_LIKE_LIFE"
                    )
                ]
            ]
        ),
    )


