import discord
from discord import bot
from discord.ext import commands

color = discord.Color.gold()

class Logout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def logout(self, ctx):
        channel = self.bot.get_channel(896617707494080612)
        embed = discord.Embed(title='🦁 LION BOT', description=f'Aplicação offline.', color=color)
        await channel.send(embed=embed)
        await self.bot.close()

def setup(bot):
    bot.add_cog(Logout(bot))