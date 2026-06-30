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
        self.gc = None
        self.sheet = None

        self.connect()

    def add_quantity(self, row: int, amount: int, column: int):

        cell = self.sheet.cell(row, column)

        try:
            current = int(cell.value)
        except (TypeError, ValueError):
            current = 0

        new_value = current + amount

        self.sheet.update_cell(row, column, new_value)

        return new_value
   
    def remove_quantity(self, row: int, amount: int, column: int):

        cell = self.sheet.cell(row, column)

        try:
            current = int(cell.value)
        except (TypeError, ValueError):
            current = 0

        new_value = current + amount

        self.sheet.update_cell(row, column, new_value)

        return new_value

    def connect(self):
        """Connexion à Google Sheets."""

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

    def get_item_info(self, row: int):

        values = self.sheet.row_values(row)

        return {
            "base_sud": values[5],
            "add_sud": values[6],
            "remove_sud": values[7],
            "stock_sud": values[8],

            "base_nord": values[12],
            "add_nord": values[13],
            "remove_nord": values[14],
            "stock_nord": values[15],

            "total": values[19],
        }


    def load_items(self):
        """Charge les objets depuis Google Sheets."""

        ITEMS.clear()

        values = self.sheet.col_values(3)

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

        return len(ITEMS.data)