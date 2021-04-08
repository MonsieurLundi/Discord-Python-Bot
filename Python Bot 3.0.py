import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Game
import requests

curselist = ['fuck','shit','wtf','stfu','ass','arse','bitch','dick','bastard','cunt','bollocks','bloody','choad','wanker','thot','piss','shag','bugger','prick','nigger','nigga','whore','shat']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        await client.change_presence(game=Game(name="computer games"))#test
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        for a in range(len(curselist)):
            if curselist[a] in message.content.lower():
                await message.delete()
        if message.content.startswith("!commandlist"):
            
    async def on_member_join(member):
        await message.channel.send('Welcome to The Server {0.member.mention}'.format(message))
    async def AUDtoUSD(): #test
        url = 'http://www.floatrates.com/daily/aud.json'
        response = requests.get(url)
        value = response.json()['usd']['rate']
        await client.say("The Australian dollar is currently buying " + str(value) + " US dollars.") #test

client = MyClient()
client.run('NTg5MDkwOTYxMDE2MDk0NzMw.XQOnxg.bcqNtmVolZ_06wic6npyGM7tVwY')
