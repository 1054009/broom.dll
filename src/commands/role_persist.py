import discord
from bot import bot

@bot.tree.command(name = "role_persist")
async def role_persist(interaction: discord.Interaction):
	await interaction.response.send_message("FUCK YOU!!")
