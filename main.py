import discord
from discord import app_commands
import time
from dotenv import load_dotenv
load_dotenv()
import os
token = os.getenv("TOKEN")



intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


client.run(token)