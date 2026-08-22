"""Transcript retrieval service."""
from youtube_transcript_api import YouTubeTranscriptApi


def fetch_transcript(video_id: str, languages: list[str] | None = None) -> str | None:
    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id, languages=languages or ["en"])
        return " ".join(snippet.text for snippet in transcript)
    except Exception:
        return None
