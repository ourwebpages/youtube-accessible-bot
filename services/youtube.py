"""YouTube metadata service."""
from dataclasses import dataclass
import yt_dlp


@dataclass(frozen=True)
class VideoInfo:
    video_id: str
    title: str
    channel: str
    url: str
    duration: int


def extract_video(url: str) -> VideoInfo:
    options = {"quiet": True, "no_warnings": True, "skip_download": True}
    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=False)
    video_id = info.get("id")
    return VideoInfo(
        video_id=video_id,
        title=info.get("title") or "Unknown title",
        channel=info.get("channel") or info.get("uploader") or "Unknown channel",
        url=f"https://www.youtube.com/watch?v={video_id}",
        duration=int(info.get("duration") or 0),
    )
