from discord.ext import commands
import config

bot = commands.Bot(
	command_prefix = ";",
	intents = config.get_intents()
)
