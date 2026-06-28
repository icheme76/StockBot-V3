from logger import logger
from core.sheets import StockSheet

def main():
    logger.info("=" * 50)
    logger.info("StockBot V3")
    logger.info("=" * 50)

    sheet = StockSheet()

    logger.info("Connexion à Google Sheets...")

    sheet.load_items()

    logger.success("Le bot est prêt.")

if __name__ == "__main__":
    main()