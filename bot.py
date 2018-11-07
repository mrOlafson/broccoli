import discord
from discord import Game
from discord.ext import commands
from discord.utils import get
import asyncio
import requests
import os
import random


TOKEN = 'NTA0NTY4NjczMjk4Njc3NzYx.DrG8Yw.vwN_QJ99hthAOjuazOKwqvsas88'

client = commands.Bot(command_prefix = '+')
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="He comes")) 
    print('READY')
    print('--------')


@client.event
async def on_message(message):
    if message.content.startswith("br. "):
        x = message.content
        x = x.replace("br. ", "https://nhentai.net/g/")
        await client.send_message(message.channel,x + "/")
    await client.process_commands(message)


@client.event
async def on_message(message):
    if message.content == '§.foo':
        await client.send_message(message.channel, 'bar')

    elif message.content.startswith("pu.game "):
        x = message.content
        x = x.replace("pu.game ", "")
        await client.change_presence(game=Game(name=x))
    await client.process_commands(message)


@client.event
async def on_message(message):
    if 'puchiko' in message.content:
        x = random.randint(0, 2)
        if x == 0:
            print('NYU 0')
            await client.send_message(message.channel, "It's 'Broccoli', not 'Puchiko', nyu.")
        elif x == 1:
            print('NYU 1')
            await client.send_message(message.channel, "You're terrible at listening, nyu.")
        elif x == 2:
            print('NYU 2')
            await client.send_message(message.channel, "Of course you would do that. After all, it is you.")
        elif x == 3:
            print('NYU 3')
            await client.send_message(message.channel, "3")
    await client.process_commands(message)





    
client.run(TOKEN)

