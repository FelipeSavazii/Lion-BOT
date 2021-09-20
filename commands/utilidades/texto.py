import discord
from discord.ext import commands
import random
import asyncio

color = 0xf79805

class Texto(commands.Cog):

    def __init__(self, bot):
      self.bot = bot

    @commands.command()
    async def texto(self, ctx, *, arg1=None):
      if arg1 == None:
        await ctx.send("Use: l.texto <texto>")
      else:
        x = arg1.replace(" ", "%20")
        img = f"http://fortnitefontgenerator.com/img.php?fontsize=66&textcolor=64B5F6&text={x}"
        embed = discord.Embed(title=f" ", description=f"📺 Clique [aqui]({img}) para baixar a imagem abaixo.", color=color)
        embed.set_image(url=img)
        embed.set_footer(text=f"Executado por {ctx.author}")
        await ctx.send(embed=embed)
      
def setup(bot):
    bot.add_cog(Texto(bot))