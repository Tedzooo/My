# code from @fayasnoushad
from pyrogram import Client as Bot
from pyrogram import filters
from pyrogram.types import *


CALCULATE_TEXT = "Made by @tedzo01"

START_BUTTONS = InlineKeyboardMarkup(
    [[InlineKeyboardButton('⚙ Feedback ⚙', url='https://telegram.me/tedzo01')]]
)

CALCULATE_BUTTONS = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('(', callback_data='('),
        InlineKeyboardButton(')', callback_data=')'),
        InlineKeyboardButton('^', callback_data='^')
    ],
    [
        InlineKeyboardButton('%', callback_data='%'),
        InlineKeyboardButton('AC', callback_data='AC'),
        InlineKeyboardButton('DEL', callback_data='DEL'),
        InlineKeyboardButton('÷', callback_data='/')
    ],
    [
        InlineKeyboardButton('7', callback_data='7'),
        InlineKeyboardButton('8', callback_data='8'),
        InlineKeyboardButton('9', callback_data='9'),
        InlineKeyboardButton('×', callback_data='*')
    ],
    [
        InlineKeyboardButton('4', callback_data='4'),
        InlineKeyboardButton('5', callback_data='5'),
        InlineKeyboardButton('6', callback_data='6'),
        InlineKeyboardButton('-', callback_data='-')
    ],
    [
        InlineKeyboardButton('1', callback_data='1'),
        InlineKeyboardButton('2', callback_data='2'),
        InlineKeyboardButton('3', callback_data='3'),
        InlineKeyboardButton('+', callback_data='+')
    ],
    [
        InlineKeyboardButton('00', callback_data='00'),
        InlineKeyboardButton('0', callback_data='0'),
        InlineKeyboardButton('=', callback_data='='),
        InlineKeyboardButton('.', callback_data='.')
    ]
])




@Bot.on_message(filters.private & filters.command(["calc", "calculate", "calculator"]))
async def calculat(_, message):
    data = message.text.replace("×", "*").replace("÷", "/")
    try:
        result = str(eval(data))
    except (SyntaxError, ZeroDivisionError, NameError) as e:
        result = "Error"
        print(f"Evaluation error: {e}")
    await message.reply_text(
        text=result,
        reply_markup=CALCULATE_BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )

@Bot.on_callback_query()
async def cb_data(_, message):
    data = message.data
    try:
        message_text = message.message.text.split("\n")[0].strip().split("=")[0].strip()
        if data == "=":
            text = str(eval(message_text))
        elif data == "DEL":
            text = message_text[:-1]
        elif data == "AC":
            text = ""
        else:
            text = message_text + data
        await message.message.edit_text(
            text=f"{text}\n\n{CALCULATE_TEXT}",
            disable_web_page_preview=True,
            reply_markup=CALCULATE_BUTTONS
        )
    except (SyntaxError, ZeroDivisionError, NameError) as error:
        print(f"Callback query error: {error}")

@Bot.on_inline_query()
async def inline(bot, query):
    results = []
    try:
        if not query.query:
            results.append(
                InlineQueryResultArticle(
                    title="Calculator",
                    description="New calculator",
                    input_message_content=InputTextMessageContent(
                        text=CALCULATE_TEXT,
                        disable_web_page_preview=True
                    ),
                    reply_markup=CALCULATE_BUTTONS
                )
            )
        else:
            data = query.query.replace("×", "*").replace("÷", "/")
            try:
                result = str(eval(data))
                results.append(
                    InlineQueryResultArticle(
                        title="Answer",
                        description=f"Result: {result}",
                        input_message_content=InputTextMessageContent(
                            text=f"{data} = {result}",
                            disable_web_page_preview=True
                        )
                    )
                )
            except (SyntaxError, ZeroDivisionError, NameError):
                results.append(
                    InlineQueryResultArticle(
                        title="Error",
                        description="Invalid expression",
                        input_message_content=InputTextMessageContent(
                            text="Error",
                            disable_web_page_preview=True
                        )
                    )
                )
    except Exception as error:
        print(f"Inline query error: {error}")
    await query.answer(results)
p
