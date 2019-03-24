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
scriptdir = os.path.dirname(os.path.abspath(__file__))+"\\scripts\\"
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
    proc = subprocess.Popen(['C:\Program Files (x86)\AutoIt3\AutoIt3.exe',scriptdir+'startbot.au3'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

bot.load_extension("cogs.management")

'''
# Test commands to set the stage for later

@bot.command()
async def test_bat(ctx):
    print(scriptdir+'\test.bat')
    proc = subprocess.Popen([scriptdir+'test.bat'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
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

# start bot
bot.run(token)
