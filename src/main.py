from bot import bot
import config

bot.run(config.get_config()["token"])
