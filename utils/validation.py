"""Input validation helpers."""
from urllib.parse import parse_qs, urlparse


def extract_video_id(url: str) -> str | None:
    parsed = urlparse(url.strip())
    host = parsed.netloc.lower().removeprefix("www.")
    if host == "youtu.be":
        value = parsed.path.strip("/").split("/")[0]
        return value or None
    if host in {"youtube.com", "m.youtube.com", "music.youtube.com"}:
        if parsed.path == "/watch":
            return parse_qs(parsed.query).get("v", [None])[0]
        for marker in ("/shorts/", "/live/"):
            if marker in parsed.path:
                return parsed.path.split(marker, 1)[1].split("/", 1)[0] or None
    return None
