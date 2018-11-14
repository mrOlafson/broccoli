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
#import spice_api


TOKEN = 'NTA0NTY4NjczMjk4Njc3NzYx.DrG8Yw.vwN_QJ99hthAOjuazOKwqvsas88'

client = commands.Bot(command_prefix = 'pu.')
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="pu.help")) 
    print('READY')
    print('--------')

embed=discord.Embed(title="Help", description="nyu", color=0xff8000)
embed.add_field(name="-=Commands =-", value="(do not add () in the command)", inline=False)
embed.add_field(name="pu.ht (numbers)", value="outputs the demanded nhentai.net link  ", inline=False)
embed.add_field(name="pu.ht_rd", value="outputs a random nhenai.net link", inline=False)
embed.add_field(name="pu.cl (number)", value="deletes (number) messages (may take a moment)", inline=False)
embed.add_field(name="pu.bulkcl (number)", value="deletes (number) messages at once", inline=False)
embed.add_field(name="pu.invite", value="sends you an invitation link to add the bot", inline=False)
embed.set_footer(text="broccoli 1.0.1  |  made by SECoY#0181")


@client.command(pass_context = True)
async def cl(ctx, number):
    number = int(number) 
    counter = 0
    async for x in client.logs_from(ctx.message.channel, limit = number):
        if counter < number:
            await client.delete_message(x)
            counter += 1
            await asyncio.sleep(0.05) 
    await client.say("All done, nyu.")

@client.command(pass_context = True)
async def bulkcl(ctx, number):
    mgs = []
    number = int(number)
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)
    await client.say("All done, nyu.")



@client.event
async def on_message(message):
    if message.content.startswith("pu.ht "):
        x = message.content
        x = x.replace("pu.ht ", "https://nhentai.net/g/")
        await client.send_message(message.channel,x + "/")

    elif message.content.startswith("pu.ht_rd"):
        x = randint(1, 999999)
        await client.send_message(message.channel, "https://nhentai.net/g/" + str(x) + "/")

    elif message.content.startswith("pu.game "):
       x = message.content
       x = x.replace("pu.game ", "")
       await client.change_presence(game=Game(name=x))

    elif message.content.startswith("pu.help"):
        await client.send_message(message.author,embed=embed)

    elif message.content.startswith("pu!goodbye"):
        if (message.author.id =='223111553891827722'):
            await client.close()
            os.system("python3 puchi.py")
        elif (message.author.id !='223111553891827722'):
            y = message.content
    elif message.content.startswith("pu.mal "):
        y = a
            
    elif message.content.startswith("pu.invite"):
         await client.send_message(message.author, "https://bit.ly/2B5wfaV")

    await client.process_commands(message)



    
client.run(TOKEN)

