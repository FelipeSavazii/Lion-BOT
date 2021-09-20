import discord
from discord.ext import commands
import asyncio

color = 0xf79805
format = "%a, %d %b %Y | %H:%M:%S %ZGMT"


class Ajuda(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ajuda(self, ctx):
        pagina = 5
        pag_atual = 1
        embed1 = discord.Embed(title="💡 PAINEL DE AJUDA", description=f"Aqui você poderá encontrar informações essenciais para a utilização do mesmo. O prefixo do bot é \"l.\", aproveite!\n\nAo reagir com ▶️ você irá para a próxima página e ao reagir com ◀️ você voltará uma página em relação a atual. (OBS: Você está na página incial.)", color=color)
        
        embed2 = discord.Embed(title=f"💡 PAINEL DE AJUDA - UTILIDADES", description=f"```\navatar\nbotinfo\nenquete\ninvite\nping\nsay\nserverinfo\nservers\ntexto\nuptime\nuserinfo```", color=color)

        embed3 = discord.Embed(title=f"💡 PAINEL DE AJUDA - MODERAÇÃO", description=f"```\nclear```", color=color)

        embed4 = discord.Embed(title=f"💡 PAINEL DE AJUDA - DIVERSÃO", description=f"```\nascii\nbobesponja\nbolsonaro\nbruno\ncaptcha\nconquista\ndeitar\nejetar\nfelipe\njoebiden\nlaranjo\nlevantar\nmchead\nmcskin\nolhaso\nsentar\nsentar\nxbox```", color=color)

        embed5 = discord.Embed(title=f'💡 PAINEL DE AJUDA - MÚSICA', description=f'```\njoin\nleave\nlyrics\npause\nplay\nqueue\nremove\nresume\nskip\nvolume```\n\nPágina 5/{pagina}')
        embed1.set_footer(text=f"Página {pag_atual}/{pagina} ┋ Executado por {ctx.author}")
        embed2.set_footer(text=f"Página {pag_atual}/{pagina} ┋ Executado por {ctx.author}")
        embed3.set_footer(text=f"Página {pag_atual}/{pagina} ┋ Executado por {ctx.author}")
        embed4.set_footer(text=f"Página {pag_atual}/{pagina} ┋ Executado por {ctx.author}")
        embed5.set_footer(text=f"Página {pag_atual}/{pagina} ┋ Executado por {ctx.author}")
        message = await ctx.send(embed=embed1)

        await message.add_reaction("◀️")
        await message.add_reaction("▶️")

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=60, check=check)

                if str(reaction.emoji) == "▶️" and pag_atual != pagina:
                    pag_atual += 1
                    if pag_atual == 1:
                      await message.edit(embed=embed1)
                    elif pag_atual == 2:
                      await message.edit(embed=embed2)
                    elif pag_atual == 3:
                      await message.edit(embed=embed3)
                    elif pag_atual == 4:
                      await message.edit(embed=embed4)
                    elif pag_atual == 5:
                      await message.edit(embed=embed5)

                    await message.remove_reaction(reaction, user)

                elif str(reaction.emoji) == "◀️" and pag_atual > 1:
                    pag_atual -= 1
                    if pag_atual == 1:
                      await message.edit(embed=embed1)
                    elif pag_atual == 2:
                      await message.edit(embed=embed2)
                    elif pag_atual == 3:
                      await message.edit(embed=embed3)
                    elif pag_atual == 4:
                      await message.edit(embed=embed4)
                    elif pag_atual == 5:
                      await message.edit(embed=embed5)

                    await message.remove_reaction(reaction, user)

                else:
                    await message.remove_reaction(reaction, user)
            except asyncio.TimeoutError:
                await message.delete()
                break

def setup(bot):
    bot.add_cog(Ajuda(bot))