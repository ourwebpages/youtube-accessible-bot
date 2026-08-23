import asyncio
from telegram import Update
from telegram.ext import ContextTypes
from services.youtube import YouTubeService
from services.transcript import TranscriptService
from services.summarizer import summarize
from database.repository import VideoRepository
from bot.keyboards.navigation import video_actions
from utils.formatting import chunks, duration
from utils.validation import extract_video_id

async def youtube_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /yt <YouTube URL>")
        return
    video_id = extract_video_id(context.args[0])
    if not video_id:
        await update.message.reply_text("Invalid YouTube URL. Use a youtube.com/watch, youtu.be, shorts, or live URL.")
        return
    try:
        info = await asyncio.to_thread(YouTubeService().get_video, video_id)
    except Exception:
        await update.message.reply_text("I could not read that video. Check that it is public and the URL is correct.")
        return
    transcript = await asyncio.to_thread(TranscriptService().get_text, video_id)
    repo = VideoRepository()
    repo.save(update.effective_user.id, info, transcript)
    summary = summarize(transcript) if transcript else "Transcript unavailable. The video was saved successfully."
    text = (f"Title: {info.title}\nChannel: {info.channel}\nDuration: {duration(info.duration)}\n"
            f"Video ID: {info.video_id}\nURL: {info.url}\n\nSummary:\n{summary}\n\nSaved to your library.")
    parts = chunks(text)
    for i, part in enumerate(parts):
        await update.message.reply_text(part, reply_markup=video_actions(info.video_id) if i == len(parts)-1 else None)
