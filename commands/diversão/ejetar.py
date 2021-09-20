import discord
from discord.ext import commands

color = 0xf79805

class Ejetar(commands.Cog):

    def __init__(self, bot):
      self.bot = bot

    @commands.command()
    async def ejetar(ctx):
        asd = str(ctx.author.name)
        x = asd.replace(" ", "+")
        font = f"https://nelesupe.sirv.com/42%20Sem%20T%C3%ADtulo_20201201015413.png?text.0.text={x}%20foi+ejetado.&text.0.position.x=-19%25&text.0.position.y=-40%25&text.0.size=40&text.0.color=ffffff&text.0.outline.blur=100.gif"
        print(asd)
        channel = ctx.channel
        embed = discord.Embed(title=f'🚀 Você foi ejetado',
                              description=f'Clique [aqui]({font}) para baixar a foto tirada da estação espacial.',
                              color=color)
        embed.set_image(url=font)
        embed.set_footer(text=f"Executado por {ctx.author}")
        await channel.send(embed=embed)
      
def setup(bot):
    bot.add_cog(Ejetar(bot))