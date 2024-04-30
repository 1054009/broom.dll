import discord
import config

bot = discord.Client(intents = config.get_intents())

bot.run(config.get_config()["token"])
