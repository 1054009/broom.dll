from pathlib import Path
import os

EXECUTING_DIRECTORY = Path(__file__).parent.resolve()

def load_from(name):
	for item in os.listdir(EXECUTING_DIRECTORY / name):
		if not item.endswith(".py"):
			continue

		if "__" in item:
			continue

		__import__(f"{name}.{item[:-3]}", locals(), globals())
