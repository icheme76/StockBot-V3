from loguru import logger
import sys
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level: <8}</level> | "
           "{message}"
)

logger.add(
    LOG_DIR / "stockbot.log",
    rotation="5 MB",
    retention="30 days",
    level="DEBUG",
    encoding="utf-8"
)