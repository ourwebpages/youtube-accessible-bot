"""Admin command hooks."""
from telegram import Update
from telegram.ext import ContextTypes
from config import load_settings


async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    settings = load_settings()
    admins = settings.admin_ids
    if update.effective_user.id not in admins:
        await update.message.reply_text("You are not authorized to use this command.")
        return
    await update.message.reply_text("Admin access confirmed.")
