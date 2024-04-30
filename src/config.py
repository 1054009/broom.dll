import discord
import json
from pathlib import Path

EXECUTING_DIRECTORY = Path(__file__).parent.resolve()
config_cache = None

def get_config():
	global config_cache

	if config_cache:
		return config_cache
	else:
		try:
			config_path = (EXECUTING_DIRECTORY / "config.json").resolve()

			config_file = open(config_path, "r")
			config_cache = json.loads(config_file.read())
			config_file.close()

			return config_cache
		except:
			print("Failed to load config.json")
			return None

def get_intents():
	intents = discord.Intents.default()
	intents.guilds = True
	intents.members = True
	intents.message_content = True

	return intents
