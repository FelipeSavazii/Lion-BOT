import discord
from discord.ext import commands

color = 0xf79805

class Laranjo(commands.Cog):

    def __init__(self, bot):
      self.bot = bot

    @commands.command()
    async def laranjo(self, ctx, *, arg1=None):
      if arg1 == None:
        await ctx.send("Use: l.laranjo <texto>")
      else:
        x = arg1.replace(" ", "%20")
        img = f"https://atchottl.sirv.com/Lion%20BOT/laranjo-meme-cke.jpg?profile=Example&text.0.text={x}&text.0.position.gravity=southwest&text.0.size=16&text.0.color=000000" 
        embed = discord.Embed(title=f" ", color=color)
        embed.set_image(url=img)
        embed.set_footer(text=f"Executado por {ctx.author}")
        await ctx.send(embed=embed)
      
def setup(bot):
    bot.add_cog(Laranjo(bot))