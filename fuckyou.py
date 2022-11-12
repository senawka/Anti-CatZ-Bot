#Import shit lol
import discord, random, time
from discord.ext import commands

client = discord.Client()
TOKEN = ''


#Discord Role
role_name = "CatZ Lover"


#Filter
with open('crankthat/souljaboy.txt', 'r') as f:
    global filter
    words = f.read()
    triggerwords = words.split()

#Responses
with open ('crankthat/woo.txt', 'r') as f:
    global response
    resp = f.read()
    response_list = resp.split(":")


#it is 5:18 am what the fuck am i doing with my life

#Discord Intent shit bcuz yeas

intent = discord.Intents.default()
intent.members = True
intent.messages = True
intent.presences = True

client = discord.Client(intents=intent)
bot = commands.Bot(command_prefix="$", intents=intent)

#activates bot
@client.event
async def on_ready():
    print('Successfully loggged in as {0.user}'.format(client))


#fun part (involves me ripping my hair out)

@client.event
async def on_message(message):
    recipient = message.author
    if message.author == client.user:
        return
    msg = message.content
    if any(word in msg.lower() for word in triggerwords) and not recipient.guild_permissions.kick_members:
        role = discord.utils.get(message.author.guild.roles, name=role_name)
        await recipient.edit(roles=[role])
        await message.channel.send(random.choice(response_list) + message.author.mention)
        while recipient is not None and role in recipient.roles:
            time.sleep(1)
            await recipient.send(random.choice(response_list) + message.author.mention)
        else:
            await recipient.send(recipient + ' left')
    if message.content.startswith('$addfilter'):
        word = message.content.split('$addfilter',1)[1]
        with open('crankthat/souljaboy.txt', 'r') as f:
            global filter
            words = f.read()
            if word.lower() not in words:
                with open('crankthat/souljaboy.txt', 'a') as f:
                    f.write(word + "\n")
            else:
                await message.channel.send('Added filter.')
    if message.content.startswith('$addresponse'):
        phrase = message.content.split('$addresponse',1)[1]
        with open('crankthat/woo.txt', 'r') as f:
            global filter
            phrases = f.read()
            if phrase not in phrases:
                with open('crankthat/woo.txt', 'a') as f:
                    f.write(phrase +":")
            else:
                await message.channel.send('Added phrase.')


#went completely bald writing this


#fucking run
client.run(TOKEN)
