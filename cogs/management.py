import os
import subprocess
import discord
import pyautogui
from discord.ext import commands

scriptdir = os.path.dirname(os.path.abspath('bot.py'))+"\\scripts\\"

class ManagementCog (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=[reboot,reset])
    async def restart(self, ctx):
        # restarts script, not watchme
        os.startfile(scriptdir+'restart.bat')
        await self.bot.close()

    @commands.command(aliases=[close])
    async def shutdown(self, ctx):
        # closes script, not watchme
        await self.bot.close()

    @commands.command()
    async def gitpull(self, ctx):
        print("git pull command called")
        # git pulls for this script/rehash
        proc = subprocess.Popen([scriptdir+'gitpull.bat'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        # send something when completed?
        # the following is currently test ones
        stdout_value = proc.stdout.read() + proc.stderr.read()
        await ctx.send(stdout_value)

    @commands.command(aliases=[startwatchme])
    async def runwatchme(self,ctx):
        # starts watchme
        proc = subprocess.Popen([scriptdir+'runwatchme.bat'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        # send something when completed?
        return

    @commands.command()
    async def screenshot(self,ctx):
        s=pyautogui.screenshot('screenshots/screenshot.png')
        with open('screenshots/screenshot.png','rb') as fp:
            await ctx.send(file=discord.File(fp,'screenshot.png'))


def setup(bot):
    bot.add_cog(ManagementCog(bot))
