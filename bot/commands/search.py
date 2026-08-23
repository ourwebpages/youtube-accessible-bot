"""Library search command."""
from telegram import Update
from telegram.ext import ContextTypes
from database.repository import VideoRepository


async def search_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("Usage: /search <query>")
        return
    rows = VideoRepository().search(update.effective_user.id, " ".join(context.args))
    if not rows:
        await update.message.reply_text("No saved videos matched your search.")
        return
    await update.message.reply_text("\n\n".join(f"{r['title']}\n{r['channel']}\n{r['url']}" for r in rows))
