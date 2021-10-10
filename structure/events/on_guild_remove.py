import discord
from discord import bot
from discord.ext import commands

from datetime import datetime

color = discord.Color.gold()

class OnGuildRemove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        channel = self.bot.get_channel(896617707494080612)
        embed = discord.Embed(title='🦁 LION BOT', description=f'Fui removido do servidor: {guild.name}.', color=color)
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(OnGuildRemove(bot))