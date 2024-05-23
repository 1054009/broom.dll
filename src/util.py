import discord
import random

denies = (
	"No",
	"NO!",
	"Fuck off",
	"I don't feel like it",
	"Why don't you ask me later?",
	"Nuh uh"
)

async def deny_interaction(interaction: discord.Interaction):
	await interaction.response.send_message(random.choice(denies))

def is_member_admin(member: discord.Member):
	if not member.guild_permissions.administrator: return False
	if not member.resolved_permissions.administrator: return False

	return True
