from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def video_actions(video_id: str):
    return InlineKeyboardMarkup([[InlineKeyboardButton("Favorite / Unfavorite", callback_data=f"favorite:{video_id}")]])
