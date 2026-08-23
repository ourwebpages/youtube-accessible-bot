"""Start/help commands."""
from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "YouTube Accessible Bot\n\n"
        "/yt <URL> — analyze and save a video\n"
        "/search <query> — search your library\n"
        "/playlist — list saved channels\n"
        "/favorites — list favorites\n"
        "/help — show commands"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await start(update, context)
