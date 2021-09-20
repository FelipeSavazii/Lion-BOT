import discord
from discord.ext import commands

color = 0xf79805
format = "%a, %d %b %Y | %H:%M:%S %ZGMT"


class Votacao(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['votação', 'votacao'])
    async def enquete(self, ctx):
        channel = ctx.channel
        embed = discord.Embed(title=f" ", description="🧮 Enquete", color=color)
        embed0 = discord.Embed(title=f" ", description="🚧 Digite o titulo:", color=color)
        embed2 = discord.Embed(title=f" ", description="🚧 Digite a descrição:", color=color)
        embed3 = discord.Embed(title=f" ", description="🚧 Marque o canal!", color=color)
        embed4 = discord.Embed(title=f" ", description="🧮 Enquete enviada!", color=color)
        if ctx.author.guild_permissions.administrator == True:
            await channel.send(embed=embed)
            await channel.send(embed=embed0)

            def check(msg):
                return msg.author == ctx.author

            msg1 = await ctx.bot.wait_for(event='message', check=check, timeout=2000.0)
            await channel.send(embed=embed2)
            msg2 = await ctx.bot.wait_for(event='message', check=check, timeout=2000.0)
            await channel.send(embed=embed3)
            try:
                msg3 = await ctx.bot.wait_for(event='message', check=check, timeout=2000.0)
                converter = commands.TextChannelConverter()
                canal = await converter.convert(ctx, msg3.content)
            except:
                embederror = discord.Embed(title=f"", description="❌ Erro ao tentar enviar a enquete!", color=color)
                await ctx.send(embed=embederror)
            embed5 = discord.Embed(title=f"{msg1.content}\n \n", description=msg2.content,
                                   color=color)
            embed5.set_footer(text=f"Enviado por: {ctx.author}")
            enviado = await canal.send(embed=embed5)
            await ctx.send(embed=embed4)
            await enviado.add_reaction('✅')
            await enviado.add_reaction('❌')
        else:
            await ctx.send(
                f"Você não tem permissão de **ADMINISTRADOR**, por tanto você não poderá enviar esta mensagem")
        
def setup(bot):
    bot.add_cog(Votacao(bot))