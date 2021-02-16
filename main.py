import discord
from discord.ext import commands
from discord import *
import random
from random import choice
import os
rec_films = []
w_films = []
intents = discord.Intents.default()
client = commands.Bot(command_prefix='!', intents=intents)
@client.command()
async def add(ctx,*,content:str):
    rec_films.append(content)
    print(rec_films)
    await ctx.send('Äîáàâëåíî!')
@client.command()
async def wat(ctx,*,content:str):
    if content in rec_films:
        rec_films.remove(content)
        w_films.append(content)
        print(rec_films)
        print(w_films)
        await ctx.send("Ïåðåìåùåíî")
    else:
        await ctx.send("Òàêîãî ôèëüìà íåòó â ñïèñêå")
@client.command()
async def spisok_r(ctx):
    await ctx.send(str(rec_films))
@client.command()
async def spisok_w(ctx):
    await ctx.send(str(w_films))
@client.command()
async def recommend(ctx):
    await ctx.send(random.choice(rec_films))
token = os.environ.get('BOT_TOKEN')
client.run(token)
