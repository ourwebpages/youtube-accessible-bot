"""Telegram application factory."""
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from config import load_settings


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "YouTube Accessible Bot is online.\n\n"
        "Commands:\n"
        "/yt <url> - analyze a YouTube video\n"
        "/search <query> - search your library\n"
        "/playlist - browse saved channels\n"
        "/help - show help"
    )


def build_application() -> Application:
    settings = load_settings()
    application = Application.builder().token(settings.telegram_token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", start))
    return application
