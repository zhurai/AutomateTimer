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
    async def wmget(self, ctx, *args):
        print ("wmget: watchme command called with arguments: '", args,"'")

        if len(args) == 0:
            # no argument given
            print("  wmget: no argument given")
            await ctx.send("[ERROR] wmget: no argument given")

        # !wmget ()
        if len(args) > 1:
            # !wmget tab ()
            if args[0].lower() == 'tab' or args[0].lower() == 'tabs':
                if len(args) > 2:
                    print("  wmget.tab: arguments: " + args[2])
                    # !wmget tab num
                    if args[1].lower() == 'num' or args[1].lower() == 'id':
                        proc = subprocess.Popen(['C:\Program Files (x86)\AutoIt3\AutoIt3.exe',scriptdir+'wmget.tabs.num.au3'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        stdout_value = proc.stdout.read() + proc.stderr.read()
                        await ctx.send(stdout_value.rstrip().decode())

                    # !wmget tab name
                    elif args[1].lower() == 'name':
                        proc = subprocess.Popen(['C:\Program Files (x86)\AutoIt3\AutoIt3.exe',scriptdir+'wmget.tabs.name.au3'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        stdout_value = proc.stdout.read() + proc.stderr.read()
                        await ctx.send(stdout_value.rstrip().decode())

                    # !wmget tab list
                    elif args[1].lower() == 'list':
                        # list of tabs
                        proc = subprocess.Popen(['C:\Program Files (x86)\AutoIt3\AutoIt3.exe',scriptdir+'wmget.tabs.list.au3'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        stdout_value = proc.stdout.read() + proc.stderr.read()
                        tabs1=stdout_value.decode().split("\r\n")
                        tabs2="\n".join(tabs1).rstrip()
                        await ctx.send("```"+tabs2+"```")

                    # !wmget tab ???
                    else:
                        print("  wmget.tab: invalid argument")
                        await ctx.send("[ERROR] wmget.tabs: invalid argument given")

                # !wmget tab
                else:
                    print("  wmget.tabs: not enough arguments")
                    await ctx.send("[ERROR] wmget.tabs: not enough arguments")

            # !wmget timer ()
            elif args[0].lower() == 'timer' or args[0].lower() == 'timers':
                if len(args) > 2:
                    print("  wm.get.timers: arguments: " + args[1])

                    # !wm get timers curr/current
                    if args[1].lower() == 'curr' or args[1].lower() == 'current':
                        # list of timers on current section / tab
                        print("  wmget.timers: current tab")
                        proc = subprocess.Popen(['C:\Program Files (x86)\AutoIt3\AutoIt3.exe',scriptdir+'wmget.timer.curr.au3'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        stdout_value = proc.stdout.read() + proc.stderr.read()
                        timers=stdout_value.decode().split("\r\n")
                        timers2=", ".join(timers).rstrip(', ')
                        await ctx.send(timers2)

                    # !wm get timers all
                    elif args[1].lower() == 'all':
                        # list of timers on all sections / tabs
                        print("  wmget.timers: all tabs")
                        proc = subprocess.Popen(['C:\Program Files (x86)\AutoIt3\AutoIt3.exe',scriptdir+'wmget.timer.all.au3'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        stdout_value = proc.stdout.read() + proc.stderr.read()
                        timers=stdout_value.decode().split("\r\n")
                        timers2=", ".join(timers).rstrip(', ')
                        await ctx.send(timers2)


                    # !wm get timers ???
                    else:
                        print("  wmget.timers: invalid argument")
                        await ctx.send("[ERROR] wmget.timers: invalid argument given")

                else:
                    # only display CURRENT tab timers by default
                    print("  wmget.timers: default (current tab only)")
                    proc = subprocess.Popen(['C:\Program Files (x86)\AutoIt3\AutoIt3.exe',scriptdir+'wmget.timer.curr.au3'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    stdout_value = proc.stdout.read() + proc.stderr.read()
                    tabs=stdout_value.decode().replace("\r\n",", ")
                    await ctx.send(tabs)

            # !wmget control ()
            elif args[0].lower() == 'control' or args[0].lower() == 'controls':
                if len(args) > 2:
                    print("  wmget.control: arguments: " + args[1])

                    # !wmget control list
                    # output all CURRENT tab timers
                    if args[1].lower() == 'list' or args[1].lower() == 'current':
                        proc = subprocess.Popen(['C:\Program Files (x86)\AutoIt3\AutoIt3.exe',scriptdir+'wmget.control.list.au3'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        stdout_value = proc.stdout.read() + proc.stderr.read()
                        control1=stdout_value.decode().split("\r\n")
                        control2="\n".join(control1).rstrip()
                        await ctx.send("```"+control2+"```")

                    # !wm get control "text"
                    # output "text" "start/stop control" "reset control"
            # !wm get ???
            else:
                print("  wmget: invalid argument")
                await ctx.send("[ERROR] wmget: invalid argument given")
        # !wm get
        else:
            # no argument given
            print("  wmget no argument given")
            await ctx.send("[ERROR] wmget: not enough arguments")

    @commands.command()
    async def wmset(self, ctx, *args):
        print ("wmset: [NI] watchme command called with arguments: '", args,"'")
        await ctx.send("[ERROR] wmset: not implemented yet")

    @commands.command()
    async def wmadd(self, ctx, *args):
        print ("wmadd: [NI] watchme command called with arguments: '", args,"'")
        await ctx.send("[ERROR] wmadd: not implemented yet")

def setup(bot):
    bot.add_cog(WatchMeCog(bot))
