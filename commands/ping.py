import discord
from discord import app_commands
from discord.ext import commands

GUILD_ID = 1503533579580342382


class Ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="ping",
        description="Teste le bot."
    )
    @app_commands.guilds(discord.Object(id=GUILD_ID))
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("🏓 Pong !")


async def setup(bot):
    await bot.add_cog(Ping(bot))