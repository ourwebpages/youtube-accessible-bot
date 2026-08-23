def duration(seconds: int) -> str:
    seconds = max(0, int(seconds or 0))
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"

def chunks(text: str, max_length: int = 4000):
    out = []
    while len(text) > max_length:
        cut = text.rfind("\n", 0, max_length)
        if cut < 1:
            cut = max_length
        out.append(text[:cut])
        text = text[cut:].lstrip()
    if text:
        out.append(text)
    return out
