import discord
from discord.ext import commands

color = 0xf79805
format = "%a, %d %b %Y | %H:%M:%S %ZGMT"


class Goku(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def goku(self, ctx, *, arg1=None):
      if arg1 == None:
        await ctx.send("Use: l.goku <texto>")
      else:
        x = arg1.replace(" ", "%20")
        img = f"https://eursonom.sirv.com/goku.jpg?profile=Example&text.0.text={x}&text.0.position.gravity=southwest&text.0.size=16&text.0.color=000000"
        embed = discord.Embed(title=f" ", color=color)
        embed.set_image(url=img)
        embed.set_footer(text=f"Executado por {ctx.author}")
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Goku(bot))