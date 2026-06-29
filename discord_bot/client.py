import discord
from discord.ext import commands

from logger import logger


class StockBot(commands.Bot):

    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(
            command_prefix="!",
            intents=intents
        )

    async def setup_hook(self):
       await self.load_extension("commands.ping")
       await self.load_extension("commands.stock")
       await self.load_extension("commands.search")
       guild = discord.Object(id=1521082473839071282)
       await self.tree.sync(guild=guild)

    async def on_ready(self):
        logger.success(f"Connecté à Discord : {self.user.name}")