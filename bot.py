import config
import requests
import subprocess
from discord.ext import commands

#debug=config.config['DEBUG'].getint('debug')
localconfig = config.config['BOT']
token = config.config['BOT']['discordtoken']
prefix= config.config['BOT']['prefix']

# create Discord Client
bot = commands.Bot(command_prefix=prefix)
    
@bot.event
async def on_ready():
    print("Logged in as: ")
    print("Username: " + bot.user.name)
    print("ID: " + str(bot.user.id))
    print("-----")

@bot.command()
async def screenshot(ctx):
    # take screenshot
    # _ScreenCapture_Capture
    # sends file through webhook
    #await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))
    return 

# Test commands to set the stage for later, will be commented out
@bot.command()
async def test_autoit(ctx):
    proc = subprocess.Popen(['C:\Program Files (x86)\AutoIt3\AutoIt3.exe','autoit.au3'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout_value = proc.stdout.read() + proc.stderr.read()
    return

@bot.command()
async def test_python(ctx):
    # python.exe based ones on PATH don't need full path
    proc = subprocess.Popen(['python.exe','test.py'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout_value = proc.stdout.read() + proc.stderr.read()
    await ctx.send(stdout_value)

# this is actually unsafe to have
'''
@bot.command()
async def cmd(ctx,*args):
    proc = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    stdout_value = proc.stdout.read() + proc.stderr.read()
    await ctx.send(stdout_value)
'''


# start bot
bot.run(token)




'''

@bot.command()
async def hello(ctx):  # registered command: `$hello`

    message_author = ctx.author
    message_channel = ctx.channel

    print("{} said hello".format(message_author))
    await message_channel.send("Hello, {}!".format(message_author.name))

'''
