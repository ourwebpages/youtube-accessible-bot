from utils.formatting import duration, chunks

def test_duration():
    assert duration(65) == "1:05"
    assert duration(3661) == "1:01:01"

def test_chunks():
    assert all(len(x) <= 4000 for x in chunks("x" * 9000))
