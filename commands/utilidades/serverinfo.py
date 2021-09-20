import discord
from discord.ext import commands

color = 0xf79805
format = "%a, %d %b %Y | %H:%M:%S %ZGMT"


class Serverinfo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverinfo(self, ctx):
        nome = str(ctx.guild.name)
        dono = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        regiao = str(ctx.guild.region)
        contagemdemembros = str(ctx.guild.member_count)
        numerodecargos = len(ctx.guild.roles)
        listadebots = [bot.mention for bot in ctx.guild.members if bot.bot]
        canaisdetexto = len(ctx.guild.text_channels)
        canaisdevoz = len(ctx.guild.voice_channels)
        categorias = len(ctx.guild.categories)

        icon = str(ctx.guild.icon_url)

        if str(ctx.guild.verification_level) == "none":
            embed = discord.Embed(title="💻 Informações do servidor.\n",
                                  description=f"\n**{nome}**\n\n"
                                              f"**Dono**: {dono}\n"
                                              f"**Server ID**: {id}\n"
                                              f"**Região**: {regiao}\n"
                                              f"**Membros**: {contagemdemembros}\n"
                                              f"**Nivel de verificação**: Desativado\n"
                                              f"**Bots**: {(', '.join(listadebots))}\n"
                                              f"**Criado em**: {ctx.guild.created_at.strftime(format)}\n"
                                              f"**Número de cargos**: {str(numerodecargos)}\n"
                                              f" **Canais de texto:** {canaisdetexto}\n"
                                              f" **Canais de voz:** {canaisdevoz}\n"
                                              f" **Categorias:** {categorias}",
                                  color=color)
        else:
            embed = discord.Embed(title="💻 Informações do servidor.",
                                  description=f"{nome}\n"
                                              f"**Dono**: {dono}\n"
                                              f"**Server ID**: {id}\n"
                                              f"**Região**: {regiao}\n"
                                              f"**Membros**: {contagemdemembros}\n"
                                              f"**Nivel de verificação**: {str(ctx.guild.verification_level)}\n"
                                              f"**Bots**: {(', '.join(listadebots))}\n"
                                              f"**Criado em**: {ctx.guild.created_at.strftime(format)}\n"
                                              f"**Número de cargos**: {str(numerodecargos)}\n"
                                              f" **Canais de texto:** {canaisdetexto}\n"
                                              f" **Canais de voz:** {canaisdevoz}\n"
                                              f" **Categorias:** {categorias}",
                                  color=color)

        embed.set_thumbnail(url=icon)
        embed.set_footer(text=f"Executado por {ctx.author}")

        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Serverinfo(bot))