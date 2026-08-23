from telegram import Update
from telegram.ext import ContextTypes
from database.repository import VideoRepository
from utils.formatting import duration

async def playlist_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    repo = VideoRepository()
    if not context.args:
        channels = repo.channels(update.effective_user.id)
        if not channels:
            await update.message.reply_text("Your library is empty.")
            return
        await update.message.reply_text("Saved channels\n\n" + "\n".join(f"{r['channel']} ({r['count']})" for r in channels))
        return
    channel = " ".join(context.args)
    rows = repo.by_channel(update.effective_user.id, channel)
    if not rows:
        await update.message.reply_text("No saved videos found for that channel.")
        return
    lines = [f"Channel: {channel}", ""]
    for row in rows:
        lines += [row["title"], f"Duration: {duration(row['duration'])}", f"ID: {row['video_id']}", row["url"], ""]
    await update.message.reply_text("\n".join(lines))

async def recent_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    rows = VideoRepository().recent(update.effective_user.id, 10)
    if not rows:
        await update.message.reply_text("Your library is empty.")
        return
    lines = ["Recent videos", ""]
    for row in rows:
        lines += [row["title"], f"{row['channel']} · ID: {row['video_id']}", row["url"], ""]
    await update.message.reply_text("\n".join(lines))
