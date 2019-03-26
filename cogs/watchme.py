import os
import subprocess
import discord
import pyautogui
from discord.ext import commands

scriptdir = os.path.dirname(os.path.abspath('bot.py'))+"\\scripts\\"

class WatchMeCog (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def autoit(self, ctx, *args):
        '''
        print("git:")
        print("git pull command called with arguments: '", args,"'" )
        # git pull

        if len(args) == 0:
            # no argument given
            print("  git: no argument given")
            await ctx.send("git: pulling from default")
            proc = subprocess.Popen([scriptdir+'gitpull.bat'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            stdout_value = proc.stdout.read() + proc.stderr.read()
            await ctx.send(stdout_value.rstrip().decode())

        elif len(args) == 1:
            # one argument given
            print("  git: argument given: '" + args[0],"'")
            if (args[0].lower() == 'watchme' or args[0].lower() == 'app'):
                # watchme itself
                print("   git: watchme selected")
                await ctx.send("git: pulling from watchmescripts")
                proc = subprocess.Popen([scriptdir+'gitpullwatchme.bat'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                stdout_value = proc.stdout.read() + proc.stderr.read()
                await ctx.send(stdout_value.rstrip().decode())
            elif (args[0].lower() == 'automatetimer' or args[0].lower() == 'self' or args[0].lower() == 'srv' or args[0].lower() == 'bot'):
                # automate timer
                print("   git: automatetimer selected")
                await ctx.send("git: pulling from automatetimer")
                proc = subprocess.Popen([scriptdir+'gitpull.bat'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                stdout_value = proc.stdout.read() + proc.stderr.read()
                await ctx.send(stdout_value.rstrip().decode())
            else:
                print("   git: none selected")
                await ctx.send("git: invalid input!")
        print(" git: finished")
        '''

        print(scriptdir+'test_consoleautoit.au3')
        proc = subprocess.Popen(['C:\Program Files (x86)\AutoIt3\AutoIt3.exe',scriptdir+'test_consoleautoit.au3'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_value = proc.stdout.read() + proc.stderr.read()
        await ctx.send(stdout_value.rstrip().encode())

def setup(bot):
    bot.add_cog(WatchMeCog(bot))
