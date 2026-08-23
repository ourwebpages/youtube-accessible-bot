from telegram import Update
from telegram.ext import ContextTypes
from database.repository import VideoRepository

async def delete_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /delete <video_id>")
        return
    if VideoRepository().delete(update.effective_user.id, context.args[0]):
        await update.message.reply_text("Video deleted from your library.")
    else:
        await update.message.reply_text("That video is not in your library.")

async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    stats = VideoRepository().stats(update.effective_user.id)
    await update.message.reply_text(f"Library statistics\n\nVideos: {stats['videos']}\nFavorites: {stats['favorites']}\nChannels: {stats['channels']}")
