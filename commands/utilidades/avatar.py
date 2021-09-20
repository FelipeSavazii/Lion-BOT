import discord
from discord.ext import commands

color = 0xf79805
format = "%a, %d %b %Y | %H:%M:%S %ZGMT"


class Avatar(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, arg1: discord.Member = None):
        if arg1 == None:
          embed = discord.Embed(title="❌ Erro!", description="Use l.avatar <args>", color=color)
        else:
          try: 
            embed = discord.Embed(title=f"Avatar de {arg1}", description=" ", color=color)
            embed.set_image(url=arg1.avatar_url)
            await ctx.send(embed=embed)
          except:
            embed = discord.Embed(title="❌ Erro!", description="Use l.avatar <args>", color=color)
            await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Avatar(bot))