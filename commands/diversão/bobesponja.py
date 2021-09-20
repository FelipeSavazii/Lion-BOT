import discord
from discord.ext import commands

color = 0xf79805

class Bobesponja(commands.Cog):

    def __init__(self, bot):
      self.bot = bot
      
    @commands.command()
    async def bobesponja(ctx, *, texto=None):
        if texto == None:
            await ctx.send("Use: l.bobesponja <texto>")
        else:
            x = texto.replace(" ", "+")
            imagem = f"https://frenchnoodles.xyz/api/endpoints/spongebobburnpaper/?text={x}"
            channel = ctx.channel
            embed = discord.Embed(title=f'🧽 O Bob Esponja não gostou da sua carta e usou ela como lenha da fogueira',
                                  description=f'Clique [aqui]({imagem}) para baixar a foto do Bob Esponja.',
                                  color=color)
            embed.set_image(url=imagem)
            embed.set_footer(text=f"Executado por {ctx.author}")
            await channel.send(embed=embed)
      
def setup(bot):
    bot.add_cog(Bobesponja(bot))