import discord
from discord.ext import commands

color = 0xf79805
format = "%a, %d %b %Y | %H:%M:%S %ZGMT"


class Falar(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['falar'])
    async def say(self, ctx, *, args=None):
        if ctx.author.guild_permissions.administrator == False:
            await ctx.send(
                f"Você não tem permissão de **ADMINISTRADOR**, por tanto você não poderá enviar esta mensagem")
        elif args == None:
            await ctx.send("Dê: l.say <texto>")
        else:
            channel = ctx.channel
            await channel.send(f"{args}\n \nEnviado por: {ctx.author.name}")
        
def setup(bot):
    bot.add_cog(Falar(bot))
