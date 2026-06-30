import discord

LOG_CHANNEL_ID = 1521147740581527714


async def send_log(bot, embed):

    channel = bot.get_channel(LOG_CHANNEL_ID)

    if channel is not None:
        await channel.send(embed=embed)