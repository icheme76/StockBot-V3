import discord

from logger import logger


class StockBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()

        super().__init__(intents=intents)

    async def on_ready(self):
        logger.success(f"Connecté à Discord : {self.user}")