import re

import discord
from discord.ext import commands
from core.items import ITEMS
from core.sheets import StockSheet

sheet = StockSheet()

SOUTH_CHANNEL = 1517220983629418648
NORTH_CHANNEL = 1517221032707100815
PLANTATION_CHANNEL = 1517220899168981134
SOUTH_ADD = 7
SOUTH_REMOVE = 8

NORTH_ADD = 14
NORTH_REMOVE = 15

PLANTATION_ADD = 7
PLANTATION_REMOVE = 8

class WebhookListener(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if not message.embeds:
            return
      
        embed = message.embeds[0]

        description = embed.description or ""

        match = re.search(
            r"\*\*(.+?)\*\* a (déposé|retiré) (\d+)x (.+)",
            description
        )

        if not match:
            return

        joueur = match.group(1)
        action = match.group(2)
        quantite = int(match.group(3))
        objet = match.group(4)

        ALIASES = {
            "Argent Sale": "SALE",
            "Argent Propre": "PROPRE",
        }

        objet = ALIASES.get(objet, objet)

        item = ITEMS.get(objet)

        if item is None:
           print(f"Objet inconnu : {objet}")
           return

        if message.channel.id == SOUTH_CHANNEL:
            add_col = SOUTH_ADD
            remove_col = SOUTH_REMOVE

        elif message.channel.id == NORTH_CHANNEL:
            add_col = NORTH_ADD
            remove_col = NORTH_REMOVE

        else:
            add_col = SOUTH_ADD
            remove_col = SOUTH_REMOVE


        if action == "déposé":
            total = sheet.add_quantity(
                item.row,
                quantite,
                add_col
            )
        else:
            total = sheet.remove_quantity(
                item.row,
                quantite,
                remove_col
            )

        print(f"{objet} mis à jour -> {total}")

async def setup(bot):
    await bot.add_cog(WebhookListener(bot))