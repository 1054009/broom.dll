import discord

from bot import Broom
from config import get_config

intents = discord.Intents.default()
intents.message_content = True

client = Broom(intents = intents)
client.run(get_config()["token"])
