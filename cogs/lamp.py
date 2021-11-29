import discord
import asyncio
import config

from discord.ext import commands, tasks
from log import *
from yeelight import Bulb

class Lamp(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.bulb = Bulb(config.LAMP_IP)
    
    @commands.command()
    async def on(self, ctx):
        self.bulb.turn_on()
        embed = discord.Embed(title='Новое состояние лампы:', description='Включена', color=0x00FF00)
        Log.send(f'{ctx.message.author} turned on the lamp')
        await ctx.send(embed=embed)
        
    @commands.command()
    async def off(self, ctx):
        self.bulb.turn_off()
        embed = discord.Embed(title='Новое состояние лампы:', description='Выключена', color=0xFF0000)
        Log.send(f'{ctx.message.author} turned off the lamp')
        await ctx.send(embed=embed)
        
    @commands.command()
    async def color(self, ctx, r, g, b):
        r, g, b = int(r), int(g), int(b)
        self.bulb.set_rgb(r, g, b)
        embed = discord.Embed(description='Цвет лампы изменен', color=discord.Color.from_rgb(r, g, b))
        Log.send(f'{ctx.message.author} changed color')
        await ctx.send(embed=embed)
        
def setup(client):
    client.add_cog(Lamp(client))