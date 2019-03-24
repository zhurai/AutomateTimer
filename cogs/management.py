import config
import os
import subprocess
import discord
from discord.ext import commands

class ManagementCog (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def restart(self, ctx):
        # restarts script, not watchme
        os.startfile(cwd+'restart.bat')
        await self.bot.close()

    @commands.command()
    async def shutdown(self, ctx):
        # closes script, not watchme
        await self.bot.close()

    @commands.command()
    async def close(self, ctx):
        # closes script, not watchme
        await self.bot.close()

    @commands.command()
    async def gitpull(self, ctx):
        print("git pull command called")
        # git pulls for this script/rehash
        proc = subprocess.Popen([cwd+'gitpull.bat'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        # send something when completed?
        # the following is currently test ones
        stdout_value = proc.stdout.read() + proc.stderr.read()
        await ctx.send(stdout_value)

def setup(bot):
    bot.add_cog(ManagementCog(bot))
