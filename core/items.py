from dataclasses import dataclass


@dataclass(slots=True)
class Item:

    name: str
    row: int


class Items:

    def __init__(self):

        self.data = {}

    def normalize(self, text: str):

        return (
            text.lower()
            .replace("é", "e")
            .replace("è", "e")
            .replace("ê", "e")
            .replace("à", "a")
            .replace("ù", "u")
            .replace("ï", "i")
            .replace("î", "i")
            .strip()
        )

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