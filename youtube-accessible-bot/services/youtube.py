from dataclasses import dataclass
import yt_dlp

@dataclass(frozen=True)
class VideoInfo:
    video_id: str
    title: str
    channel: str
    url: str
    duration: int

class YouTubeService:
    def get_video(self, video_id: str) -> VideoInfo:
        url = f"https://www.youtube.com/watch?v={video_id}"
        opts = {"quiet": True, "no_warnings": True, "skip_download": True, "noplaylist": True}
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(url, download=False)
        return VideoInfo(
            video_id=info.get("id") or video_id,
            title=info.get("title") or "Untitled",
            channel=info.get("channel") or info.get("uploader") or "Unknown channel",
            url=f"https://www.youtube.com/watch?v={info.get('id') or video_id}",
            duration=int(info.get("duration") or 0),
        )
