import discord
import config

bot = discord.Client(intents = config.get_intents())
