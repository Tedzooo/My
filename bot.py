import os
import time
from pyrogram import Client, filters
import ffmpeg
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from tqdm import tqdm

# Define your API ID and API HASH from my.telegram.org
API_ID = '15453419'
API_HASH = '6c9c9e5a2e65daf192e7dd9dde026f45'
BOT_TOKEN = '7161717671:AAEdv03kNLb6QSn8NCFVTgxASO0qgjl4AFs'

# Initialize the Client
app = Client("video_sample_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


def generate_sample(input_file, output_file, duration=30):
    try:
        (
            ffmpeg
            .input(input_file, t=duration)
            .output(output_file)
            .run(overwrite_output=True)
        )
        return True
    except Exception as e:
        print(f"Error generating sample: {e}")
        return False

async def handle_video_message(client, message):
    # Inform the user that the download has started
    reply_message = await message.reply_text("Downloading file...")
    input_file = await message.download()
    for i in range(10):
        await reply_message.edit_text(f"Downloading file... ({(i + 1) * 10}%)")
        time.sleep(0.5)
    await reply_message.edit_text("Generating sample video...")
    output_file = "sample_" + os.path.basename(input_file)
    if generate_sample(input_file, output_file):
        for i in range(10):
            await reply_message.edit_text(f"Generating sample video... ({(i + 1) * 10}%)")
            time.sleep(0.5)
        await reply_message.edit_text("Uploading sample video...")
        await message.reply_video(video=output_file, caption="Here's your 30-second sample video!")
        os.remove(input_file)
        os.remove(output_file)
        await reply_message.edit_text("Sample video generated and uploaded successfully!")
    else:
        await reply_message.edit_text("Failed to generate sample video.")

@app.on_message(filters.document | filters.video)
async def media_handler(client, message):
    if message.video or (message.document and message.document.mime_type in ["video/x-matroska", "video/mp4"]):
        await handle_video_message(client, message)
    else:
        await message.reply_text("Please send a valid video file (MKV or MP4).")


####################################################################################################


@app.on_message(filters.command("start"))
async def start(client, message):
    start_message = (
        "👋 Hello welcome to the Video Sample Bot!\n\n"
        "Send me a video file (MKV or MP4), and I'll generate a 30-second sample video for you."
    )
    
    # Define inline keyboard with buttons
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📣 Join my channel 📣", url="https://t.me/PBX1_BOTS"),
                InlineKeyboardButton("👥 Support group 👥", url="https://t.me/PBX1_SUPPORT_CHAT"),
            ],
            [
                InlineKeyboardButton("👩‍💻 Developer 👩‍💻", url="https://t.me/PBX1_OP"),
                InlineKeyboardButton("⛔️ Cancel ⛔️", callback_data="cancel"),
            ]
        ]
    )

    await message.reply_text(start_message, reply_markup=keyboard)


@app.on_callback_query(filters.regex("cancel"))
async def cancel(client, callback_query):
    await callback_query.message.delete()


@app.on_message(filters.command("help"))
async def help_command(client, message):
    help_text = (
        "Welcome to the Video Sample Bot Help!\n\n"
        "Commands:\n"
        "/start - Start the bot and get instructions.\n"
        "/help - Get this help message.\n\n"
        "Usage:\n"
        "Send me a video file (MKV or MP4), and I'll generate a 30-second sample video for you.\n\n"
        "Note:\n"
        "This bot currently supports MKV and MP4 video formats for generating samples."
    )
    await message.reply_text(help_text)




####################################################################################################


# Run the bot
app.run()
