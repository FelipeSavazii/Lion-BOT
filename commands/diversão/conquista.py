import discord
from discord.ext import commands
import random

color = 0xf79805

class Conquista(commands.Cog):

    def __init__(self, bot):
      self.bot = bot

    @commands.command()
    async def conquista(self, ctx, *, texto=None):
        if texto == None:
            await ctx.send("Use: l.conquista <texto>")
        else:
            x = texto.replace(" ", "%20")
            sorteio_1_39 = random.randint(1, 39)
            imagem = f"https://minecraftskinstealer.com/achievement/{sorteio_1_39}/Nova+conquista%21/{x}"
            channel = ctx.channel
            embed = discord.Embed(title=f'🏆 Conquista',
                                  description=f'Clique [aqui]({imagem}) para baixar a foto da conquista.',
                                  color=color)
            embed.set_image(url=imagem)
            embed.set_footer(text=f"Executado por {ctx.author}")
            await channel.send(embed=embed)
      
def setup(bot):
    bot.add_cog(Conquista(bot))