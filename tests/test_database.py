from database.repository import VideoRepository


def test_favorite(tmp_path):
    repo = VideoRepository(str(tmp_path / "bot.db"))
    repo.save(7, {"video_id":"x", "title":"X", "channel":"C", "url":"https://youtu.be/x"})
    repo.set_favorite(7, "x", True)
    assert len(repo.favorites(7)) == 1
