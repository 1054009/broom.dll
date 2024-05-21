from dotenv import load_dotenv

load_dotenv()

import os
from bot import bot

import config
import event_loader
import mobile
import database.engine
import database.session

bot.run(os.getenv("BROOM_TOKEN"))
