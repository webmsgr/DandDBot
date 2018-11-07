#! python3
import os,sys,json
if not "key.secret" in os.listdir():
    print("Please create key.secret and put your discord bot key inside.")
    sys.exit(0)
if not "spells.json" in os.listdir():
    print("Please build spells.")
    sys.exit(0)
spelld = json.load(open("spells.json"))
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
async def spell(*, spell: str):
    '''Get info on a spell'''
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
    emb = discord.Embed(title = spelli,type = "rich", description = thespell.pop("desc"))
    for thing in thespell:
        emb.add_field(name=thing,value=thespell[thing])
    await bot.say("",embed=emb)
@bot.command()
async def search(*, spellLook: str):
    '''Search the database'''
    spelll = []
    matched = []
    for cat in spelld:
        for spell in spelld[cat]:
            spelll.append("{}:{}".format(cat,spell))
    for spell in spelll:
        if spellLook.lower() in spell.split(":")[1].lower() :
            matched.append(spell)
    if matched == []:
        await bot.say("No results!")
    else:
        emb = discord.Embed(title = "Search Results", type = "rich", description = "Search results for {}".format(spellLook))
        out = ""
        for matchedspell in matched:
            out += "!spell {}\n".format(matchedspell)
        out = out[:-1]
        emb.add_field(name="Results",value=out)
        await bot.say("",embed=emb)

bot.run(token)
