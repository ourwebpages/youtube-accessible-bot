import sqlite3
from services.youtube import VideoInfo
from database.migrations import SCHEMA

class VideoRepository:
    def __init__(self, path: str = "bot.db"):
        self.path = path.replace("sqlite:///", "")
        with self._connect() as conn:
            conn.executescript(SCHEMA)

    def _connect(self):
        conn = sqlite3.connect(self.path, timeout=30)
        conn.row_factory = sqlite3.Row
        return conn

    def save(self, user_id: int, video: VideoInfo, transcript: str | None = None):
        with self._connect() as conn:
            conn.execute("""INSERT INTO videos(user_id,video_id,title,channel,url,duration,transcript)
            VALUES(?,?,?,?,?,?,?)
            ON CONFLICT(user_id,video_id) DO UPDATE SET title=excluded.title,channel=excluded.channel,
            url=excluded.url,duration=excluded.duration,transcript=COALESCE(excluded.transcript,videos.transcript)""",
            (user_id, video.video_id, video.title, video.channel, video.url, video.duration, transcript))

    def search(self, user_id, query, limit=10):
        like = f"%{query}%"
        with self._connect() as c:
            return c.execute("SELECT * FROM videos WHERE user_id=? AND (title LIKE ? OR channel LIKE ? OR transcript LIKE ?) ORDER BY created_at DESC LIMIT ?", (user_id,like,like,like,limit)).fetchall()

    def recent(self, user_id, limit=10):
        with self._connect() as c:
            return c.execute("SELECT * FROM videos WHERE user_id=? ORDER BY created_at DESC LIMIT ?", (user_id,limit)).fetchall()

    def channels(self, user_id):
        with self._connect() as c:
            return c.execute("SELECT channel,COUNT(*) count FROM videos WHERE user_id=? GROUP BY channel ORDER BY channel COLLATE NOCASE", (user_id,)).fetchall()

    def by_channel(self, user_id, channel, limit=20):
        with self._connect() as c:
            return c.execute("SELECT * FROM videos WHERE user_id=? AND channel=? ORDER BY created_at DESC LIMIT ?", (user_id,channel,limit)).fetchall()

    def favorites(self, user_id):
        with self._connect() as c:
            return c.execute("SELECT * FROM videos WHERE user_id=? AND favorite=1 ORDER BY created_at DESC", (user_id,)).fetchall()

    def toggle_favorite(self, user_id, video_id):
        with self._connect() as c:
            row = c.execute("SELECT favorite FROM videos WHERE user_id=? AND video_id=?", (user_id,video_id)).fetchone()
            if row is None:
                return None
            value = not bool(row["favorite"])
            c.execute("UPDATE videos SET favorite=? WHERE user_id=? AND video_id=?", (int(value),user_id,video_id))
            return value

    def delete(self, user_id, video_id):
        with self._connect() as c:
            cur = c.execute("DELETE FROM videos WHERE user_id=? AND video_id=?", (user_id,video_id))
            return cur.rowcount > 0

    def stats(self, user_id):
        with self._connect() as c:
            row = c.execute("SELECT COUNT(*) videos, COUNT(DISTINCT channel) channels, COALESCE(SUM(favorite),0) favorites FROM videos WHERE user_id=?", (user_id,)).fetchone()
            return dict(row)

    def global_stats(self):
        with self._connect() as c:
            row = c.execute("SELECT COUNT(DISTINCT user_id) users, COUNT(*) videos, COALESCE(SUM(favorite),0) favorites FROM videos").fetchone()
            return dict(row)
