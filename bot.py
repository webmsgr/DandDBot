#! python3
import os
if not "key.secret" in os.listdir():
    print("Please create key.secret and put your discord bot key inside.")

import discord
from discord.ext import commands
import random

description = '''A D&D Bot'''
bot = commands.Bot(command_prefix='!', description=description)
token = open("key.secret").read().strip()
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
async def diceroll(dice):
    rolls, limit = map(int, dice.split('d'))
    rolls = [random.randint(1, limit) for r in range(rolls)]
    return rolls
bot.run(token)
