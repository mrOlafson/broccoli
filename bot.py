import discord
from discord import Game
from discord.ext import commands
import asyncio
import requests
import os
import random


TOKEN = 'NTA0NTY4NjczMjk4Njc3NzYx.DrG8Yw.vwN_QJ99hthAOjuazOKwqvsas88'

client = commands.Bot(command_prefix = '§.')
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="use §.")) 
    print('READY')
    print('--------')

@client.command()
async def foo():
    await client.say("bar")

@client.command(pass_context=True)
async def setup(ctx):
    await bot.say('`Not in use')



client.run(TOKEN)

