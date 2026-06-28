from pathlib import Path
import os

from dotenv import load_dotenv

# ==========================================================
# DOSSIERS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

# ==========================================================
# CHARGEMENT DU .ENV
# ==========================================================

load_dotenv(BASE_DIR / ".env")

# ==========================================================
# DISCORD
# ==========================================================

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

if not DISCORD_TOKEN:
    raise RuntimeError("Le token Discord est introuvable dans le fichier .env")

# ==========================================================
# GOOGLE SHEETS
# ==========================================================

GOOGLE_CREDENTIALS = BASE_DIR / "credentials.json"

SPREADSHEET_NAME = os.getenv("SPREADSHEET_NAME")

if not SPREADSHEET_NAME:
    raise RuntimeError("SPREADSHEET_NAME est introuvable dans le fichier .env")

WORKSHEET_NAME = os.getenv("WORKSHEET_NAME")

if not WORKSHEET_NAME:
    raise RuntimeError("WORKSHEET_NAME est introuvable dans le fichier .env")

# ==========================================================
# LOGS
# ==========================================================

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")