"""Accessible, predictable Telegram formatting helpers."""


def duration(seconds: int) -> str:
    seconds = max(0, int(seconds))
    hours, rem = divmod(seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    return f"{hours}:{minutes:02d}:{seconds:02d}" if hours else f"{minutes}:{seconds:02d}"


def chunks(text: str, limit: int = 4000) -> list[str]:
    result = []
    while len(text) > limit:
        cut = text.rfind("\n", 0, limit)
        if cut <= 0:
            cut = limit
        result.append(text[:cut])
        text = text[cut:].lstrip()
    if text:
        result.append(text)
    return result
