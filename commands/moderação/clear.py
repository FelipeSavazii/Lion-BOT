import discord
from discord.ext import commands
import random

color = 0xf79805

class Clear(commands.Cog):

    def __init__(self, bot):
      self.bot = bot
      
    @commands.command()
    async def clear(ctx, *args):
        if len(args) != 0:
            if ctx.channel.permissions_for(ctx.author).manage_messages:
                try:
                    qtdd = float(args[0])
                except ValueError:
                    embed = discord.Embed(title=" ",
                                          description=f"🗑️ **O valor informado não é um número.**",
                                          color=color)
                    embed.set_footer(text=f"Executado por {ctx.author}")
                    await ctx.send(embed=embed)
                else:
                    if ctx.channel.permissions_for(ctx.me).manage_messages:
                        qtdd = int(qtdd)
                        if (qtdd < 2) or (qtdd > 1000):
                            embed = discord.Embed(title=" ",
                                                  description=f"🗑️ **O número de mensagens que serão apagadas tem que ser no mínimo 2 e no máximo 1000.**",
                                                  color=color)
                            embed.set_footer(text=f"Executado por {ctx.author}")
                            await ctx.send(embed=embed)
                        else:
                            msgs = await ctx.channel.purge(limit=(qtdd + 1))
                            embed = discord.Embed(title=" ",
                                                  description=f"🗑️ **{len(msgs) - 1} mensagens apagadas!**",
                                                  color=color)
                            embed.set_footer(text=f"Executado por {ctx.author}")
                            await ctx.send(embed=embed, delete_after=10)
                    else:
                        embed = discord.Embed(title=" ",
                                              description=f"🗑️ **Eu preciso ter permissão de `GERENCIAR MENSAGENS` para executar este comando.**",
                                              color=color)
                        embed.set_footer(text=f"Executado por {ctx.author}")
                        await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title=" ",
                                      description=f"🗑️ **Você precisa ter permissão de `GERENCIAR MENSAGENS` para executar este comando.**",
                                      color=color)
                embed.set_footer(text=f"Executado por {ctx.author}")
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=" ", description=f"🗑️ **Informe o número de mensagens que serão apagadas sendo que o número mínimo é 2 e o máximo é 1000.**",
                                  color=color)
            embed.set_footer(text=f"Executado por {ctx.author}")
            await ctx.send(embed=embed)
      
def setup(bot):
    bot.add_cog(Clear(bot))