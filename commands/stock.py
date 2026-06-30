import discord
from discord import app_commands
from discord.ext import commands

from core.items import ITEMS

GUILD_ID = 1503533579580342382


class Stock(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="stock",
        description="Affiche le nombre d'objets chargés."
    )
    @app_commands.guilds(discord.Object(id=GUILD_ID))
    async def stock(self, interaction: discord.Interaction):

        await interaction.response.send_message(
            f"📦 {len(ITEMS.data)} objets chargés."
        )


async def setup(bot):
    await bot.add_cog(Stock(bot))