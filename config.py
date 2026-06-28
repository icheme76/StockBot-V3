from pathlib import Path
import os

from dotenv import load_dotenv

# ==========================
# DOSSIERS
# ==========================

BASE_DIR = Path(__file__).resolve().parent

# ==========================
# .env
# ==========================

load_dotenv(BASE_DIR / ".env")

# ==========================
# DISCORD
# ==========================

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

if not DISCORD_TOKEN:
    raise RuntimeError("Le token Discord est introuvable dans le fichier .env")

# ==========================
# GOOGLE
# ==========================

GOOGLE_CREDENTIALS = BASE_DIR / "credentials.json"

SPREADSHEET_NAME = os.getenv(
    "SPREADSHEET_NAME",
    "stockage wsl"
)

WORKSHEET_NAME = os.getenv(
    "WORKSHEET_NAME",
    "stockage wsl"
)