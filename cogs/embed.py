import discord
import config
import json

from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure
from log import *

class Embed(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @has_permissions(administrator=True)
    async def embed(self, ctx, title, text, logo):
        embed = discord.Embed(title=title, description=text, color=0xf2ff42)
        logo = json.loads(logo.lower())
        
        if logo:
            embed.set_image(url='https://i.ibb.co/zP6kRYm/discord.png')
            
        Log.send(f'{ctx.message.author} created embed')
        await ctx.message.delete()
        await ctx.send(embed=embed)
        
def setup(client):
    client.add_cog(Embed(client))