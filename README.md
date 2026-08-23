# YouTube Accessible Bot

A modular, accessibility-first Telegram assistant for saving, searching, and understanding YouTube videos.

## Planned features

- YouTube metadata extraction with `yt-dlp`
- Transcript retrieval when available
- Optional summaries and key points
- Persistent SQLite storage
- Per-user libraries, favorites, and search
- Accessible text-first commands with optional inline navigation
- Admin controls, logging, validation, and rate limiting
- Automated tests and GitHub Actions CI
- Docker-ready deployment

## Status

Initial architecture scaffold. Configuration and services are being implemented incrementally with tests.

## Quick start

1. Copy `.env.example` to `.env`.
2. Set `TG_TOKEN`.
3. Install dependencies with `pip install -r requirements.txt`.
4. Run `python app.py`.
