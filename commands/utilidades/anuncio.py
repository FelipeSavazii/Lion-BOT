import discord
from discord.ext import commands

color = 0xf79805

class Confirm(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    # When the confirm button is pressed, set the inner value to `True` and
    # stop the View from listening to more input.
    # We also send the user an ephemeral message that we're confirming their choice.
    @discord.ui.button(label='Confirmar', style=discord.ButtonStyle.green)
    async def confirm(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message('📣 Anuncio enviado!', ephemeral=True)
        self.value = True
        self.stop()

    # This one is similar to the confirmation button except sets the inner value to `False`
    @discord.ui.button(label='Cancelar', style=discord.ButtonStyle.red)
    async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message('❌ Operação cancelada.', ephemeral=True)
        self.value = False
        self.stop()

class Anunciar(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['anuncio'])
    async def anunciar(self, ctx):
        channel = ctx.channel
        embed = discord.Embed(title=f" ", description="📣 Anúncio", color=color)
        embed0 = discord.Embed(title=f" ", description="🚧 Digite o titulo:", color=color)
        embed2 = discord.Embed(title=f" ", description="🚧 Digite a descrição:", color=color)
        embed3 = discord.Embed(title=f" ", description="🚧 Marque o canal:", color=color)
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
                embederror = discord.Embed(title=f"", description="❌ Erro ao tentar enviar o anúncio!", color=color)
                await ctx.send(embed=embederror)
            view = Confirm()
            await ctx.send('Tem certeza de que quer enviar esse anúncio?', view=view)
            await view.wait()
            if view.value is None:
                ctx.send('Tempo esgotado.')
            elif view.value:
                embed5 = discord.Embed(title=f"{msg1.content}\n \n", description=msg2.content, color=color)
                embed5.set_footer(text=f"Enviado por: {ctx.author}")
                await canal.send(embed=embed5)
        else:
            await ctx.send(
                f"Você não tem permissão de **ADMINISTRADOR**, por tanto você não poderá enviar esta mensagem")
    
def setup(bot):
    bot.add_cog(Anunciar(bot))
