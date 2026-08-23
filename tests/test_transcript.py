from services.transcript import fetch_transcript


def test_transcript_failure_is_safe(monkeypatch):
    class Broken:
        def fetch(self, *args, **kwargs): raise RuntimeError("no captions")
    import services.transcript as module
    monkeypatch.setattr(module, "YouTubeTranscriptApi", lambda: Broken())
    assert fetch_transcript("abc") is None
