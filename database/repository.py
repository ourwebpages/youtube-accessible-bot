"""SQLite persistence primitives."""
import sqlite3


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

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row
        return conn

    def save(self, user_id: int, video: dict) -> None:
        with self._connect() as conn:
            conn.execute(
                """INSERT INTO videos
                (user_id, video_id, title, channel, url, duration, transcript)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(user_id, video_id) DO UPDATE SET
                title=excluded.title, channel=excluded.channel,
                url=excluded.url, duration=excluded.duration,
                transcript=excluded.transcript""",
                (user_id, video["video_id"], video["title"], video["channel"],
                 video["url"], video.get("duration", 0), video.get("transcript")),
            )
