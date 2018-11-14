import discord
from discord import Game
from discord.ext import commands
from discord.utils import get
import asyncio
import requests
import os
import random
import string
from random import randint


TOKEN = 'NTA0NTY4NjczMjk4Njc3NzYx.DrG8Yw.vwN_QJ99hthAOjuazOKwqvsas88'

client = commands.Bot(command_prefix = '+')
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Oh no.")) 
    print('READY')
    print('--------')



@client.event
async def on_message(message):
    if message.content.startswith("ht. "):
        x = message.content
        x = x.replace("ht. ", "https://nhentai.net/g/")
        await client.send_message(message.channel,x + "/")

    elif message.content.startswith("rd."):
        x = randint(1, 999999)
        await client.send_message(message.channel, "https://nhentai.net/g/" + str(x) + "/")

    elif message.content.startswith("pu.game "):
       x = message.content
       x = x.replace("pu.game ", "")
       await client.change_presence(game=Game(name=x))
    await client.process_commands(message)



    
client.run(TOKEN)

