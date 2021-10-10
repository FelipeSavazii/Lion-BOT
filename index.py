import discord
from discord.ext import commands

import os, re

bot = commands.Bot(command_prefix='l!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Aplicação: {bot.user} está online.')

for root, _, files in os.walk('structure'):
    for file in files:
        path = os.path.join(root, file)

        if not os.path.isfile(path):
            continue

        path, ext = os.path.splitext(path)
        if ext != '.py':
            continue

        extension = re.sub('\\\\|\/', '.', path)

        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Ocorreu o erro {e} ao tentar carregar a extensão {extension}.')
        else:
            print(f'Extensão {extension} carregada com sucesso!')

bot.run(TOKEN)
