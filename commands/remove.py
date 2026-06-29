import discord
from discord import app_commands
from discord.ext import commands

from core.items import ITEMS
from core.sheets import StockSheet

GUILD_ID = 1521082473839071282


class Remove(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.sheet = StockSheet()

    @app_commands.command(
        name="remove",
        description="Retire une quantité."
    )
    @app_commands.guilds(discord.Object(id=GUILD_ID))
    async def remove(
        self,
        interaction: discord.Interaction,
        objet: str,
        quantite: int
    ):

        item = ITEMS.get(objet)

        if item is None:
            await interaction.response.send_message(
                "❌ Objet introuvable."
            )
            return

        total = self.sheet.remove_quantity(
            item.row,
            quantite
        )

        await interaction.response.send_message(
            f"✅ {quantite} retirés de **{item.name}**\n"
            f"Nouvelle valeur : **{total}**"
        )


async def setup(bot):
    await bot.add_cog(Remove(bot))