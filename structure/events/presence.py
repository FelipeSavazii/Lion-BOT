import discord
from discord import bot
from discord.ext import commands

import asyncio

class Presence(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        while True:
            await self.bot.change_presence(
                activity=discord.Activity(type=discord.ActivityType.watching, name="use l.ajuda"))
            await asyncio.sleep(5)

            await self.bot.change_presence(
                activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(self.bot.guilds)} servidores"))
            await asyncio.sleep(5)

            await self.bot.change_presence(
                activity=discord.Activity(type=discord.ActivityType.watching, name="o meu desenvolvimento"))
            await asyncio.sleep(5)

            await self.bot.change_presence(
                activity=discord.Activity(type=discord.ActivityType.watching, name="use l.invite"))
            await asyncio.sleep(5)

            await self.bot.change_presence(
                activity=discord.Activity(type=discord.ActivityType.listening, name='sabia que fui criado pelo Felipe Savazi#9407?'))
            await asyncio.sleep(5)

def setup(bot):
    bot.add_cog(Presence(bot))