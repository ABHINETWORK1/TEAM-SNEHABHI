# SNEHABHI SERVER - Telegram bot for streaming audio in group calls
# Copyright (C) 2021  SNEHABHI SERVER

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


from asyncio import QueueEmpty
from AdityaPlayer.config import que
from pyrogram import Client, filters
from pyrogram.types import Message

from AdityaPlayer.function.admins import set
from AdityaPlayer.helpers.channelmusic import get_chat_id
from AdityaPlayer.helpers.decorators import authorized_users_only, errors
from AdityaPlayer.helpers.filters import command, other_filters
from AdityaPlayer.services.callsmusic import callsmusic
from AdityaPlayer.services.queues import queues


@Client.on_message(filters.command("adminreset"))
async def update_admin(client, message: Message):
    chat_id = get_chat_id(message.chat)
    set(
        chat_id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("**@SNEHABHI_SERVER ✨ 𝐀𝐃𝐌𝐈𝐍𝐂𝐀𝐂𝐇𝐄 𝐔𝐏𝐃𝐀𝐓𝐄𝐃 ✨**")


@Client.on_message(command("pause") & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[chat_id] == "paused"
    ):
        await message.reply_text("**@SNEHABHI_SERVER 😗 𝗡𝗼𝘁𝗵𝗶𝗻𝗴 𝗜𝘀 𝗣𝗹𝗮𝘆𝗶𝗻𝗴 ✨**")
    else:
        callsmusic.pytgcalls.pause_stream(chat_id)
        await message.reply_text("**@SNEHABHI_SERVER 😗 𝗣𝗮𝘂𝘀𝗲𝗱 😔🤟**️")


@Client.on_message(command("resume") & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[chat_id] == "playing"
    ):
        await message.reply_text("**@SNEHABHI_SERVER 😗 𝗡𝗼𝘁𝗵𝗶𝗻𝗴 𝗜𝘀 𝗣𝗹𝗮𝘆𝗶𝗻𝗴 ✨**")
    else:
        callsmusic.pytgcalls.resume_stream(chat_id)
        await message.reply_text("**@SNEHABHI_SERVER 😗 𝗥𝗲𝘀𝘂𝗺𝗲𝗱 ❤️🤟**")


@Client.on_message(command("end") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("**@SNEHABHI_SERVER 😗 𝗡𝗼𝘁𝗵𝗶𝗻𝗴 𝗜𝘀 𝗣𝗹𝗮𝘆𝗶𝗻𝗴 ✨**")
    else:
        try:
            callsmusic.queues.clear(chat_id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(chat_id)
        await message.reply_text("**@SNEHABHI_SERVER 😗 𝗦𝘁𝗼𝗽 🛑 𝗦𝘁𝗿𝗲𝗮𝗺𝗶𝗻𝗴 ✨**")


@Client.on_message(command("skip") & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("**@SNEHABHI_SERVER 😗 𝗡𝗼𝘁𝗵𝗶𝗻𝗴 😔 𝗜𝘀 𝗣𝗹𝗮𝘆𝗶𝗻𝗴 🎶 𝗧𝗼 𝗦𝗸𝗶𝗽 💫**")
    else:
        callsmusic.queues.task_done(chat_id)

        if callsmusic.queues.is_empty(chat_id):
            callsmusic.pytgcalls.leave_group_call(chat_id)
        else:
            callsmusic.pytgcalls.change_stream(
                chat_id, callsmusic.queues.get(chat_id)["file"]
            )

    qeue = que.get(chat_id)
    if qeue:
        skip = qeue.pop(0)
    if not qeue:
        return
    await message.reply_text(f"**@SNEHABHI SERVER 😗 𝗦𝗸𝗶𝗽 💫 𝗧𝗵𝗲 𝗖𝘂𝗿𝗿𝗲𝗻𝘁 😊 𝗦𝗼𝗻𝗴 ❤️🤟** **{skip[0]}**\n**▶️ Ɲøω Ƥɭɑƴɩɳʛ** **{qeue[0][0]}**")


@Client.on_message(filters.command("admincache"))
@errors
async def admincache(client, message: Message):
    set(
        message.chat.id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("**@SNEHABHI_SERVER ✨ 𝐀𝐃𝐌𝐈𝐍𝐂𝐀𝐂𝐇𝐄 𝐔𝐏𝐃𝐀𝐓𝐄𝐃 ✨**")

