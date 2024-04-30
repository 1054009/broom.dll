from bot import bot

@bot.event
async def on_message(message):
	author = message.author

	if author.bot:
		return

	await message.reply("shut up")
