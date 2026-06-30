import discord
from discord import app_commands
from discord.ext import commands
from core.permissions import has_permission
from core.autocomplete import item_autocomplete
from core.logs import send_log

from core.items import ITEMS
from core.sheets import StockSheet

GUILD_ID = 1503533579580342382


class Remove(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.sheet = StockSheet()

    @app_commands.command(
        name="remove",
        description="Retire une quantité."
    )
    @app_commands.guilds(discord.Object(id=GUILD_ID))
    @app_commands.autocomplete(objet=item_autocomplete)
    async def remove(
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

        total = self.sheet.remove_quantity(
            item.row,
            quantite
        )

        await interaction.response.send_message(
            f"✅ {quantite} retirés de **{item.name}**\n"
            f"Nouvelle valeur : **{total}**"
        )

        embed = discord.Embed(
            title="🔴 Stock retiré",
            color=discord.Color.red()
        )

        embed.add_field(
            name="Utilisateur",
            value=interaction.user.mention,
            inline=False
        )

        embed.add_field(
            name="Objet",
            value=item.name,
            inline=True
        )

        embed.add_field(
            name="Quantité",
            value=f"-{quantite}",
            inline=True
        )

        await send_log(self.bot, embed)


async def setup(bot):
    await bot.add_cog(Remove(bot))