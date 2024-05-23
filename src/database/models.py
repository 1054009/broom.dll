from sqlalchemy.dialects.mysql import INTEGER, BIGINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
	pass

class PersistentRole(Base):
	__tablename__ = "role_persists"

	id:Mapped[int] = mapped_column(
		INTEGER(unsigned = True),

		primary_key = True
	)

	guild_id:Mapped[int] = mapped_column(
		BIGINT(unsigned = True)
	)

	user_id:Mapped[int] = mapped_column(
		BIGINT(unsigned = True)
	)

	role_id:Mapped[int] = mapped_column(
		BIGINT(unsigned = True)
	)
