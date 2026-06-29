import discord
from discord import app_commands
from discord.ext import commands
from core.permissions import has_permission

from core.items import ITEMS
from core.sheets import StockSheet

GUILD_ID = 1521082473839071282


class Add(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.sheet = StockSheet()

    @app_commands.command(
        name="add",
        description="Ajoute une quantité."
    )
    @app_commands.guilds(discord.Object(id=GUILD_ID))
    async def add(
        self,
        interaction: discord.Interaction,
        objet: str,
        quantite: int
    ):

        if not has_permission(interaction.user):
            await interaction.response.send_message(
                "❌ Vous n'avez pas la permission.",
                ephemeral=True
            )
            return


        item = ITEMS.get(objet)

        if item is None:
            await interaction.response.send_message(
                "❌ Objet introuvable."
            )
            return

        total = self.sheet.add_quantity(
            item.row,
            quantite
        )

        await interaction.response.send_message(
            f"✅ {quantite} ajoutés à **{item.name}**\n"
            f"Nouvelle valeur : **{total}**"
        )


async def setup(bot):
    await bot.add_cog(Add(bot))