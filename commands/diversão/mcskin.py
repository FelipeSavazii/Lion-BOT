import discord
from discord.ext import commands

color = 0xf79805

class Mcskin(commands.Cog):

    def __init__(self, bot):
      self.bot = bot

    @commands.command()
    async def mcskin(self, ctx, arg1):
      if arg1 == None:
          await ctx.send("Use: l.mcskin <nickname>")
      else:
          x = arg1.replace(" ", "+")
          skin = f"https://www.mc-heads.net/body/{x}/right?width=112&height=269"
          embed = discord.Embed(title=f'👱 Skin de {arg1}',
                                description=f'Clique [aqui]({skin}) para baixar a skin do mesmo.',
                                color=color)
          embed.set_image(url=skin)
          embed.set_footer(text=f"Executado por {ctx.author}")
          await ctx.send(embed=embed)  
          
def setup(bot):
    bot.add_cog(Mcskin(bot))