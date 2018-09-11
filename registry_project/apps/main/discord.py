import discord

CLIENT_ID = '486175396644126720'
CLIENT_SECRET = 'mgXRBYhpl92RbdxUwmx4RfU1zqTSDuk6'
TOKEN= 'NDg2MTc1Mzk2NjQ0MTI2NzIw.Dm8JLg.L8_k-ePnCp13t79EF2rPjrES0KA'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)