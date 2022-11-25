import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('玖夜'):
        await message.channel.send('哦呀？')

client.run(os.getenv('MTA0NTY1MzY4ODQ1NjMxOTAwNw.Gvep4p.A-CiyJAJLKmmXC58BIIBxkc9rDzgD2j6tAqfXk'))
