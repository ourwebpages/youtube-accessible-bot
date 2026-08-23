from services.youtube import VideoInfo
from database.repository import VideoRepository

def video():
    return VideoInfo("abc", "Title", "Channel", "https://youtu.be/abc", 65)

def test_user_isolation(tmp_path):
    repo = VideoRepository(str(tmp_path / "db.sqlite"))
    repo.save(1, video())
    assert len(repo.recent(1)) == 1
    assert len(repo.recent(2)) == 0

def test_favorite_and_delete(tmp_path):
    repo = VideoRepository(str(tmp_path / "db.sqlite"))
    repo.save(1, video())
    assert repo.toggle_favorite(1, "abc") is True
    assert repo.favorites(1)[0]["video_id"] == "abc"
    assert repo.delete(1, "abc")
    assert repo.favorites(1) == []
