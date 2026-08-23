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
CREATE INDEX IF NOT EXISTS idx_videos_user_created ON videos(user_id, created_at);
CREATE INDEX IF NOT EXISTS idx_videos_user_channel ON videos(user_id, channel);
CREATE INDEX IF NOT EXISTS idx_videos_user_favorite ON videos(user_id, favorite);
"""
