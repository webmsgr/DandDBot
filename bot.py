#! python3
import os
if not "key.secret" in os.listdir():
    print("Please create key.secret and put your discord bot key inside.")
spelld = {"First Level":{
    "warp":{"des":"teleport","range":"100ft"}
    },
        "Second Level":{
        "explode":{"des":"boom","range":"100ft"}
        }
}
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
@bot.command()
async def rolldice(dicestring):
    '''roll a NdN'''
    dice = await diceroll(dicestring)
    total = 0
    for item in dice:
        total += item
    await bot.say(str(dice).replace("[","").replace("]","").replace(","," + ") + " = {}".format(total))
@bot.command()
async def spells():
    '''Print the spell database'''
    emb = discord.Embed(title = "SpellBook",type = "rich",description = "The Discord spellbook")
    for field in spelld:
        fdata = ""
        for spelli in spelld[field]:
            print(spelli)
            fdata += spelli + "\n"
            fdata = fdata[:-1]
        emb.add_field(name=field, value=fdata)
    await bot.say("",embed=emb)
@bot.command()
async def spell(*, spell: str):
    try:
        cat, spelli = map(str,spell.split(":"))
    except:
        await bot.say("Spell format is catigory:spellname")
        return
    if not cat in spelld:
        await bot.say("That catigory does not exist!")
        return
    spelll = spelld[cat]
    if not spelli in spelll:
        await bot.say("That spell does not exist")
        return
    thespell = spelll[spelli]

    await bot.say("I would respond, but the \"{}\" spell is smelly".format(spell))
bot.run(token)
