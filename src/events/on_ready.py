from bot import bot
from database.engine import engine
from database.models import Base

@bot.event
async def on_ready():
	print("Here I go!")

	engine.connect()

	Base.metadata.create_all(engine)
