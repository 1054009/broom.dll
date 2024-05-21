from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import os

connection_url = URL(
	"mysql+mysqlconnector",
	os.getenv("BROOM_SQL_USERNAME"),
	os.getenv("BROOM_SQL_PASSWORD"),
	"localhost",
	3306,
	os.getenv("BROOM_SQL_DB"),
	{}
)

engine = create_engine(connection_url)
