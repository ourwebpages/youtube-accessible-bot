"""YouTube command handler."""
import asyncio
from telegram import Update
from telegram.ext import ContextTypes
from services.youtube import YouTubeService
from services.transcript import TranscriptService
from services.summarizer import summarize
from database.repository import VideoRepository
from utils.formatting import chunks, duration
from utils.validation import extract_video_id


async def youtube_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("Usage: /yt <YouTube URL>")
        return
    video_id = extract_video_id(context.args[0])
    if not video_id:
        await update.message.reply_text("That does not look like a supported YouTube URL.")
        return
    try:
        info = await asyncio.to_thread(YouTubeService().get_video, video_id)
    except Exception as exc:
        await update.message.reply_text(
            f"I couldn't read that video. Please check the URL and try again. ({type(exc).__name__})"
        )
        return

    transcript = await asyncio.to_thread(TranscriptService().get_text, video_id)
    user_id = update.effective_user.id
    VideoRepository().save(user_id, info, transcript)
    summary = summarize(transcript) if transcript else "Transcript unavailable. The video was saved successfully."
    text = (
        f"{info.title}\n\nChannel: {info.channel}\nDuration: {duration(info.duration)}\n"
        f"URL: {info.url}\n\nSummary:\n{summary}\n\nSaved to your library."
    )
    for part in chunks(text):
        await update.message.reply_text(part)
