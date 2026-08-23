from utils.validation import extract_video_id


def test_supported_youtube_urls():
    assert extract_video_id("https://www.youtube.com/watch?v=abc") == "abc"
    assert extract_video_id("https://youtu.be/abc") == "abc"
    assert extract_video_id("https://youtube.com/shorts/abc") == "abc"
    assert extract_video_id("https://example.com/video/abc") is None
