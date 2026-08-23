from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class StoredVideo:
    user_id: int
    video_id: str
    title: str
    channel: str
    url: str
    duration: int
    transcript: str | None
    favorite: bool
    created_at: datetime | None = None
