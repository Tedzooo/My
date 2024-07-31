import os
import time
from pyrogram import Client, filters
import random
import asyncio
import ffmpeg
from dotenv import load_dotenv
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from tqdm import tqdm

# Define your API ID and API HASH from my.telegram.org
API_ID = '15453419'
API_HASH = '6c9c9e5a2e65daf192e7dd9dde026f45'
BOT_TOKEN = '7161717671:AAF4VBmLu3JGECaPXMdVPxrawt3SrE0LbcQ'
# Define a list of prank messages

# Initialize the Clien

load_dotenv()

app = Client(
    "mybottttt",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    workers=100,
    plugins=dict(root="plugins")
)
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
  
####################################################################################################


# Run the bot
app.run()
