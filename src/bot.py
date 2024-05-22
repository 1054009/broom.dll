import discord
from discord.ext import commands

bot = commands.Bot(
	command_prefix = "!",
	intents = discord.Intents.all(),

	case_insensitive = True
)
