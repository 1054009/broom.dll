from pathlib import Path
import os

EXECUTING_DIRECTORY = Path(__file__).parent.resolve()

for event in os.listdir(EXECUTING_DIRECTORY / "events"):
	if not event.endswith(".py"):
		continue

	if "__" in event:
		continue

	__import__(f"events.{event[:-3]}", locals(), globals())
