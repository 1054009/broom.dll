import discord
import config

client = discord.Client(config.get_intents())

@client.event
async def on_ready():
	print("WAHHH\nWAHHhWAHHH\nWAHHhWAHHH\nWAHHhWAHHH\nWAHHhWAHHH\nWAHHh")


client.run(config.get_config()["token"])
