import discord
from discord.ext import commands
import random
import asyncio

color = 0xf79805

class Olhaso(commands.Cog):

    def __init__(self, bot):
      self.bot = bot

    @commands.command()
    async def olhaso(self, ctx, *, arg1=None):
      if arg1 == None:
        await ctx.send("Use: l.olhaso <texto>")
      else:
        x = arg1.replace(" ", "%20")
        img = f"https://eursonom.sirv.com/olhasomeme.png?text.0.text={x}&text.0.position.gravity=center&text.0.size=24"
        embed = discord.Embed(title=f" ", color=color)
        embed.set_image(url=img)
        embed.set_footer(text=f"Executado por {ctx.author}")
        await ctx.send(embed=embed)
      
def setup(bot):
    bot.add_cog(Olhaso(bot))