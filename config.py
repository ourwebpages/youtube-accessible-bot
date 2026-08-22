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


def load_settings() -> Settings:
    token = os.getenv("TG_TOKEN", "").strip()
    if not token:
        raise RuntimeError("TG_TOKEN is required")
    return Settings(
        telegram_token=token,
        database_url=os.getenv("DATABASE_URL", "sqlite:///bot.db"),
        log_level=os.getenv("LOG_LEVEL", "INFO"),
    )
