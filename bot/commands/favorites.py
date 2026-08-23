"""Favorites command."""
from telegram import Update
from telegram.ext import ContextTypes
from database.repository import VideoRepository


async def favorites_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    rows = VideoRepository().favorites(update.effective_user.id)
    if not rows:
        await update.message.reply_text("You have no favorites yet.")
        return
    await update.message.reply_text("\n\n".join(f"{r['title']}\n{r['url']}" for r in rows))
