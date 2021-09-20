import discord
from discord.ext import commands

color = 0xf79805

class Captcha(commands.Cog):

    def __init__(self, bot):
      self.bot = bot

    @commands.command()
    async def captcha(ctx, *, texto=None):
        if texto == None:
            await ctx.send("Use: l.captcha <texto>")
        else:
            x = texto.replace(" ", "+")
            imagem = f"https://api.cool-img-api.ml/captcha?text={x}"
            channel = ctx.channel
            embed = discord.Embed(title=f'🤖 Você é um robo?',
                                  description=f'Clique [aqui]({imagem}) para baixar a foto do capcha.',
                                  color=color)
            embed.set_image(url=imagem)
            embed.set_footer(text=f"Executado por {ctx.author}")
            await channel.send(embed=embed)
      
def setup(bot):
    bot.add_cog(Captcha(bot))