import os
import sys
from datetime import datetime
import asyncio
import discord
import time
from discord.ext import commands
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config
from bs4 import BeautifulSoup
import requests

scriptdir = os.path.dirname(os.path.abspath('bot.py'))+"\\scripts\\"
padscriptdir = scriptdir+"pad\\"
channelid=int(config.config['BOT']['autochannel'])

class PADCog (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def skyozora_check(self):
        await self.bot.wait_until_ready()

        # scrape at reset
        import time
        padtime_scrapeskyozora = '08:01'
        if time.localtime().tm_isdst == 1:
            padtime_scrapeskyozora = '08:01'
        elif time.localtime().tm_isdst == 0:
            padtime_scrapeskyozora = '07:01'

        channel = self.bot.get_channel(channelid)
        dst = time.localtime().tm_isdst
        dailies_time=[]
        dailies_string=[]

        # scrape at startup
        ################################################
        r=requests.get("http://pad.skyozora.com/")
        soup = BeautifulSoup(r.content, 'html.parser')
        tables = soup.find("table","sample")
        rows = tables.find_all('tr')

        for i,row in enumerate(rows):
            if i > 1:
                cols = row.find_all('td')
                cols2 = [ele.text.strip() for ele in cols]
                if i == 2:
                    descends=cols2[1].split(" ")
                    message = "\n- ".join(descends).rstrip()
                    message = "[ Today's Descended ]\n" + message
                    await channel.send("```css\n"+message+"```")
                elif i == len(rows)-1 or i == len(rows)-2:
                    None
                else:
                    offset=0
                    if dst==0:
                        offset=16
                    else:
                        offset=15
                    daily = int(cols2[0][:-1])-offset
                    if daily < 0:
                        daily=daily+24
                        daily=str('{0:02d}'.format(daily))+":00"
                        dailies_time.append(daily)
                        name=row.find_all('td')[0].find('a')["title"]
                        dailies_string.append(name)

        dailies="Today's Guerrilla Schedule\n"
        for i,row in enumerate(dailies_time):
            dailies = dailies+row+" "+dailies_string[i]+"\n"
        await channel.send("```"+dailies+"```")

        ################################################

        while self is self.bot.get_cog("PADCog"):
            now = datetime.strftime(datetime.now(),'%H:%M')
            if now == padtime_scrapeskyozora:
                # scrape current events

                r=requests.get("http://pad.skyozora.com/")
                soup = BeautifulSoup(r.content, 'html.parser')
                tables = soup.find("table","sample")
                rows = tables.find_all('tr')

                for i,row in enumerate(rows):
                    if i > 1:
                        cols = row.find_all('td')
                        cols2 = [ele.text.strip() for ele in cols]
                        if i == 2:
                            descends=cols2[1].split(" ")
                            message = "\n- ".join(descends).rstrip()
                            message = "[ Today's Descended ]\n" + message
                            await channel.send("```css\n"+message+"```")
                        elif i == len(rows)-1 or i == len(rows)-2:
                            None
                        else:
                            offset=0
                            if dst==0:
                                offset=16
                            else:
                                offset=15

                            # get the time in UTC+8
                            # cols[0] because I only care about red one
                            daily = int(cols2[0][:-1])-offset
                            if daily < 0:
                                daily=daily+24
                            daily=str('{0:02d}'.format(daily))+":00"
                            dailies_time.append(daily)
                            name=row.find_all('td')[0].find('a')["title"]
                            dailies_string.append(name)

                dailies="Today's Guerrilla Schedule\n"
                for i,row in enumerate(dailies_time):
                    dailies = dailies+row+" "+dailies_string[i]+"\n"
                await channel.send("```"+dailies+"```")

                if time.localtime().tm_isdst == 1:
                    padtime_scrapeskyozora = '08:01'
                elif time.localtime().tm_isdst == 0:
                    padtime_scrapeskyozora = '07:01'
                await asyncio.sleep(61)
            else:
                await asyncio.sleep(1)


def setup(bot):
    b = PADCog(bot)
    bot.loop.create_task(b.skyozora_check())
    bot.add_cog(b)
