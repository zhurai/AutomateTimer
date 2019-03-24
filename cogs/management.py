import config
import os
import subprocess
import discord
from discord.ext import commands

class ManagementCog:
	@bot.command()
	async def restart(ctx):
	    # restarts script, not watchme
		os.startfile(cwd+'restart.bat')
		await bot.close()

	@bot.command()
	async def shutdown(ctx):
	    # closes script, not watchme
	    await bot.close()

	@bot.command()
	async def close(ctx):
	    # closes script, not watchme
	    await bot.close()

	@bot.command()
	async def gitpull(ctx):
	    print("git pull command called")
	    # git pulls for this script/rehash
	    proc = subprocess.Popen([cwd+'gitpull.bat'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	    # send something when completed?
	    # the following is currently test ones
	    stdout_value = proc.stdout.read() + proc.stderr.read()
	    await ctx.send(stdout_value)

def setup(bot):
    bot.add_cog(ManagementCog(bot))
