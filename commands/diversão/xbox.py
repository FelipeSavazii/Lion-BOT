import discord
from discord.ext import commands

color = 0xf79805

class Xbox(commands.Cog):

    def __init__(self, bot):
      self.bot = bot

    @commands.command()
    async def xbox(ctx, *, arg1=texto):
        if texto == None:
            await ctx.send("Use: l.xbox <texto>")
        else:
            x = texto.replace(" ", "%20")
            imagem = f"http://www.achievement-maker.com/xbox/{x}%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20?header=CONQUISTA%20DESBLOQUEADA&email=savazifelipe@hotmail.com.png"
            channel = ctx.channel
            embed = discord.Embed(title=f'🏆 Conquista no xbox',
                                  description=f'Clique [aqui]({imagem}) para baixar a foto da conquista de xbox.',
                                  color=color)
            embed.set_image(url=font)
            embed.set_footer(text=f"Executado por {ctx.author}")
            await channel.send(embed=embed)
      
def setup(bot):
    bot.add_cog(Xbox(bot))