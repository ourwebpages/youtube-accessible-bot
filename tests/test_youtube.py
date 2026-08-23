from services.youtube import extract_video


def test_extract_video_smoke(monkeypatch):
    class FakeDL:
        def __enter__(self): return self
        def __exit__(self, *args): return False
        def extract_info(self, url, download=False):
            return {"id": "abc", "title": "Test", "channel": "Channel", "duration": 65}
    import services.youtube as module
    monkeypatch.setattr(module.yt_dlp, "YoutubeDL", lambda options: FakeDL())
    result = extract_video("https://youtube.com/watch?v=abc")
    assert result.video_id == "abc"
    assert result.title == "Test"
