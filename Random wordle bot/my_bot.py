import discord
import random
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
load_dotenv()


#Open the text file in read mode.
with open("5_letter_word.txt", "r") as file:
    all_txt = file.read()
    words = list(map(str, all_txt.split()))

#Set command Prefix
bot = commands.Bot(command_prefix='!')

#Command 1
@bot.command()
async def hello(ctx):
    await ctx.reply('hello')

#Command 2
@bot.command()
async def word(ctx):
    await ctx.reply(random.choice(words))

bot.run(getenv('Token'))