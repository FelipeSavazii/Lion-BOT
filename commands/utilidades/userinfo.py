import discord
from discord.ext import commands

color = 0xf79805
format = "%a, %d %b %Y | %H:%M:%S %ZGMT"


class Userinfo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        channel = ctx.channel
        date_format = "%a, %d %b %Y %I:%M %p"

        if member is None:
            id = ctx.author.id
            accountcreate = ctx.author.created_at.strftime(date_format)
            join = ctx.author.joined_at.strftime(date_format)
            embed = discord.Embed(title=f"📚 Informações de {ctx.author.name}.", description=f"**User ID:** {id}\n"
                                                                                             f"**Entrou aqui em:** {join}\n"
                                                                                             f"**Conta criada em:** {accountcreate}",
                                  color=color)
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_footer(text=f"Executado por {ctx.author}")

            await channel.send(embed=embed)

        else:
            id = member.id
            accountcreate = member.created_at.strftime(date_format)
            join = member.joined_at.strftime(date_format)
            embed = discord.Embed(title=f"📚 Informações de {member.name}.", description=f"**User ID:** {id}\n"
                                                                                         f"**Entrou aqui em:** {join}\n"
                                                                                         f"**Conta criada em:** {accountcreate}",
                                  color=color)
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text=f"Executado por {ctx.author}")

            await channel.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Userinfo(bot))