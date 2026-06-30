from aiohttp import web

from core.items import ITEMS
from core.sheets import StockSheet

routes = web.RouteTableDef()

sheet = StockSheet()


@routes.get("/")
async def home(request):
    return web.json_response({
        "status": "online",
        "service": "StockBot V3"
    })


@routes.post("/stock/add")
async def stock_add(request):

    data = await request.json()

    objet = data.get("item")
    quantite = int(data.get("quantity", 0))

    item = ITEMS.get(objet)

    if item is None:
        return web.json_response(
            {"success": False, "error": "Objet introuvable"},
            status=404
        )

    total = sheet.add_quantity(item.row, quantite)

    return web.json_response({
        "success": True,
        "item": item.name,
        "quantity": quantite,
        "total": total
    })


async def start_api(bot):

    app = web.Application()
    app["bot"] = bot

    app.add_routes(routes)

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(
        runner,
        "127.0.0.1",
        8080
    )

    await site.start()