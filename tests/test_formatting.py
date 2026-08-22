from utils.formatting import chunks, duration


def test_duration():
    assert duration(65) == "1:05"
    assert duration(3661) == "1:01:01"


def test_chunks():
    parts = chunks("a\n" * 3000, 100)
    assert all(len(part) <= 100 for part in parts)
