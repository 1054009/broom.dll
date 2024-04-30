import discord

from config import get_config

class Retard(discord.Client):
	async def on_read(self):
		print(self.user)

	async def on_message(self, message):
		print(message)

intents = discord.Intents.default()
intents.message_content = True

client = Retard(intents = intents)
client.run(get_config()["token"])
