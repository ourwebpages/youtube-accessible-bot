from services.youtube import VideoInfo
from database.repository import VideoRepository

def test_search_transcript(tmp_path):
    repo = VideoRepository(str(tmp_path / "db.sqlite"))
    repo.save(1, VideoInfo("abc","Hello","Channel","https://youtu.be/abc",10), "python automation")
    assert len(repo.search(1, "automation")) == 1
