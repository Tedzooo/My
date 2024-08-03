import random
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


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
 

@Client.on_message(filters.command("start") & filters.incoming)
async def start(client: Client, message: Message):
    await message.reply_text(
        f"""<b>assalamualaikum {message.from_user.first_name}! hy i am verthe oru bot
 </b>""",
            reply_markup=InlineKeyboardMarkup(
               [
                [
                    InlineKeyboardButton(
                        "Support Group  ", url="https://t.me/tedzo01"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )

@Client.on_message(filters.command("help") & filters.incoming)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\n/start <song name> - play song you requested
/id <song name> - play song you requested via deezer
/calculator <song name> - play song you requested via jio saavn
/webs - Show now playing list
/wallpaper- Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly
\n*Admins only*
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Need Help❓", url="https://t.me/telegram"
                    )
                ]
            ]
        )
    )    

@Client.on_callback_query()
async def callback(bot, msg: CallbackQuery):
    if msg.data == "close1":
        await msg.answer("Closed")
        await msg.message.delete()
    
    elif msg.data == "close":
        await msg.answer("Closed")
        await msg.message.delete()
