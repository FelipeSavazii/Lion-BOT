from discord.ext import commands
import discord
from discord.utils import get
import youtube_dl
from discord.voice_client import VoiceClient
import asyncio
import aiohttp

playlist = []
musica_atual = ''

color = 0xf79805

youtube_dl.utils.bug_reports_message = lambda: ''


ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' 
}

ffmpeg_options = {
  'before_options': '-nostdin',
  'options': '-vn',
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)



class Play(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def start(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

class Musica(commands.Cog):

    def __init__(self, bot):
      self.bot = bot

    @commands.command(aliases=['entrar'])
    async def join(self, ctx):
        canal = ctx.author.voice.channel
        if not canal:
            embed = discord.Embed(title="❌️ Erro!", description="Você não está em nenhum canal de voz.", color=color)  
            embed.set_footer(text=f"Executado por {ctx.author}")
            await ctx.send(embed=embed)
        if ctx.voice_client is not None:
            embed = discord.Embed(title="❌️ Erro!", description="Eu já estou conectado a um canal de voz.", color=color)  
            embed.set_footer(text=f"Executado por {ctx.author}")
            await ctx.send(embed=embed) 
        else:
            embed = discord.Embed(title="✅ Conectado!", description="Use l.play para que eu toque uma música para você.", color=color)  
            embed.set_footer(text=f"Executado por {ctx.author}")
            await ctx.send(embed=embed)
            await canal.connect()
    
    @commands.command(aliases=['sair'])
    async def leave(self, ctx):
        if ctx.voice_client is None:
            embed = discord.Embed(title="❌️ Erro!", description="Não estou em nenhum canal! Se quiser que eu esteja, pode me chamar com l.entrar ou simplesmente use l.play e entrarei tocando.", color=color)   
            embed.set_footer(text=f"Executado por {ctx.author}")
            await ctx.send(embed=embed) 
        else:
            embed = discord.Embed(title="✅ Desconectado!", description="Fui desconectado, para me conectar novamente, use l.join ou simplesmente dê o play em uma música com l.play e entrarei tocando.", color=color)
            embed.set_footer(text=f"Executado por {ctx.author}")  
            await ctx.send(embed=embed)
            await ctx.voice_client.disconnect()

    @commands.command(aliases=['p'])
    async def play(self, ctx, *, url=None):
          canal = ctx.author.voice.channel
          if url == None:
              await ctx.send(f'{ctx.author.mention}, use l.play <música>')
          else:
              if ctx.voice_client is None:
                  await canal.connect()
                  async with ctx.typing():
                      global musica_atual
                      player = await Play.start(url, loop=self.bot.loop)
                      ctx.voice_client.play(player)
                  embed = discord.Embed(title=f"✅ Tocando: {player.title}!", description="Boa música! Use l.stop para pausar ou l.leave para me desconectar do canal de voz atual.", color=color)
                  embed.set_footer(text=f"Executado por {ctx.author}")
                  await ctx.send(embed=embed)
                  musica_atual = url

              elif ctx.voice_client.is_playing() or len(playlist) != 0:
                  playlist.append(url)
                  embed = discord.Embed(title=f"✅ Música adicionada a playlist!", description="Boa música! Use l.skip para pular a música atual.", color=color)
                  embed.set_footer(text=f"Executado por {ctx.author}")
                  await ctx.send(embed=embed)
              else:
                  async with ctx.typing():
                      player = await Play.start(url, loop=self.bot.loop)
                      ctx.voice_client.play(player)
                  embed = discord.Embed(title=f"✅ Tocando {player.title}!", description="Boa música! Use l.stop para pausar ou l.leave para me desconectar do canal de voz atual.", color=color)
                  embed.set_footer(text=f"Executado por {ctx.author}")
                  await ctx.send(embed=embed)
                  musica_atual = url

    @commands.command()
    async def volume(self, ctx, volume: int):
        if ctx.voice_client is None:
            embed = discord.Embed(title="❌️ Erro!", description="Não estou em nenhum canal! Se quiser que eu esteja, pode me chamar com l.entrar ou simplesmente use l.play e entrarei tocando.", color=color)  
            embed.set_footer(text=f"Executado por {ctx.author}")
            await ctx.send(embed=embed)
        if volume >= 101 or volume <= -1:
            embed = discord.Embed(title="❌️ Erro!", description="Nivel de volume inválido, use números entre 0 e 100", color=color)  
            embed.set_footer(text=f"Executado por {ctx.author}")
            await ctx.send(embed=embed)
        else:
            ctx.voice_client.source.volume = volume / 100
            embed = discord.Embed(title=f"✅ Volume atualizado!", description=f"Volume atual: {volume}%.", color=color)
            embed.set_footer(text=f"Executado por {ctx.author}")
            await ctx.send(embed=embed)

    @commands.command()
    async def pause(self, ctx):
       if not ctx.voice_client.is_playing():
            embed = discord.Embed(title="❌ Erro!", description="Não estou tocando nada! Para me fazer tocar, use l.play <musica>.")
            embed.set_footer(text=f"Executado por {ctx.author}")
            await ctx.send(embed=embed)  
       else:   
            embed = discord.Embed(title="⏸ Pausado!", description="Pausei a música atual. Para continuá-la do ponto onde parei, use l.resume. Caso queira que eu saia do canal, use l.sair.", color=color)
            embed.set_footer(text=f"Executado por {ctx.author}")
            ctx.voice_client.pause()
            await ctx.send(embed=embed)   

    @commands.command()
    async def resume(self, ctx):
       embed = discord.Embed(title="▶ Resumido!", description="Pronto! Dei play na música no ponto onde paramos. Se quiser que eu pause, use l.pause. Se quiser que eu saia do canal, use l.sair.", color=color)
       embed.set_footer(text=f"Executado por {ctx.author}")
       if not ctx.voice_client.is_playing():
            ctx.voice_client.resume()
            await ctx.send(embed=embed)  


    @commands.command(aliases=['s'])
    async def skip(self, ctx):
      embed = discord.Embed(title="⏩ Pulado!", description="Pronto! Pulei a música.", color=color)
      embed.set_footer(text=f"Executado por {ctx.author}")
      if ctx.voice_client.is_playing():
            ctx.voice_client.pause()
            async with ctx.typing():
                player = await Play.start(playlist[0], loop=self.bot.loop)
                ctx.voice_client.play(player)
            await ctx.send(embed=embed)
            musica_atual = playlist[0]
            del(playlist[0])  
      elif playlist == None:
            embed = discord.Embed(title="❌ Erro!", description="Não estou com nada na playlist! Para me fazer tocar, use l.play <musica>.")
            embed.set_footer(text=f"Executado por {ctx.author}")
            await ctx.send(embed=embed)  
      else:
            async with ctx.typing():
                player = await Play.start(playlist[0], loop=self.bot.loop)
                ctx.voice_client.play(player)
            await ctx.send(embed=embed) 
            musica_atual = playlist[0]
            del(playlist[0]) 


    @commands.command()
    async def remove(self, ctx, numero=None):
      embed = discord.Embed(title="❌ Removido!", description="Pronto! Removi a música da playlist.", color=color)
      embed.set_footer(text=f"Executado por {ctx.author}")
      if numero == None:
        await ctx.send(f'{ctx.author.mention}, use l.remove <numero>')
      else:
        global playlist

        try:
          del(playlist[int(numero)])
          await ctx.send(embed=embed)
        
        except:
          embed = discord.Embed(title="❌ Erro!", description="Sua fila está vazia ou o valor descrito não está atribuido a nenhuma música da play.", color=color)
          embed.set_footer(text=f"Executado por {ctx.author}")
          await ctx.send(embed=embed) 

    @commands.command()
    async def queue(self, ctx):
      if len(playlist) == 0:
        embed = discord.Embed(title="📃 Lista de músicas.", description=f"Nenhuma música na fila", color=color)
        embed.set_footer(text=f"Executado por {ctx.author}")
        await ctx.send(embed=embed)
      else:
        embed = discord.Embed(title="📃 Lista de músicas.", description=f" ", color=color)
        for pos, musicas in enumerate(playlist):
          player = await Play.start(playlist[pos], loop=self.bot.loop)
          embed.add_field(name=f'{pos+1}ª música:', value=f"{player.title}", inline=False)
        embed.set_footer(text=f"Executado por {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['letra'])
    async def lyrics(self, ctx, *, nome=None):
      try:
        if nome == None:
          x = musica_atual.replace(" ", "%20")
          async with ctx.typing():
            async with aiohttp.ClientSession() as session:
              async with session.get(f'https://some-random-api.ml/lyrics?title={x}') as response:
                lyric = await response.json()
                embed = discord.Embed(title=f"🔤 {lyric['title']} - {lyric['author']}.", description=lyric['lyrics'], color=color)
                embed.set_footer(text=f"Executado por {ctx.author}")
                await ctx.send(embed=embed)
        else:
          x = nome.replace(" ", "%20")
          async with ctx.typing():
            async with aiohttp.ClientSession() as session:
              async with session.get(f'https://some-random-api.ml/lyrics?title={x}') as response:
                lyric = await response.json()
                embed = discord.Embed(title=f"🔤 {lyric['title']} - {lyric['author']}.", description=lyric['lyrics'], color=color)
                embed.set_footer(text=f"Executado por {ctx.author}")
                await ctx.send(embed=embed)  
      except:
        if nome == None:
          x = musica_atual.replace(" ", "%20")
          async with ctx.typing():
            async with aiohttp.ClientSession() as session:
              async with session.get(f'https://some-random-api.ml/lyrics?title={x}') as response:
                lyric = await response.json()
                embed = discord.Embed(title=f"🔤 {lyric['title']} - {lyric['author']}.", description=lyric['lyrics'], color=color)
                embed.set_footer(text=f"Executado por {ctx.author}")
                await ctx.send(embed=embed)    
        else:
          x = nome.replace(" ", "%20")
          async with ctx.typing():
            async with aiohttp.ClientSession() as session:
              async with session.get(f'https://some-random-api.ml/lyrics?title={x}') as response:
                lyric = await response.json()
                embed = discord.Embed(title=f"🔤 {lyric['title']} - {lyric['author']}.", description=f'{lyric["links"]["genius"]}', color=color)
                embed.set_footer(text=f"Executado por {ctx.author}")
                await ctx.send(embed=embed)  
          

def setup(bot):
    bot.add_cog(Musica(bot))    