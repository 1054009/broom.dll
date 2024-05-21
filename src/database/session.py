from database.engine import engine
from sqlalchemy.orm import Session

session = Session(engine)
