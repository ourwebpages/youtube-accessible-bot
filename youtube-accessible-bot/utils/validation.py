from urllib.parse import urlparse, parse_qs

def extract_video_id(url: str) -> str | None:
    try:
        p = urlparse(url.strip())
        host = p.netloc.lower().split(":")[0]
        if host in {"youtube.com", "www.youtube.com", "m.youtube.com"}:
            if p.path == "/watch":
                value = parse_qs(p.query).get("v", [None])[0]
                return value or None
            for prefix in ("/shorts/", "/live/"):
                if p.path.startswith(prefix):
                    return p.path[len(prefix):].split("/")[0] or None
        if host in {"youtu.be", "www.youtu.be"}:
            return p.path.strip("/").split("/")[0] or None
    except Exception:
        return None
    return None
