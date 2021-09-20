import discord
from discord.ext import commands

color = 0xf79805
format = "%a, %d %b %Y | %H:%M:%S %ZGMT"


class Invite(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx):
      embed = discord.Embed(title=" ", description=f"📃 **Meu convite**\n\n Clique [aqui](https://discord.com/api/oauth2/authorize?client_id=858380932187947049&permissions=8&scope=bot) para me adicionar.\nClique [aqui](https://discord.gg/KSvuX2fpCn) para entrar no servidor meu servidor de suporte.", color=color)
      embed.set_footer(text=f"Executado por {ctx.author}")
      await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Invite(bot))