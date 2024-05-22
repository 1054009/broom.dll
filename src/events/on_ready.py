import discord
from bot import bot
from database.engine import engine
from database.models import Base

@bot.event
async def on_ready():
	libbys = discord.Object(id = 1138420436397473852) # TODO: Make this not this

	print("Syncing commnads")
	bot.tree.copy_global_to(guild = libbys)
	await bot.tree.sync(guild = libbys)

	print("Connecting to database")
	engine.connect()

	print("Creating tables")
	Base.metadata.create_all(engine)

	print("Here I go!")
