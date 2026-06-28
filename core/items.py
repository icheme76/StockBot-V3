from dataclasses import dataclass
import unicodedata

@dataclass(slots=True)
class Item:

    name: str
    row: int


class Items:

    def __init__(self):

        self.data = {}

    def normalize(self, text: str) -> str:
        text = unicodedata.normalize("NFD", text)
        text = text.encode("ascii", "ignore").decode("utf-8")

        return text.lower().strip()

    def add(self, name, row):

        self.data[self.normalize(name)] = Item(
            name=name,
            row=row
        )

    def get(self, name):

        return self.data.get(
            self.normalize(name)
        )

    def clear(self):

        self.data.clear()


ITEMS = Items()