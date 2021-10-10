import discord
from discord import bot
from discord.ext import commands
from discord.app import slash_command

import datetime
import time

color = discord.Color.gold()

class Uptime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        global startTime
        startTime = time.time()

    @commands.command()
    async def uptime(self, ctx):
        uptime = str(datetime.timedelta(seconds=int(round(time.time() - startTime))))
        embed = discord.Embed(title="⏲️ UPTIME", description=f"Estou acordado há **{uptime}**.", color=color)
        embed.set_footer(text=f"Executado por {ctx.author}")
        await ctx.send(embed=embed)

class UptimeSlash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def uptime(self, ctx):
        uptime = str(datetime.timedelta(seconds=int(round(time.time() - startTime))))
        embed = discord.Embed(title="⏲️ UPTIME", description=f"Estou acordado há **{uptime}**.", color=color)
        embed.set_footer(text=f"Executado por {ctx.author}")
        await ctx.respond(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(Uptime(bot))
    bot.add_cog(UptimeSlash(bot))
