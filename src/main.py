from dotenv import load_dotenv

load_dotenv()

import os
from bot import bot

import mobile
import database.engine
import database.session

from folder_loader import load_from

load_from("commands")
load_from("events")

bot.run(os.getenv("BROOM_TOKEN"))
