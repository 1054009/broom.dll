import discord
from bot import bot

print("APOKPOPGKEO")

@bot.tree.command(name = "role_persist", description = "TESST", guild = discord.Object(id = 1138420436397473852))
async def role_persist(interaction: discord.Interaction):
	await interaction.response.send_message("FKo")
