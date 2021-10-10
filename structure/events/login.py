import discord
from discord import bot
from discord.ext import commands

color = discord.Color.gold()

class Login(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = self.bot.get_channel(896617707494080612)
        embed = discord.Embed(title='🦁 LION BOT', description=f'Aplicação online.', color=color)
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Login(bot))