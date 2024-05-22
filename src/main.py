from dotenv import load_dotenv

load_dotenv()

import os
from bot import bot

import config
import mobile
import database.engine
import database.session

from folder_loader import load_from

load_from("events")
load_from("commands")

bot.run(os.getenv("BROOM_TOKEN"))
