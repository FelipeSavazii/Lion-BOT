import discord
from discord.ext import commands

color = 0xf79805

class Bolsonaro(commands.Cog):

    def __init__(self, bot):
      self.bot = bot

    @commands.command()
    async def bolsonaro(self, ctx, *, texto=None):
      if texto == None:
        await ctx.send("Use: l.bolsonaro <texto>")
      else:
        x = arg1.replace(" ", "%20")
        imagem = f"https://eursonom.sirv.com/bolsonaro_t.png?text.0.text={x}&text.0.position.x=-30%25&text.0.position.y=-54%25&text.0.size=20&text.0.color=000000"
        embed = discord.Embed(title=f" ", color=color)
        embed.set_image(url=imagem)
        embed.set_footer(text=f"Executado por {ctx.author}")
        await ctx.send(embed=embed) 
      
def setup(bot):
    bot.add_cog(Bolsonaro(bot))