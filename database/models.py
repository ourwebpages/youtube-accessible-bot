"""Lightweight database models represented as dataclasses."""
from dataclasses import dataclass

@dataclass(frozen=True)
class SavedVideo:
    user_id: int
    video_id: str
    title: str
    channel: str
    url: str
    duration: int = 0
    transcript: str | None = None
    favorite: bool = False
