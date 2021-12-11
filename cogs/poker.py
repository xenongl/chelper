import discord
import config
import requests
import json

from discord.ext import commands
from log import *

# Games ID:
# Youtube Together - 755600276941176913
# Betrayal.io - 773336526917861400
# Fishington.io - 814288819477020702
# Poker Night - 755827207812677713
# Chess - 832012774040141894

class Poker(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def poker(self, ctx):
        data = {
            "max_age": 86400,
            "max_uses": 0,
            "target_application_id": 755827207812677713, # Game ID
            "target_type": 2,
            "temporary": False,
            "validate": None
        }
        headers = {
            "Authorization": f"Bot {config.TOKEN}",
            "Content-Type": "application/json"
        }

        if ctx.author.voice is not None:
            if ctx.author.voice.channel is not None:
                channel = ctx.author.voice.channel.id
            else:
                await ctx.send('Зайдите в канал')
        else:
            await ctx.send('Зайдите в канал')
        response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
        link = json.loads(response.content)

        await ctx.send(f'https://discord.com/invite/{link["code"]}')
    
def setup(client):
    client.add_cog(Poker(client))