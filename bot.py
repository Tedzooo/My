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
BOT_TOKEN = '7161717671:AAEce94mPO28ecL8qKR8VvKVttMHz_HMrE4'
# Define a list of prank messages
prank_messages = [
    "Oops! You've been pranked! 😜",
    "Surprise! It's just a prank! 🎉",
    "Gotcha! Prank time! 🃏",
    "You're the lucky winner of a prank! 🥳",
    "This message will self-destruct in 3... 2... 1... BOOM! Just kidding 😄",
    "Congratulations! You've won a free imaginary vacation to Mars! 🚀",
    "Warning: This message contains extreme levels of prankiness! Proceed with caution. 😄",
    "You've unlocked the secret prank level! Prepare for the unexpected! 🎈",
    "You just missed the prank train! 🚂 Better luck next time! 😄",
    "Unexpected error: Prank.exe has stopped working. Just kidding! 😂",
    "Important announcement: You've been officially pranked! 📢",
    "Prank level: Expert! You're now a certified prankster! 🏆",
]
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
    
# Define a function to handle the /start command
@app.on_message(filters.command("start"))
async def start_command(client, message):
    # Send a welcome message to the user
    await message.reply_text("Welcome to the Prank Bot! Get ready to be pranked! 😄")

# Define a function to handle incoming messages
@app.on_message(filters.private)
async def handle_message(client, message):
    # Choose a random prank message
    prank_message = random.choice(prank_messages)
    
    # Send the prank message to the user
    if "BOOM" in prank_message:
        await message.reply_animation(animation="https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif")
    else:
        await message.reply_text(prank_message)




####################################################################################################


# Run the bot
app.run()
