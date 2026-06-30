import discord
from discord.ext import commands
from api.server import start_api

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
       await self.load_extension("commands.add")
       await self.load_extension("commands.remove")
       await self.load_extension("commands.info")
       await self.load_extension("commands.webhook_listener")
       await start_api(self)
       guild = discord.Object(id=1503533579580342382)
       await self.tree.sync(guild=guild)

    async def on_ready(self):
        logger.success(f"Connecté à Discord : {self.user.name}")