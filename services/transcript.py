"""Transcript retrieval service."""
from youtube_transcript_api import YouTubeTranscriptApi


class TranscriptService:
    def get_text(self, video_id: str, languages: list[str] | None = None) -> str | None:
        return fetch_transcript(video_id, languages)


def fetch_transcript(video_id: str, languages: list[str] | None = None) -> str | None:
    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id, languages=languages or ["en"])
        return " ".join(snippet.text for snippet in transcript)
    except Exception:
        return None
