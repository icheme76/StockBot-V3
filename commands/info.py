import discord
from discord import app_commands
from discord.ext import commands
from core.autocomplete import item_autocomplete

from core.items import ITEMS
from core.sheets import StockSheet

GUILD_ID = 1503533579580342382


class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.sheet = StockSheet()

    @app_commands.command(
        name="info",
        description="Affiche les informations d'un objet."
    )
    @app_commands.guilds(discord.Object(id=GUILD_ID))
    @app_commands.autocomplete(objet=item_autocomplete)
    async def info(
        self,
        interaction: discord.Interaction,
        objet: str
    ):

        item = ITEMS.get(objet)

        if item is None:
            await interaction.response.send_message(
                "❌ Objet introuvable."
            )
            return

        data = self.sheet.get_item_info(item.row)

        embed = discord.Embed(
            title=f"📦 {item.name}",
            color=discord.Color.green()
        )

        embed.add_field(
            name="🌴 Sud",
            value=(
                f"Base : {data['base_sud']}\n"
                f"Ajouter : {data['add_sud']}\n"
                f"Retirer : {data['remove_sud']}\n"
                f"En stock : {data['stock_sud']}"
            ),
            inline=False
        )

        embed.add_field(
            name="❄️ Nord",
            value=(
                f"Base : {data['base_nord']}\n"
                f"Ajouter : {data['add_nord']}\n"
                f"Retirer : {data['remove_nord']}\n"
                f"En stock : {data['stock_nord']}"
            ),
            inline=False
        )

        embed.add_field(
            name="📊 Total",
            value=data["total"],
            inline=False
        )

        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Info(bot))