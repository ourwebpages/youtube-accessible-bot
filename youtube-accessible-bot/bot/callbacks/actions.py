from telegram import Update
from telegram.ext import ContextTypes
from database.repository import VideoRepository

async def favorite_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    _, video_id = (query.data or "").split(":", 1)
    state = VideoRepository().toggle_favorite(update.effective_user.id, video_id)
    if state is None:
        await query.answer("Video is no longer in your library.", show_alert=True)
    else:
        await query.answer("Added to favorites." if state else "Removed from favorites.")
