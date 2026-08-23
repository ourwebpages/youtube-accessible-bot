"""Accessible callback actions placeholder for future inline navigation."""
from telegram import Update
from telegram.ext import ContextTypes


async def noop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.callback_query:
        await update.callback_query.answer()
