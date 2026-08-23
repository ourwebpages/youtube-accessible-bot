"""Environment-backed configuration."""
from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    telegram_token: str
    database_url: str = "sqlite:///bot.db"
    log_level: str = "INFO"
    admin_ids: frozenset[int] = frozenset()


def load_settings() -> Settings:
    token = os.getenv("TG_TOKEN", "").strip()
    if not token:
        raise RuntimeError("TG_TOKEN is required")
    raw = os.getenv("ADMIN_IDS", "")
    admin_ids = frozenset(int(x.strip()) for x in raw.split(",") if x.strip().isdigit())
    return Settings(token, os.getenv("DATABASE_URL", "sqlite:///bot.db"), os.getenv("LOG_LEVEL", "INFO"), admin_ids)
