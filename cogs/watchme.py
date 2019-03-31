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
        if len(args) > 0 and args[0].lower() == 'get':
            if len(args) > 1:


                # !wm get tab ()
                if args[1].lower() == 'tab' or args[1].lower() == 'tabs':
                    if len(args) > 2:
                        print("  wm.get.tabs: arguments: " + args[2])

                        # !wm get tab num
                        if args[2].lower() == 'num' or args[2].lower() == 'id':
                            proc = subprocess.Popen(['C:\Program Files (x86)\AutoIt3\AutoIt3.exe',scriptdir+'wmget.tabs.num.au3'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                            stdout_value = proc.stdout.read() + proc.stderr.read()
                            await ctx.send(stdout_value.rstrip().decode())

                        # !wm get tab name
                        elif args[2].lower() == 'name':
                            proc = subprocess.Popen(['C:\Program Files (x86)\AutoIt3\AutoIt3.exe',scriptdir+'wmget.tabs.name.au3'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                            stdout_value = proc.stdout.read() + proc.stderr.read()
                            await ctx.send(stdout_value.rstrip().decode())

                        # !wm get tab list
                        elif args[2].lower() == 'list':
                            # list of tabs
                            proc = subprocess.Popen(['C:\Program Files (x86)\AutoIt3\AutoIt3.exe',scriptdir+'wmget.tabs.list.au3'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                            stdout_value = proc.stdout.read() + proc.stderr.read()
                            tabs1=stdout_value.decode().split("\r\n")
                            tabs2="\n".join(tabs1).rstrip()
                            await ctx.send("```"+tabs2+"```")


                        # !wm get tab ???
                        else:
                            print("  wm.get.tabs: invalid argument")
                            await ctx.send("[ERROR] wm.get.tabs: invalid argument given")
                    # !wm get tab
                    else:
                        print("  wm.get.tabs: not enough arguments")
                        await ctx.send("[ERROR] wm.get.tabs: not enough arguments")


                # !wm get timer ()
                elif args[1].lower() == 'timer' or args[1].lower() == 'timers':
                    if len(args) > 2:
                        print("  wm.get.timers: arguments: " + args[2])

                        # !wm get timers curr/current
                        if args[2].lower() == 'curr' or args[2].lower() == 'current':
                            # list of timers on current section / tab
                            print("  wm.get.timers: current tab")
                            proc = subprocess.Popen(['C:\Program Files (x86)\AutoIt3\AutoIt3.exe',scriptdir+'wmget.timer.curr.au3'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                            stdout_value = proc.stdout.read() + proc.stderr.read()
                            timers=stdout_value.decode().split("\r\n")
                            timers2=", ".join(timers).rstrip(', ')
                            await ctx.send(timers2)

                        # !wm get timers all
                        elif args[2].lower() == 'all':
                            # list of timers on all sections / tabs
                            print("  wm.get.timers: all tabs")
                            proc = subprocess.Popen(['C:\Program Files (x86)\AutoIt3\AutoIt3.exe',scriptdir+'wmget.timer.all.au3'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                            stdout_value = proc.stdout.read() + proc.stderr.read()
                            timers=stdout_value.decode().split("\r\n")
                            timers2=", ".join(timers).rstrip(', ')
                            await ctx.send(timers2)


                        # !wm get timers ???
                        else:
                            print("  wm.get.timers: invalid argument")
                            await ctx.send("[ERROR] wm.get.timers: invalid argument given")
                    else:
                        # only display CURRENT tab timers by default
                        print("  wm.get.timers: default (current tab only)")
                        proc = subprocess.Popen(['C:\Program Files (x86)\AutoIt3\AutoIt3.exe',scriptdir+'wmget.timer.curr.au3'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        stdout_value = proc.stdout.read() + proc.stderr.read()
                        tabs=stdout_value.decode().replace("\r\n",", ")
                        await ctx.send(tabs)

                elif args[1].lower() == 'control' or args[1].lower() == 'controls':
                    if len(args) > 2:
                        print("  wm.get.control: arguments: " + args[2])

                        # !wm get control list
                        # output all CURRENT tab timers
                        if args[2].lower() == 'list' or args[2].lower() == 'current':
                            proc = subprocess.Popen(['C:\Program Files (x86)\AutoIt3\AutoIt3.exe',scriptdir+'wmget.control.list.au3'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                            stdout_value = proc.stdout.read() + proc.stderr.read()
                            control1=stdout_value.decode().split("\r\n")
                            control2="\n".join(control1).rstrip()
                            await ctx.send("```"+control2+"```")


                        # !wm get control "text"
                        # output "text" "start/stop control" "reset control"


                # !wm get ???
                else:
                    print("  wm.get: invalid argument")
                    await ctx.send("[ERROR] wm.get: invalid argument given")
            # !wm get
            else:
                # no argument given
                print("  wm.get no argument given")
                await ctx.send("[ERROR] wm.get: not enough arguments")




        #elif len(args) > 0 and args[0].lower() == 'set':
        #    None




        elif len(args) > 0 and args[0].lower() == 'add':
            if len(args) > 1:
                # !wm add tab ()
                if args[1].lower() == 'tab':
                    None
                #elif args[1].lower() == '':
                #    None


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
