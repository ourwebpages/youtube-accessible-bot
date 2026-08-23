"""YouTube command handler."""
import asyncio
from telegram import Update
from telegram.ext import ContextTypes
from services.youtube import YouTubeService
from services.transcript import TranscriptService
from database.repository import VideoRepository
from utils.formatting import duration
from utils.validation import extract_video_id


async def youtube_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("Usage: /yt <YouTube URL>")
        return
    url = context.args[0]
    video_id = extract_video_id(url)
    if not video_id:
        await update.message.reply_text("That does not look like a supported YouTube URL.")
        return
    try:
        info = await asyncio.to_thread(YouTubeService().get_video, video_id)
    except Exception as exc:
        await update.message.reply_text(f"I couldn't read that video. Error: {type(exc).__name__}")
        return
    transcript = await asyncio.to_thread(TranscriptService().get_text, video_id)
    VideoRepository().save_video(info)
    summary = transcript[:1200] if transcript else "Transcript unavailable. The video was saved successfully."
    await update.message.reply_text(
        f"{info.title}\n\nChannel: {info.channel}\nDuration: {duration(info.duration)}\n\n"
        f"Transcript preview:\n{summary}\n\nSaved."
    )
