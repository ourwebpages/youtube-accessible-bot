from telegram import Update
from telegram.ext import ContextTypes
from database.repository import VideoRepository

async def favorites_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    rows = VideoRepository().favorites(update.effective_user.id)
    if not rows:
        await update.message.reply_text("You have no favorites yet. Use /favorite <video_id> after saving a video.")
        return
    lines = ["Favorites", ""]
    for row in rows:
        lines += [row["title"], f"{row['channel']} · ID: {row['video_id']}", row["url"], ""]
    await update.message.reply_text("\n".join(lines))

async def favorite_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /favorite <video_id>")
        return
    state = VideoRepository().toggle_favorite(update.effective_user.id, context.args[0])
    if state is None:
        await update.message.reply_text("That video is not in your library.")
    else:
        await update.message.reply_text("Added to favorites." if state else "Removed from favorites.")
