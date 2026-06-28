import discord

intents = discord.Intents.default()


class StockBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)

    async def on_ready(self):
        print(f"✅ Connecté en tant que {self.user}")