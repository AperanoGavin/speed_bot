import discord
from discord import app_commands
import time
import tweepy
import youtube_dl
from dotenv import load_dotenv
load_dotenv()
import os
token = os.getenv("TOKEN")
bearer_tokenn = os.getenv("BEARER_TWITTER")



intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
GUILD = os.getenv('1047812022789734480')
client_twitter = tweepy.Client(bearer_token=bearer_tokenn)
id_twitter = "1040214455525797888"
id_youtube = "UCWsDFcIhY2DBi3GB5uykGXA"
@client.event
async def on_ready():
    synced = await tree.sync()
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
 


#last tweet
@tree.command(name="last_tweet" , description="last tweet")
async def last_tweet( interaction: discord.Interaction ):
    ishow_twitter = client_twitter.get_users_tweets(id_twitter,  tweet_fields=['context_annotations','created_at','geo'] )
    await interaction.response.send_message(ishow_twitter[0][0])
    print (ishow_twitter)
   # last_tweet = response_twitter["data"]["tweets"][0]["text"]
  #  await interaction.response.send_message(last_tweet)
  

@tree.command(name="last_youtube" , description="last video")
async def last_youtube( interaction: discord.Interaction ):
    ishow_youtube = client_twitter.get_users_tweets(id_youtube,  tweet_fields=['context_annotations','created_at','geo'] )
    await interaction.response.send_message(ishow_youtube[0][0])
    print (ishow_youtube)


client.run(token)