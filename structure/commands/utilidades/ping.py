import discord
from discord import bot
from discord.ext import commands
from discord.app import slash_command

color = discord.Color.gold()

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(title="🏓 PING", description=f"Minha latência é **{int(self.bot.latency * 1000)}ms**", color=color)
        embed.set_footer(text=f"Executado por {ctx.author}")
        await ctx.send(embed=embed)

class PingSlash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def ping(self, ctx):
        embed = discord.Embed(title="🏓 PING", description=f"Minha latência é **{int(self.bot.latency * 1000)}ms**", color=color)
        embed.set_footer(text=f"Executado por {ctx.author}")
        await ctx.respond(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(Ping(bot))
    bot.add_cog(PingSlash(bot))
