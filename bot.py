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
    responses = ['It is certain', 'Dont count on it']
    await ctx.send(f'Question: {question}\nAswer: {random.choice(responses)}')


client.run('NzIwMzYwMTY1MDQ3NTMzNjA5.XuE9gA.eGvIPM-Ly1Ay3s8lJQFXPaK_qe4')
