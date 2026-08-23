"""Deterministic summarizer fallback; provider integration can be added later."""


def summarize(text: str, sentences: int = 4) -> str:
    if not text:
        return "No transcript available."
    parts = [p.strip() for p in text.replace("!", ".").replace("?", ".").split(".") if p.strip()]
    result = ". ".join(parts[:sentences])
    return result + ("." if result and not result.endswith(".") else "")
