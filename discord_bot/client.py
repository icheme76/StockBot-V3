import discord
from discord.ext import commands

from logger import logger


class StockBot(commands.Bot):

    def __init__(self):
        intents = discord.Intents.default()

        super().__init__(
            command_prefix="!",
            intents=intents,
        )

    async def setup_hook(self):
        # Rien pour le moment
        pass

    async def on_ready(self):
        logger.success(f"Connecté à Discord : {self.user.name}")