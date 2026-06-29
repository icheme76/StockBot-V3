from config import DISCORD_TOKEN
from logger import logger
from discord.ext import commands

from core.sheets import StockSheet
from discord_bot.client import StockBot


def main():

    logger.info("=" * 50)
    logger.info("StockBot V3")
    logger.info("=" * 50)

    logger.info("Connexion à Google Sheets...")

    sheet = StockSheet()

    count = sheet.load_items()

    logger.info(f"{count} objets chargés.")

    bot = StockBot()

    logger.info("Connexion à Discord...")

    @bot.command()
    async def ping(ctx):
        await ctx.send("🏓 Pong !")

    bot.run(DISCORD_TOKEN)


if __name__ == "__main__":
    main()