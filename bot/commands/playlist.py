"""Playlist browsing command."""
from telegram import Update
from telegram.ext import ContextTypes
from database.repository import VideoRepository


async def playlist_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = " ".join(context.args).strip() if context.args else ""
    if query:
        rows = VideoRepository().search(update.effective_user.id, query, 20)
    else:
        rows = VideoRepository().search(update.effective_user.id, "", 20)
    if not rows:
        await update.message.reply_text("Your library is empty.")
        return
    await update.message.reply_text("\n\n".join(f"{r['channel']} — {r['title']}\n{r['url']}" for r in rows))
