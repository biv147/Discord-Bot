import discord
import random
from discord.ext import commands

#client = discord.Client('!')
client = commands.Bot(command_prefix = '!') #initialise the bot

@client.event
async def on_ready(): #make sure the bot is ready
    print('Bot is ready')

@client.event
async def on_member_join(member): #lets the bot know that a user has joined
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member): #lets the bot know a user has left
    print(f'{member} has been removed')

@client.command()
async def ping(ctx): #returns a message into the chat
    await ctx.send('Pong!')

@client.command(aliases = ['8ball'])
async def _8ball(ctx, *, question): # answers a users question, also '*' allows many parameters as one parameter
    responses = ["It is certain.",
"It is decidedly so.",
"Without a doubt.",
"Yes - definitely.",
"You may rely on it.",
"As I see it, yes.",
"Most likely.",
"Outlook good.",
"Yes.",
"Signs point to yes.",
"Reply hazy, try again.",
"Ask again later.",
"Better not tell you now.",
"Cannot predict now.",
"Concentrate and ask again.",
"Don't count on it.",
"My reply is no.",
"My sources say no.",
"Outlook not so good.",
"Very doubtful."]
    await ctx.send(f'Question: {question}\nAswer: {random.choice(responses)}')


client.run("token") #replace token with the bot token
