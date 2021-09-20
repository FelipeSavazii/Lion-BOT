import discord
from discord.ext import commands

color = 0xf79805

class Mchead(commands.Cog):

    def __init__(self, bot):
      self.bot = bot
      
    @commands.command()
    async def mchead(self, ctx, arg1):
      if arg1 == None:
          await ctx.send("Use: l.mchead <nickname>")
      else:
          x = arg1.replace(" ", "+")
          skin = f"https://www.mc-heads.net/head/{x}/right?width=112&height=269"
          embed = discord.Embed(title=f'👱 Cabeça de {arg1}',
                                description=f'Clique [aqui]({skin}) para baixar a cabeça do mesmo.',
                                color=color)
          embed.set_image(url=skin)
          embed.set_footer(text=f"Executado por {ctx.author}")
          await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Mchead(bot))