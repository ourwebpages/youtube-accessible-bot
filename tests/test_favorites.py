from database.repository import VideoRepository


def test_toggle_favorite(tmp_path):
    repo = VideoRepository(str(tmp_path / "bot.db"))
    repo.save(5, {"video_id": "abc", "title": "Video", "channel": "Channel", "url": "https://youtu.be/abc"})
    assert repo.toggle_favorite(5, "abc") is True
    assert repo.favorites(5)[0]["favorite"] == 1
    assert repo.toggle_favorite(5, "abc") is False
    assert repo.favorites(5) == []
