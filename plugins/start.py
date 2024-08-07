#hyyy
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import *
from random import choice



START_TEXT = """Hello {},
I am an under 5MB media or file to telegra.ph link uploader bot.

Made by @tedzo01"""

HELP_TEXT = """--**Help**--
----------------------______---------------
"""
 
DOWNLOAD_LOCATION = ("DOWNLOAD_LOCATION", "./DOWNLOADS/")
ABOUT_TEXT = """--**About Me**--

- **Bot :** `Telegraph Uploader`
- **Developer :**
  • [GitHub](https://github.com/FayasNoushad)
  • [Telegram](https://telegram.me/FayasNoushad)
- **Source :** [Click here](https://github.com/FayasNoushad/Telegraph-Uploader-Bot)
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram](https://pyrogram.org)"""

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Feedback', url='https://telegram.me/tedzo01')
        ],
        [
            InlineKeyboardButton('Help', callback_data='help'),
            InlineKeyboardButton('About', callback_data='about'),
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

HELP_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Home', callback_data='home'),
            InlineKeyboardButton('About', callback_data='about'),
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

ABOUT_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Home', callback_data='home'),
            InlineKeyboardButton('Help', callback_data='help'),
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)


@Client.on_message(filters.new_chat_members)
async def start_(client: Client, message: Message):
       await message.reply_text(
        f"""<b>Hi {message.from_user.first_namel}!
\nWelcome To {message.chat.title}
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                      "✨CamilaAssistant", url="https://t.me/camilaowner",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Help Group", url="https://t.me/warbotzsupport"
                    ),
                    InlineKeyboardButton(
                        "stickers💖", url="https://t.me/stickersbag"
                    ),
                    InlineKeyboardButton(
                        "✨GitHub✨", url="http://www.github.com/xabhishek/camilavcbot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/camillaMusicbot?startgroup=true"
                    ) 
                ]
            ]
        )
    )


@Client.on_callback_query()
async def cb_data(bot, update):
    
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "close":
        await update.answer("Closed")
        await update.message.delete()

    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    
    else:
        await update.message.delete()
    

@Client.on_message(filters.private & filters.command(["start"]))
async def stat(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        quote=True,
        reply_markup=START_BUTTONS
    )


