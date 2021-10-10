import discord
from discord import bot
from discord.ext import commands
from discord.app import slash_command

import time
import datetime

color = discord.Color.gold()

class BotInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        global startTime
        startTime = time.time()

    @commands.command()
    async def botinfo(self, ctx):
        gerador = self.bot.get_all_channels()
        lista = list(gerador)
        canais = len(lista)
        print(lista)
        uptime = str(datetime.timedelta(seconds=int(round(time.time() - startTime))))
        embed = discord.Embed(title="🤖 INFORMAÇÕES DO BOT:", description=f"Olá {ctx.author}! Aqui você encontrará "
                                          f"algumas informações sobre mim. Meu prefixo é `l.` e sinta-se à vontade "
                                          f"para dar sugestões sobre meu desenvolvimento e usar meus comandos.\n\n"
                                          f"**ESTATISTICAS:**\n\n"
                                          f"**Servidores:** {len(self.bot.guilds)};\n"
                                          f"**Usuários:** {len(self.bot.users)};\n"
                                          f"**Canais:** {canais};\n"
                                          f"**Ping:** {int(self.bot.latency * 1000)}ms;\n"
                                          f"**Uptime:** {uptime}.\n\n"
                                          f"**INFORMAÇÕES:**\n\n"
                                          f"**Criado em:** 7 de setembro de 2021;\n"
                                          f"**Criador:** Felipe Savazi#9407;\n"
                                          f"**Linguagem:** Python;\n"
                                          f"**Versão:** v2.0.0.", color=color)
        embed.set_footer(text=f"Executado por {ctx.author}")
        await ctx.send(embed=embed)

class BotInfoSlash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def botinfo(self, ctx):
        gerador = self.bot.get_all_channels()
        lista = list(gerador)
        canais = len(lista)
        print(lista)
        uptime = str(datetime.timedelta(seconds=int(round(time.time() - startTime))))
        embed = discord.Embed(title="🤖 INFORMAÇÕES DO BOT:", description=f"Olá {ctx.author}! Aqui você encontrará "
                                          f"algumas informações sobre mim. Meu prefixo é `l.` e sinta-se à vontade "
                                          f"para dar sugestões sobre meu desenvolvimento e usar meus comandos.\n\n"
                                          f"**ESTATISTICAS:**\n\n"
                                          f"**Servidores:** {len(self.bot.guilds)};\n"
                                          f"**Usuários:** {len(self.bot.users)};\n"
                                          f"**Canais:** {canais};\n"
                                          f"**Ping:** {int(self.bot.latency * 1000)}ms;\n"
                                          f"**Uptime:** {uptime}.\n\n"
                                          f"**INFORMAÇÕES:**\n\n"
                                          f"**Criado em:** 7 de setembro de 2021;\n"
                                          f"**Criador:** Felipe Savazi#9407;\n"
                                          f"**Linguagem:** Python;\n"
                                          f"**Versão:** v2.0.0.", color=color)
        embed.set_footer(text=f"Executado por {ctx.author}")
        await ctx.send(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(BotInfo(bot))
    bot.add_cog(BotInfoSlash(bot))
