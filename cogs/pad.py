import os
import sys
import datetime
import sched
import discord
from discord.ext import commands
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

scriptdir = os.path.dirname(os.path.abspath('bot.py'))+"\\scripts\\"
padscriptdir = scriptdir+"pad\\"
channelid=int(config.config['BOT']['autochannel'])
padtime_scrapeskyozora = '6:30' # 6:30 AM PT

class PADCog (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def time_check(self):
        await client.wait_until_ready()

        while not client.is_closed:
            channel = client.get_channel(channelid)
            messages = ('Test')
            f = '%H:%M'

            now = datetime.strftime(datetime.now(), f)
            diff = (datetime.strptime(padtime_scrapeskyozora, f) - datetime.strptime(now, f)).total_seconds()

            s = sched.scheduler(time.perf_counter, time.sleep)
            args = (client.send_message(channel, message), )
            s.enter(seconds, 1, client.loop.create_task, args)
            s.run()



def setup(bot):
    b = PADCog(bot)
    bot.loop.create_task(b.time_check())
    bot.add_cog(b)
