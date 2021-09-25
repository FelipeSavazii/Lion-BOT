import asyncio
import datetime
import time

import os
import re

import aiohttp
import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="l.", intents=discord.Intents.all())
color = 0xf79805

for root, _, files in os.walk('commands'):
    for file in files:
        path = os.path.join(root, file)

        if not os.path.isfile(path):
            continue

        path, ext = os.path.splitext(path)
        if ext != '.py':
            continue

        extension = re.sub('\\\\|\/', '.', path)

        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Falha ao carregar {extension}. ({e})')
        else:
            print(f'{extension} carregado com sucesso.')


@bot.event
async def on_ready():
    channel = bot.get_channel(833158979659104263)
    print('Online')
    global startTime
    startTime = time.time()
    bot.remove_command('help')
    embed = discord.Embed(title="Estou online!", description=f" ", color=color)
    await channel.send(embed=embed)
    while True:
        await bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="use l.ajuda"))
        await asyncio.sleep(5)
        await bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name=f"{len(bot.guilds)} servidores"))
        await asyncio.sleep(5)
        await bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="o meu desenvolvimento"))
        await asyncio.sleep(5)
        await bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="use l.invite"))
        await asyncio.sleep(5)
        await bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening,
                name='sabia que fui criado pelo Felipe Savazi#9407?'))
        await asyncio.sleep(6)

@bot.command()
async def ping(ctx):
    embed = discord.Embed(title="🏓 PING", description=f"**Minha latência é {int(bot.latency * 1000)}ms**", color=color)
    embed.set_footer(text=f"Executado por {ctx.author}")
    await ctx.send(embed=embed)


@bot.command()
async def uptime(ctx):
    uptime = str(datetime.timedelta(seconds=int(round(time.time() - startTime))))
    embed = discord.Embed(title="⏲️ UPTIME", description=f"**Estou acordado há {uptime}**", color=color)
    embed.set_footer(text=f"Executado por {ctx.author}")
    await ctx.send(embed=embed)
    
@bot.command()
@commands.is_owner()
async def reload(ctx):
    embed = discord.Embed(title="🔄 RELOAD", color=color)  
    for root, _, files in os.walk('commands'):
        for file in files:
            path = os.path.join(root, file)

            if not os.path.isfile(path):
                continue

            path, ext = os.path.splitext(path)
            if ext != '.py':
                continue

            extension = re.sub('\\\\|\/', '.', path)
            try:
                bot.reload_extension(extension) 
                embed.add_field(name='\u200b', value=f'Carregada com sucesso: {extension}.', inline=False)
            except Exception as e:
                embed.add_field(name='\u200b', value=f'Falha ao carregar: {extension}. ({e})', inline=False)
            embed.set_footer(text=f"Executado por {ctx.author}")
    await ctx.send(embed=embed)

bot.run(TOKEN)
