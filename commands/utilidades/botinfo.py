import discord
from discord.ext import commands

color = 0xf79805

class Botinfo(commands.Cog):

    def __init__(self, bot):
      self.bot = bot

    @commands.command()
    async def botinfo(self, ctx):
        gerador = self.bot.get_all_channels()
        lista = list(gerador)
        canais = len(lista)
        print(lista)
        uptime = str(datetime.timedelta(seconds=int(round(time.time() - startTime))))
        embed = discord.Embed(title=" ",
                              description=f"🤖 **Informações do bot:**\n\nOlá {ctx.author}! Aqui você encontrará "
                                          f"algumas informações sobre mim. Meu prefixo é `l.` e sinta-se à vontade "
                                          f"para dar sugestões sobre meu desenvolvimento e usar meus comandos.\n\n"
                                          f"**Estatisticas:**\n\n"
                                          f"**Servidores:** {len(self.bot.guilds)}\n"
                                          f"**Usuários:** {len(self.bot.users)}\n"
                                          f"**Canais:** {canais}\n"
                                          f"**Ping:** {int(bot.latency * 1000)}ms\n"
                                          f"**Uptime:** {uptime}\n\n"
                                          f"**Informações:**\n\n"
                                          f"**Criado em:** 7 de setembro de 2021\n"
                                          f"**Criador:** Felipe Savazi#9407\n"
                                          f"**Linguagem:** Python\n"
                                          f"**Versão:** v0.0.1", color=color)
        embed.set_footer(text=f"Executado por {ctx.author}")
        await ctx.send(embed=embed)
      
def setup(bot):
    bot.add_cog(Botinfo(bot))