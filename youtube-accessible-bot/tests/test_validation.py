from utils.validation import extract_video_id

def test_watch_url():
    assert extract_video_id("https://www.youtube.com/watch?v=abc123") == "abc123"

def test_short_url():
    assert extract_video_id("https://youtu.be/abc123?t=4") == "abc123"

def test_short_video():
    assert extract_video_id("https://youtube.com/shorts/abc123") == "abc123"

def test_invalid():
    assert extract_video_id("https://example.com/video/abc") is None
