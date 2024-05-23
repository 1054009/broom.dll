import discord
from bot import bot

from commands.role_persist import update_persist

@bot.event
async def on_member_join(member: discord.Member):
	await update_persist(member.guild.id, member.id)
