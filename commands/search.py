import discord
from discord import app_commands
from discord.ext import commands
from core.autocomplete import item_autocomplete

from core.items import ITEMS

GUILD_ID = 1503533579580342382


class Search(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="search",
        description="Recherche un objet."
    )
    @app_commands.guilds(discord.Object(id=GUILD_ID))
    @app_commands.autocomplete(objet=item_autocomplete)
    async def search(
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

        await interaction.response.send_message(
            f"📦 **{item.name}**\n"
            f"Ligne : {item.row}"
        )


async def setup(bot):
    await bot.add_cog(Search(bot))