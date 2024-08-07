from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import MessageIdInvalid, ChatAdminRequired, EmoticonInvalid, ReactionInvalid 
import random 
import asyncio
from pyrogram.errors import FloodWait

EMOJIS = [
        "👍", "👎", "❤", "🔥", 
        "🥰", "👏", "😁", "🤔",
        "🤯", "😱", "🤬", "😢",
        "🎉", "🤩", "🤮", "💩",
        "🙏", "👌", "🕊", "🤡",
        "🥱", "🥴", "😍", "🐳",
        "❤‍🔥", "🌚", "🌭", "💯",
        "🤣", "⚡", "🍌", "🏆",
        "💔", "🤨", "😐", "🍓",
        "🍾", "💋", "🖕", "😈",
        "😴", "😭", "🤓", "👻",
        "👨‍💻", "👀", "🎃", "🙈",
        "😇", "😨", "🤝", "✍",
        "🤗", "🫡", "🎅", "🎄",
        "☃", "💅", "🤪", "🗿",
        "🆒", "💘", "🙉", "🦄",
        "😘", "💊", "🙊", "😎",
        "👾", "🤷‍♂", "🤷", "🤷‍♀",
        "😡"
]
STICKERS = ["CAACAgUAAxkBAAEGPnNgPcbx75_XWKMwgMtZIJlvpUa9gAACsQIAAkzoiVdQPozmP6_Gjx4E", "CAACAgUAAxkBAAEGPnVgPccf4H7Yj7GAoVY9NuoNH9CslAACEQIAApuT8FXBRjVF95zJJR4E"]
STICKER = random.choice(STICKERS)

# Help Message


@Client.on_message(filters.command(["help"]))
async def _help(_, msg):
    try:
        await msg.react(choice(EMOJIS))
    except (
        MessageIdInvalid,
        EmoticonInvalid,
        ChatAdminRequired,
        ReactionInvalid
    ):
    pass
	m= await msg.reply_sticker(STICKER)

    try:
        ...  # Your code
    except FloodWait as e:
        await asyncio.sleep(e.value)  # Wait "value" seconds before continuing
        await msg.delete
