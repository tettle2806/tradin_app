from sqlalchemy.orm import Mapped

from database.base import Base


class User(Base):

    user_name: Mapped[str] = Mapped()
    user_rate: Mapped[str]
    balance: Mapped[float]
    user_role: Mapped[str]
