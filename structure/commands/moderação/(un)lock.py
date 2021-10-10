

    @commands.command()
    async def lock(ctx):
        guild = ctx.guild
        if ctx.author.guild_permissions.administrator:
            if ctx.author.name == ctx.author.name:
                if ctx.author.name == ctx.author.name:
                    try:
                        cargo = discord.utils.get(guild.roles, name="🏆 | Membro")
                        await ctx.channel.set_permissions(cargo, send_messages=False, read_message_history=True, read_messages=True)
                        embed1 = discord.Embed (
                                title=f"{name} - LOCK",
                                description=f"O canal foi travado com sucesso.",
                                color=cor)
                        await ctx.send(embed=embed1)
                    except Exception as e:
                        if ctx.channel.permissions_for(ctx.me).administrator == None:
                            embederr = discord.Embed (
                                title=f"{name} - LOCK",
                                description=f"Preciso ter permissão para usar esse comando.",
                                color=16711680)
                            await ctx.send(embed=embederr)
                        print(e)
        else:
            embed = discord.Embed (
                title=f"{name} - LOCK",
                description=f"Você não tem permissão para usar este comando!",
                color=cor)
            await ctx.send(embed=embed)

    @commands.command()
    async def unlock(ctx):
        guild = ctx.guild
        if ctx.author.guild_permissions.administrator:
            if ctx.author.name == ctx.author.name:
                if ctx.author.name == ctx.author.name:
                    try:
                        cargo = discord.utils.get(guild.roles, name="🏆 | Membro")
                        await ctx.channel.set_permissions(cargo, send_messages=True, read_message_history=True, read_messages=True)
                        embed1 = discord.Embed (
                                title=f"{name} - UNLOCK",
                                description=f"O canal foi destravado com sucesso.",
                                color=cor)
                        await ctx.send(embed=embed1)
                    except Exception as e:
                        if ctx.channel.permissions_for(ctx.me).administrator == None:
                            embederr = discord.Embed (
                                title=f"{name} - UNLOCK",
                                description=f"Preciso ter permissão para usar esse comando.",
                                color=16711680)
                            await ctx.send(embed=embederr)
                        print(e)
        else:
            embed = discord.Embed (
                title=f"{name} - LOCK",
                description=f"Você não tem permissão para usar este comando!",
                color=cor)
            await ctx.send(embed=embed)