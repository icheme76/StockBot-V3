import gspread
from google.oauth2.service_account import Credentials

from config import (
    GOOGLE_CREDENTIALS,
    SPREADSHEET_NAME,
    WORKSHEET_NAME,
)

from core.items import ITEMS


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


class StockSheet:

    def __init__(self):

        creds = Credentials.from_service_account_file(
            GOOGLE_CREDENTIALS,
            scopes=SCOPES
        )

        self.gc = gspread.authorize(creds)

        self.sheet = (
            self.gc
            .open(SPREADSHEET_NAME)
            .worksheet(WORKSHEET_NAME)
        )

    def load_items(self):

        ITEMS.clear()

        values = self.sheet.col_values(3)   # Colonne C

        ignored = {
            "",
            "Plantation",
            "Drogue",
            "Produit",
            "Argent",
        }

        for row, value in enumerate(values, start=1):

            value = value.strip()

            if value in ignored:
                continue

            ITEMS.add(value, row)

        print(f"{len(ITEMS.data)} objets chargés.")