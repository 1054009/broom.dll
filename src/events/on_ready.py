import discord
from bot import bot
from database.engine import engine
from database.models import Base

@bot.event
async def on_ready():
	print("Syncing commands")
	synced = await bot.tree.sync(guild = discord.Object(id = 1138420436397473852))
	print(f"Synced {synced}")

	print("Connecting to database")
	engine.connect()

	print("Creating tables")
	Base.metadata.create_all(engine)

	print("Here I go!")
