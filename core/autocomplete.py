from discord import app_commands

from core.items import ITEMS


async def item_autocomplete(
    interaction,
    current: str,
):

    results = []

    for item in ITEMS.data.values():

        if current.lower() in item.name.lower():

            results.append(
                app_commands.Choice(
                    name=item.name,
                    value=item.name,
                )
            )

        if len(results) >= 25:
            break

    return results