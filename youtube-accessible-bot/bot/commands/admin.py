from telegram import Update
from telegram.ext import ContextTypes
from config import load_settings
from database.repository import VideoRepository

async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    settings = load_settings()
    if update.effective_user.id not in settings.admin_ids:
        await update.message.reply_text("You are not authorized to use this command.")
        return
    stats = VideoRepository().global_stats()
    await update.message.reply_text(
        f"Admin diagnostics\n\nUsers: {stats['users']}\nVideos: {stats['videos']}\nFavorites: {stats['favorites']}"
    )
