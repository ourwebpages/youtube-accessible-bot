"""Database schema initialization."""
from .repository import VideoRepository


def migrate(path: str = "bot.db") -> None:
    VideoRepository(path)
