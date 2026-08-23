import re

def summarize(text: str, sentences: int = 5) -> str:
    if not text:
        return "No transcript available."
    cleaned = " ".join(text.split())
    pieces = [p.strip() for p in re.split(r"(?<=[.!?])\s+", cleaned) if p.strip()]
    result = " ".join(pieces[:sentences])
    return result if result.endswith((".", "!", "?")) else result + "."
