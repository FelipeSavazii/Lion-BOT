import discord
from discord.ext import commands

color = 0xf79805

class Joebiden(commands.Cog):

    def __init__(self, bot):
      self.bot = bot

    @commands.command()
    async def joebiden(ctx, *, arg1=None):
        if arg1 == None:
            await ctx.send("Use: l.joebiden <args>")
        else:
            x = arg1.replace(" ", "+")
            font = f"https://gofaizen.sirv.com/Joe%20Biden%20Tweet.jpeg?w=900&h=900&text.0.text={x}&text.0.position.x=-55%25&text.0.position.y=-64%25&text.0.size=32&text.0.color=000000&text.0.font.weight=700"
            channel = ctx.channel
            embed = discord.Embed(title=f'🐦 Twitter de Joe Biden',
                                  description=f'Clique [aqui]({font}) para baixar a foto do Twitter de Joe Biden.',
                                  color=color)
            embed.set_image(url=font)
            embed.set_footer(text=f"Executado por {ctx.author}")
            await channel.send(embed=embed)
      
def setup(bot):
    bot.add_cog(Joebiden(bot))