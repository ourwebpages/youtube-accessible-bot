"""Search service."""
from database.repository import VideoRepository


def search_library(user_id: int, query: str, limit: int = 10):
    return VideoRepository().search(user_id, query, limit)
