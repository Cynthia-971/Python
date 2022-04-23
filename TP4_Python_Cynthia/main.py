import os
import discord
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")

default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)

@client.event
async def on_ready():
    print("Le bot est prêt !")

@client.event 
async def on_message(message):
    if message.content.startswith("!del"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()

client.run(os.getenv("TOKEN"))