from telegram import Update
from telegram.ext import ContextTypes

HELP = """YouTube Accessible Bot

YouTube:
 /yt <url>       Analyze and save a video

Library:
 /search <text>  Search saved videos
 /playlist       List saved channels
 /playlist <channel>  List channel videos
 /recent         Recent videos
 /favorites      Favorite videos
 /favorite <id>  Toggle favorite
 /delete <id>    Delete a saved video
 /stats          Library statistics

Other:
 /help           Show this help
 /admin          Admin diagnostics
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("YouTube Accessible Bot is online.\n\nUse /help for commands.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP)
