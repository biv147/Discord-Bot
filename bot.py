import discord
import random
from discord.ext import commands
import json
#import aysncio
import youtube_dl
import os
from discord.utils import get

token = #your token here

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

@client.command()
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)

    if voice and voice_is.connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    await ctx.sent(f"Joined {channel}")


@client.command()
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send(f"left {channel}")


client.run(token)
