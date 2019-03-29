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
    async def wm(self, ctx, *args):
        print ("wm: watchme command called with arguments: '", args,"'")

        if len(args) == 0:
            # no argument given
            print("  wm: no argument given")
            await ctx.send("[ERROR] wm: no argument given")

        # !wm get ()
        if len(args) > 0 and args[0].lower()=='get':
            if len(args) > 1:


                # !wm get tab ()
                if args[1].lower()=='tab':
                    if len(args) > 2:
                        print("  wm.get.tabs: arguments: "+args[2])

                        # !wm get tab num
                        if args[2] == 'num':
                            proc = subprocess.Popen(['C:\Program Files (x86)\AutoIt3\AutoIt3.exe',scriptdir+'wmget.tabs.num.au3'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                            stdout_value = proc.stdout.read() + proc.stderr.read()
                            await ctx.send(stdout_value.rstrip().decode())

                        # !wm get tab name
                        elif args[2] == 'name':
                            proc = subprocess.Popen(['C:\Program Files (x86)\AutoIt3\AutoIt3.exe',scriptdir+'wmget.tabs.name.au3'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                            stdout_value = proc.stdout.read() + proc.stderr.read()
                            await ctx.send(stdout_value.rstrip().decode())

                        # !wm get tab list
                        elif args[2] == 'list':
                            # list of tabs
                            proc = subprocess.Popen(['C:\Program Files (x86)\AutoIt3\AutoIt3.exe',scriptdir+'wmget.tabs.list.au3'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                            stdout_value = proc.stdout.read() + proc.stderr.read()
                            await ctx.send(stdout_value)

                        # !wm get tab ???
                        else:
                            print("  wm.get.tabs: invalid argument")
                            await ctx.send("[ERROR] wm.get.tabs: invalid argument given")
                    # !wm get tab
                    else:
                        print("  wm.get.tabs: not enough arguments")
                        await ctx.send("[ERROR] wm.get.tabs: not enough arguments")


                #elif args[1].lower()=='':
                #    None

                #elif args[1].lower()=='':
                #    None


            # !wm get
            else:
                # no argument given
                print("  wm.get no argument given")
                await ctx.send("[ERROR] wm.get: not enough arguments")




        elif len(args) > 0 and args[0].lower() == 'set':
            None




        elif len(args) > 0 and args[0].lower() == 'add':
            if len(args) > 1:
                # !wm add tab ()
                if args[1].lower() == 'tab':
                    None
                elif args[1].lower() == ''
                    None


        # !wm ()
        else:
            # invalid arguments
            print("  wm: invalid arguments")
            await ctx.send("[ERROR] wm: invalid arguments")



        '''
                if args[1].lower()=='timers':
                    None

                elif args[1].lower()=='control':
                    None

                elif args[1].lower()=='control':
                    None

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

def setup(bot):
    bot.add_cog(WatchMeCog(bot))
