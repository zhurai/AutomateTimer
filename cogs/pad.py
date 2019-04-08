import os
import sys
from datetime import datetime
import asyncio
import sched
import discord
from discord.ext import commands
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

scriptdir = os.path.dirname(os.path.abspath('bot.py'))+"\\scripts\\"
padscriptdir = scriptdir+"pad\\"
channelid=int(config.config['BOT']['autochannel'])
padtime_scrapeskyozora = '07:11' # 6:30 PT
message = "Test"

class PADCog (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def skyozora_check(self):
        while self is self.bot.get_cog("PADCog"):
            now = datetime.strftime(datetime.now(),'%H:%M')
            if now == padtime_scrapeskyozora:
                channel = self.bot.get_channel(channelid)
                await channel.send(message)
                await asyncio.sleep(90)
            else:
                await asyncio.sleep(1)


def setup(bot):
    b = PADCog(bot)
    bot.loop.create_task(b.skyozora_check())
    bot.add_cog(b)
