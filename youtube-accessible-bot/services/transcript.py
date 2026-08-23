import logging
from youtube_transcript_api import YouTubeTranscriptApi

log = logging.getLogger(__name__)

class TranscriptService:
    def get_text(self, video_id: str) -> str | None:
        try:
            transcript = YouTubeTranscriptApi().fetch(video_id, languages=["en"])
            return " ".join(item.text for item in transcript)
        except Exception as exc:
            log.info("Transcript unavailable for %s: %s", video_id, type(exc).__name__)
            return None
