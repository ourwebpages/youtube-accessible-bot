# YouTube Accessible Bot

A text-first, accessibility-focused Telegram bot for saving, searching, summarizing, and managing YouTube videos.

## Features

- `/yt <url>` — analyze and save a YouTube video
- `/search <query>` — search your saved library
- `/playlist` — list saved channels
- `/playlist <channel>` — list videos from a channel
- `/recent` — recent saved videos
- `/favorites` — favorite videos
- `/favorite <video_id>` — toggle a favorite
- `/delete <video_id>` — remove a saved video
- `/stats` — personal library statistics
- `/admin` — admin-only diagnostics
- Optional inline Favorite button
- Per-user SQLite library
- Transcript fallback when captions are unavailable
- Safe Telegram message splitting
- Rate limiting
- Docker support
- Automated tests

## Setup

```bash
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows:
# .venv\Scripts\activate

pip install -r requirements.txt
cp .env.example .env
```

Set `TG_TOKEN` in `.env`, then:

```bash
python app.py
```

## Optional AI summaries

The default summarizer is deterministic and requires no API key. Replace `services/summarizer.py` if you want to connect an LLM provider.

## Accessibility

Every core feature is available through commands and does not require inline keyboards. Buttons are convenience navigation only. Responses use simple headings, predictable labels, and short actionable errors.
