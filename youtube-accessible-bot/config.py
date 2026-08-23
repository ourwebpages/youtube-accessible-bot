import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    telegram_token: str
    database_path: str
    admin_ids: frozenset[int]
    rate_limit_per_minute: int

def load_settings() -> Settings:
    token = os.getenv("TG_TOKEN", "").strip()
    if not token:
        raise RuntimeError("TG_TOKEN is missing. Copy .env.example to .env and set TG_TOKEN.")
    raw_admins = os.getenv("ADMIN_IDS", "")
    admins = frozenset(int(x.strip()) for x in raw_admins.split(",") if x.strip())
    return Settings(
        telegram_token=token,
        database_path=os.getenv("DB_PATH", "bot.db"),
        admin_ids=admins,
        rate_limit_per_minute=max(1, int(os.getenv("RATE_LIMIT_PER_MINUTE", "10"))),
    )
