import config
import utils
import requests
import subprocess
import os
import sys
import discord
import pyautogui
from discord.ext import commands

localconfig = config.config['BOT']
cwd = os.path.dirname(os.path.abspath(__file__))+"\\scripts\\"
token = config.config['BOT']['discordtoken']
prefix= config.config['BOT']['prefix']

# create Discord Client
bot = commands.Bot(command_prefix=prefix)
    
@bot.event
async def on_ready():
    print("Logged in")
    print("Username: " + bot.user.name)
    print("ID: " + str(bot.user.id))
    print("-----")
    proc = subprocess.Popen(['C:\Program Files (x86)\AutoIt3\AutoIt3.exe',cwd+'startbot.au3'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

# MANAGEMENT COMMANDS

@bot.command()
async def restart(ctx):
    # restarts script, not watchme
	#os.execv(sys.executable, ['python'] + sys.argv)
    #await bot.logout()
    #proc = subprocess.call([sys.executable, "bot.py"])
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

# INTRO COMMANDS

@bot.command()
async def runwatchme(ctx):
    # starts watchme
    proc = subprocess.Popen([cwd+'runwatchme.bat'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    # send something when completed?
    return

@bot.command()
async def screenshot(ctx):
    s=pyautogui.screenshot('screenshots/screenshot.png')
    with open('screenshots/screenshot.png','rb') as fp:
        await ctx.send(file=discord.File(fp,'screenshot.png'))

# WATCH ME COMMANDS

    

'''
# Test commands to set the stage for later

@bot.command()
async def test_bat(ctx):
    print(cwd+'\test.bat')
    proc = subprocess.Popen([cwd+'test.bat'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout_value = proc.stdout.read() + proc.stderr.read()
    await ctx.send(stdout_value)

@bot.command()
async def test_autoit(ctx):
    proc = subprocess.Popen(['C:\Program Files (x86)\AutoIt3\AutoIt3.exe','test.au3'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout_value = proc.stdout.read() + proc.stderr.read()
    return

@bot.command()
async def test_python(ctx):
    # python.exe based ones on PATH don't need full path
    proc = subprocess.Popen(['python.exe','test.py'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout_value = proc.stdout.read() + proc.stderr.read()
    await ctx.send(stdout_value)

# this is actually unsafe to have

@bot.command()
async def cmd(ctx,*args):
    proc = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    stdout_value = proc.stdout.read() + proc.stderr.read()
    await ctx.send(stdout_value)
'''

'''
@bot.command()
async def gitpull(ctx):
    proc = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
'''


# start bot
bot.run(token)
