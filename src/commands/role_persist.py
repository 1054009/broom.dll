import discord
from bot import bot
from database.models import PersistentRole
from database.session import session

async def update_persist(guild_id, user_id):
	guild = bot.get_guild(guild_id)

	if guild is None:
		print(f"Can't find guild {guild_id}!")
		return

	guild_user = guild.get_member(user_id)

	if guild_user is None:
		print(f"Can't find user {user_id}!")
		return

	guild_user_persists = session.query(PersistentRole)						\
							.filter(PersistentRole.guild_id == guild_id)	\
							.filter(PersistentRole.user_id == user_id)		\
							.all()

	for persist in guild_user_persists:
		role = guild.get_role(persist.role_id)

		if role is None:
			print(f"Invalid role {persist.role_id}!") # TODO: Remove invalid roles
			continue

		await guild_user.add_roles(role, reason = "Role persist")


def find_user_persist(guild_id, user_id, role_id):
	guild_user_persists = session.query(PersistentRole)						\
							.filter(PersistentRole.guild_id == guild_id)	\
							.filter(PersistentRole.user_id == user_id)

	if len(guild_user_persists.all()) < 1:
		return None

	role_persists = guild_user_persists.filter(PersistentRole.role_id == role_id).all()

	if len(role_persists) > 0:
		return role_persists[0]
	else:
		return None

def create_persist(guild_id, user_id, role_id):
	persist = PersistentRole(
		guild_id = guild_id,
		user_id = user_id,
		role_id = role_id
	)

	session.add(persist)
	session.commit()

def delete_persist(guild_id, user_id, role_id):
	guild_user_persists = session.query(PersistentRole)						\
							.filter(PersistentRole.guild_id == guild_id)	\
							.filter(PersistentRole.user_id == user_id)		\
							.filter(PersistentRole.role_id == role_id)		\
							.delete()

	session.commit()

@bot.tree.command(name = "role_persist")
async def role_persist(interaction: discord.Interaction, target: discord.Member, role: discord.Role):
	existing = find_user_persist(interaction.guild_id, target.id, role.id)

	if existing is None:
		create_persist(interaction.guild_id, target.id, role.id)

		await interaction.response.send_message("Persisted!")
	else:
		delete_persist(interaction.guild_id, target.id, role.id)

		await target.remove_roles(role, reason = "Role persist")
		await interaction.response.send_message("Persist removed!")

	await update_persist(interaction.guild_id, target.id)
