import discord

class Broom(discord.Client):
	async def on_read(self):
		print(self.user)

	async def on_message(self, message):
		print(message)
