"""SQLite persistence primitives."""
import sqlite3
from services.youtube import VideoInfo

SCHEMA = """
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    video_id TEXT NOT NULL,
    title TEXT NOT NULL,
    channel TEXT NOT NULL,
    url TEXT NOT NULL,
    duration INTEGER NOT NULL DEFAULT 0,
    transcript TEXT,
    favorite INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, video_id)
);
"""

class VideoRepository:
    def __init__(self, path: str = "bot.db") -> None:
        self.path = path
        with self._connect() as conn:
            conn.executescript(SCHEMA)

    def _connect(self):
        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row
        return conn

    def save(self, user_id: int, video: dict | VideoInfo, transcript: str | None = None) -> None:
        if isinstance(video, VideoInfo):
            video = {"video_id": video.video_id, "title": video.title, "channel": video.channel,
                     "url": video.url, "duration": video.duration, "transcript": transcript}
        with self._connect() as conn:
            conn.execute("""INSERT INTO videos
                (user_id, video_id, title, channel, url, duration, transcript)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(user_id, video_id) DO UPDATE SET
                title=excluded.title, channel=excluded.channel, url=excluded.url,
                duration=excluded.duration, transcript=excluded.transcript""",
                (user_id, video["video_id"], video["title"], video["channel"], video["url"],
                 video.get("duration", 0), video.get("transcript")))

    def save_video(self, video: VideoInfo, user_id: int = 0, transcript: str | None = None) -> None:
        self.save(user_id, video, transcript)

    def search(self, user_id: int, query: str, limit: int = 10):
        with self._connect() as conn:
            return conn.execute("""SELECT * FROM videos WHERE user_id=? AND (title LIKE ? OR channel LIKE ?)
                ORDER BY created_at DESC LIMIT ?""", (user_id, f"%{query}%", f"%{query}%", limit)).fetchall()

    def favorites(self, user_id: int):
        with self._connect() as conn:
            return conn.execute("SELECT * FROM videos WHERE user_id=? AND favorite=1 ORDER BY created_at DESC", (user_id,)).fetchall()

    def set_favorite(self, user_id: int, video_id: str, value: bool = True) -> None:
        with self._connect() as conn:
            conn.execute("UPDATE videos SET favorite=? WHERE user_id=? AND video_id=?", (int(value), user_id, video_id))
