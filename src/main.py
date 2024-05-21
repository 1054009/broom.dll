from dotenv import load_dotenv

load_dotenv()

import os
from bot import bot

import config
import event_loader
import mobile

bot.run(str(os.getenv("BROOM_TOKEN")))
