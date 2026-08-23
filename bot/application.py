"""Telegram application factory."""
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from config import load_settings
from bot.commands.start import start, help_command
from bot.commands.youtube import youtube_command
from bot.commands.search import search_command
from bot.commands.playlist import playlist_command
from bot.commands.favorites import favorites_command
from bot.commands.admin import admin_command
from bot.callbacks.actions import favorite_callback


def build_application() -> Application:
    settings = load_settings()
    application = Application.builder().token(settings.telegram_token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("yt", youtube_command))
    application.add_handler(CommandHandler("search", search_command))
    application.add_handler(CommandHandler("playlist", playlist_command))
    application.add_handler(CommandHandler("favorites", favorites_command))
    application.add_handler(CommandHandler("admin", admin_command))
    application.add_handler(CallbackQueryHandler(favorite_callback, pattern=r"^favorite:"))
    return application
