from bot import bot

import config
import event_loader

bot.run(config.get_config()["token"])
