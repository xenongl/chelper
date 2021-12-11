import discord
import config

from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure
from log import *

class Embed(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @has_permissions(administrator=True)
    async def embed(self, ctx, title, text):
        embed = discord.Embed(title=title, description=text, color=0xf2ff42)
        Log.send(f'{ctx.message.author} created embed')
        await ctx.message.delete()
        await ctx.send(embed=embed)
        
def setup(client):
    client.add_cog(Embed(client))