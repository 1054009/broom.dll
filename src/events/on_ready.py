from bot import bot
from database.engine import engine

@bot.event
async def on_ready():
	print("Here I go!")

	engine.connect()
