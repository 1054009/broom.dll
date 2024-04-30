from bot import bot

import config
import event_loader
import mobile

bot.run(config.get_config()["token"])
