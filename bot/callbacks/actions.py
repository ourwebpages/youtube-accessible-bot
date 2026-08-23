"""Inline callback actions for optional keyboard navigation."""
from telegram import Update
from telegram.ext import ContextTypes
from database.repository import VideoRepository


async def favorite_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    parts = (query.data or "").split(":", 1)
    if len(parts) != 2 or not parts[1]:
        return
    state = VideoRepository().toggle_favorite(update.effective_user.id, parts[1])
    await query.answer("Added to favorites." if state else "Removed from favorites.", show_alert=False)


async def noop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.callback_query:
        await update.callback_query.answer()
