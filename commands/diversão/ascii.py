import discord
from discord.ext import commands
import aiohttp

color = 0xf79805

class Ascii(commands.Cog):

    def __init__(self, bot):
      self.bot = bot

    @commands.command()
    async def ascii(self, ctx, *, arg1=None):
        if arg1 == None:
            await ctx.send("Use: l.ascii <args>")
        else:
            x = arg1.replace(" ", "+")
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://artii.herokuapp.com/make?text={x}') as response:
                    teste = await response.text()
                    await ctx.send(f"```{teste}```")
                    await ctx.send(f"Executado por: {ctx.author}")
      
def setup(bot):
    bot.add_cog(Ascii(bot))