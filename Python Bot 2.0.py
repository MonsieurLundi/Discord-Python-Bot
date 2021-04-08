import random
import discord
from discord.ext import commands

curselist = ['fuck','shit','wtf','stfu','ass','arse','bitch','dick','bastard','cunt','bollocks','bloody','choad','wanker','thot','piss','shag','bugger','prick','nigger','nigga','whore','shat']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        for a in range(len(curselist)):
            if curselist[a] in message.content.lower():
                await message.delete()

client = MyClient()
client.run('INSERT TOKEN HERE')
