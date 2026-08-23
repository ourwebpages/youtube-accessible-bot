from database.repository import VideoRepository


def test_search(tmp_path):
    repo = VideoRepository(str(tmp_path / "bot.db"))
    repo.save(1, {"video_id":"a", "title":"Python Tutorial", "channel":"Dev", "url":"https://youtu.be/a", "duration":10})
    rows = repo.search(1, "python")
    assert len(rows) == 1
    assert rows[0]["video_id"] == "a"
