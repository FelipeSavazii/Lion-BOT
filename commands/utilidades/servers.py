import discord
from discord.ext import commands

color = 0xf79805
format = "%a, %d %b %Y | %H:%M:%S %ZGMT"


class Servers(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def servers(self, ctx):
        serversinfo = len(self.bot.guilds)
        embed = discord.Embed(title=" ", description=f'Atualmente eu estou em {serversinfo} servidores.', color=color)
        embed.set_footer(text=f"Executado por {ctx.author}")
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Servers(bot))