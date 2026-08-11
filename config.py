import os
import logging
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file (if present)
load_dotenv()

# BOT token (required)
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN or BOT_TOKEN.strip() == "" or BOT_TOKEN == "ISI_TOKEN_BOT_DI_SINI":
    raise RuntimeError(
        "BOT_TOKEN is not set. Please create a .env file or set the BOT_TOKEN environment variable.\n"
        "See .env.example for format."
    )

# Path to SQLite database file (default)
DB_PATH = os.getenv("DB_PATH", "data/anomess.db")
DB_PATH = str(Path(DB_PATH))

# Logging level
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

# Admin IDs (optional, comma separated list)
_ADMIN_IDS = os.getenv("ADMIN_IDS", "").strip()
if _ADMIN_IDS:
    try:
        ADMIN_IDS = [int(x.strip()) for x in _ADMIN_IDS.split(",") if x.strip()]
    except ValueError:
        ADMIN_IDS = []
        logging.warning("Invalid ADMIN_IDS in environment - must be comma separated integers")
else:
    ADMIN_IDS = []


def init_logging():
    """Initialize root logging according to LOG_LEVEL."""
    numeric_level = getattr(logging, LOG_LEVEL, logging.INFO)
    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )


# Exported names
__all__ = [
    "BOT_TOKEN",
    "DB_PATH",
    "LOG_LEVEL",
    "ADMIN_IDS",
    "init_logging",
]
