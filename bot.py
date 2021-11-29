import discord
import os
import config

from log import *
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '!')
status = cycle(['santy gay', 'santy cool'])

# Check activity
@client.event
async def on_ready():
    change_status.start()
    Log.send('Successfully connected')
    
# Status
@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
    # Log.send('Status changed')

# Command Error
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Проверьте правильность ввода аргументов')

# Reload command
@client.command()
async def reload(ctx, extension):
    if ctx.author.id == 455367009878933505:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.send('Модуль успешно обновлен!')

# Initializing
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(config.TOKEN)