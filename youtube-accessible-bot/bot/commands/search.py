from telegram import Update
from telegram.ext import ContextTypes
from database.repository import VideoRepository
from utils.formatting import duration

async def search_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /search <query>")
        return
    rows = VideoRepository().search(update.effective_user.id, " ".join(context.args), 10)
    if not rows:
        await update.message.reply_text("No matching saved videos were found.")
        return
    lines = ["Search results", ""]
    for row in rows:
        lines += [f"{row['title']}", f"Channel: {row['channel']}", f"Duration: {duration(row['duration'])}", f"ID: {row['video_id']}", row['url'], ""]
    await update.message.reply_text("\n".join(lines))
