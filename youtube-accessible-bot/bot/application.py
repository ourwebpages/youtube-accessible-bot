from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from config import load_settings
from bot.commands.start import start, help_command
from bot.commands.youtube import youtube_command
from bot.commands.search import search_command
from bot.commands.playlist import playlist_command, recent_command
from bot.commands.favorites import favorites_command, favorite_command
from bot.commands.admin import admin_command
from bot.commands.library import delete_command, stats_command
from bot.callbacks.actions import favorite_callback
from bot.middleware.rate_limit import RateLimiter

def build_application() -> Application:
    settings = load_settings()
    app = Application.builder().token(settings.telegram_token).build()
    limiter = RateLimiter(settings.rate_limit_per_minute)
    for handler in [
        CommandHandler("start", start),
        CommandHandler("help", help_command),
        CommandHandler("yt", youtube_command),
        CommandHandler("search", search_command),
        CommandHandler("playlist", playlist_command),
        CommandHandler("recent", recent_command),
        CommandHandler("favorites", favorites_command),
        CommandHandler("favorite", favorite_command),
        CommandHandler("delete", delete_command),
        CommandHandler("stats", stats_command),
        CommandHandler("admin", admin_command),
    ]:
        app.add_handler(handler)
    app.add_handler(CallbackQueryHandler(favorite_callback, pattern=r"^favorite:"))
    app.bot_data["rate_limiter"] = limiter
    return app
