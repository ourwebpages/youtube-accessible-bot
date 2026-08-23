"""Optional, compact inline navigation keyboards."""
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def video_actions(video_id: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[InlineKeyboardButton("Favorite", callback_data=f"favorite:{video_id}")]])
