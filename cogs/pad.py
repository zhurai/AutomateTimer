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

    @staticmethod
    async def _padjp_scrape_skyozora():
        dailies_time=[]
        dailies_string=[]
        descends=[]

        # scrape from skyozora
        r=requests.get("http://pad.skyozora.com/")
        soup = BeautifulSoup(r.content, 'html.parser')
        tables = soup.find("table","sample")
        rows = tables.find_all('tr')

        for i,row in enumerate(rows):
            if i > 1:
                cols = row.find_all('td')
                a = cols[1].find_all('a')

                if i == 2:
                    for link in a:
                        descends.append(link.text.strip())
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
        return descends,dailies_time,dailies_string

    @commands.command()
    async def padjp (self, ctx, *args):
        if len(args) == 1:
            if args[0] == 'dailies' or args[0] == 'daily':
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
                descends=[]

                descends,dailies_time,dailies_string = await self._padjp_scrape_skyozora()

                descend_message = "\n- ".join(descends).rstrip()
                descend_message = "[ Today's Descended ]\n- " + descend_message
                await channel.send("```css\n"+descend_message+"```")

                dailies_message = "Today's Guerrilla Schedule\n"
                for i,row in enumerate(dailies_time):
                    dailies_message = dailies_message+"["+row+"] "+dailies_string[i]+"\n"
                await channel.send("```css\n"+dailies_message+"```")

            # !wm get ???
            else:
                print("  padjp: invalid argument")
                await ctx.send("[ERROR] padjp: invalid argument given")
        # !wm get
        else:
            # no argument given
            print("  padjp: no argument given")
            await ctx.send("[ERROR] padjp: not enough arguments")



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
        descends=[]

        # first run
        descends,dailies_time,dailies_string = await self._padjp_scrape_skyozora()

        descend_message = "\n- ".join(descends).rstrip()
        descend_message = "[ Today's Descended ]\n- " + descend_message
        await channel.send("```css\n"+descend_message+"```")

        dailies_message = "Today's Guerrilla Schedule\n"
        for i,row in enumerate(dailies_time):
            dailies_message = dailies_message+"["+row+"] "+dailies_string[i]+"\n"
        await channel.send("```css\n"+dailies_message+"```")


        # later/daily scheduling

        while self is self.bot.get_cog("PADCog"):
            now = datetime.strftime(datetime.now(),'%H:%M')
            if now == padtime_scrapeskyozora:
                # scrape current events
                dailies_time=[]
                dailies_string=[]
                descends=[]

                # first run
                descends,dailies_time,dailies_string = await self._padjp_scrape_skyozora()

                descend_message = "\n- ".join(descends).rstrip()
                descend_message = "[ Today's Descended ]\n- " + descend_message
                await channel.send("```css\n"+descend_message+"```")

                dailies_message = "Today's Guerrilla Schedule\n"
                for i,row in enumerate(dailies_time):
                    dailies_message = dailies_message+"["+row+"] "+dailies_string[i]+"\n"
                await channel.send("```css\n"+dailies_message+"```")

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
