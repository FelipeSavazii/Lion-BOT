import discord
from discord.ext import commands

color = 0xf79805
format = "%a, %d %b %Y | %H:%M:%S %ZGMT"


class FelipeBruno(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def felipe(self, ctx, *, arg1=None):
      if arg1 == None:
        await ctx.send("Use: l.felipe <texto>")
      else:
        x = arg1.replace(" ", "%20")
        img = f"https://eursonom.sirv.com/lion.png?text.0.text={x}&text.0.position.gravity=south&text.0.size=20&text.0.color=ffffff"
        embed = discord.Embed(title=f" ", color=color)
        embed.set_image(url=img)
        embed.set_footer(text=f"Executado por {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command()
    async def bruno(self, ctx, *, arg1=None):
      if arg1 == None:
        await ctx.send("Use: l.bruno <texto>")
      else:
        x = arg1.replace(" ", "%20")
        img = f"https://atchottl.sirv.com/Lion%20BOT/12-35-16.png?text.0.text={x}&text.0.position.x=-64%25&text.0.position.y=-84%25&text.0.size=34&text.0.color=000000"
        embed = discord.Embed(title=f" ", color=color)
        embed.set_image(url=img)
        embed.set_footer(text=f"Executado por {ctx.author}")
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(FelipeBruno(bot))